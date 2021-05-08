#coding:utf8
import os
import rv
import re
import sys
import time
import uuid
import shutil
import subprocess

from PySide.QtCore     import *
from PySide.QtGui      import *
from PySide.QtWebKit   import * 


class TimeLineView( QDockWidget ):
    def __init__( self ):
        super( TimeLineView, self ).__init__()
        self.setUI()
    def setUI( self ):
        self.Gdata = []
        self.setObjectName( "TimeLineView" )
        self.setAllowedAreas( Qt.BottomDockWidgetArea )
        self.setWindowTitle( "TimeLine" )
        self.setMinimumHeight( 158 )
        self.setMaximumHeight( 158 )
        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount( 1 )
        self.tablewidget.horizontalHeader().setDefaultSectionSize(96)
        self.tablewidget.verticalHeader().setDefaultSectionSize(100)
        self.tablewidget.verticalHeader().setVisible(False)
        self.tablewidget.horizontalHeader().setVisible(False)
        self.tablewidget.itemDoubleClicked.connect( self.slot_item_clicked )
        self.tablewidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tablewidget.customContextMenuRequested.connect( self.slot_menu )           
        self.tablewidget.setStyleSheet( "QTableWidget::item{border-left:1px solid black;}"
                                        "QTableWidget::item:selected{background-color:#3BAFDA;}"
                                        )
        self.m_layout = QVBoxLayout()
        self.m_layout.addWidget( self.tablewidget )
        TMPWidget = QWidget()
        TMPWidget.setLayout( self.m_layout )
        self.setWidget( TMPWidget )        
    def setData( self , data=False ):
        self.Gdata = []
        rv.commands.clearSession()
        self.tablewidget.clear()     
        self.tablewidget.setColumnCount( 0 )
        ShotList = data[ 0 ]
        ShotDict = data[ 1 ]
        
        for Shot in ShotList:
            PlayData = ShotDict[ Shot ]
            PLayMoV = self.get_first( PlayData )
            if PLayMoV != False :
                if "_L_v" in PLayMoV or "_L." in PLayMoV:
                    PLayMoV_R = PLayMoV.replace("_L", "_R")
                    rv.commands.addSource( PLayMoV)
                    rv.commands.addToSource( PLayMoV_R )
                else:
                    rv.commands.addSource(PLayMoV)
                NodeName = ''
                Pix = ''
                SourceNodeList = rv.commands.nodesOfType( "RVSource" )
                for i in range( len(SourceNodeList) ):
                    SourceNode = SourceNodeList[i]  
                    SourceNodeMedia = rv.commands.sourceMediaInfoList( SourceNode )
                    for Media in SourceNodeMedia:    
                        Path  = Media["file"]
                        if Path == PLayMoV:
                            NodeName = SourceNode
                            if "%" in Path:
                                Pix = self.call_Get_Pix( Path%(int(Media["startFrame"])), False )
                            elif ".exr" in Path:
                                Pix = self.get_image_thumbnails( Path )
                            else:
                                Pix = self.call_Get_Pix( Path, True )
                                
                column = self.tablewidget.columnCount()
                self.tablewidget.insertColumn( column )

                Label = QLabel()
                Label.setStyleSheet( "QLabel{border-image:url('%s');padding:5px;margin:0px;}"%Pix )
                # print Pix
                laybel2 = QLabel()
                laybel2.setText( Shot )
                laybel2.setFixedHeight( 28 )
                widget = QWidget()
                layout = QVBoxLayout()
                layout.setContentsMargins( 2,2,2,2 )
                layout.setSpacing( 0 )
                widget.setLayout( layout )
                layout.addWidget( Label )
                layout.addWidget( laybel2 )
                
                self.tablewidget.setCellWidget( 0, column, widget )
                item = QTableWidgetItem()
                item.setData( 32, PlayData )
                item.setData( 33, Label )
                item.setData( 34, NodeName )
                item.setData( 35, PLayMoV )
                self.tablewidget.setItem( 0, column , item )
                self.Gdata.append( [  PLayMoV, PlayData, Pix, NodeName, Shot ] )
    def slot_item_clicked( self , item ):
        t_frame = 0
        rv.commands.stop()
        nodename = item.data(34)
        for i in range( self.tablewidget.columnCount() ):
            nodenames = self.tablewidget.item( 0, i ).data(34)
            if nodename != nodenames:
                SourceNodeMedia = rv.commands.sourceMediaInfoList( nodenames )
                for d in SourceNodeMedia:
                    t_frame = t_frame + d["endFrame"] - d["startFrame"] + 1
            else:
                rv.commands.setFrame( int(t_frame+1) )
                return True
    def slot_menu( self , event ):
        Items = self.tablewidget.selectedItems()
        if len(Items) == 1:
            menu = QMenu()
            item1=menu.addAction( u"切换版本" )
            item2=menu.addAction( u"还原" )
            action=menu.exec_(QCursor.pos())
            if action == item1:
                self.Version = Version( Items[0] )
                self.Version.signal.connect( self.slot_replace_source )
                self.Version.exec_()
            elif action == item2:
                self.huanyuan()
        elif len(Items) > 1:
            menu = QMenu()
            item2=menu.addAction( u"并播" )
            item3=menu.addAction( u"串播" )
            item4=menu.addAction( u"还原" )
            action=menu.exec_(QCursor.pos())
            if action == item2:
                t_node_list = []
                for item in Items:
                    Nodename = item.data( 35 )
                    t_node_list.append( Nodename )
                for i in self.Gdata:
                    ViewNode  = i[3].split("_")[0]
                    InputNode = i[0]
                    if rv.commands.nodeExists( ViewNode ) and not InputNode in t_node_list :
                        rv.commands.deleteNode( ViewNode )    
                rv.commands.setViewNode( "defaultLayout" )
                self.rrfersh_ui( )
            elif action == item3:
                t_node_list = []
                for item in Items:
                    Nodename = item.data( 35 )
                    t_node_list.append( Nodename )
                for i in self.Gdata:
                    ViewNode  = i[3].split("_")[0]
                    InputNode = i[0]
                    if rv.commands.nodeExists( ViewNode ) and not InputNode in t_node_list :
                        rv.commands.deleteNode( ViewNode )    
                rv.commands.setViewNode( "defaultSequence" )
                self.rrfersh_ui( )
            elif action == item4:
                self.huanyuan()                
    def call_Get_Pix( self, path, isMov=False ):
        if isMov:
            try:
                ffmbc_path   = "C:/cgteamwork/bin/cgtw/ffmbc.exe"
                out_put = "C:/Users/" + os.environ["USERNAME"] + "/AppData/Local/Temp/"+ str(uuid.uuid4()) + ".jpg"
                cmd = '"' + ffmbc_path + '"' + " -i " +'"' + path + '"' + " -y -f image2  -vframes 1 -qscale 200 -s 96x72  " + '"' + out_put + '"'
                subprocess.Popen( cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT ).wait()
            except Exception,e:
                print False
            return out_put
        else:
            try:
                a_size = "96x72"
                convert_path = "C:/cgteamwork/bin/cgtw/convert.exe"
                out_put = "C:/Users/" + os.environ["USERNAME"] + "/AppData/Local/Temp/"+ str(uuid.uuid4()) + ".jpg"
                cmd = '"'+convert_path+'"'+' -quality 70 -thumbnail %s  '%a_size+'"'+path+'" '+'"'+out_put+'"'
                subprocess.Popen( cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT ).wait()
            except Exception,e:
                pass
            return out_put
    def slot_replace_source( self, itemparent  ):
        if itemparent[ 2 ] == "Y":
            item = itemparent[0]
            item.setSelected( True )
            self.tablewidget.setCurrentItem( item )   
            self.slot_item_clicked( item )
            
            
            PlayData = item.data( 32 )
            nodename = item.data( 34 )
            SourceNodeMedia = rv.commands.sourceMediaInfoList( nodename )
            for Media in SourceNodeMedia:    
                Path  = Media["file"]
                if Path == itemparent[1]:
                    if "%" in Path:
                        Pix = self.call_Get_Pix( Path%(int(Media["startFrame"])), False )
                    elif ".exr" in Path:
                        Pix = self.get_image_thumbnails( Path )                        
                    else:
                        Pix = self.call_Get_Pix( Path, True )
                    for ssss in range( len( self.Gdata ) ) :
                        if self.Gdata[ ssss ][1] == PlayData:
                            self.Gdata[ ssss ][0] = Path
                            self.Gdata[ ssss ][2] = Pix
            item.data( 33 ).setStyleSheet( "QLabel{border-image:url('%s');padding:5px;margin:0px;}"%Pix )
        elif itemparent[ 2 ] == "B":
            rv.commands.clearSession()
            self.tablewidget.clear()                 
            self.version_bc( itemparent[1] )
            rv.commands.setViewNode( "defaultLayout" )
        elif itemparent[ 2 ] == "C":
            rv.commands.clearSession()
            self.tablewidget.clear()                 
            self.version_bc( itemparent[1] )
            rv.commands.setViewNode( "defaultSequence" )
    def rrfersh_ui( self ):
        SourceNodeList = rv.commands.nodesOfType( "RVSource" )
        self.tablewidget.clear()
        self.tablewidget.setColumnCount( len(SourceNodeList) )           
        for i in range( len(SourceNodeList) ):
            SourceNode = SourceNodeList[i]
            for data in self.Gdata:
                if data[3] == SourceNode:
                    Label = QLabel()
                    Label.setStyleSheet( "QLabel{border-image:url('%s');padding:5px;margin:0px;}"%data[2] )
                    
                    laybel2 = QLabel()
                    laybel2.setText( data[4] )
                    laybel2.setFixedHeight( 28 )
                    widget = QWidget()
                    layout = QVBoxLayout()
                    layout.setContentsMargins( 2,2,2,2 )
                    layout.setSpacing( 0 )
                    widget.setLayout( layout )
                    layout.addWidget( Label )
                    layout.addWidget( laybel2 )
                    
                    self.tablewidget.setCellWidget( 0, i, widget )
                    item = QTableWidgetItem()
                    item.setData( 32, data[1] )
                    item.setData( 33, Label )
                    item.setData( 34, data[3] )  
                    item.setData( 35, data[0] )
                    self.tablewidget.setItem( 0, i , item)      
    def huanyuan( self ):
        rv.commands.clearSession()
        self.tablewidget.clear()     
        self.tablewidget.setColumnCount( len(self.Gdata) )
        for i in range( len( self.Gdata) ) :
            rv.commands.addSource( self.Gdata[i][0] )

            SourceNodeList = rv.commands.nodesOfType( "RVSource" )
            for s in range( len(SourceNodeList) ):
                SourceNode = SourceNodeList[s]  
                SourceNodeMedia = rv.commands.sourceMediaInfoList( SourceNode )
                for Media in SourceNodeMedia:    
                    Path  = Media["file"]
                    if Path == self.Gdata[i][0]:
                        self.Gdata[i][3] = SourceNode

            Label = QLabel()
            Label.setStyleSheet( "QLabel{border-image:url('%s');padding:5px;margin:0px;}"%self.Gdata[i][2] )
            laybel2 = QLabel()
            laybel2.setText( self.Gdata[i][4] )
            laybel2.setFixedHeight( 28 )
            widget = QWidget()
            layout = QVBoxLayout()
            layout.setContentsMargins( 2,2,2,2 )
            layout.setSpacing( 0 )
            widget.setLayout( layout )
            layout.addWidget( Label )
            layout.addWidget( laybel2 )            
            
            self.tablewidget.setCellWidget( 0, i, widget )
            item = QTableWidgetItem()
            item.setData( 32, self.Gdata[i][1] )
            item.setData( 33, Label )
            item.setData( 34, self.Gdata[i][3] )
            item.setData( 35, self.Gdata[i][0] )
            self.tablewidget.setItem( 0, i , item )
    def slot_framechanged( self ):
        if rv.commands.viewNode() == "defaultSequence":
            node = rv.commands.sourcesAtFrame( rv.commands.frame() )
            
            for i in range( self.tablewidget.columnCount() ):
                Item = self.tablewidget.item( 0, i )
                if node[0] == Item.data( 34 ):
                    Item.setSelected( True )
                    self.tablewidget.setCurrentItem( Item )  
    def get_first( self , data ):
        t_ = False
        for i in data:
            if i != []:
                t_ = i[-1]
                break
        return t_
    def version_bc( self, allfiles ):
        self.tablewidget.setColumnCount( 0 )
        for PLayMoV in allfiles:
            rv.commands.addSource( PLayMoV )
            NodeName = ''
            Pix = ''
            SourceNodeList = rv.commands.nodesOfType( "RVSource" )
            for i in range( len(SourceNodeList) ):
                SourceNode = SourceNodeList[i]  
                SourceNodeMedia = rv.commands.sourceMediaInfoList( SourceNode )
                for Media in SourceNodeMedia:    
                    Path  = Media["file"]
                    if Path == PLayMoV:
                        NodeName = SourceNode
                        if "%" in Path:
                            Pix = self.call_Get_Pix( Path%(int(Media["startFrame"])), False )
                        elif ".exr" in Path:
                            Pix = self.get_image_thumbnails( Path )                            
                        else:
                            Pix = self.call_Get_Pix( Path, True )
            column = self.tablewidget.columnCount()
            self.tablewidget.insertColumn( column )
                
                
                
            Label = QLabel()
            Label.setStyleSheet( "QLabel{border-image:url('%s');padding:5px;margin:0px;}"%Pix )
                
            laybel2 = QLabel()
            laybel2.setText( os.path.basename(PLayMoV) )
            laybel2.setFixedHeight( 28 )
            widget = QWidget()
            layout = QVBoxLayout()
            layout.setContentsMargins( 2,2,2,2 )
            layout.setSpacing( 0 )
            widget.setLayout( layout )
            layout.addWidget( Label )
            layout.addWidget( laybel2 )
                
            self.tablewidget.setCellWidget( 0, column, widget )
            item = QTableWidgetItem()
            item.setData( 32, [ PLayMoV ] )
            item.setData( 33, Label )
            item.setData( 34, NodeName )
            item.setData( 35, PLayMoV )
            self.tablewidget.setItem( 0, column , item )         
    def get_image_thumbnails( self, a_image, a_size="320x240", out_put=""):
        return ""
        #convert_path = "C:/cgteamwork/bin/cgtw/convert.exe"
        #if out_put=="":
            #out_put= os.environ["TMP"]+ "\\" + unicode(uuid.uuid4()) + ".jpg"
        #if os.path.exists(convert_path)==False:
            #return False
        #if os.path.exists( out_put ):
            #try:
                #os.remove(out_put)
            #except Exception,e:
                #return False
        #if os.path.exists(a_image)==False:
            #return False
        #temp_file=os.environ["TMP"]+"\\"+unicode(uuid.uuid4())+".jpg"
        #if os.path.exists(temp_file):
            #os.remove(temp_file)
        #shutil.copyfile(a_image, temp_file)
    
        #self.com_execCmd('"'+convert_path+'"'+' -quality 70 -thumbnail %s  '%a_size+'"'+temp_file+'" '+'"'+out_put+'"')
        #if os.path.exists(temp_file):
            #os.remove(temp_file)
        #if os.path.exists(out_put)==False or os.path.getsize(out_put) <=0:
            #return False
        #else:
            #out_put = out_put.replace( "\\", "/" )
            #return out_put            
    def com_execCmd( self, cmd ):
        t_text=''
        try:
            p = subprocess.Popen( cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                t_text = t_text + line
        except:
            return t_text
        return t_text       
class Version( QDialog ):
    signal = Signal( list )
    def __init__( self, itemparent ):
        super( Version, self ).__init__()
        self.itemparent = itemparent
        self.setWindowTitle( u"切换版本" )
        self.resize( 300, 400 )
        self.m_layout = QVBoxLayout()
        self.setLayout( self.m_layout )
        self.treewidget = QTreeWidget()
        self.treewidget.headerItem().setHidden(True) 
        self.m_layout.addWidget( self.treewidget )
        self.m_button = QPushButton()
        self.m_button.setText( u"切换版本" )
        self.m_button_b = QPushButton()
        self.m_button_b.setText( u"所选并播" )
        self.m_button_c = QPushButton()
        self.m_button_c.setText( u"所选串播" )        
        self.m_button.clicked.connect( self.slot_Y )
        self.m_button_b.clicked.connect( self.slot_B )
        self.m_button_c.clicked.connect( self.slot_C )
        layout_bottom = QHBoxLayout()
        layout_bottom.addStretch()
        layout_bottom.addWidget( self.m_button_b )
        layout_bottom.addWidget( self.m_button_c )
        layout_bottom.addWidget( self.m_button )
        self.m_layout.addLayout( layout_bottom )        
        self.NodeName = itemparent.data( 34 )
        SourceNodeMedia = rv.commands.sourceMediaInfoList( self.NodeName )
        for Media in SourceNodeMedia:        
            self.Files = Media["file"]
        playdata = itemparent.data( 32 )
        playdata = list( reversed( playdata ) )
        for i in  playdata:
            for s in i:
                item = QTreeWidgetItem( self.treewidget )
                t_name = os.path.basename( s )
                item.setText( 0, t_name )
                item.setData( 0, 32, s )   
                item.setData( 0,33,self.NodeName)
                if self.Files == s:
                    item.setCheckState( 0, Qt.Checked )
                    self.T_All_Checket = item
                else:
                    item.setCheckState( 0, Qt.Unchecked )
    def slot_Y( self ):
        itemlist = self.get_sle()
        if len( itemlist ) == 1:
            t_current_data = itemlist[0]
            if self.Files == t_current_data:
                self.close()
            else:
                rv.commands.setSourceMedia( self.NodeName, [t_current_data], "" )
                self.signal.emit( [self.itemparent, t_current_data, "Y" ] )
                self.close()
        else:
            QMessageBox.warning( self , u'错误', u"必须选中一项" )
            
    def slot_B( self ):
        itemlist = self.get_sle()
        self.signal.emit( [self.itemparent, itemlist, "B" ] )
        self.close()
    def slot_C( self ):
        itemlist = self.get_sle()
        self.signal.emit( [self.itemparent, itemlist, "C" ] )
        self.close()
    def get_sle( self ):
        List = []
        for count in range( self.treewidget.topLevelItemCount() ):
            item = self.treewidget.topLevelItem( count )        
            if item.checkState( 0 ) == Qt.Checked:
                List.append( item.data( 0, 32 ) )
        return List
#coding:utf8
import os
import re
import sys
import time
import uuid
import RvConfig
import subprocess
import glob

from PySide.QtCore     import *
from PySide.QtGui      import *
from PySide.QtWebKit   import * 


class PlayView( QDockWidget ):
    m_data_signal = Signal( list )
    def __init__( self, Parent ):
        super( PlayView, self ).__init__()
        self.Parent = Parent
        self.setUI()
        self.setData()
        self.setSignal()
        
    def setUI( self ):
        self.setObjectName( "Play" )
        self.setAllowedAreas( Qt.RightDockWidgetArea )
        self.setWindowTitle( "Play" )
        self.setMinimumWidth( 250 )
        self.m_cgteamWorkBox = QWidget()
        self.m_cgteamWorkBox_layout = QVBoxLayout()
        self.m_cgteamWorkBox.setLayout( self.m_cgteamWorkBox_layout )     
        self.setWidget( self.m_cgteamWorkBox )


        self.m_label_project = QLabel()
        self.m_label_project.setText( u"项目:" )
        self.m_label_project.setFixedWidth( 40 )
        self.m_combobox_project = QComboBox()
        self.m_combobox_project.setFixedWidth( 120 )
        
        
        self.m_label_module = QLabel()
        self.m_label_module.setText( u"模块:" )
        self.m_label_module.setFixedWidth( 40 )
        self.m_combobox_module = QComboBox()
        self.m_combobox_module.setFixedWidth( 120 )
        
        
        
        self.m_label_eps = QLabel()
        self.m_label_eps.setText( u"场次:" )
        self.m_label_eps.setFixedWidth( 40 )
        self.m_combobox_eps = QComboBox()
        self.m_combobox_eps.setFixedWidth( 120 )
        self.m_combobox_type = QCheckBox()
        self.m_combobox_type.setText( u'整场模式' )
        #self.m_combobox_type.setChecked( True )
        
        
        self.m_label_filebox = QLabel()
        self.m_label_filebox.setText( u"阶段/文件筐:" )
        self.m_treewidget = QTreeWidget()
        self.m_treewidget.headerItem().setHidden(True) 
        
        
        self.m_cgteamWorkBox_layout_1 = QHBoxLayout()
        self.m_cgteamWorkBox_layout_1.addWidget( self.m_label_project )
        self.m_cgteamWorkBox_layout_1.addWidget( self.m_combobox_project ) 
        self.m_cgteamWorkBox_layout_1.addStretch()
        self.m_cgteamWorkBox_layout.addLayout( self.m_cgteamWorkBox_layout_1 )
        
        
        self.m_cgteamWorkBox_layout_2 = QHBoxLayout()
        self.m_cgteamWorkBox_layout_2.addWidget( self.m_label_module )
        self.m_cgteamWorkBox_layout_2.addWidget( self.m_combobox_module ) 
        self.m_cgteamWorkBox_layout_2.addStretch()
        self.m_cgteamWorkBox_layout.addLayout( self.m_cgteamWorkBox_layout_2 )
        
        
        self.m_cgteamWorkBox_layout_3 = QHBoxLayout()
        self.m_cgteamWorkBox_layout_3.addWidget( self.m_label_eps )
        self.m_cgteamWorkBox_layout_3.addWidget( self.m_combobox_eps ) 
        self.m_cgteamWorkBox_layout_3.addStretch()
        self.m_cgteamWorkBox_layout_3.addWidget( self.m_combobox_type ) 
        self.m_cgteamWorkBox_layout.addLayout( self.m_cgteamWorkBox_layout_3 )
        
        
        self.m_cgteamWorkBox_layout.addWidget( self.m_label_filebox )
        self.m_cgteamWorkBox_layout.addWidget( self.m_treewidget )
        

        self.m_button_left = QCheckBox()
        self.m_button_left.setText(u"播放左右眼")
        self.m_button_Filter = QCheckBox()
        self.m_button_Filter.setText( u"仅播放当天" )
        self.m_button_Filter_lastest = QCheckBox()
        self.m_button_Filter_lastest.setText(u"按最新时间播放")
        self.m_button_mov = QCheckBox()
        self.m_button_mov.setText( u"仅视频文件" )    
        self.m_button_mov.setChecked( True )
        self.m_button_mov.toggled.connect( self.call_mov )
        self.m_button_sig = QCheckBox()
        self.m_button_sig.setText( u"仅单帧" )    
        self.m_button_sig.setChecked( False )
        self.m_button_sig.toggled.connect( self.call_sig )
        self.m_button_epsplay = QPushButton()
        self.m_button_epsplay.setText( u"播放" )       
        
        self.m_cgteamWorkBox_layout_4 = QHBoxLayout()
        self.m_cgteamWorkBox_layout_4.addWidget(self.m_button_left)
        self.m_cgteamWorkBox_layout_4.addWidget( self.m_button_Filter )
        self.m_cgteamWorkBox_layout_4.addWidget(self.m_button_Filter_lastest)
        self.m_cgteamWorkBox_layout_4.addWidget( self.m_button_mov )
        self.m_cgteamWorkBox_layout_4.addWidget( self.m_button_sig )
        self.m_cgteamWorkBox_layout_4.addStretch()
        self.m_cgteamWorkBox_layout_4.addWidget( self.m_button_epsplay ) 
        self.m_cgteamWorkBox_layout.addLayout( self.m_cgteamWorkBox_layout_4 )         
    def call_mov( self ):
        if self.m_button_mov.isChecked():
            self.m_button_sig.setChecked( False )        
    def call_sig( self ):
        if self.m_button_sig.isChecked():
            self.m_button_mov.setChecked( False )
        
    def setData( self ):
        self.m_tw = self.Parent.m_tw
        try:
            t_project_class = self.m_tw.info_module("public","project")
            t_project_class.init_with_filter([["project.database","has","%"], "and", ["project.status", "!=", "Close"]])
            t_project_data  = t_project_class.get(["project.database","project.code"])
            for data in t_project_data:
                if not data["project.code"] in RvConfig.Hidden_Project:
                    self.m_combobox_project.addItem(data["project.code"], data["project.database"])
        except Exception, e:
            self.m_combobox_project.clear()
        for module in RvConfig.Show_Module:
            self.m_combobox_module.addItem(module[0], module[1])
        self.call_refersh_combobox_eps()
        self.call_refersh_treewidget()
    def setSignal( self ):
        self.m_combobox_module.currentIndexChanged.connect( self.slot_module )
        self.m_combobox_eps.activated.connect( self.slot_eps )     
        self.m_combobox_type.toggled.connect( self.call_refersh_treewidget )
        self.m_button_epsplay.clicked.connect( self.call_play )
        self.m_data_signal.connect( self.Parent.slot_signal )
        self.m_combobox_project.currentIndexChanged.connect(self.call_refersh_combobox_eps)
        self.m_combobox_module.currentIndexChanged.connect(self.call_refersh_combobox_eps)
    def call_refersh_combobox_eps( self ):
        self.m_combobox_eps.clear()
        database = self.m_combobox_project.itemData( self.m_combobox_project.currentIndex(), 32 )      
        shot_task_class  = self.m_tw.task_module( database, "shot_task" )
        eps_id_list = shot_task_class.get_distinct_with_filter( "eps.id", [["eps.eps_name","has","%"]], ["eps.eps_name"] )
        if type(eps_id_list)!=list:
            QMessageBox.warning( self, "Error", "Get data from CgTeamWork fail!" )
            return []
        else:
            eps_class = self.m_tw.info_module( database,"eps" )
            eps_class.init_with_id( eps_id_list )
            eps_name_and_id = eps_class.get(["eps.eps_name"],["eps.eps_name"])
            if type(eps_name_and_id)!=list:
                QMessageBox.warning( self, "Error", "Get data from CgTeamWork fail!" )
                return []
            else:
                for data in eps_name_and_id:
                    self.m_combobox_eps.addItem(data["eps.eps_name"], data["id"])
    def call_refersh_treewidget( self ):
        self.m_treewidget.clear()
        module   = self.m_combobox_module.itemData( self.m_combobox_module.currentIndex(), 32 )
        database = self.m_combobox_project.itemData( self.m_combobox_project.currentIndex(), 32 )
        if "xcm" in database.lower():
            ProjectStege = RvConfig.SHotTaskShowFileBOxFXCM
        elif "dsf" in database.lower():
            ProjectStege = RvConfig.SHotTaskShowFileBOxDSF
        else:
            ProjectStege = RvConfig.SHotTaskShowFileBOx
        
        if module == 'asset_task':
            for filebox in RvConfig.AssetTaskShowFileBoX:
                item = QTreeWidgetItem( self.m_treewidget )
                item.setText( 0, filebox[0] + "--->" + filebox[1] )  
                item.setData( 0, 32, filebox )
                item.setCheckState( 0, Qt.Unchecked )             
        else:
            if self.m_combobox_type.isChecked():
                for filebox in ProjectStege:
                    item = QTreeWidgetItem( self.m_treewidget )
                    item.setText( 0, filebox[0] + "--->" + filebox[1] )  
                    item.setData( 0, 32, filebox )
                    item.setCheckState( 0, Qt.Unchecked )  
            else:
                #database = self.m_combobox_project.itemData( self.m_combobox_project.currentIndex(), 32 )
                t_eps_id = self.m_combobox_eps.itemData( self.m_combobox_eps.currentIndex(), 32 )
                shot_task_class = self.m_tw.task_module( database ,"shot_task")
                t_all_shot      = shot_task_class.get_distinct_with_filter( "shot.shot", [["eps.id","=",t_eps_id]],["shot.shot"])
                for shot in t_all_shot:
                    Topitem = QTreeWidgetItem( self.m_treewidget )
                    Topitem.setText(0,shot)     
                    for filebox in ProjectStege:     
                        item = QTreeWidgetItem( Topitem )
                        item.setText( 0, filebox[0] + "--->" + filebox[1] )  
                        item.setData( 0, 32, filebox )
                        item.setCheckState( 0, Qt.Unchecked )     
    def slot_module( self, a_index ):
        module = self.m_combobox_module.itemData( self.m_combobox_module.currentIndex(), 32 )
        if module == 'asset_task':
            self.m_label_eps.setHidden( True )
            self.m_combobox_eps.setHidden( True )
            self.m_combobox_type.setHidden( True )
            self.call_refersh_treewidget()     
        else:
            self.m_label_eps.setHidden( False )
            self.m_combobox_eps.setHidden( False )
            self.m_combobox_type.setHidden( False )
            self.call_refersh_treewidget()     
    def slot_eps( self, a_index ):
        self.call_refersh_treewidget()     
    def call_play( self ):
        Shot_List = []
        Dict      = {}    
        
        database = self.m_combobox_project.itemData( self.m_combobox_project.currentIndex(), 32 )
        module = self.m_combobox_module.itemData( self.m_combobox_module.currentIndex(), 32 )
        if module == 'shot_task':
            # all seq
            if self.m_combobox_type.isChecked():
                t_eps_id   = self.m_combobox_eps.itemData( self.m_combobox_eps.currentIndex(), 32 )
                t_filebox_dict = self.call_get_fileBoxID_PipeID_Data( database, module )
                t_filebox_list = []
                for count in range( self.m_treewidget.topLevelItemCount() ):
                    item = self.m_treewidget.topLevelItem( count )
                    if item.checkState( 0 ) == Qt.Checked:
                        for ss in t_filebox_dict[ item.data( 0, 32 )[0] ]:
                            if ss['title'] == item.data( 0, 32 )[1]:
                                t_filebox_list.append( [ item.data( 0, 32 )[0], ss['id'] ] )
                                break

                shot_task       = self.m_tw.task_module( database, "shot_task" )
                for filebox in t_filebox_list:
                    t_task_id_list      = shot_task.get_distinct_with_filter( "shot_task.id", [ ["eps.id", "=", t_eps_id], "and", ["shot_task.pipeline", "=", filebox[0] ] ], ["shot.shot","shot_task.pipeline_sort_id"] )
                    for taskId in t_task_id_list:
                        shot_task = self.m_tw.task_module( database, "shot_task", [taskId] )
                        Filebox  = shot_task.get_filebox_with_filebox_id( filebox[1] )
                        Shot     = shot_task.get( ["shot.shot"] )[0]["shot.shot"]
                        PathList = self.call_Path( Filebox )
                        #print PathList, "sssss"
                        if not Shot in Shot_List:
                            Shot_List.append( Shot )
                        if Dict.has_key( Shot ):
                            OldList = Dict[ Shot ]
                            NewList = [ PathList ]
                            Dict[ Shot ] = NewList + OldList
                        else:
                            Dict[ Shot ] = [ PathList ]
            else:
                # single
                shot_task       = self.m_tw.task_module( database, "shot_task" )
                t_eps_id   = self.m_combobox_eps.itemData( self.m_combobox_eps.currentIndex(), 32 )
                t_filebox_dict = self.call_get_fileBoxID_PipeID_Data( database, module )
                for count in range( self.m_treewidget.topLevelItemCount() ):
                    item = self.m_treewidget.topLevelItem( count )  
                    for i in range( item.childCount() ):
                        cliendItem = item.child( i )                        
                        if cliendItem.checkState( 0 ) == Qt.Checked:
                            for ss in t_filebox_dict[ cliendItem.data( 0, 32 )[0] ]:
                                if ss['title'] == cliendItem.data( 0, 32 )[1]:
                                    t_task_id  = shot_task.get_distinct_with_filter( "shot_task.id", [ ["eps.id", "=", t_eps_id], "and", [ 'shot.shot', '=', item.text(0) ],"and", ["shot_task.pipeline", "=", cliendItem.data( 0, 32 )[0] ] ], ["shot.shot","shot_task.pipeline_sort_id"] )
                                    if len( t_task_id ) == 1:
                                        shot_task = self.m_tw.task_module( database, "shot_task", [t_task_id[0]] )
                                        Filebox  = shot_task.get_filebox_with_filebox_id( ss['id'] )
                                        Shot     = shot_task.get( ["shot.shot"] )[0]["shot.shot"]
                                        PathList = self.call_Path( Filebox )
                                        
                                        if not Shot in Shot_List:
                                            Shot_List.append( Shot )
                                        if Dict.has_key( Shot ):
                                            OldList = Dict[ Shot ]
                                            NewList = [ PathList ]
                                            Dict[ Shot ] = NewList + OldList
                                        else:
                                            Dict[ Shot ] = [ PathList ]                                    
                                        break
        else:
            t_filebox_dict = self.call_get_fileBoxID_PipeID_Data( database, module )
            t_filebox_list = []
            for count in range( self.m_treewidget.topLevelItemCount() ):
                item = self.m_treewidget.topLevelItem( count )
                if item.checkState( 0 ) == Qt.Checked:
                    for ss in t_filebox_dict[ item.data( 0, 32 )[0] ]:
                        if ss['title'] == item.data( 0, 32 )[1]:
                            t_filebox_list.append( [ item.data( 0, 32 )[0], ss['id'] ] )
                            break

            for FileBoxData in t_filebox_list:
                t_pipe       = FileBoxData[0]
                t_filebox_id = FileBoxData[1]  
                asset_task   = self.m_tw.task_module( database, module )
                t_task_id_list = asset_task.get_distinct_with_filter( "asset_task.id", [ ["asset_task.pipeline", "=", t_pipe] ], ["asset.asset_name","asset_task.pipeline_sort_id"] )
                for taskId in t_task_id_list:
                    asse_task = self.m_tw.task_module( database, "asset_task", [taskId] )
                    Filebox   = asse_task.get_filebox_with_filebox_id( t_filebox_id )
                    asset_name = asse_task.get( ["asset.asset_name"] )[0]["asset.asset_name"]
                    PathList   = self.call_Path( Filebox )
                    if not asset_name in Shot_List:
                        Shot_List.append( asset_name )
                    if Dict.has_key( asset_name ):
                        OldList = Dict[ asset_name ]
                        NewList = [ PathList ]
                        Dict[ asset_name ] = NewList + OldList
                    else:
                        Dict[ asset_name ] = [ PathList ]        

        Shot_List = list(sorted( Shot_List ))
        #print "Shot_List: ", Shot_List
        #print "Dict: ", Dict
        self.m_data_signal.emit( [ Shot_List, Dict ] )
    def call_get_fileBoxID_PipeID_Data( self,database,module ):
        T_All_Dict = {}
        t_pipeline_list = self.m_tw.pipeline( database ).get_with_module( module, ["name","#id"] )
        for pipeline in t_pipeline_list:
            t_filebox_list = self.m_tw.filebox( database ).get_with_pipeline_id( pipeline["id"], module )
            T_All_Dict[ pipeline['name'] ] = t_filebox_list
        return T_All_Dict
    
    
    def call_Path( self, Filebox ):
        Path           = Filebox["path"]
        Rule           = Filebox["rule"]
        List           = []
        if not os.path.exists( Path ):
            print "Non[320]"
            return []
        if Filebox["classify"] == "3DConversion":
            if self.m_button_mov.isChecked():
                _subDir = glob.glob(Path + "/*v??_v??")
                _subDir.sort()
                if not _subDir:
                    return []
                Path = _subDir[-1].replace("\\", "/")
                LRPath = list()
                for unit in os.listdir(Path):
                    if "_L" in unit:
                        LRPath.append(os.path.join(Path, unit).replace("\\", "/"))
                    elif "R" in unit:
                        LRPath.append(os.path.join(Path, unit).replace("\\", "/"))
                if len(LRPath) < 2:
                    return []
                LRPath.sort()
                return [LRPath[0]]
            else:
                _subDir = glob.glob(Path + "/*v??_L_v??")
                if not _subDir:
                    return []
                Path = _subDir[0].replace("\\", "/")
                return [Path]
        # elif Filebox["classify"] == "ani":
        #     print Filebox, "ssssss"
        else:
            for PathClient in os.listdir( Path ):
                if not ".db" in PathClient:
                    if self.com_match_CGRule( Rule, PathClient ):
                        if os.path.isfile( Path + "/" + PathClient ) :
                            if self.m_button_mov.isChecked():
                                if ".mov" in PathClient or ".mp4" in PathClient or ".avi" in PathClient:
                                    T_abs = Path + "/" + PathClient
                                    T_abs = T_abs.replace("\\","/")
                                    if self.is_today( T_abs ):
                                        List.append( T_abs )
                            if self.m_button_sig.isChecked():
                                if ".exr" in PathClient:
                                    T_abs = Path + "/" + PathClient
                                    T_abs = T_abs.replace("\\","/")
                                    if self.is_today( T_abs ):
                                        List.append( T_abs )
                        else:
                            #print PathClient, "sssss"
                            if self.m_button_mov.isChecked() == False:
                                if self.m_button_sig.isChecked() == False:
                                    for PathClientClient in os.listdir( Path + "/" + PathClient ):
                                        if not ".db" in PathClientClient:
                                            Re_version_findall = re.findall( "\.[0-9]+\.", PathClientClient )
                                            if Re_version_findall != []:
                                                for Re_version in Re_version_findall:
                                                    for number in re.findall( "[0-9]+", Re_version ):
                                                        PathClientClient = PathClientClient.replace( Re_version, Re_version.replace( number, "%" + str(len(number)).zfill( len(number) ) + "d" ) )
                                                        T_abs = Path + "/" + PathClient + "/" + PathClientClient
                                                        T_abs = T_abs.replace("\\","/")
                                                        if self.is_today( T_abs ):
                                                            List.append( T_abs )
                            else:
                                # left right
                                for PathClientClient in os.listdir(Path + "/" + PathClient):
                                    if not ".db" in PathClientClient:
                                        #if "_L_" in PathClientClient:
                                        if "_L" in PathClientClient and "_Ly" not in PathClientClient:
                                            T_abs = Path + "/" + PathClient + "/" + PathClientClient
                                            T_abs = T_abs.replace("\\", "/")
                                            if self.is_today(T_abs):
                                                List.append(T_abs)
            lis = sorted(list(set(List)))
            lis = self.get_left_sort(lis)
            if self.m_button_Filter_lastest.isChecked():
                return self.get_time_sort(lis)

            else:
                return self.get_v_sort( lis )

    def com_match_CGRule( self, a_CGRuleList, a_file ):
        for CGRule in a_CGRuleList:
            RERule = CGRule.replace("#", "[0-9]").replace("?", "[a-zA-Z]").replace("*", "[a-zA-Z0-9_]*").replace(".","\.")
            if re.match( RERule, a_file ):
                return True
        return False

    def is_today( self, path ):
        if self.m_button_Filter.isChecked():
            if time.strftime(  "%Y/%m/%d", time.localtime(),  ) == time.strftime( "%Y/%m/%d",  time.localtime( os.path.getmtime( path ) ) ):
                return True
            else:
                return False
        else:
            return True

    def get_v_sort( self, a_list ):
        new_data = {}
        new_list = []
        for a in a_list:
            basename = os.path.splitext( os.path.basename( a ) )[0]
            vNum = 0
            try:
                vNum = basename.index("_v")
            except:
                pass    
            #if len(basename)>3 and re.match( "v[0-9][0-9]", basename[-3:].lower() ):
                #v = basename[-2:]
            if len(basename)>3 and vNum:
                v = basename[vNum+2:vNum+4]
                new_list.append( v )
                if new_data.has_key( v ):
                    new_data[ v ].append( a )
                else:
                    new_data[ v ] = [ a ]
            else:
                v = "00"
                new_list.append( v ) 
                if new_data.has_key( v ):
                    new_data[ v ].append( a )
                else:
                    new_data[ v ] = [ a ]                
        res_list = []
        new_list = sorted(list(set(new_list)))   
        for i in new_list:
            n = sorted(list(set(new_data[i])))
            res_list = res_list + n
        return res_list

    def get_time_sort(self, a_list):
        new_data = {}
        new_list = []
        for a in a_list:
            t = os.path.getmtime(a)
            new_data[str(t)] = a

        sort_list = new_data.keys()
        sort_list.sort()
        for unit in sort_list:
            new_list.append(new_data[unit])
        return new_list

    def get_left_sort(self, a_list):
        left = []
        nomal = []
        for unit in a_list:
            #if "_L_" in unit:
            if "_L" in unit  and "_Ly" not in unit:
                left.append(unit)
            else:
                nomal.append(unit)
        if self.m_button_left.isChecked():
            return left
        else:
            return nomal










##coding:utf8
#import os
#import rv
#import re
#import sys
#import time
#import uuid
#import RvConfig
#import subprocess

#from PySide.QtCore     import *
#from PySide.QtGui      import *
#from PySide.QtWebKit   import * 




#class PlayView( QDockWidget ):
    #m_signal = Signal( list )
    #def __init__( self, Parent ):
        #super( PlayView, self ).__init__()
        #self.Parent = Parent
        #self.setUI()
        #self.setDatas()
        #self.setSignal()
    #def setUI( self ):
        #self.setObjectName( "Play" )
        #self.setAllowedAreas( Qt.RightDockWidgetArea )
        #self.setWindowTitle( "Play" )
        #self.setMinimumWidth( 250 )
        #self.resize( 250, rv.qtutils.sessionWindow().size().height() )

        
        #self.m_cgteamWorkBox = QWidget()
        #self.m_cgteamWorkBox_layout = QVBoxLayout()
        #self.m_cgteamWorkBox.setLayout( self.m_cgteamWorkBox_layout )     
        #self.setWidget( self.m_cgteamWorkBox )


        #self.m_label_project = QLabel()
        #self.m_label_project.setText( u"项目:" )
        #self.m_label_project.setFixedWidth( 40 )
        #self.m_combobox_project = QComboBox()
        #self.m_combobox_project.setFixedWidth( 120 )
        
        
        #self.m_label_module = QLabel()
        #self.m_label_module.setText( u"模块:" )
        #self.m_label_module.setFixedWidth( 40 )
        #self.m_combobox_module = QComboBox()
        #self.m_combobox_module.setFixedWidth( 120 )
        
        
        
        #self.m_label_eps = QLabel()
        #self.m_label_eps.setText( u"场次:" )
        #self.m_label_eps.setFixedWidth( 40 )
        #self.m_combobox_eps = QComboBox()
        #self.m_combobox_eps.setFixedWidth( 120 )
        
        
        #self.m_label_filebox = QLabel()
        #self.m_label_filebox.setText( u"阶段/文件筐:" )
        #self.m_treewidget = QTreeWidget()
        #self.m_treewidget.headerItem().setHidden(True) 
        
        
        #self.m_cgteamWorkBox_layout_1 = QHBoxLayout()
        #self.m_cgteamWorkBox_layout_1.addWidget( self.m_label_project )
        #self.m_cgteamWorkBox_layout_1.addWidget( self.m_combobox_project ) 
        #self.m_cgteamWorkBox_layout_1.addStretch()
        #self.m_cgteamWorkBox_layout.addLayout( self.m_cgteamWorkBox_layout_1 )
        
        
        #self.m_cgteamWorkBox_layout_2 = QHBoxLayout()
        #self.m_cgteamWorkBox_layout_2.addWidget( self.m_label_module )
        #self.m_cgteamWorkBox_layout_2.addWidget( self.m_combobox_module ) 
        #self.m_cgteamWorkBox_layout_2.addStretch()
        #self.m_cgteamWorkBox_layout.addLayout( self.m_cgteamWorkBox_layout_2 )
        
        
        #self.m_cgteamWorkBox_layout_3 = QHBoxLayout()
        #self.m_cgteamWorkBox_layout_3.addWidget( self.m_label_eps )
        #self.m_cgteamWorkBox_layout_3.addWidget( self.m_combobox_eps ) 
        #self.m_cgteamWorkBox_layout_3.addStretch()
        #self.m_cgteamWorkBox_layout.addLayout( self.m_cgteamWorkBox_layout_3 )
        
        
        #self.m_cgteamWorkBox_layout.addWidget( self.m_label_filebox )
        #self.m_cgteamWorkBox_layout.addWidget( self.m_treewidget )
        
        
        #self.m_button_Filter = QPushButton()
        #self.m_button_Filter.setText( u"过滤" )    
        
        #self.m_button_epsplay = QPushButton()
        #self.m_button_epsplay.setText( u"播放" )       
        
        #self.m_cgteamWorkBox_layout_4 = QHBoxLayout()
        #self.m_cgteamWorkBox_layout_4.addStretch()
        #self.m_cgteamWorkBox_layout_4.addWidget( self.m_button_Filter ) 
        #self.m_cgteamWorkBox_layout_4.addWidget( self.m_button_epsplay ) 
        #self.m_cgteamWorkBox_layout.addLayout( self.m_cgteamWorkBox_layout_4 )            
    #def setDatas( self ):
        #self.m_tw = self.Parent.m_tw
        #try:
            #t_project_class = self.m_tw.info_module("public","project")
            #t_project_class.init_with_filter([["project.database","has","%"], "and", ["project.status", "!=", "Close"]])
            #t_project_data  = t_project_class.get(["project.database","project.code"])
            #for data in t_project_data:
                #if not data["project.code"] in RvConfig.Hidden_Project:
                    #self.m_combobox_project.addItem(data["project.code"], data["project.database"])
        #except Exception, e:
            #self.m_combobox_project.clear()
            

        #for module in RvConfig.Show_Module:
            #self.m_combobox_module.addItem(module[0], module[1])
        
        #self.call_eps_AddItems( 0 )
        #self.call_pipe_addItems( 'shot_task' )
    #def setSignal( self ):
        #self.m_combobox_project.currentIndexChanged.connect( self.slot_project )
        #self.m_combobox_module.currentIndexChanged.connect( self.slot_module )
        #self.m_combobox_eps.activated.connect( self.slot_eps )
        #self.m_treewidget.itemClicked.connect( self.slot_tree )
        #self.m_button_Filter.clicked.connect( self.slot_filter )
        #self.m_button_epsplay.clicked.connect( self.slot_paly )
        #self.m_signal.connect( self.Parent.slot_signal )
    #def slot_project( self, Pindex ):
        #module = self.m_combobox_module.itemData( self.m_combobox_module.currentIndex(), 32 )
        #if module == 'asset_task':
            #self.m_label_eps.setHidden( True )
            #self.m_combobox_eps.setHidden( True )
            #self.call_pipe_addItems( 'asset_task' )
        #else:
            #self.m_label_eps.setHidden( False )
            #self.m_combobox_eps.setHidden( False )            
            #self.call_eps_AddItems( Pindex )
            #self.call_pipe_addItems( 'shot_task' )
    #def slot_module( self, a_index ):
        #module = self.m_combobox_module.itemData( self.m_combobox_module.currentIndex(), 32 )
        #if module == 'asset_task':
            #self.m_label_eps.setHidden( True )
            #self.m_combobox_eps.setHidden( True )
            #self.call_pipe_addItems( 'asset_task' )
        #else:
            #self.m_label_eps.setHidden( False )
            #self.m_combobox_eps.setHidden( False )
            #self.call_pipe_addItems( 'shot_task' )
    #def slot_eps( self, a_index ):
        #self.call_pipe_addItems( 'shot_task' )
    #def slot_tree( self, index ):
        #filebox_id = index.data( 0, 32 )
        #t_pipe     = index.data( 0, 33 )
        #if type(filebox_id) in [ str, unicode ] and type(t_pipe) in [ str, unicode ]: 
            #data       = filebox_id + "|@|" + t_pipe
            #if index.checkState( 0 ) == Qt.Unchecked:
                #if data in RvConfig.CurrentFileBoxList:
                    #RvConfig.CurrentFileBoxList.remove( data )
            #else:
                #if not data in RvConfig.CurrentFileBoxList:
                    #RvConfig.CurrentFileBoxList.append( data )
    #def call_eps_AddItems( self, Pindex ):
        #self.m_combobox_eps.clear()
        #database = self.m_combobox_project.itemData( Pindex, 32 )        
        #shot_task_class  = self.m_tw.task_module( database, "shot_task" )
        #eps_id_list = shot_task_class.get_distinct_with_filter( "eps.id", [["eps.eps_name","has","%"]], ["eps.eps_name"] )
        #if type(eps_id_list)!=list:
            #QMessageBox.warning( self, "Error", "Get data from CgTeamWork fail!" )
            #return []
        #else:
            #eps_class = self.m_tw.info_module( database,"eps" )
            #eps_class.init_with_id( eps_id_list )
            #eps_name_and_id = eps_class.get(["eps.eps_name"],["eps.eps_name"])
            #if type(eps_name_and_id)!=list:
                #QMessageBox.warning( self, "Error", "Get data from CgTeamWork fail!" )
                #return []
            #else:
                #for data in eps_name_and_id:
                    #self.m_combobox_eps.addItem(data["eps.eps_name"], data["id"])
    #def call_pipe_addItems( self, module ):
        #database = self.m_combobox_project.itemData( self.m_combobox_project.currentIndex(), 32 )        
        #if module == 'asset_task':
            #self.m_treewidget.clear()
            #RvConfig.CurrentFileBoxList = []
            #asset_task_class = self.m_tw.task_module( database , module )
            #t_all_pipeline  = asset_task_class.get_distinct_with_filter( "asset_task.pipeline", [ ["asset_task.id","has",'%'] ],["asset_task.pipeline_sort_id"])
            #t_pipeline_list = self.m_tw.pipeline( database ).get_with_module( "asset_task", ["name","#id"] )    
            #if type(t_all_pipeline) == list and type(t_pipeline_list) == list:
                #for t_pipeline in t_all_pipeline:
                    #Topitem = QTreeWidgetItem( self.m_treewidget )
                    #Topitem.setText(0,t_pipeline)
                    #for pipe in t_pipeline_list:
                        #if pipe["name"] == t_pipeline:
                            #t_filebox_list= self.m_tw.filebox( database ).get_with_pipeline_id( pipe["id"], "asset_task" )
                            #if type(t_filebox_list)==list and len(t_filebox_list)>0:
                                #for filebox in t_filebox_list:
                                    #t_name    = filebox["title"]
                                    #t_id      = filebox["id"]      
                                    #item = QTreeWidgetItem( Topitem )
                                    #item.setText( 0, t_name )  
                                    #item.setData( 0, 32, t_id )
                                    #item.setData( 0, 33, pipe["name"] )
                                    #item.setCheckState( 0, Qt.Unchecked )
            #else:
                #QMessageBox.warning( self, "Error", "Get data from CgTeamWork fail!" )
        #else:
            #t_eps_id = self.m_combobox_eps.itemData( self.m_combobox_eps.currentIndex(), 32 )
            #self.m_treewidget.clear()
            #RvConfig.CurrentFileBoxList = []
            #shot_task_class = self.m_tw.task_module( database ,"shot_task")
            #t_all_pipeline  = shot_task_class.get_distinct_with_filter( "shot_task.pipeline", [["eps.id","=",t_eps_id]],["shot_task.pipeline_sort_id"])
            #t_pipeline_list = self.m_tw.pipeline( database ).get_with_module( "shot_task", ["name","#id"] )
            #if type(t_all_pipeline) == list and type(t_pipeline_list) == list:
                #for t_pipeline in t_all_pipeline:
                    #Topitem = QTreeWidgetItem( self.m_treewidget )
                    #Topitem.setText(0,t_pipeline)
                    #for pipe in t_pipeline_list:
                        #if pipe["name"] == t_pipeline:
                            #t_filebox_list= self.m_tw.filebox( database ).get_with_pipeline_id( pipe["id"], "shot_task" )
                            #if type(t_filebox_list)==list and len(t_filebox_list)>0:
                                #for filebox in t_filebox_list:
                                    #t_name    = filebox["title"]
                                    #t_id      = filebox["id"]      
                                    #item = QTreeWidgetItem( Topitem )
                                    #item.setText( 0, t_name )  
                                    #item.setData( 0, 32, t_id )
                                    #item.setData( 0, 33, pipe["name"] )
                                    #item.setCheckState( 0, Qt.Unchecked )
            #else:
                #QMessageBox.warning( self, "Error", "Get data from CgTeamWork fail!" )
    #def slot_filter( self ):
        #self.GFilterView = FilterView()
        #self.GFilterView.exec_()
    #def slot_paly( self ):
        #Shot_List = []
        #Dict      = {}    

        #timeRule  = []
        #if len( RvConfig.FilterList ) != 0:
            #for timerext in RvConfig.FilterList[ 0 ].split( ";" ):
                #time_1 = timerext.split(",")[0][1:].strip().lower()
                #time_2 = timerext.split(",")[1][:-1].strip().lower()
                #timeRule.append( [ time_1, time_2 ] )
            
            
        #module = self.m_combobox_module.itemData( self.m_combobox_module.currentIndex(), 32 )
        #database     = self.m_combobox_project.itemData( self.m_combobox_project.currentIndex(), 32 )
        #if module == 'shot_task':
            #t_eps_id     = self.m_combobox_eps.itemData( self.m_combobox_eps.currentIndex(), 32 )
            #for FileBoxData in RvConfig.CurrentFileBoxList:
                #t_pipe       = FileBoxData.split( "|@|" )[1]
                #t_filebox_id = FileBoxData.split( "|@|" )[0]  
                #shot_task    = self.m_tw.task_module( database, "shot_task" )
                #t_task_id_list = shot_task.get_distinct_with_filter( "shot_task.id", [ ["eps.id", "=", t_eps_id], "and", ["shot_task.pipeline", "=", t_pipe] ], ["shot.shot","shot_task.pipeline_sort_id"] )
                #for taskId in t_task_id_list:
                    #shot_task = self.m_tw.task_module( database, "shot_task", [taskId] )
                    #Filebox  = shot_task.get_filebox_with_filebox_id( t_filebox_id )
                    #Shot     = shot_task.get( ["shot.shot"] )[0]["shot.shot"]   
                    #PathList = self.call_Path( Filebox , timeRule )
                    #if not Shot in Shot_List:
                        #Shot_List.append( Shot )
                    #if Dict.has_key( Shot ):
                        #OldList = Dict[ Shot ]
                        #NewList = [ PathList ]
                        #Dict[ Shot ] = NewList + OldList
                    #else:
                        #Dict[ Shot ] = [ PathList ]
        #else:
            #for FileBoxData in RvConfig.CurrentFileBoxList:
                #t_pipe       = FileBoxData.split( "|@|" )[1]
                #t_filebox_id = FileBoxData.split( "|@|" )[0]  
                #asset_task   = self.m_tw.task_module( database, module )
                #t_task_id_list = asset_task.get_distinct_with_filter( "asset_task.id", [ ["asset_task.pipeline", "=", t_pipe] ], ["asset.asset_name","asset_task.pipeline_sort_id"] )
                #for taskId in t_task_id_list:
                    #asse_task = self.m_tw.task_module( database, "asset_task", [taskId] )
                    #Filebox   = asse_task.get_filebox_with_filebox_id( t_filebox_id )
                    #asset_name = asse_task.get( ["asset.asset_name"] )[0]["asset.asset_name"]   
                    #PathList = self.call_Path( Filebox , timeRule )
                    #if not asset_name in Shot_List:
                        #Shot_List.append( asset_name )
                    #if Dict.has_key( asset_name ):
                        #OldList = Dict[ asset_name ]
                        #NewList = [ PathList ]
                        #Dict[ asset_name ] = NewList + OldList
                    #else:
                        #Dict[ asset_name ] = [ PathList ]                
                
                
        #self.m_signal.emit( [ Shot_List, Dict ] )
    #def call_Path( self, Filebox, timeRule ):
        #Path           = Filebox["path"]
        #Rule           = Filebox["rule"]
        #List           = []
        #if not os.path.exists( Path ):
            #return []
        #for PathClient in os.listdir( Path ):
            #if not ".db" in PathClient:
                #if self.com_match_CGRule( Rule, PathClient ):
                    #if os.path.isfile( Path + "/" + PathClient ) :
                        #if ".mov" in PathClient:
                            #T_abs = Path + "/" + PathClient
                            #T_abs = T_abs.replace("\\","/")
                            ##-------------------
                            #ctime  = self.call_get_file_data( T_abs )

                            #if timeRule == []:
                                #isTime = True
                            #else:
                                #isTime = False
                                
                                
                            #for timerecv in timeRule:
                                #if "none" in timerecv[0]:
                                    #if "none" in timerecv[1]:
                                        #isTime =True
                                    #else:
                                        #endtime = time.strptime( timerecv[1], '%Y/%m/%d')
                                        #if ctime <= endtime:
                                            #isTime =True
                                #else:
                                    #if "none" in timerecv[1]:
                                        #strtime = time.strptime( timerecv[0], '%Y/%m/%d')
                                        #if strtime <= ctime:
                                            #isTime =True                                        
                                    #else:
                                        #strtime = time.strptime( timerecv[0], '%Y/%m/%d')
                                        #endtime = time.strptime( timerecv[1], '%Y/%m/%d')
                                        #if strtime <= ctime <= endtime:
                                            #isTime =True
                            #if isTime:
                                #List.append( T_abs )
                            ##-------------------
                    #else:
                        #for PathClientClient in os.listdir( Path + "/" + PathClient ):
                            #if not ".db" in PathClientClient:
                                #Re_version_findall = re.findall( "\.[0-9]+\.", PathClientClient )
                                #if Re_version_findall != []:
                                    #for Re_version in Re_version_findall:
                                        #for number in re.findall( "[0-9]+", Re_version ):
                                            #PathClientClient = PathClientClient.replace( Re_version, Re_version.replace( number, "%" + str(len(number)).zfill( len(number) ) + "d" ) )
                                            #T_abs = Path + "/" + PathClient + "/" + PathClientClient
                                            #T_abs = T_abs.replace("\\","/")
                                            ##-------------------
                                            #ctime  = self.call_get_file_data( Path + "/" + PathClient )
                                            
                                                
                                                
                                            #if timeRule == []:
                                                #isTime = True
                                            #else:
                                                #isTime = False
                                                
                                                
                                            #for timerecv in timeRule:
                                                #if "none" in timerecv[0]:
                                                    #if "none" in timerecv[1]:
                                                        #isTime =True
                                                    #else:
                                                        #endtime = time.strptime( timerecv[1], '%Y/%m/%d')
                                                        #if ctime <= endtime:
                                                            #isTime =True
                                                #else:
                                                    #if "none" in timerecv[1]:
                                                        #strtime = time.strptime( timerecv[0], '%Y/%m/%d')
                                                        #if strtime <= ctime:
                                                            #isTime =True                                        
                                                    #else:
                                                        #strtime = time.strptime( timerecv[0], '%Y/%m/%d')
                                                        #endtime = time.strptime( timerecv[1], '%Y/%m/%d')
                                                        #if strtime <= ctime <= endtime:
                                                            #isTime =True
                                            #if isTime:
                                                #List.append( T_abs )
                                            ##-------------------                                            
        #return sorted(list(set(List)))   
    #def com_match_CGRule( self, a_CGRuleList, a_file ):
        #for CGRule in a_CGRuleList:
            #RERule = CGRule.replace("#", "[0-9]").replace("?", "[a-zA-Z]").replace("*", "[a-zA-Z0-9_]*").replace(".","\.")
            #if re.match( RERule, a_file ):
                #return True
        #return False
    #def call_get_file_data( self, path ):
        ##path = path.lower().replace( 'n:', '//coco.zone/abcandxyz$' )
        ##sd = win32security.GetFileSecurity( path, win32security.OWNER_SECURITY_INFORMATION )
        ##PySid = sd.GetSecurityDescriptorOwner()
        ##name, yu, i =  win32security.LookupAccountSid( None, PySid )
        #ctime = time.strptime( time.strftime( "%Y/%m/%d", time.localtime( os.path.getmtime( path ) ) )   , '%Y/%m/%d')
        
        ##time.strptime( timerecv[1], '%Y/%m/%d')
        #return ctime    
#class FilterView( QDialog ):
    #def __init__( self ):
        #super( FilterView, self ).__init__()
        #self.setUI()
        #self.setSignal()
    #def setUI( self ):
        #self.clearFocus()
        #self.resize( 400, 300 )
        #self.setWindowTitle( 'Filter' )
        #self.setObjectName( 'Filter' )
        #self.m_layout = QVBoxLayout()
        #self.setLayout( self.m_layout )
        
        #self.m_lable_1 = QLabel()
        #self.m_lable_1.setText( u'文件修改日期:' )
        #self.m_combobox_1 = QLineEdit()
        #self.m_combobox_1.setPlaceholderText( "[ None, 2018/08/08 ];" )
        #if len(RvConfig.FilterList) != 0:
            #self.m_combobox_1.setText( RvConfig.FilterList[0] )
        #self.m_1_layout = QHBoxLayout()
        #self.m_1_layout.addWidget( self.m_lable_1 )
        #self.m_1_layout.addWidget( self.m_combobox_1 )
        #self.m_layout.addLayout( self.m_1_layout )
        #self.m_layout.addStretch()
        #self.m_bottom_layout = QHBoxLayout()
        #self.m_layout.addLayout( self.m_bottom_layout )
        #self.m_button_ok = QPushButton()
        #self.m_button_ok.setText( u'确定' )
        #self.m_bottom_layout.addStretch()
        #self.m_bottom_layout.addWidget( self.m_button_ok )
    #def setSignal( self ):
        #self.m_button_ok.clicked.connect( self.slot_ok )
    #def slot_ok( self ):
        #RvConfig.FilterList = [ self.m_combobox_1.text() ]
        #self.close()
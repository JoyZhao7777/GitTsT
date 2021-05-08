#coding:utf8
import rv
import os
import sys
import RvConfig
import PlayView
import TimeLineView
try:
    from PySide.QtCore     import *
    from PySide.QtGui      import *
    from PySide.QtWebKit   import *
except:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    #from PySide2.QtWebKitWidgets import *

import AddSave
sys.path.append( "J:/common_libs/" )
import Net
import RmFirstFrame

class RvMenu( rv.rvtypes.MinorMode ):
    def __init__( self ):
        rv.rvtypes.MinorMode.__init__( self )
        self.Create_Login()
        self.Create_Menu()
        self.Bind_CallBack()
        #self.createServer()
    def Create_Menu( self ):
        Menu = \
        [
            ( 
                "COCO2",
                [
                    ( u"Play",     self.Slot_Play     ),
                    ( u"TimeLine", self.Slot_TimeLine ),
                    ( u"Add and Export",      self.Slot_Add ),
                    #( u"Bat",      self.Slot_Bat ),
                    #( u"rm first frame",      self.Slot_rm_first ),
                ]
            )
        ]
        self.init( "CocoMenuId2", None, None, Menu )        
    def Slot_Play( self, event ):
        if hasattr( self, 'PlayViews' ):
            self.PlayViews.show()
        else:
            self.PlayViews = PlayView.PlayView( self )
            rv.qtutils.sessionWindow().addDockWidget( Qt.RightDockWidgetArea, self.PlayViews )
            self.PlayViews.show()
    def Slot_TimeLine( self, event ):
        if hasattr( self, 'TimeLineViews' ):
            self.TimeLineViews.show()
        else:
            self.TimeLineViews = TimeLineView.TimeLineView()
            rv.qtutils.sessionWindow().addDockWidget( Qt.BottomDockWidgetArea, self.TimeLineViews )
            self.TimeLineViews.show()
    def Bind_CallBack( self ):
        rv.commands.bindRegex( "default", "global", "frame-changed", self.Slot_FrameChanged, "" )
    def Slot_FrameChanged( self, event ):
        if hasattr( self, 'TimeLineViews' ):
            if self.TimeLineViews.isVisible( ):
                self.TimeLineViews.slot_framechanged()
    def Create_Login( self ):
        # sys.path.append( RvConfig.CgTeamWorkPath )
        # cgtw = __import__( 'cgtw' )
        # self.m_tw = cgtw.tw( RvConfig.CgTeamWorkServerIP )
        # self.m_tw.sys().login( RvConfig.DefineCgTeamWorkAccount, RvConfig.DefineCgTeamWorkPassword )

        import sys
        cocoPipePath = 'J:/coco_dev/coco'
        if cocoPipePath not in sys.path:
            sys.path.append(cocoPipePath)
        import cocoPipeline.lib.python.ftrackLib.ftrackSession as ftrackSession
        reload(ftrackSession)
        self.session = ftrackSession.createSession()




    def slot_signal( self , data ):
        if hasattr( self, 'TimeLineViews' ):
            self.TimeLineViews.setData( data )
            self.TimeLineViews.show()
        else:
            self.TimeLineViews = TimeLineView.TimeLineView()
            self.TimeLineViews.setData( data )
            rv.qtutils.sessionWindow().addDockWidget( Qt.BottomDockWidgetArea, self.TimeLineViews )
            self.TimeLineViews.show()     
    def createServer( self ):
        Port        = Net.GetPort( 14250 )
        TMP         = os.environ["TMP"]
        if not os.path.exists( TMP+"/Port" ):
            os.makedirs( TMP+"/Port" )
        try:
            fs = open( TMP+"/Port/Port.log" , "w" )
            fs.write( str(Port) )
            fs.close()
        except :
            pass
        print Port
        self.Server = Net.Server( "127.0.0.1", Port )
        self.Server.signal.connect( self.ServerData )
    def ServerData( self, Str ):
        try:
            print Str
            exec Str
        except Exception,e:
            print e            
    def Slot_Add( self, event ):
        reload( AddSave )
        AddSave.Add()
    def Slot_Bat( self, event ):
        AddSave.Bat()     
    def Slot_rm_first( self, event ):
        reload( RmFirstFrame )
        RmFirstFrame.test()
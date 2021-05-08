#coding:utf8
import os
import re
import sys
import time
import uuid
import RvConfig
import subprocess
import glob

try:
    from PySide.QtCore     import *
    from PySide.QtGui      import *
    from PySide.QtWebKit   import *
except:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    #from PySide2.QtWebKitWidgets import *


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

        self.m_comboboxAll_type = QCheckBox()
        self.m_comboboxAll_type.setText( u'所有场次' )
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
        self.m_cgteamWorkBox_layout_3.addWidget( self.m_comboboxAll_type ) 
        
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
        self.session = self.Parent.session
        try:
            projects = self.session.query('Project')
            for data in projects:
                self.m_combobox_project.addItem(data["full_name"], data["name"])        
        except Exception, e:
            self.m_combobox_project.clear()
        for module in RvConfig.Show_Module:
            self.m_combobox_module.addItem(module[0], module[1])
        #场次    
        self.call_refersh_combobox_eps()
        #环节
        self.call_refersh_treewidget()
    def setSignal( self ):
        self.m_combobox_module.currentIndexChanged.connect( self.slot_module )
        self.m_combobox_eps.activated.connect( self.slot_eps )     
        self.m_combobox_type.toggled.connect( self.call_refersh_treewidget )
        self.m_comboboxAll_type.toggled.connect( self.call_refersh_treewidget ) 
        self.m_button_epsplay.clicked.connect( self.call_play )
        self.m_data_signal.connect( self.Parent.slot_signal )
        self.m_combobox_project.currentIndexChanged.connect(self.call_refersh_combobox_eps)
        self.m_combobox_module.currentIndexChanged.connect(self.call_refersh_combobox_eps)
    def call_refersh_combobox_eps( self ):
        self.m_combobox_eps.clear()
        database = self.m_combobox_project.itemData( self.m_combobox_project.currentIndex() )
        eps_class = self.session.query('Ep where project.name is "{0}"'.format(database)).all()
        for eps in eps_class:
            for Seq in eps['children']:
                self.m_combobox_eps.addItem(Seq["name"], Seq["id"])

    def call_refersh_treewidget( self ):
        self.m_treewidget.clear()
        module   = self.m_combobox_module.itemData( self.m_combobox_module.currentIndex())
        database = self.m_combobox_project.itemData( self.m_combobox_project.currentIndex() )
        ProjectStege = RvConfig.SHotTaskShowFileBOx
        
        if module == 'asset_task':
            for filebox in RvConfig.AssetTaskShowFileBoX:
                item = QTreeWidgetItem( self.m_treewidget )
                item.setText( 0, filebox[0] + "--->" + filebox[1] )  
                item.setData( 0, 32, filebox )
                item.setCheckState( 0, Qt.Unchecked )             
        else:
            if self.m_combobox_type.isChecked() or self.m_comboboxAll_type.isChecked():
                for filebox in ProjectStege:
                    item = QTreeWidgetItem( self.m_treewidget )
                    item.setText( 0, filebox[0] + "--->" + filebox[1] )  
                    item.setData( 0, 32, filebox )
                    item.setCheckState( 0, Qt.Unchecked )  
            else:
                t_eps_id = self.m_combobox_eps.itemData( self.m_combobox_eps.currentIndex())
                #t_all_shot = self.session.query('Shots where parent.id is "{0}"'.format(t_eps_id)).all()
                t_all_shot_name = self.get_shotlist_from_eps_id(t_eps_id)
                for shot in t_all_shot_name:
                    Topitem = QTreeWidgetItem( self.m_treewidget )
                    Topitem.setText(0,shot)     
                    for filebox in ProjectStege:     
                        item = QTreeWidgetItem( Topitem )
                        item.setText( 0, filebox[0] + "--->" + filebox[1] )  
                        item.setData( 0, 32, filebox )
                        item.setCheckState( 0, Qt.Unchecked )     
    def slot_module( self, a_index ):
        module = self.m_combobox_module.itemData( self.m_combobox_module.currentIndex())
        if module == 'asset_task':
            self.m_label_eps.setHidden( True )
            self.m_combobox_eps.setHidden( True )
            self.m_combobox_type.setHidden( True )
            self.m_comboboxAll_type.setHidden( True )
            self.call_refersh_treewidget()     
        else:
            self.m_label_eps.setHidden( False )
            self.m_combobox_eps.setHidden( False )
            self.m_combobox_type.setHidden( False )
            self.m_comboboxAll_type.setHidden( False )
            self.call_refersh_treewidget()     
    def slot_eps( self, a_index ):
        self.call_refersh_treewidget()     
    def call_play( self ):
        Shot_List = []
        Dict      = {}    
        
        database = self.m_combobox_project.itemData( self.m_combobox_project.currentIndex())
        module = self.m_combobox_module.itemData( self.m_combobox_module.currentIndex())
        if module == 'shot_task':
            # all seq 整场播放
            if self.m_combobox_type.isChecked() or self.m_comboboxAll_type.isChecked():
                t_eps_id   = self.m_combobox_eps.itemData( self.m_combobox_eps.currentIndex())
                #t_filebox_dict = self.call_get_fileBoxID_PipeID_Data( database, module )
                t_Task_asset_list = []
                for count in range( self.m_treewidget.topLevelItemCount() ):
                    item = self.m_treewidget.topLevelItem( count )
                    if item.checkState( 0 ) == Qt.Checked:
                        task_name = item.data(0, 32)[0]
                        asset_name = item.data(0, 32)[1]
                        t_Task_asset_list.append([task_name,asset_name])

                t_all_shot_name = self.get_shotlist_from_eps_id(t_eps_id)
                for shot_name in t_all_shot_name:
                    for task_asset in t_Task_asset_list:
                        shotTask = self.get_shotTask_from_TasknameAnd_shotName(task_asset[0], shot_name,database)
                        if shotTask:
                            movpath = self.get_mov_path(shotTask,shot_name, task_asset[-1])
                            if not movpath:
                                continue 
                            Shot = shot_name
                            PathList = [movpath]
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
                # 任务ID
                t_eps_id   = self.m_combobox_eps.itemData( self.m_combobox_eps.currentIndex())

                for count in range( self.m_treewidget.topLevelItemCount() ):
                    item = self.m_treewidget.topLevelItem( count ) 
                    #镜头号
                    shot_name = item.text(0)
                    Shot = shot_name
                    for i in range( item.childCount() ):
                        cliendItem = item.child( i )                    
                        if cliendItem.checkState( 0 ) == Qt.Checked:
                            #任务名 已经组件类型
                            task_name = cliendItem.data( 0, 32 )[0]
                            asset_name = cliendItem.data(0, 32)[1]
                            shotTask = self.get_shotTask_from_TasknameAnd_shotName(task_name,shot_name,database)
                            #shotTask = self.session.query('Task where name is "{0}" and parent.parent.parent.name is "{1}"'.format(task_name,shot_name)).one()
                            if shotTask:
                                #获取视频路径
                                movpath = self.get_mov_path(shotTask,shot_name,asset_name)
                                if not movpath:
                                    continue 
                                PathList = [movpath] 
                                # 勾选的多项任务 优先播放靠下 的任务视频                         
                                if not Shot in Shot_List:
                                    Shot_List.append( Shot )
                                if Dict.has_key( Shot ):
                                    OldList = Dict[ Shot ]
                                    NewList = [ PathList ]
                                    Dict[ Shot ] = NewList + OldList
                                else:
                                    Dict[ Shot ] = [ PathList ]                                    
                            
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
        #print "Path:", Path    
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
                                        if "_L" in PathClientClient and "_Ly" not in PathClientClient and "a_L" not in PathClientClient and "f_L" not in PathClientClient:
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
            if "_L" in unit  and "_Ly" not in unit and "a_L" not in unit and "f_L" not in unit:
                left.append(unit)
            else:
                nomal.append(unit)
        if self.m_button_left.isChecked():
            return left
        else:
            return nomal


    def get_mov_path(self,shotTask,shot_name,asset_name = 'ok'):
        movpath = ''
        taskAssetVersion = self.session.query(
            'AssetVersion where task.id is "{0}" and asset.name is {1}'.format(shotTask['id'],asset_name)
        ).all()
        taskAssetVersion.sort(key=lambda orderby: (orderby.get('version', 0)), reverse=True)
        #if shotTask['name'] in RvConfig.aniTypeList:
        if taskAssetVersion:
            for taskAssetVersionC in taskAssetVersion[0]['components']:
                if taskAssetVersionC['file_type'] == ".ma":
                    for loca in taskAssetVersionC['component_locations']:
                        mov_Path = loca['resource_identifier']
                    movName = taskAssetVersionC['name']
                    movpath = self.get_mov_outpath(mov_Path, movName,shot_name)
                    if movpath:
                        return movpath

                if taskAssetVersionC['file_type'] == ".mov":
                    for loca in taskAssetVersionC['component_locations']:
                        mov_Path = loca['resource_identifier']
                    movName = taskAssetVersionC['name']
                    movpath = self.get_mov_outpath(mov_Path, movName,shot_name)
                    if movpath:
                        return movpath

    def get_shotlist_from_eps_id(self,eps_id):

        AllShotID = []
        t_all_shot_name = []
        if self.m_comboboxAll_type.isChecked():
            database = self.m_combobox_project.itemData( self.m_combobox_project.currentIndex() )
            eps_class = self.session.query('Ep where project.name is "{0}"'.format(database)).all()
            for eps in eps_class:
                for Seq in eps['children']:
                    if not 'zzz' in Seq["name"]:
                        AllShotID.append(Seq["id"])

        if AllShotID:
            for shotId in AllShotID:
                t_all_shot = self.session.query('Shots where parent.id is "{0}"'.format(shotId)).all()
                t_all_shot_name = t_all_shot_name + sorted([shots['name'] for shots in t_all_shot])                
        else:
            t_all_shot = self.session.query('Shots where parent.id is "{0}"'.format(eps_id)).all()
            t_all_shot_name = sorted([shots['name'] for shots in t_all_shot])    
        
        return t_all_shot_name

    def get_shotTask_from_TasknameAnd_shotName(self,task_name, shot_name,database):
        try:
            shotTask = self.session.query('Task where name is "{0}" and parent.parent.parent.name is "{1}" and project.name is "{2}"'.format(task_name,shot_name,database)).one()
        except:
            return
        return shotTask


    def get_mov_outpath(self,movPath,movName,shot_name):
        if movName == "main":
            movName = shot_name

        movPath = RvConfig.Project_diver+"/"+movPath.split('/v0')[0]+"/"+movName+"*.mov"
        Outpath = glob.glob(movPath)
        if Outpath:
            for outitem in sorted(Outpath,reverse=True):
                if os.path.exists(outitem):
                    return outitem.replace("\\","/")
        else:
            return

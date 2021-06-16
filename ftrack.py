# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import sys
# sys.path.append('D:\\zhaojiayi\\Documents\\coco')
# # import os
# # import getpass
# # import cocoPipeline.lib.python.ftrackLib.ftrackSession as ftrackSession
# # reload(ftrackSession)
# # import cocoPipeline.lib.python.ftrackLib.ftrackQuery as ftrackQuery
# # reload(ftrackQuery)
# # from cocoPipeline.lib.python.dataLib import entityObject
# # from cocoPipeline.lib.python.dataLib import getEntity
# import cocoPipeline.lib.python.ftrackLib.pipelineos as pipelineos



# # def create_componet():
# #     jpgList = ['TDtest',  'shot',  'Light',  'SC027',  'SC027_cam001_01',  'SC027_cam001_01']
# #     jpgPath = "D:/ftrackrvTest/SC027_cam001_01_lgt_v01.jpeg"
# #     # TDtest / shot / Light / SC027 / SC027_cam001_01 / SC027_cam001_01
# #     project_name = 'TDtest'
# #     session = ftrackSession.createSession()
# #     task = session.query(
# #             'Task where name is "{0}" \
# #              and parent.name is "{1}" \
# #              and parent.parent.parent.name is "{2}" \
# #              and project.name is "{3}"'\
# #              .format(jpgList[-1], jpgList[-2], jpgList[-4],  project_name)
# #         )
# #     taskJoy = task[0]
# #     asset = session.query(
# #         'Asset where name is "{0}" \
# #          and parent.name is "{1}" \
# #          and parent.parent.parent.name is "{2}" \
# #          and parent.project.name is "{3}"'\
# #          .format('review', jpgList[-2], jpgList[-4],project_name)
# #     )

# #     if not asset:
# #         assetType = session.query('AssetType where short is "{}"'.format(taskJoy['type']['name'])).one()
# #         assetParent = taskJoy['parent']
# #         assetJoy = session.create('Asset', {
# #                         'name': 'review',
# #                         'type': assetType,
# #                         'parent': assetParent
# #                         })
# #     else:
# #         assetJoy = asset[0]
# #     entity = entityObject.Project().objects(project_name)
# #     location = session.query('Location where name is "{0}"'.format(entity.ftrack_pipeline_location)).one()
# #     asset_version = session.create('AssetVersion', {
# #         'asset': assetJoy,
# #         'task': taskJoy
# #     })
# #     session.commit()
# #     asset_version.create_component(
# #         jpgPath,
# #         data={
# #             'name': 'RVTETS'
# #         },
# #         location=location
# #     )
# #     asset_version.create_thumbnail(jpgPath)

# # def change_component_exist():
# #     project_name = 'TDtest'
# #     session = ftrackSession.createSession()
# #     entity = entityObject.Project().objects(project_name)
# #     location = session.query('Location where name is "ftrack.unmanaged"').one()

# #     jpgList = ['TDtest',  'shot',  'Light',  'SC027',  'SC027_cam001_01',  'SC027_cam001_01']
# #     asset = session.query(
# #         'Asset where name is "{0}" \
# #          and parent.name is "{1}" \
# #          and parent.parent.parent.name is "{2}" \
# #          and parent.project.name is "{3}"'\
# #          .format('review', jpgList[-2], jpgList[-4],project_name)
# #     )
# #     assetJoy = asset[0]
# #     assetversionList = assetJoy['versions']
# #     asset_version = assetversionList[0]
# #     componet = asset_version['components'][0]
# #     componet['name'] = 'main'
# #     session.commit()
# #     # jpgPath_ftrack = componet['component_locations'][0]['resource_identifier']
# #     # asset_version.create_component(
# #     #   jpgPath_ftrack,
# #     #   data={
# #     #       'name': 'main'
# #     #   },
# #     #   location=location
# #     # )
# # def find_component():
# #     project_name = 'TDtest'
# #     session = ftrackSession.createSession()
# #     entity = entityObject.Project().objects(project_name)
# #     location = session.query('Location where name is "ftrack.unmanaged"').one()

# #     jpgList = ['TDtest',  'shot',  'Light',  'SC027',  'SC027_cam001_01',  'SC027_cam001_01']
# #     # tp = ['mov' , 'jpg' , 'jpeg']
# #     asset = session.query(
# #         'Asset where name is "{0}" \
# #          and parent.name is "{1}" \
# #          and parent.parent.parent.name is "{2}" \
# #          and parent.project.name is "{3}"'\
# #          .format('review', jpgList[-2], jpgList[-4],project_name)
# #     )
# #     assetJoy = asset[0]
# #     assetversionList = assetJoy['versions']
# #     asset_version = assetversionList[0]
# #     componetList = asset_version['components']
# #     for c in componetList:
# #         filePath = c['component_locations'][0]['resource_identifier']
# #         if 'mov' in filePath or 'jpg' in filePath or 'jpeg' in filePath:
# #             print c['name']





# # projectName = 'TDtest'
# # session = ftrackSession.createSession()
# # entity = entityObject.Project().objects(projectName)
# # location = session.query('Location where name is "{0}"'.format(entity.ftrack_pipeline_location)).one()
# # # location key 包括 [u'description', u'location_components', u'id', u'name', u'label']
# # serverRoot = os.path.abspath(location.get_accessor_prefix())
# # serverRoot = os.environ['SERVER_ROOT'].capitalize()
# # task = session.query(
# #             'Task where parent.name is "{0}" \
# #              and parent.parent.name is "{1}" \
# #              and parent.parent.parent.name is "{2}" \
# #              and parent.parent.parent.parent.name is "{3}" \
# #              and project.name is "{4}"'\
# #              .format('comp', 'cmp', 'dhd067', 'dhd', 'TDtest')
# #         )
# # # 'TDtest/shots/ep001/dhd/dhd067/cmp/comp/comp'
# # # task[0].keys()  [u'sort', u'managers', u'type_id', u'priority_id', u'status_changes', u'_link', \
# # #  u'incoming_links', u'id', u'timelogs', u'ancestors', u'end_date', u'status_id', u'custom_attributes',\
# # # u'children', u'priority', u'parent_id', u'project_id', u'type', u'start_date', u'metadata', u'status', \
# # # u'scopes', u'object_type', u'description', u'parent', u'descendants', u'thumbnail_id', u'bid', u'lists',\
# # # u'appointments', u'link', u'time_logged', u'bid_time_logged_difference', u'name', u'assets', u'context_type',\
# # # u'notes', u'thumbnail', u'project', u'assignments', u'thumbnail_url', u'object_type_id', u'outgoing_links', u'allocations']

# # # asset = session.query(
# # #           'Asset where name is "{0}" \
# # #            and parent.name is "{1}" \
# # #            and parent.parent.name is "{2}" \
# # #            and parent.parent.parent.name is "{3}" \
# # #            and parent.parent.parent.parent.name is "{4}" \
# # #            and project.name is "{5}"'\
# # #            .format('comp', 'cmp', 'cmp', 'hdd','ep001', 'TDtest')
# # #       )

# # print task[0]
# # print asset[0]
# # #         王者荣耀_澜/shots/ep001/hdd/hdd076/animation/ani/ani
# # # 'TDtest/shots/ep001/hdd/cmp/comp/comp/comp'
# # # project = session.query('Project').first()
# # # project.keys() [u'managers', u'calendar_events', u'color', u'thumbnail', u'_link', u'full_name', \
# # # u'disk', u'id', u'timelogs', u'parent', u'parent_id', u'disk_id', u'children', u'user_security_role_projects',\
# # # u'start_date', u'metadata', u'status', u'scopes', u'project_schema_id', u'end_date', u'descendants', u'thumbnail_id',\
# # # u'review_sessions', u'appointments', u'link', u'is_private', u'assets', u'is_global', u'name', u'context_type', u'notes',
# # # u'project_schema', u'assignments', u'thumbnail_url', u'allocations', u'custom_attributes', u'root']

# # # print project['task_templates']
# # # print session.types.keys()
# # # projects = session.query('Project')
# # # for proj in projects:
# # #   print proj['name']
# # # active_projects = session.query('Project where status is active')
# # # for proj in active_projects:
# # #   print proj['name']
# # # projects[0].keys()
# # # taskDir = 'TDtest/shots/ep001/dhd/dhd067/cmp/comp/comp'
# # # if asset == None:
# # #   taskJoy = task[0]
# # #   assetParent = taskJoy['parent']
# # #   assetType = session.query('AssetType where short is "{}"'.format(taskJoy['type']['name'])).one()
# # #   assetName = os.path.abspath(taskDir).split('/')[-1]
# # #   asset = session.create('Asset', {
# # #                           'name': assetName,
# # #                           'type': assetType,
# # #                           'parent': assetParent
# # #                           })
# # # assetJoy = asset[0]
# # # entity = entityObject.Project().objects(projectName)
# # # location = session.query('Location where name is "{0}"'.format(entity.ftrack_pipeline_location)).one()

# # # asset_version = session.create('AssetVersion', {
# # #               'asset': asset,
# # #               'task': taskJoy
# # #           })
# # # "J:/test/joyfiles/dhd067_scene_ok.mov"
# # # movPath = 'J:/test/joyfiles/dhd067_scene_ok.mov'
# # # fileList = [movPath]
# # # asset_version['comment'] = 'i wannne create component'

# # # session.commit()
# # # for item in fileList:
# # #   asset_version.create_component(
# # #       item,
# # #       data={
# # #           'name': 'rv'
# # #       },
# # #       location=location
# # #   )




# # # 'TDtest/shots/ep001/dhd/dhd067/cmp/comp/comp'
# # # asset = session.query(
# # #     'Asset where name is "{0}" \
# # #      and parent.name is "{1}" \
# # #      and parent.parent.name is "{2}" \
# # #      and parent.parent.parent.name is "{3}" \
# # #      and parent.parent.parent.parent.name is "{4}" \
# # #      and parent.project.name is "{5}"'\
# # #      .format('comp', 'comp', 'cmp','dhd067', 'dhd', 'TDtest')
# # # )

# # # asset = session.query(
# # #   'Asset where name is "{0}" \
# # #    and parent.project.name is "{1}"'\
# # #    .format('My asset', 'TDtest')
# # # )
# # # assetJoy = asset[0]
# # # task = session.query(
# # #           'Task where parent.name is "{0}" \
# # #            and parent.parent.name is "{1}" \
# # #            and parent.parent.parent.name is "{2}" \
# # #            and parent.parent.parent.parent.name is "{3}" \
# # #            and project.name is "{4}"'\
# # #            .format('comp', 'cmp', 'dhd067', 'dhd', 'TDtest')
# # #       )



# # # def create_componet():




# # # def publishTask(self, taskDir, workRoot, componentList, playableMedia=None, 
# # #   thumbnail=None, publishStatus='review', sendMail = False):
# # ------------------------taskDir-------------------------
# # serverRoot = 'Z:\\'
# import os
# from cocoPipeline.lib.python import resource
# from cocoLib.python.configLib import confParser
# reload(confParser)
# reload(resource)
# # Dir = 'Z:\\tdtest\\shots\\ep001\\dhd\\dhd068\\animation\\ani\\final' 
# # DirTask = 'Z:/TDtest/shots/ep001/dhd/dhd068/animation/ani/'
# # # Dir = os.path.abspath(Dir).replace('Z:\\','')
# # Dir = os.path.abspath(Dir).replace('Z:\\','')
# # print Dir
# # folderList = Dir.split("\\")
# # print len(folderList)
# # print folderList
# # print 'parent.name ' + folderList[-2]
# # print 'parent.parent.name ' + folderList[-3]
# # print 'parent.parent.parent.name ' + folderList[-4]
# # print 'parent.parent.parent.parent.name ' + folderList[-5]
# # print 'project.name ' + folderList[-8]

# # -asset
# # asset: "{projectRoot}/{projectName}/{productionType}/{assetType}/{assetName}/{taskName}/{subTaskName}/{variantName}
# # /{assetFile}"
# # -shot
# # shot:  "{projectRoot}/{projectName}/{productionType}/{episode}/{sequence}/{shot}/{taskName}/{subTaskName}
# # /{assetFile}"

# def get_entity():
#     entity_template = os.path.realpath(os.path.join(resource.get_config(), 'mapping.yml'))
#     cp = confParser.DeepYamlParser(entity_template)
#     return cp.parse()

# def getShotEntityDir(mapAttrDic):
#     # workRoot = mapAttrDic['projectRoot']
#     entity = get_entity()
#     taskWorkPath = entity['shot'].format(projectRoot=mapAttrDic['projectRoot'],
#                                           projectName=mapAttrDic['projectName'],
#                                           productionType=mapAttrDic['productionType'],
#                                           episode=mapAttrDic['episode'],
#                                           sequence=mapAttrDic['sequence'],
#                                           shot=mapAttrDic['shot'],
#                                           taskName=mapAttrDic['taskName'],
#                                           subTaskName=mapAttrDic['subTaskName'],
#                                           assetFile=mapAttrDic['assetFile'])
#     return os.path.abspath(taskWorkPath)

# dictMap={'projectRoot':'Z:','projectName':'TDtest','productionType':'shots','episode':'ep001','sequence':'dhd','shot':'dhd068','taskName':'animation','subTaskName':'ani','assetFile':'dhd068_ani_final.ma'}

# Dir = getShotEntityDir(dictMap)
# print Dir
# Dir = os.path.abspath(Dir).replace('Z:','')
# print Dir
# folderList = Dir.split("\\")
# print len(folderList)
# print folderList
# print 'parent.name ' + folderList[-2]
# print 'parent.parent.name ' + folderList[-3]
# print 'parent.parent.parent.name ' + folderList[-4]
# print 'parent.parent.parent.parent.name ' + folderList[-5]
# print 'project.name ' + folderList[-8]

# # ----------------------------taskDir---------------------------------------------------
# # taskDir = 'Z:\\TDtest\\shots\\ep001\\dhd\\dhd068\\animation\\ani\\final'
# # ----------------------------taskDir---------------------------------------------------

# # ----------------------------workRoot---------------------------------------------------
# # workRoot = 'Z:'
# # ----------------------------workRoot---------------------------------------------------

# # componentList = ['D:\\tstfiles\\ftrack\\dhd068_ani_final.ma','D:\\tstfiles\\ftrack\\dhd068_ani_final.mov']
# # componentList = list(set(componentList))
# # workRoot = 'D:'
# # serverRoot = 'Z:'

# # print componentList
# # fileList = []
# # dirList = []
# # for item in componentList:
# #     fileNameSplit = os.path.split(item)
# #     fileExt = os.path.splitext(fileNameSplit[1])[1]
# #     # 扩展名为空表示为文件夹
# #     if fileExt != '':
# #         fileList.append(item)
# #     else:
# #         dirList.append(item)
# # print fileList,dirList
# # try:
# #     openList = []
# #     for item in fileList:
# #         serverFile = item.replace(workRoot + "\\", serverRoot)
# #         fileOpen = pipelineos.isFileOpen(serverFile)
# #         print serverFile
# #         if fileOpen == 3:
# #             openList.append(serverFile)

# #     for item in dirList:
# #         serverDir = item.replace(workRoot + "\\", self.serverRoot)
# #         for fileItem in getFilesFromDir(serverDir):
# #             fileOpen = pipelineos.isFileOpen(fileItem)
# #             if fileOpen == 3:
# #                 openList.append(fileItem)
# # except:
# #     print u'没有和工作路径对应的服务器路径'
# # print 
# # print fileOpen



# # ----------------------------------tempVersion---------------------------------------------------
# taskDir = 'Z:\\TDtest\\shots\\ep001\\dhd\\dhd068\\animation\\ani\\dhd068_ani_final.ma'
# assetName = os.path.abspath(taskDir).split('\\')[-1]
# print assetName
# folderList = ['', 'TDtest', 'shots', 'ep001', 'dhd', 'dhd068', 'animation', 'ani', 'final']
# folderList_smxm = ['', 'smxm', 'shots', 'ep001', 'dhd', 'dhd068', 'animation', 'ani', 'polishing']
# folderList_poli = ['', 'smxm', 'shots', 'ep001', 'dhd', 'dhd068', 'animation', 'ani', 'polishing']

# taskVersion = session.query(
#             'Task where parent.name is "{0}" \
#              and parent.parent.name is "{1}" \
#              and parent.parent.parent.name is "{2}" \
#              and parent.parent.parent.parent.name is "{3}" \
#              and project.name is "{4}"'\
#              .format(folderList[-2], folderList[-3], folderList[-4], folderList[-5], folderList[-8])
#         )
# print taskVersion[0].keys()
# print taskVersion[0]['parent']['name']
# task = taskVersion[0]
# print len(taskVersion)
# print task['name']

# assetName = 'final'

# assetAA = session.query(
#     'Asset where name is "{0}" \
#      and parent.name is "{1}" \
#      and parent.parent.name is "{2}" \
#      and parent.parent.parent.name is "{3}" \
#      and parent.parent.parent.parent.name is "{4}" \
#      and parent.project.name is "{5}"'\
#      .format(folderList[-1],folderList[-2], folderList[-3], folderList[-4], folderList[-5], folderList[-8])
# )
# assetAA = session.query(
#     'Asset where parent.name is "{0}" \
#      and parent.parent.name is "{1}" \
#      and parent.parent.parent.name is "{2}" \
#      and parent.parent.parent.parent.name is "{3}" \
#      and parent.project.name is "{4}"'\
#      .format(folderList[-2], folderList[-3], folderList[-4], folderList[-5], folderList[-8])
# )
# print len(assetAA)
# for a in assetAA:
#     print a['name']
# asset = assetAA[0]
# print asset['name']
# print asset.keys()
# print asset['versions']
# print len(asset['versions'])
# asset_version = asset['versions'][1]
# print asset_version.keys()
# print asset_version['version']
# session = ftrackSession.createSession()
# asset_version = session.create('AssetVersion', {
#     'asset': asset,
#     'task': task
# })
# asset_version['comment'] = 'for componenet'
# session.commit()
# fileList = ['D:\\tstfiles\\ftrack\\dhd068_ani_final.ma','D:\\tstfiles\\ftrack\\dhd068_ani_final.mov']
# for item in fileList:
#     splitPath = os.path.split(item)
#     fileName = os.path.splitext(splitPath[1])[0]
#     asset_version.create_component(
#         item,
#         data={
#             'name': fileName
#         },
#         location=location
#     )
# session.commit()
# cList = asset_version['components']
# for c in cList:
#     filePath = c['component_locations'][0]['resource_identifier']
#     if 'mov' in filePath or 'jpg' in filePath or 'jpeg' in filePath:
#         c['name'] = 'main'
#         session.commit()

# # ----------------------------------tempVersion---------------------------------------------------


# forderList = 
import sys,os
sys.path.append(r"D:\\zhaojiayi\\Documents\\coco")
# proPath = 'Z:\\smxm\\assets'
# typePath = 
# import cocoPipeline.lib.python.ftrackLib as fl
# print(fl)
# from cocoPipeline.lib.python.ftrackLib import asset

# a = asset.Asset()
# for i in a.get_assets("smxm"):
# 	print(i["name"])
# 	t = a.get_asset_task(i,"geo")
# 	print(a.get_parent_path(t[1]))
#     break
proj = 'smxm'

def get_proj_assets(proj):
	assetDict = {}
	projPath = 'Z:\\{}\\assets\\'.format(proj)
	typeList = os.listdir(projPath)
	for t in typeList:
		typePath = projPath + t
		assetList = os.listdir(typePath)
		for a in assetList:
			assetDict[a] = t
	return assetDict
# get_proj_assets('smxm')
# '"Z:\smxm\assets\char\c001001xiongmaox\mod\geo\main\ok\c001001xiongmaox_geo_main.png"'
def get_asset_png(proj,assetType,asset):
	pngPath = 'Z:\\{0}\\assets\\{1}\\{2}\\mod\\geo\\main\\ok\\{3}_geo_main.png'.format(proj,assetType,asset,asset)
	if os.path.isfile(pngPath):
		return pngPath
	else:
		return None

assetDict = get_proj_assets(proj)
for k,v in assetDict.items():
	print get_asset_png(proj,v,k)





















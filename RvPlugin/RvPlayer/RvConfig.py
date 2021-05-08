#coding:utf8
CgTeamWorkPath = "C:/CgteamWork/bin/base"
CgTeamWorkServerIP = '192.168.1.183'
DefineCgTeamWorkAccount = 'user'
DefineCgTeamWorkPassword = ''
CurrentFileBoxList = []
FilterList = []
Hidden_Project = [ 'Libray', 'testPrj', 'DSTV', "xlr" ]
Show_Module = [ [u"镜头制作","shot_task"], [u"资产制作",'asset_task'] ]

Project_diver = "Z:"
aniTypeList = ['ani','bk','lay']

AssetTaskShowFileBoX = [
    #阶段        文件筐名字
    ["crowd",   "preview"  ],
    ["crowd",   "reference"]
]


SHotTaskShowFileBOx = [ 
    # 阶段     文件筐名
    [ "lay",            "ok" ], 
    [ "bk",             "ok" ], 
    [ "ani",         "final" ], 
    [ "ani",     "polishing" ],
    [ "comp",     "preview" ],
    # [ "CFX",           "cfx_msAll"],
    # [ "lgt",           "preview"],
    # [ "cmp",           "preview"],
    # [ "efx",           "preview"],
    # [ "efx",           "final"],
    # [ "lgt",           "shotCheck"],
    # [ "3DConversion",  "3DConversion"],
]


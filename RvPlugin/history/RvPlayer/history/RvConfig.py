#coding:utf8
CgTeamWorkPath = "C:/CgteamWork/bin/base"
CgTeamWorkServerIP = '192.168.1.98'
DefineCgTeamWorkAccount = 'user'
DefineCgTeamWorkPassword = ''
CurrentFileBoxList = []
FilterList = []
Hidden_Project = [ 'Libray', 'testPrj', 'dsf', 'DSTV', "xlr" ]
Show_Module = [ [u"镜头制作","shot_task"], [u"资产制作",'asset_task'] ]



AssetTaskShowFileBoX = [
    #阶段        文件筐名字
    ["crowd",   "preview"  ],
    ["crowd",   "reference"]
]


SHotTaskShowFileBOx = [ 
    # 阶段     文件筐名
    [ "lay",            "preview" ], 
    [ "reference",      "00reference" ], 
    # [ "blocking",       "preview" ],
    # [ "finalpass",      "preview" ],
    # [ "polishing",      "preview" ],
    [ "ani",            "preview"],
    [ "CFX",           "cfx_msAll"],
    [ "lgt",           "preview"],
    [ "cmp",           "preview"],
    [ "efx",           "preview"],
    [ "efx",           "final"],
    [ "lgt",           "shotCheck"],
    [ "3DConversion",  "3DConversion"],
]

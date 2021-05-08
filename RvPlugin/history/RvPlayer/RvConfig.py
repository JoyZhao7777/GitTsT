#coding:utf8
CgTeamWorkPath = "C:/CgteamWork/bin/base"
CgTeamWorkServerIP = '192.168.1.183'
DefineCgTeamWorkAccount = 'user'
DefineCgTeamWorkPassword = ''
CurrentFileBoxList = []
FilterList = []
Hidden_Project = [ 'Libray', 'testPrj', 'DSTV', "xlr" ]
Show_Module = [ [u"镜头制作","shot_task"], [u"资产制作",'asset_task'] ]



AssetTaskShowFileBoX = [
    #阶段        文件筐名字
    ["crowd",   "preview"  ],
    ["crowd",   "reference"]
]


SHotTaskShowFileBOx = [ 
    # 阶段     文件筐名
    [ "stb",            "ok" ],
    [ "lay",            "preview" ], 
    [ "reference",      "00reference" ], 
    [ "blocking",      "reference" ], 
    [ "blocking",       "preview" ],
    [ "finalpass",      "preview" ],
    [ "polishing",      "preview" ],
    [ "ani",            "preview"],
    [ "CFX",           "cfx_msAll"],
    [ "lgt",           "preview"],
    [ "cmp",           "preview"],
    [ "efx",           "preview"],
    [ "efx",           "final"],
    [ "lgt",           "shotCheck"],
    [ "3DConversion",  "3DConversion"],
]


SHotTaskShowFileBOxFXCM = [ 
    # 阶段     文件筐名
    [ "lay",            u"preview"],
    [ "blocking",       u"动画文件"],
    [ "animation",      u"动画文件"],
    [ "animation",      u"sculpt"],
    [ "Lighting",       u"preview"],
    [ "Compositing",    u"preview"],
    [ "CFX",    u"preview"],
]

SHotTaskShowFileBOxDSF = [ 
    # 阶段     文件筐名
    [ "Ly",            u"preview \ ma"],
    [ "Ly",            u"预演文件汇总"],
    [ "Ly",            u"2D故事版"],
    ["blocking",       u"preview"],
    ["Final",          u"preview \ ma"],
]

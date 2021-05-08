# coding=utf-8
from rv import rvtypes, commands
import os
import glob
import re


class SwitchVersion(rvtypes.MinorMode):
    def __init__(self):
        rvtypes.MinorMode.__init__(self)

        self.init("SwitchVersion",
                  [("key-down--Z", self.hanZdleVersionUp, "Version up"),
                   ("key-down--X", self.handleVersionDown, "Version down")],
                  None)

    def getFilePath(self, up=True):
        node = commands.sourcesAtFrame(commands.frame())
        if not node:
            return
        SourceNodeMedia = commands.sourceMediaInfoList(node[0])
        currentVersion = None
        for media in SourceNodeMedia:
            currentVersion = media["file"]
        result = re.findall(r".+_(v\d\d).*", currentVersion)
        if not result:
            print u"file type error %s"%currentVersion
            return
        rePath = currentVersion.replace(result[0], "v??")
        upVersionPath = None
        if "#." not in rePath:
            allPath = glob.glob(rePath)
            allPath.sort()
            for index in range(len(allPath)):
                if allPath[index].replace("\\", "/") == currentVersion:
                    if up:
                        if index == len(allPath) - 1:
                            print u"已经是最大版本了"
                            upVersionPath = currentVersion
                        else:
                            upVersionPath = allPath[index+1]
                    else:
                        if index == 0:
                            print u"已经是最小版本了"
                            upVersionPath = currentVersion
                        else:
                            upVersionPath = allPath[index-1]
        else:
            rep = re.findall(r".+\.([\d\#-]+)\..+", rePath)
            if not rep:
                print u"file type error %s" % currentVersion
                return
            rePath = rePath.replace(rep[0], "*")
            allPath = glob.glob(rePath)
            allPath.sort()
            allPathList = list()
            start = os.path.dirname(allPath[0]).replace("\\", "/")
            temp = list()
            for unit in allPath:
                if os.path.dirname(unit).replace("\\", "/") == start:
                    temp.append(unit)
                else:
                    start = os.path.dirname(unit).replace("\\", "/")
                    allPathList.append(temp)
                    temp = [unit]
            if temp:
                allPathList.append(temp)
            seqPath = list()
            for unit in allPathList:
                firstFrame = re.findall(r".+\.([\d\#-]+)\..+", unit[0])[0]
                lastFrame = re.findall(r".+\.([\d\#-]+)\..+", unit[-1])[0]
                if firstFrame == lastFrame:
                    seqPath.append(unit[0])
                else:
                    seqPath.append(unit[0].replace(firstFrame, "%s-%s#"%(firstFrame, lastFrame)).replace("\\", "/"))
            for index in range(len(seqPath)):
                if seqPath[index] == currentVersion:
                    if up:
                        if index == len(seqPath) - 1:
                            print u"this is min version"
                            upVersionPath = currentVersion
                        else:
                            upVersionPath = seqPath[index+1]
                    else:
                        if index == 0:
                            print u"this is mix version"
                            upVersionPath = currentVersion
                        else:
                            upVersionPath = seqPath[index-1]
        return upVersionPath

    def handleVersionUp(self, event):
        upVersionPath = self.getFilePath(True)
        if not upVersionPath:
            print "Can\'t find anything file"
            return
        node = commands.sourcesAtFrame(commands.frame())
        commands.setSourceMedia(node[0], [upVersionPath], "")


    def handleVersionDown(self, event):
        downVersionPath = self.getFilePath(False)
        if not allPath:
            print "Can\'t find anything file"
            return
        node = commands.sourcesAtFrame(commands.frame())
        commands.setSourceMedia(node[0], [downVersionPath], "")


def createMode():
    "Required to initialize the module. RV will call this function to create your mode."
    return SwitchVersion()
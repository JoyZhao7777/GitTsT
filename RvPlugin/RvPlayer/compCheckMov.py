# coding=utf-8

import re
import os
import shutil
import tempfile
import subprocess

templateRvFile = os.path.join(os.path.dirname(__file__), "Template.rv")
tmpPath = os.path.join(os.environ["tmp"], "rvTemp.rv").replace("\\", "/")

def GetWaitCheckMov():
    WaitCheckMovList = []
    for eps in os.listdir( "N:/production/film/" ):
        if re.match( "f_[A-Z][A-Z][A-Z]", eps ):
            for shot in os.listdir( "N:/production/film/%s/"%eps ):
                if re.match( "f_[A-Z0-9]*", shot ):
                    if os.path.exists( "N:/production/film/%s/%s/vfx/cfx/cfx_msAll/"%( eps, shot ) ):
                        for mov in os.listdir( "N:/production/film/%s/%s/vfx/cfx/cfx_msAll/"%( eps, shot ) ):
                            if ".mov" in mov and "Check.mov" not in mov:
                                movPath = "N:/production/film/%s/%s/vfx/cfx/cfx_msAll/%s"%( eps, shot, mov )
                                WaitCheckMovList.append( movPath )
    return WaitCheckMovList


def GetMaxVersionFile( Path, Pattern ):
    FileList = []
    if os.path.exists( Path ):
        for File in os.listdir( Path ):
            if re.match( Pattern, File ):
                FileList.append( File )
    if len( FileList ) != 0:
        return sorted( FileList )[-1]
    else:
        return False


def GetPolishing(cfxPath):
    T_SourceList = cfxPath
    for source in T_SourceList:
        t_fin = re.findall( "f_[A-Z0-9]*", os.path.basename( source ) )
        if t_fin:
            t_load = "N:/production/film/%s/%s/ani/preview/"%( t_fin[0][:5], t_fin[0] )
            t_file = GetMaxVersionFile( t_load, "nz_%s_polishing_[vV][0-9][0-9].mov"%( t_fin[0] ) )
            if t_file:
                t_load_file = t_load + t_file
                # if t_load_file not in T_SourceList:
                #     rv.commands.addSource( t_load_file )
                outPath = source.replace( ".mov", "Check.mov" ).replace( "N:/", "//coco.zone/abcandxyz$/" )
                return t_load_file, outPath
    return False, False

def exportMov(firstPath, lastPath, outputPath):
    with open(templateRvFile, "r") as file:
        content = file.read()
        content = content.replace("firstReplacePath", firstPath)
        content = content.replace("lastReplacePath", lastPath)

    with open(tmpPath, "w") as file:
        file.write(content)

    cmd = '"C:/Program Files/Shotgun/RV-7.2.0/bin/rvio_hw.exe" %s -o %s -outsrgb'%(tmpPath, outputPath)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutput, erroutput) = p.communicate()
    print erroutput

def main():
    WaitCheckMovList = GetWaitCheckMov()
    errorPath = list()
    for wait in WaitCheckMovList:
        # print wait
        try:
            aniPath, OutputMov = GetPolishing([wait])
            if OutputMov and aniPath:
                print [wait, aniPath, OutputMov]
                exportMov(wait, aniPath, OutputMov)
        except:
            errorPath.append(errorPath)
    print "errorPath: ", errorPath

if __name__ == '__main__':
    main()
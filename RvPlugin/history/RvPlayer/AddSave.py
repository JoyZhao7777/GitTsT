#coding:utf8
import rv
import re
import os
import rv.extra_commands
def Add():
    OutputMov = GetPolishing()
    if OutputMov:
        AddViewMode()
        ExportMov( frameStart(), frameEnd(), OutputMov, Blocking="false" )
def Bat():
    WaitCheckMovList = GetWaitCheckMov()
    for wait in WaitCheckMovList:
        print wait
        rv.commands.clearSession()
        rv.commands.addSource( wait )
        OutputMov = GetPolishing()
        if OutputMov:
            if not os.path.exists( OutputMov ):
                AddViewMode()
                ExportMov( frameStart(), frameEnd(), OutputMov, Blocking="false" )
#-------------------------------------------------------------
#以下为Rv可调用函数
def GetSourcePath():
    SourcePathList = []
    SourceNodeList = rv.commands.nodesOfType( "RVSource" )
    for SourceNodeIndex in range( len(SourceNodeList) ):
        SourceNode = SourceNodeList[ SourceNodeIndex ]  
        SourceNodeMedia = rv.commands.sourceMediaInfoList( SourceNode )
        for Media in SourceNodeMedia:    
            SourcePath  = Media["file"]
            SourcePathList.append( SourcePath )
    return SourcePathList
def ExportMov( FrameStart, FrameEnd, OutputMov, Blocking="false" ):
    return rv.commands.eval( 'export_utils.exportMovieOverRange( %s, %s, "%s", %s, "default" );'%( str(FrameStart), str(FrameEnd), OutputMov, Blocking ) )
def AddViewMode():
    defaultStack = "defaultStack"
    if not rv.commands.nodeExists( defaultStack ):
        defaultStack = rv.commands.newNode( "RVStackGroup", defaultStack )
        rv.extra_commands.setUIName( defaultStack, "Add Model" )
    if rv.commands.viewNode() != defaultStack:
        rv.commands.setViewNode( defaultStack )
        rv.commands.setInPoint( rv.commands.frameStart() )
        rv.commands.setOutPoint( rv.commands.frameEnd() )    
    rv.commands.setStringProperty( "#RVStack.composite.type", ["add"] )    
def frameStart():
    return rv.commands.frameStart()
def frameEnd():
    return rv.commands.frameEnd()
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
def GetPolishing():
    T_SourceList = GetSourcePath()
    for source in T_SourceList:
        t_fin = re.findall( "f_[A-Z0-9]*", os.path.basename( source ) )
        if t_fin:
            t_load = "N:/production/film/%s/%s/ani/preview/"%( t_fin[0][:5], t_fin[0] )
            t_file = GetMaxVersionFile( t_load, "nz_%s_polishing_[vV][0-9][0-9].mov"%( t_fin[0] ) )
            if t_file:
                t_load_file = t_load + t_file
                if t_load_file not in T_SourceList:
                    rv.commands.addSource( t_load_file )
                outPath = source.replace( ".mov", "Check.mov" ).replace( "N:/", "//coco.zone/abcandxyz$/" )
                return outPath
    return False
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

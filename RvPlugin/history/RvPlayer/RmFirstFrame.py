#coding:utf8
import rv
import re
import os
import rv.extra_commands


def test():
        print rv.commands.nodesOfType( "RVSourceGroup" )
        #print rv.commands.viewNode()
        #print rv.commands.nodeType( rv.commands.viewNode() )
        #for i in rv.commands.nodesOfType( "RVFileSource" ):
                #print  rv.commands.nodeType( i ), i
        #for s in range( len(SourceNodeList) ):
        #SourceNode = SourceNodeList[s]  
        #SourceNodeMedia = rv.commands.sourceMediaInfoList( SourceNode )
        #print SourceNodeMedia
        #print rv.commands.sourceAttributes( SourceNode ) 
        #set("#RVFileSource.cut.in",  -int.max);
        #set("#RVFileSource.cut.out",  int.max);
        #print "%s.cut.in"%SourceNode, "2"
        #print rv.commands.eval( 'commands.getIntProperty("#RVFileSource.cut.in").front();' )    
        


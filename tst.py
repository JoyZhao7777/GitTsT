# !/usr/bin/env python
# -*- coding: utf-8 -*-
# from collections import Iterable
# from types import MethodType
# import logging
# class Student(object):

#   @property
#   def score(self):
#       return self._score

#   @score.setter
#   def score(self,value):
#       if not isinstance(value,int):
#           raise ValueError('score must be an integer!')
#       if value<0 or value>100:
#           raise ValueError('score must be 0~100!')
#       self._score =value

# s=Student()
# s.score=60
# print s.score
	
# class Student(object):

#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self,value):
#         self._birth=value
#     @property
#     def age(self):
#         return 2015 - self._birth

# class Screen(object):

#     @property
#     def width(self):
#         return self._width

#     @property
#     def height(self):
#         return self._height
	
#     @width.setter
#     def width(self,screenwidth):
#         self.screenwidth=screenwidth

#     @height.setter
#     def height(self,screenheight):
#         self.screenheight=screenheight

#     @property
#     def resolution(self):
#         return self.screenwidth * self.screenheight

# s=Screen()
# s.width = 1024
# s.height= 768
# print(s.resolution)
	
# class Animal(object):
#     pass

# class Mammal(Animal):
#     pass

# class Bird(Animal):
#     pass

# class Dog(Mammal):
#     pass

# class Bat(Mammal):
#     pass

# class Parrot(Bird):
#     pass

# class Ostrich(Bird):
#     pass

# class Runnable(object):
#     def run(self):
#         print('Running...')

# class Flyable(object):
#     def fly(self):
#         print('Flying...')

# class Dog(Mammal,Runnable):
#     pass

# class Bat(Mammal,Flyable):
#     pass
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name = %s)' % self.name
#     __repr__=__str__

# s=Student('Michael')
# print(s)
	
# class Fib(object):
#     def __init__(self):
#         self.a, self.b=0,1

#     def __iter__(self):
#         return self

#     def next(self):
#         self.a, self.b =self.b, self.a + self.b
#         if self.a >100000:
#             raise StopIteration()
#         return self.a

# for n in Fib():
#     print(n)

# class Fib(object):
#     def __getitem__(self,n):
#         if isinstance(n,int):
#             a,b =1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n,slice):
#             start=n.start
#             stop=n.stop
#             if start is None:
#                 start=0
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x>=start:
#                     L.append(a)
#                 a,b=b,a+b
#             return L

# f=Fib()
# print f[0:5]

# class Chain(object):

#     def __init__(self,path=''):
#         self._path = path

#     def __getattr__(self,path):
#         return Chain('%s/%s'%(self._path,path))

#     def __str__(self):
#         return self._path

#     __repr__=__str__

# print Chain().status.user.timeline.list

# class Student(object):
#     def __init__(self,name):
#         self.name=name

#     # def __call__(self):
#     #     print('My name is %s.'% self.name)

# s=Student('Michael')
# s()
# print callable(Student)

# class Hello(object):
#     def hello(self,name='World'):
#         print('Hello,%s.'% name)

# class ListMetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         attrs['add']=lambda self, value:self.append(value)
#         return type.__new__(cls,name,bases,attrs)

# class MyList(list):
#     __metaclass__=ListMetaclass

# class User(Model):
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')

# u=User(id=12345,name='Michael',email='test@orm.org',password='my-pwd')
# u.save()

# class Field(object):
#     def __init__ (self,name,colum_type):
#         self.name=name
#         self.column_type=column_type
#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__,self.name)

# class StringField(Field):
#     def __init__(self, name):
#         super(StringField,self).__init__(name,'varchar(100)')

# class IntegeField(Field):
#     def __init__(self,name):
#         super(IntegeField, self).__init__(name,'bigint')

# class ModelMetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         if name=='Model':
#             return type.__new__(cls, name, bases, attrs)
#         mapping=dict()
#         for k,v in attrs.iteritems():
#             if isinstance(v,Field):
#                 print('Found mapping: %s==>%s'%(k,v))
#                 mapping[k]=v
#             for k in mapping.iterkeys():
#                 attrs.pop(k)
#             attrs['__table__']=name
#             attrs['__mappings__']=mappings 
#             return type.__new__(cls,name,bases,attrs)

# class Model(dict):
#     __metaclass__=ModelMetaclass

#     def __init__(self, **kw):
#         super(Model,self).__init__(**kw)

#     def __getattr__(self,key):
#         try:
#             return self[key]

# try:
#     print 'try...'
#     r=10/int('a')
#     print 'result:',r
# except ValueError,e:
#     print 'ValueError:',e
# except ZeroDivisionError,e:
#     print 'except:', e
# finally:
#     print 'finally...'
# print 'END'

# def foo(s):
#     return 10/int(s)

# def bar(s):
#     return foo(s)*2

# def main():
#     try:
#         bar('0')
#     except StandardError,e:
#         logging.exception(e)

# main()
# print 'END'

# class FooError(StandardError):
#     pass

# def foo(s):
#     n=int(s)
#     if n==0:
#         raise FooError('invalid value: %s'% s)
#     return 10/n

# print foo('0')

# def foo(s):
#     n=int(s)
#     return 10/n

# def bar(s):
#     try:
#         return foo(s)*2
#     except StandardError, e:
#         print 'Error!'
#         raise

# def main():
#     bar('0')

# main()
# import logging
# logging.basicConfig(level=logging.INFO)
# # def foo(s):
# #     n=int(s)
# #     assert n!=0,'n is zero'
# #     return 10/n

# # def main():
# #     foo('0')

# # main()

# s='0'
# n=int(s)
# logging.info('n=%d'%n)
# print 10/n
# import pdb
# s='0'
# n=int(s)
# pdb.set_trace()
# print 10/n
# class Dict(dict):
#     def __init__(self,**kw):
#         super(Dict,self).__init__(**kw)

#     def __getattr__(self,key):
#         try:
#             return self[key]
#         except keyError:
#             raise AttributeError(r" 'Dict' object has no attribute '%s' " %key)

#     def __setattr__(self,key,value):
#         self[key]=value

# import unittest

# class TestDict(unittest.TestCase):

#     def setUp(self):
#         print 'setUp...'

#     def test_init(self):
#         d=Dict(a=1,b='test')
#         self.assertEquals(d.a,1)
#         self.assertEquals(d.b,'test')
#         self.assertTrue(isinstance(d,dict))

#     def test_key(self):
#         d=Dict()
#         d['key']='value'
#         self.assertEquals(d['key'],'value')

#     def test_keyerror(self):
#         d=Dict()
#         with self.assertRaises(keyError):
#             value=d['empty']

#     def test_attrerror(self):
#         d=Dict()
#         with self.assertRaises(AttributeError):
#             value=d.empty

#     def tearDown(self):
#         print 'tearDown...'



# if __name__=='__main__':
#     unittest.main()

# f=open('/home/jiayi/Documents/ani.png','rb')
# f=open('/home/jiayi/Documents/tst.txt','rb')
# u=f.read().decode('gbk')
# u
# print u


# try:
#     import cPickle as pickle
# except ImportError:
#     import pickle
# d=dict(name='Bob',age=20,score=88)
# f=open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()

# import os,time,random
# from multiprocessing import Process,Queue
# from multiprocessing import Pool
# print 'Process (%s) start...'% os.getpid()
# pid = os.fork()
# if pid==0:
#     print 'I am child process(%s) and my parent is %s.'%(os.getpid(),os.getppid())
# else:
#     print 'I (%s) just created a child process (%s).' %(os.getpid(),pid)

# def run_proc(name):
#     print 'Run child process %s (%s)...' %(name,os.getpid())

# if __name__=='__main__':
#     print 'parent process %s. ' % os.getpid()
#     p=Process(target=run_proc, args=('test',))
#     print 'Process will start.'
#     p.start()
#     p.join()
#     print 'Process end.'

# def long_time_task(name):
#     print 'Run task %s (%s)...' % (name,os.getpid())
#     start =time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print 'task %s runs %0.2f seconds.' %(name,(end-start))

# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p=Pool()
#     for i in range(9):
#         p.apply_async(long_time_task,args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done.'

# def write(q):
#     for value in ['A','B','C']:
#         print 'Put %s from queue.' %value
#         q.put(value)
#         time.sleep(random.random())

# def read(q):
#     while True:
#         value = q.get(True)
#         print 'Get %s from queue.' %value

# if __name__=='__main__':
#     q=Queue()
#     pw= Process(target=write, args=(q,))
#     pr= Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()

# import time, threading

# def loop():
#     print 'thread %s is running...' % threading.current_thread().name
#     n=0
#     while n<5:
#         n=n+1
#         print 'thread %s >>> %s' %(threading.current_thread().name, n)
#         time.sleep(1)
#     print 'thread %s ended.' %threading.current_thread().name

# print 'thread %s is running...' % threading.current_thread().name
# t= threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print 'thread %s ended.' % threading.current_thread().name

# import time,threading

# balance=0
# lock=threading.Lock()

# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print balance

# import threading

# local_school=threading.local()

# def process_student():
#     print 'Hello, %s (in %s)' %(local_school.student, threading.current_thread().name)

# def process_thread(name):
#     local_school.student = name
#     process_student()

# t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# import re
# test='010-12345'
# if re.match(r'^\d{3}\-\d{3,8}$',test):
#     print 'ok'
# else:
#     print 'failed'

# re_email=re.compile(r'^\w+(\.+\w+|w*)\@\w+\.\w+$')
# print re_email.match('someone@gmial.com')
# print re_email.match('bill.gates@microsoft.com')
# print re_email.match('bill.gates@microsoft.')

# from collections import OrderedDict
# class LastUpdatedOderedDict(OrderedDict):

#     def __init__(self, capacity):
#         super(LastUpdatedOderedDict,self).__init__()
#         self._capacity = capacity

#     def __setitem__(self, key, value):
#         containKey=1 if key in self else 0
#         if len(self) - containKey >= self._capacity:
#             last = self.popitem(last=False)
#             print 'remove:', last
#         if containKey:
#             del self[key]
#             print 'set:', (key, value)
#         else:
#             print 'add:', (key, value)
#         OrderedDict.__setitem__(self, key, value)

# from xml.parsers.expat import ParserCreate

# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' %(name, str(attrs)))

#     def end_element(self,name):
#         print ('sax: end_element: %s' %name)

#     def char_data(self, text):
#         print ('sax:char_data: %s' % text)

# xml=r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
# handlder = DefaultSaxHandler()
# parser = ParserCreate()
# parser.returns_unicode=True
# parser.StartElementHandler = handlder.start_element
# parser.EndElementHandler = handlder.end_element
# parser.CharacterDataHandler = handlder.char_data
# parser.Parse(xml)

# L = []
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(encode('some & data'))
# L.append(r'</root>')
# print ''.join(L)

# from Tkinter import *

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()

# app=Application()
# app.master.title('Hello World')
# app.mainloop()

# def update_srf_geo(lgt_node=[]):
#     if not lgt_node:
#         lgt_node=cku.get_lgt_shot_maker_node()
#     for node in lgt_node:
#         xmlFile=node.getParameter('user.srfXml').getValue(0)
#         if not xmlFile or not os.path.isfile(xmlFile):
#             continue

#         assetXmlInfo=cast.AssetXml(xmlFile,xml_context='SRF_SG_UPDATE',context_data=node)

#         saveToXml=assetXmlInfo.setNewFilePath(xmlFile)
#         newPath=cku.getNewVersion(saveToXml)
#         assetXmlInfo.saveTo(newPath)

#         node.getParameter('user.srfXml').setValue(newPath,0)
# /mnt/proj/projects/cat/asset/chr/blanket/srf/publish/blanket.srf.surfacing.v033/scene_graph_xml/blanket.xml
# tstpath = '/mnt/work/projects/cat/asset/asb/silk_factory_asb/srf/task/katana/jiayi_xml/silk_factory_asb_srf.034.xml'
# import os,re, shutil, datetime

# def change_name_time(xml_tmp_path):
#     new_name = 't' + datetime.datetime.now().strftime("%s") + '.' + xml_tmp_path.split('/')[-1]
#     new_xml_path = xml_tmp_path.replace(xml_tmp_path.split('/')[-1],new_name)
#     os.rename(xml_tmp_path,new_xml_path)
#     return new_xml_path

# def update_group_srf_xml(group_xml_path):
#     task_name_xml = (group_xml_path.split('/')[11]) 
#     task_name = task_name_xml.split('_')[0]
#     new_path = group_xml_path.split(task_name_xml)[0] + task_name +'_tmp'
#     if not os.path.isdir(new_path):
#         os.mkdir(new_path)
#     new_path_xml = new_path + group_xml_path.split(task_name_xml)[1]
#     shutil.copy(group_xml_path,new_path)
#     new_path_xml = change_name_time(new_path_xml)
#     from xml.etree import ElementTree as ET
#     root = ET.parse(new_path_xml)
#     for asset in root.getiterator('instance'):
#         if asset.get('type') == 'reference':
#             asset_xml_path = asset.get('refFile')
#             asset_name = asset_xml_path.split('/')[7]
#             path = asset_xml_path.split('publish')[0] + 'publish'
#             srf_list=os.listdir(path)
#             srf_list.sort()
#             latest_version = srf_list[-1]
#             if srf_list[-1]=='tex' :
#                 latest_version=srf_list[-2]
#             else:
#                 latest_version=srf_list[-1]
#             # print srf_list
#             latest_xml = path+'/'+ latest_version + '/scene_graph_xml/' + asset_name +'.xml'
#             if asset_xml_path != latest_xml:
#                 print asset_xml_path
#                 print latest_xml
#                 print 'Yes'
				# asset.set('refFile',latest_xml)
	# root.write(new_path_xml)
	# return new_path_xml
# tstpath1 = tstpath.replace('xml','tmp')
# print tstpath

 
# print update_group_srf_xml(tstpath)

# task_name_xml = (tstpath.split('/')[11])
# task_name = task_name_xml.split('_')[0]
# new_path = tstpath.split(task_name_xml)[0] + task_name +'_tmp' + tstpath.split(task_name_xml)[1]
# new_path = tstpath.split(task_name_xml)[0] + task_name +'_tmp' 
# shutil.copy(tstpath,new_path)
# print new_path

# path='/mnt/proj/projects/cat/asset/prp/house_inside_silk_factory_a/srf/publish'
# path=os.listdir(path)[-1]
# path=path.split('.')
# print path
# if os.listdir(path)[-1].split('.')[-1] == 'surfacing':
#     print 'Yes'
# tstpath='/mnt/proj/projects/cat/asset/prp/rock_antelope/srf/publish'
# print os.listdir(tstpath)

# def readXml(self,xml,step):
#     assetDict={}
#     infoDic={}
#     root = ET.parse(xml)
#     for asset in root.getiterator('arbitraryList'):
#         for ch in asset.getchildren():
#             ver=ch.get('name')
#             verNum=ch.get('value') 
#             infoDic[ver]=verNum

#     assetDict[step]=infoDic
#     return assetDict

# def latestDownStreamVer(self,step):
#     path='/mnt/proj/projects/%s/asset/%s/%s/%s/publish'%(self.proj,self.assettype,self.assetName,step)
#           /mnt/work/projects/cat/asset/asb/silk_factory_asb/srf/task/katana/fuqiang_xml/silk_factory_asb_srf.034.xml
#           /mnt/proj/projects/cat/asset/asb/silk_factory_asb/srf/publish
#     if os.path.isdir(path):
#         if self.getLatest(path,step):
#             latestVer=self.getLatest(path,step)[0]
#             latestXml=self.getLatest(path,step)[1]
#             return latestVer,latestXml
#     return None

# def getLatest(self,path,step):
#     verDict={}
#     if os.path.isdir(path):
#         for p in os.listdir(path):
#             if step=='rig' and '.rig.rigging.' in p:
#                 xml=path+'/'+p+'/scene_graph_xml/%s.xml'%self.assetName
#                 if os.path.isfile(xml):
#                     verDict[p]=xml
#             elif step=='mod' and '.mod.model.' in p:
#                 xml=path+'/'+p+'/scene_graph_xml/%s.xml'%self.assetName
#                 if os.path.isfile(xml):
#                     verDict[p]=xml
#             elif step=='srf' and '.srf.surfacing.' in p:
#                 xml=path+'/'+p+'/scene_graph_xml/%s.xml'%self.assetName
#                 if os.path.isfile(xml):
#                     verDict[p]=xml

#     if verDict:
#         verList=verDict.keys()
#         verList.sort()
#         return verList[-1],verDict[ verList[-1] ] #return version,asset.xml
#     else:
#         return None
# import os
# path='/mnt/proj/projects/cat/asset/asb/silk_factory_asb/srf/publish'
# print os.listdir(path)

# /mnt/proj/projects/tst/asset/prp/chair_b/srf/publish/chair_b.srf.surfacing.v035/scene_graph_xml/chair_b.xml
# subdiv_objects = []
# subdiv_objects.append ({'name':'Michael','iter': '95'})
# subdiv_objects.append ({'name':'Bob','iter': '75'})
# subdiv_objects.append ({'name':'Tracy','iter': '85'})
# subdiv_objects.append ({'name':'Thoma','iter': '1'})
# subdiv_objects.append ({'name':'Thom','iter': '1'})
# subdiv_objects.append ({'name':'Tho','iter': '1'})
# subdiv_objects.append ({'name':'Thas','iter': '1'})
# subdiv_objects.append ({'name':'Thobs','iter': '1'})
# for o in d:
#     if int(o['scores'])>76:
#         print 'Yes'

# d = {'Michael': 95, 'Bob' : 75, 'Tracy': 85}
# subdiv_objects.append({'name':o[master_pt+1:],'iter':str(iter_value),'iter_origin':str(iter_value_origin)})
# d.append({'Thomas':88})

# print d
# import sys
# from xml.etree import ElementTree as ET
# sys.path.append('/mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts')
# import common.katanaUtils as cku
# tree = ET.parse('country_data.xml')
# root = tree.getroot()


# xml_file = 'country_data.xml'
# root = ET.fromstring(country_data_as_string)
# for child in root:
#     print child.tag, child.attrib
# print root[0][2]
# for neighbor in root.iter('neighbor'):
#     print neighbor.attrib

# inst_list=root.getiterator('instance')
# for inst in inst_list:
#     if inst.attrib.get('name','') == 'master':
#         inst_attr = inst.getiterator('objAttributeList')
#         if inst_attr:
#             for i in inst_attr:
#                 i.clear()
#             inst_attr_temp=inst_attr[0]
#         else:
#             inst_attr_temp = ET.SubElement(inst, 'objAttributeList')

#         inst_attr_temp.set('version','0.0')
#         for obj_attr in subdiv_objects:
#             attr_elem=ET.SubElement(inst_attr_temp, 'attribute')
#             attr_elem.set('name',obj_attr.get('name',''))
#             attr_elem.set('attr','subdivide')
#             if(int(obj_attr['iter']) > 3):
#                 attr_elem.set('value', '3')
#                 attr_elem.set('value_origin', obj_attr.get('iter',''))
#             else:
#                 attr_elem.set('value', obj_attr.get('iter',''))
# cku.indent(root)
# if tree:
#     try:
#         tree.write(xml_file)
#     except:
#         print('写入subdividedata失败')

# ard.getParameter('args.arnoldStatements.iterations.value').setValue(3,0)


# scan_katana() # loading xml 

# check_subdiv()

# bake_look_file

# copy_output_task():

	

#     look_file_bake

#     write_attrs_to_publish_xml() # writing xml


# def getCollectionPath(self,ard):
#     pathStr=""

#     if ard and ard.getParameter('CEL'):
#         objects = ard.getParameter('CEL').getValue(0)
#         pattern='\$(\w+)'
#         collectionList=re.findall(pattern,objects)
#         if not collectionList==[]:
#             for collection in collectionList:
#                 if ngapi.GetNode(collection):
#                     pathList=ngapi.GetNode(collection).getParameter('CEL').getValue(0)
#                     pathStr=pathStr+pathList
#         for ob in objects.split('+'):
#             if not '$' in ob:
#                 pathStr=pathStr+ob
#     return pathStr

# subdiv_objects = [{'name': 'master/poly/hi/geometry/shell/shell_2/shell_2Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/shell/shell_8/shell_8Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/shell/shell_5/shell_5Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/sundries/sundries_c/sundries_c_1/sundries_c_1Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/sundries/sundries_b/sundries_b_1/sundries_b_1Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/sundries/sundries_b/sundries_b_3/sundries_b_3Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/sundries/sundries_b/sundries_b_4/sundries_b_4Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/sundries/sundries_b/sundries_b_2/sundries_b_2Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/sundries/sundries_c/sundries_c_2/sundries_c_2Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/sundries/sundries_c/sundries_c_3/sundries_c_3Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/tyre_PLY/tyre_PLYShape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/shell/shell_1/shell_1Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/shell/shell_3/shell_3Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/shell/shell_12/shell_12Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/shell/shell_4/shell_4Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/railing/railing_2/railing_2Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/fireplug/fireplugShape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/antenna/antenna_1/antenna_1Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/antenna/antenna_2/antenna_2Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/megaphone/megaphone_6/megaphone_6Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/megaphone/megaphone_1/megaphone_1Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/megaphone/megaphone_3/megaphone_3Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/megaphone/megaphone_2/megaphone_2Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/radar/radar_2/radar_2Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/radar/radar_1/radar_1Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/window/windowShape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/door_a/door_a_2/door_a_2Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/door_b/door_b_2/door_b_2Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/shell/shell_6/shell_6Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/shell/shell_7/shell_7Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/shell/shell_10/shell_10Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/shell/shell_11/shell_11Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/shell/shell_9/shell_9Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/buoy/buoyShape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/glass_PLY/glass_PLYShape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/door_a/door_a_1/door_a_1Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/door_b/door_b_1/door_b_1Shape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/cargo/cargoShape', 'iter': '5.0'}, {'name': 'master/poly/hi/geometry/clo/cloShape', 'iter': '5.0'}]

# for obj_attr in subdiv_objects:
#     if(float(obj_attr['iter']) > 3):
		# attr_elem.set('value', '3')
		# attr_elem.set('value_origin', obj_attr.get('iter',''))
	#     print 'over 3'
	# else:
	#     print 'ok'
		# attr_elem.set('value', obj_attr.get('iter',''))
# print int('5')
# import os,sys
# preview_mov = '/mnt/proj/projects/tst/asset/prp/chair_b/srf/publish/chair_b.srf.surfacing.v037/preview/chair_b.srf.surfacing.v037.srf_publish.mov'
# print os.path.basename(preview_mov).split('.')[0]
# print os.path.basename(preview_mov)
# sys.path.append('/mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts')
# import common.ShotGunProj as csgp
# reload(csgp)

# xml_file = '/mnt/proj/projects/tst/asset/prp/chair_b/srf/publish/chair_b.srf.surfacing.v037/scene_graph_xml/chair_b.xml'

# asset_name = os.path.basename(xml_file).split('.')[0]
# proje = xml_file.split('/')[4]
# sgp=csgp.ShotGunProj(proje)
# sgp.update_asset_sg_attr1(asset_name, '6')



# import pymel.core as pm
# t=pm.PyNode('pPlane1')

# def get_face(f0):
#     p_list=f0.getVertices()
#     f_c=f0.connectedFaces()
#     f_l=[]
#     for p in p_list:
#         f_l.extend(pm.MeshVertex(t,p).connectedFaces())
#     f_n=[]
#     for f in f_l:
#         if f not in f_c and f not in f_n and f!=f0:
#             f_n.append(f)
#     return f_n
# def unselect_face(f0):
#     f_u=[]
#     f_u=f0.connectedFaces()
#     return f_u
# f0 = t.f[0]
# face_select_list = [f0]
# num =0
# k =0
# face_output_list = []
# unselect_face_list = []
# while(1):
#     for face_input in face_select_list:
#         face_output_list.extend (get_face(face_input))
#         unselect_face_list.extend(unselect_face(face_input))
#     for face_select in face_output_list:
#         if face_select not in face_select_list and unselect_face_list:
#             face_select_list.append(face_select)
#             k=k+1
#     if num == k:
#         break
#     else:
#         num = k
# for face_select in face_select_list:
#     pm.select(face_select,add=True)

# k=4
# l=6
# num=l-k

# list_tst = []
# unselect_list_1 = []
# num=0
# unselect_list_1 = [1,2,34,555,7]
# list_1 = [1]
# list_2 = [1,2]
# list_3 = [1,2,3]
# list_4 = [1,2,3,4]
# list_5 = [1,2,3,4,5]
# list_6 = [1,2,3,4,5,6]
# unselect_list_2 = [6,7,8,9,10]
# list_tst_tst = [1,2,3,4,5,6,7,8,9,10]
# for a in list_tst_tst:
#     if a not in unselect_list_1 :
#         if a not in unselect_list_2:
#             list_tst.append(a)
# unselect_list_1.extend(list_1)
# unselect_list_1.extend(list_2)
# unselect_list_1.extend(list_3)
# unselect_list_1.extend(list_4)
# unselect_list_1.extend(list_5)
# unselect_list_1.extend(list_6)
# unselect_list_1 = list(set(unselect_list_1))
# print unselect_list_1

# GrowPolygonSelectionRegion

# list_tst = [MeshFace(u'pSphereShape1.f[54]'),
#  MeshFace(u'pSphereShape1.f[43]'),
#  MeshFace(u'pSphereShape1.f[45]'),
#  MeshFace(u'pSphereShape1.f[65]'),
#  MeshFace(u'pSphereShape1.f[63]'),
#  MeshFace(u'pSphereShape1.f[32]'),
#  MeshFace(u'pSphereShape1.f[34]'),
#  MeshFace(u'pSphereShape1.f[52]'),
#  MeshFace(u'pSphereShape1.f[36]'),
#  MeshFace(u'pSphereShape1.f[56]'),
#  MeshFace(u'pSphereShape1.f[76]'),
#  MeshFace(u'pSphereShape1.f[74]'),
#  MeshFace(u'pSphereShape1.f[72]'),
#  MeshFace(u'pSphereShape1.f[21]'),
#  MeshFace(u'pSphereShape1.f[23]'),
#  MeshFace(u'pSphereShape1.f[41]'),
#  MeshFace(u'pSphereShape1.f[25]'),
#  MeshFace(u'pSphereShape1.f[61]'),
#  MeshFace(u'pSphereShape1.f[27]'),
#  MeshFace(u'pSphereShape1.f[47]'),
#  MeshFace(u'pSphereShape1.f[67]'),
#  MeshFace(u'pSphereShape1.f[97]'),
#  MeshFace(u'pSphereShape1.f[95]'),
#  MeshFace(u'pSphereShape1.f[93]'),
#  MeshFace(u'pSphereShape1.f[91]'),
#  MeshFace(u'pSphereShape1.f[10]'),
#  MeshFace(u'pSphereShape1.f[12]'),
#  MeshFace(u'pSphereShape1.f[30]'),
#  MeshFace(u'pSphereShape1.f[14]'),
#  MeshFace(u'pSphereShape1.f[50]'),
#  MeshFace(u'pSphereShape1.f[16]'),
#  MeshFace(u'pSphereShape1.f[70]'),
#  MeshFace(u'pSphereShape1.f[18]'),
#  MeshFace(u'pSphereShape1.f[38]'),
#  MeshFace(u'pSphereShape1.f[58]'),
#  MeshFace(u'pSphereShape1.f[78]'),
#  MeshFace(u'pSphereShape1.f[90]'),
#  MeshFace(u'pSphereShape1.f[92]'),
#  MeshFace(u'pSphereShape1.f[94]'),
#  MeshFace(u'pSphereShape1.f[99]'),
#  MeshFace(u'pSphereShape1.f[98]'),
#  MeshFace(u'pSphereShape1.f[96]'),
#  MeshFace(u'pSphereShape1.f[9]'),
#  MeshFace(u'pSphereShape1.f[1]'),
#  MeshFace(u'pSphereShape1.f[29]'),
#  MeshFace(u'pSphereShape1.f[3]'),
#  MeshFace(u'pSphereShape1.f[49]'),
#  MeshFace(u'pSphereShape1.f[5]'),
#  MeshFace(u'pSphereShape1.f[69]'),
#  MeshFace(u'pSphereShape1.f[7]')]

#  MeshFace(u'pSphereShape1.f[79]'),
#  MeshFace(u'pSphereShape1.f[71]'),
#  MeshFace(u'pSphereShape1.f[73]'),
#  MeshFace(u'pSphereShape1.f[75]'),
#  MeshFace(u'pSphereShape1.f[77]'),
#  MeshFace(u'pSphereShape1.f[88]'),
#  MeshFace(u'pSphereShape1.f[80]'),
#  MeshFace(u'pSphereShape1.f[82]'),
#  MeshFace(u'pSphereShape1.f[84]'),
#  MeshFace(u'pSphereShape1.f[86]'),
#  MeshFace(u'pSphereShape1.f[68]'),
#  MeshFace(u'pSphereShape1.f[60]'),
#  MeshFace(u'pSphereShape1.f[62]'),
#  MeshFace(u'pSphereShape1.f[64]'),
#  MeshFace(u'pSphereShape1.f[66]'),
#  MeshFace(u'pSphereShape1.f[81]'),
#  MeshFace(u'pSphereShape1.f[83]'),
#  MeshFace(u'pSphereShape1.f[85]'),
#  MeshFace(u'pSphereShape1.f[87]'),
#  MeshFace(u'pSphereShape1.f[89]'),
#  MeshFace(u'pSphereShape1.f[57]'),
#  MeshFace(u'pSphereShape1.f[59]'),
#  MeshFace(u'pSphereShape1.f[51]'),
#  MeshFace(u'pSphereShape1.f[53]'),
#  MeshFace(u'pSphereShape1.f[55]'),
#  MeshFace(u'pSphereShape1.f[2]'),
#  MeshFace(u'pSphereShape1.f[0]'),
#  MeshFace(u'pSphereShape1.f[4]'),
#  MeshFace(u'pSphereShape1.f[6]'),
#  MeshFace(u'pSphereShape1.f[8]'),
#  MeshFace(u'pSphereShape1.f[46]'),
#  MeshFace(u'pSphereShape1.f[48]'),
#  MeshFace(u'pSphereShape1.f[40]'),
#  MeshFace(u'pSphereShape1.f[42]'),
#  MeshFace(u'pSphereShape1.f[44]'),
#  MeshFace(u'pSphereShape1.f[13]'),
#  MeshFace(u'pSphereShape1.f[11]'),
#  MeshFace(u'pSphereShape1.f[19]'),
#  MeshFace(u'pSphereShape1.f[15]'),
#  MeshFace(u'pSphereShape1.f[17]'),
#  MeshFace(u'pSphereShape1.f[35]'),
#  MeshFace(u'pSphereShape1.f[37]'),
#  MeshFace(u'pSphereShape1.f[39]'),
#  MeshFace(u'pSphereShape1.f[31]'),
#  MeshFace(u'pSphereShape1.f[33]'),
#  MeshFace(u'pSphereShape1.f[24]'),
#  MeshFace(u'pSphereShape1.f[22]'),
#  MeshFace(u'pSphereShape1.f[20]'),
#  MeshFace(u'pSphereShape1.f[28]'),
#  MeshFace(u'pSphereShape1.f[26]')]

# for tst in list_tst:
#     n=n+1
# print n

# [MeshFace(u'pSphereShape1.f[12]'),
#  MeshFace(u'pSphereShape1.f[6]'),
#  MeshFace(u'pSphereShape1.f[8]'),
#  MeshFace(u'pSphereShape1.f[23]'),
#  MeshFace(u'pSphereShape1.f[21]'),
#  MeshFace(u'pSphereShape1.f[0]'),
#  MeshFace(u'pSphereShape1.f[2]'),
#  MeshFace(u'pSphereShape1.f[10]'),
#  MeshFace(u'pSphereShape1.f[4]'),
#  MeshFace(u'pSphereShape1.f[14]'),
#  MeshFace(u'pSphereShape1.f[20]'),
#  MeshFace(u'pSphereShape1.f[24]'),
#  MeshFace(u'pSphereShape1.f[19]'),
#  MeshFace(u'pSphereShape1.f[16]'),
#  MeshFace(u'pSphereShape1.f[9]'),
#  MeshFace(u'pSphereShape1.f[18]'),
#  MeshFace(u'pSphereShape1.f[15]'),
#  MeshFace(u'pSphereShape1.f[5]'),
#  MeshFace(u'pSphereShape1.f[11]'),
#  MeshFace(u'pSphereShape1.f[22]'),
#  MeshFace(u'pSphereShape1.f[13]'),
#  MeshFace(u'pSphereShape1.f[3]'),
#  MeshFace(u'pSphereShape1.f[17]'),
#  MeshFace(u'pSphereShape1.f[1]'),
#  MeshFace(u'pSphereShape1.f[7]')] 
# import pymel.core as pm



# def get_face(f0):
#     p_list=f0.getVertices()
#     f_c=f0.connectedFaces()
#     f_l=[]
#     for p in p_list:
#         f_l.extend(pm.MeshVertex(t,p).connectedFaces())
#     f_n=[]
#     for f in f_l:
#         if f not in f_c and f not in f_n and f!=f0:
#             f_n.append(f)
#     return f_n

# def unselect_face(f0):
#     f_u = []
#     f_u=f0.connectedFaces()
#     return f_u

# node_name = pm.ls(sl=True)
# node_name=node_name[0] 
# selectface_id = node_name.index()
# t=pm.PyNode(node_name)
# f0 = t.f[selectface_id]
# face_select_list = [f0]
# face_output_list = []
# unselect_face_list = []
# num = 0
# k = 0
# l = 0


# while(1):
#     num_1 = len(face_output_list)
#     for face_input in face_select_list[-num:]:
#         face_output_list.extend (get_face(face_input))
#         unselect_face_list.extend(unselect_face(face_input))
#     num_2 = len(face_output_list)
#     num_3 = num_2-num_1
#     for face_select in face_output_list[-num_3:]:
#         if face_select not in face_select_list and face_select not in unselect_face_list:
#             face_select_list.append(face_select)
#             k=k+1
#     if l == k:
#         break
#     else:
#         num=k-l
#         l = k

# for face_select in face_select_list:
#     pm.select(face_select,add=True)

# import maya.cmds as cmds
# import pymel.core as pm

# sel = cmds.ls(sl=True)
# poly_obj = cmds.ls(*sel, o=True)[0]
# poly_node = pm.PyNode(poly_obj)
# face_count = pm.polyEvaluate(poly_obj, f=True)
# face_list = []
# to_select = []
# explored = [False]*face_count
# selected = [False]*face_count

# for i in range(face_count):
#     face_list.append(poly_node.f[i])

# start_face = pm.PyNode(sel[0])
# bfs_list = [start_face]
# selected[start_face.index()]=True
# while bfs_list:
#     curr_face = bfs_list.pop(0)
#     curr_index = curr_face.index()
#     if not explored[curr_index]:
#         explored[curr_index]=True
#         connected_faces = curr_face.connectedFaces()
#         for conn in connected_faces:
#             conn_index = conn.index()
#             if not explored[conn_index]:
#                 bfs_list.append(conn)
#                 if not selected[curr_index]:
#                     selected[conn_index] = True
#                     to_select.append(conn)
					
# pm.select(to_select,add=True)
# rvio='/usr/local/rv/rv-Linux-x86-64-6.2.2/bin/rvio'
# self_check_folder = '/home/jiayi/Desktop/tst'
# preview_mov = '/home/jiayi/Desktop/tst/daisy_a.srf.surfacing.v005.srf_publish.mov'
# preview_shotgun_mov = '/home/jiayi/Desktop/tst/daisy_a.srf.surfacing.v005.mov'
# import os
# all_files={}
# mov_files = []
# for f in os.listdir(self_check_folder):
#     f_path=self_check_folder+'/'+f
#     if os.path.isfile(f_path) and f_path.endswith('.exr'):
#         all_files[f.split('.')[-2]]=f_path
# print all_files
# for k,v in all_files.items():
#     image_pass_tag_args=' -overlay topleft "render_time : '+'shashasha'+'" .7 1 30'+\
#                         ' -overlay topright "peak_memory : '+'5'+ 'MB" .7 1 30'+\
#                         ' -overlay bottomleft "user : '+'jiayi'+ '" .7 1 30'+\
#                         ' -overlay bottomright "look_pass : '+'what'+ '" .7 1 30'+\
#                         ' -overlay bottomcenter '+'whatever'+ ' .7 1 30'
#     cmd_str=rvio+' '+v+image_pass_tag_args+' -outsrgb -o '+v.replace('.exr','.mov')
#     print '\nRV Cmd :',cmd_str,'\n'
#     os.system(cmd_str)
#     mov_files.append(v.replace('.exr','.mov'))
#     print '\n-------Convert exr',v,'to',mov_files[-1],'\n'
#     check_v_name='tst'+'.'+"v001"+'.'+k+'.jpg'
#     check_v=os.path.join('/home/jiayi/Desktop/tst',check_v_name)
#     check_cmd_str=rvio+' '+v+' -outsrgb -o '+ check_v
#     os.system(check_cmd_str)
#     print '\n-------Copy to check Folder',v,'to',check_v,'\n'
# self_check_folder = '/mnt/proj/projects/tst/asset/flg/daisy_a/srf/publish/daisy_a.srf.surfacing.v005/self_check'
#                      /mnt/proj/projects/tst/asset/flg/daisy_a/srf/publish/daisy_a.srf.surfacing.v005
# what = self_check_folder.rsplit('/',1)[0]
# print what
# version_folder_path = '/mnt/proj/projects/tst/asset/flg/daisy_a/srf/publish/daisy_a.srf.surfacing.v005'
# version_folder=os.path.basename( version_folder_path)
# mov_f=os.path.join(version_folder_path,'preview',version_folder+'.mov')
# print mov_f
# if os.path.isfile(preview_mov) :
#     print 'Yes'
#     temp_mov=preview_shotgun_mov.replace('.mov','.tmp.mov')
#     combine_cmd=rvio+' '+' '.join(mov_files)+' '+preview_mov+' -o '+temp_mov
#     os.system(combine_cmd)
# /mnt/proj/projects/tst/asset/flg/daisy_a/srf/publish/daisy_a.srf.surfacing.v005/self_check/direct_backlight.####.exr

# c80040:4085,4640,66250
# c80050:4105,4660,64000
# c80060:4090,4637,59018
# c80070:70,5,10355
# c80080:4093,4615,47733
# c80090:3990,4623,39952

# c70100:3825,4618,31670

# c80110:3828,4616,30244
# c80120:2787,4639,31805
# c80130:1836,-51088,17630

# c80150:1935,9000,16939
# c80160:1935,13300,15000
# c80170:1950,11130,15000
# c80190:1954,15850,14980
# c80200:1960,-168340,14365



# c80 010-030 0 0 -40000
# c80 040-130 4039 4686 44376
# c80 140-140 0 0 -40000
# c80 150-220 4039 4686 44376

# c80 230-230 0 0 -40000
# c80 240-240 4039 4686 44376

# c80 360-370 0 0 -40000

# def minus(a,b,c,strin_t):
#     result=[]
#     a_1 = a-4039 
#     b_1 = b-4686 
#     c_1 = c-44376  
#     result.append(a_1)
#     result.append(b_1)
#     result.append(c_1)
#     print strin_t
#     print result 

# def minus_2(a,b,c,strin_t):
#     result=[]
#     a_1 = a-4039 
#     b_1 = b-4686 
#     c_1 = c-44376  
#     result.append(a_1)
#     result.append(b_1)
#     result.append(c_1)
#     print strin_t
#     print result 

# str1 ='c80040'
# minus(4085,4640,66250,str1)
# str2 = 'c80050'
# minus(4105,4660,64000,str2)
# str3 = 'c80060'
# minus(4090,4637,59018,str3)
# str4 ='c80070:'
# minus(70,5,10355,str4)
# str5 = 'c80080:'
# minus(4093,4615,47733,str5)
# str6 = 'c80090:'
# minus(3990,4623,39952,str6)
# str1 = 'c80100:'
# minus(3825,4618,31670,str1)
# str1 = 'c80110:'
# minus(3828,4616,30244,str1)
# str1 = 'c80120:'
# minus(2787,4639,31805,str1)
# str1 = 'c80130:'
# minus(1836,-51088,17630,str1)
# str1 = 'c80150:'
# minus(1935,9000,16939,str1)
# str1 = 'c80160:'
# minus(1935,13300,15000,str1)
# str1 = 'c80170:'
# minus(1950,11130,15000,str1)
# str1 ='c80190:'
# minus(1954,15850,14980,str1)
# str1 = 'c80200:'
# minus(1960,-168340,14365,str1)
# str1 = 'c80100:'
# minus(3825,4618,31670,str1)
# c80040
# [46, -46, 21874]
# c80050
# [66, -26, 19624]
# c80060
# [51, -49, 14642]
# c80070:
# [-3969, -4681, -34021]
# c80080:
# [54, -71, 3357]
# c80090:
# [-49, -63, -4424]
# c80100:
# [-214, -68, -12706]
# c80110:
# [-211, -70, -14132]
# c80120:
# [-1252, -47, -12571]
# c80130:
# [-2203, -55774, -26746]
# c80150:
# [-2104, 4314, -27437]
# c80160:
# [-2104, 8614, -29376]
# c80170:
# [-2089, 6444, -29376]
# c80190:
# [-2085, 11164, -29396]
# c80200:
# [-2079, -173026, -30011]
# c80100:
# [-214, -68, -12706]

# tst = '/tmp/wulala.exr'
# size = len(tst.split('/'))
# new_seq=tst.replace(tst.split('/')[-1],'default.exr')
# print new_seq
# import os
# print os.getenv('LCTOOLSET')
# tst = '/mnt/proj/projects/tst/asset/flg/daisy_a/srf/publish/daisy_a.srf.surfacing.v011/self_check/daisy_a.default.exr'
# str(getParam("AutoEasyRender.user.image_path")).replace(str(getParam("AutoEasyRender.user.image_path")).split('.')[-2],'back_light')
# str(getParam("AutoEasyRender.user.image_path")).replace(str(getParam("AutoEasyRender.user.image_path")).split('/')[-1],'back_light.exr')
# print tst.replace(tst.split('.')[-2],'back_light')
# tst = '/mnt/proj/projects/tst/asset/flg/daisy_a/srf/publish/daisy_a.srf.surfacing.v011/self_check/daisy_a.back_light.exr'
# if tst.split('.')[-2]=='back_light':
#     print 'it is 1'
# else:
#     print 'it is 2'

# (1)self.iter = ''
# (2)self.iter = str(iter_value)
# (3)sgp.update_asset_sg_attr1(asset_name, self.iter)
# (4)update_asset_sg_attr1(self,asset,subdivide_level)
# (5)sg.update('Asset', asset_data[0]['id'], {'sg_attr1':float(subdivide_level)})

# import os,sys
# from scipy import stats 
# import numpy as np 
# f= 
# tst = ''
# print float(tst)
# os.path.dirname(old_path)                  +'/'+self.args.get('asset','').split('.')[-1]+        '.' +ap+'.exr'
# /mnt/proj/projects/tst/asset/flg/daisy_a/srf/publish/daisy_a.srf.surfacing.v001/self_check/daisy_a.default.exr
# /mnt/proj/projects/tst/asset/flg/daisy_a/srf/publish/daisy_a.srf.surfacing.v001/self_check/daisy_a.default.exr
# /mnt/public/Share/zhaojiayi/gitrepo/lcatools/tools/set/wulala/wulala  -p tst -ssc 1 -d 0 -c 1 -usp 1 -u jiayi srf.daisy_a
# self_check_folder = '/mnt/proj/projects/tst/asset/flg/daisy_a/srf/publish/daisy_a.srf.surfacing.v012/self_check'
# print self_check_folder.split('/')[-2].split('.')[-1]

# import sys
# sys.path.append('/mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts')
# import os

# import common.ShotGunProj as csgp
# reload(csgp)



# global sg
# sg=None

# def init_shotgun():
#     global sg
#     if not sg:
#         from production.shotgun_connection import Connection
#         sg = Connection('get_project_info').get_sg()


# proje = 'tst'
# sgp=csgp.ShotGunProj(proje)

# asset_name = 'chair_b'
# sgp.update_asset_sg_attr1(asset_name, 6.0)
# assembly_file = '/home/jiayi/Desktop/tst/assembly_definition.ma'
# f = open(assembly_file, 'r')
# l_lines = f.readlines()
# f.close()
# f = open(assembly_file, 'w')
# for line in l_lines:
#     new_line = line.replace('{ASSET}', 'asset_name')
#     new_line = new_line.replace('{GPU_CACHE}', 'gpu_cache')
#     new_line = new_line.replace('{MAYA_FILE}', 'maya_file')
#     new_line = new_line.replace('{GPU_CACHE_HI}', 'gpu_hi')
#     new_line = new_line.replace('{MAYA_FILE_HI}', 'maya_hi')
#     if 'rep[0].rda' in line:
#         new_line = new_line.replace('{GPU_CACHE_PROXY}', 'gpu_hi')
#     else:
#         new_line = new_line.replace('{GPU_CACHE_PROXY}', 'gpu_proxy')
#     new_line = new_line.replace('{GPU_CACHE_COLOR_ID}', 'gpu_color_id')
#     new_line = new_line.replace('{MAYA_FILE_PROXY}', 'maya_proxy')
#     f.write(new_line)
# f.close()

# setAttr ".rep[0].rda" -type "string" "/mnt/proj/projects/tst/asset/asb/accessories/mod/publish/accessories.mod.model.v031/assembly_reference/accessories.ma";
# setAttr ".rep[0].rda" -type "string" "/mnt/proj/projects/tst/asset/asb/accessories/mod/publish/accessories.mod.model.v032/assembly_reference/accessories.ma";
# if 'rep[0].rda' in line and not 'No USD' in proj_tags:
# shot_list = ['e50010','e50020','e50030','e50035','e50040','e50050','e50060','e50070','e50080',
#              'e50090','e50100','e50110','e50120','e50130','e50140',e50150,e50170,e50180,
#              e50190,e50200,e50210,e50220,e50230,e50240,e50250,e50260,e50265,
#              e50270,e50280,e50290,e50300,e50310,e50320,e50330,e50340,e50350,
#              e50360,e50370,e50380,e50390,e50400,e50410,e50420,e50430,e50440,
#              e50450,e50460,e50470,e50480,e50490,e50500]
# from production import shotgun_connection
# sg = shotgun_connection.Connection('get_shot_info').get_sg()
# import os,sys,re

# try:
#     from lxml import etree as ET
# except:
#     import xml.etree.ElementTree as ET

# def GetshotlistFromShotGun(proj,sequence,priority=None):
#     #sg_priority
#     if priority:
#         shotEntitylist=sg.find('Shot',[['project','name_is',proj],["sg_sequence",'name_is',sequence],["sg_priority",'is',priority],["sg_status_list","is_not","omt"]],['code'])
#     else:
#         shotEntitylist=sg.find('Shot',[['project','name_is',proj],["sg_sequence",'name_is',sequence],["sg_status_list","is_not","omt"]],['code'])
#     if shotEntitylist:
#         shotlist=[x["code"] for x  in shotEntitylist if x]
#         shotlist.sort()
#         return shotlist

# shot_list = GetshotlistFromShotGun('cat','c80')
# # shot_list_c80 =GetshotlistFromShotGun('cat','c80')
# # print shot_list
# latest_version_path_list = []
# for shot in shot_list:
#     version_path = ('/mnt/proj/projects/cat/shot/c80/%s/flo/publish'%shot)
#     latest_flo_version = os.listdir(version_path)
#     if all(x is None for x in latest_flo_version):
#         pass
#     else:
#         latest_version_path_list.append('/mnt/proj/projects/cat/shot/c80/%s/flo/publish/%s/scene_graph_xml/%s.xml'%(shot,latest_flo_version[-1],shot))
# xml = '/home/jiayi/Desktop/untitled_folder/e50035.xml'
# def readXml(xml):
#     tag = 0
#     root = ET.parse(xml)
#     for asset in root.getiterator('instance'):
#         if asset.get('type')=='reference':
#             bo = asset.getiterator('bounds')
#             if bo[0].get('maxx') == '999999.999':
#                 if tag==0:
#                     print xml
#                     tag=1
#                 print asset.get('name')

# def editXml(xml):
#     tree = ET.parse(xml)
#     root = tree.getroot()
#     for asset in root.getiterator('instance'):
#         if asset.get('name')=='trees_in_south' and asset.get('type')=='group' :
#             parentNode = asset.getparent()
#             ParentNode.remove(asset)
#             # print asset
#             # root.remove(asset)
#     tree.write(xml)
# for xml in latest_version_path_list:
#     editXml(xml)
# editXml(xml)

# def editXml(xml):
#     tree = ET.parse(xml)
#     root = tree.getroot()
#     inst_nodes=root.xpath('//instance')
#     for node in inst_nodes:
#         if node.attrib.has_key('type') and node.attrib['type']=="group" and node.attrib.has_key('groupType') and node.attrib['groupType']=="assembly" and node.attrib['name'] == "trees_in_south":
#             instanceParent = node.getparent()
#             instanceParent.remove(node)
#             print xml
#     tree.write(xml)

# for xml in latest_version_path_list:
#     if os.path.isfile(xml):
#         editXml(xml)


# from xml.parsers.expat import ParserCreate

# class DefaultSaxHandler(object):
#     def start_element(self,name,attrs):
#         print('sax:start_element: %s, attrs: %s' %(name, str(attrs)))

#     def end_element(self,name):
#         print('sax:end_element: %s'%name)

#     def char_data(self,text):
#         print('sax:char_data:%s'%text)

# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''

# handlder = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handlder.start_element
# parser.EndElementHandler = handlder.end_element
# parser.CharacterDataHandler = handlder.char_data
# parser.Parse(xml)

# try:
#     from lxml import etree
#     print("running with lxml.etree")
# except ImportError:
#     try:
#         import xml.etree.cElementTree as etree
#         print("running with cElementTree on python 2.5+")
#     except ImportError:
#         try:
#             import xml.etree.ElementTree as etree
#             print("running with ElementTree on python 2.5+")
#         except ImportError:
#             try:
#                 import cElementTree as etree
#                 print("running with cElementTree")
#             except ImportError:
#                 try:
#                     import elementtree.ElementTree as etree
#                     print("runing with ElementTree")
#                 except ImportError:
#                     print ("Failed to import ElementTree from any known place")

# try:
#     from lxml import etree 
# except:
#     import xml.etree.ElementTree as etree
# from io import BytesIO
# class DataSource:
#     data = [ b"<roo", b"t><", b"a/", b"><", b"/root>" ]
#     def read(self, requested_size):
#         try:
#             return self.data.pop(0)
#         except IndexError:
#             return b''

# tree = etree.parse(DataSource())
# print etree.tostring(tree)

# parser = etree.XMLParser()
# parser.feed("<roo")
# parser.feed("t><")
# parser.feed("a/")
# parser.feed("><")
# parser.feed("/root>")
# root = parser.close()
# print etree.tostring(root)

# parser.feed("<root/>")
# root = parser.close()
# print etree.tostring(root)
# some_file_like = BytesIO(b"<root><a>data</a></root>")
# for event, element in tree.iterparse(some_file_like):
#     print("%s, %4s, %s" % (event, element.tag, element.text))

# some_file_like = BytesIO(b"<root><a>data</a></root>")

# for event, element in etree.iterparse(some_file_like, events= ("start","end")):
#     print("%5s, %4s, %s" % (event, element.tag, element.text))

# some_file_like =  BytesIO(b"<root><a><b>data</b></a><a><b/></a></root>")

# for event, element in etree.iterparse(some_file_like):
#     if element.tag == 'b':
#         print(element.text)
#     elif element.tag == 'a':
#         print("** cleaning up the subtree")
#         element.clear()

# xml_file = BytesIO(b'''\
#     <root>
#       <a><b>ABC</b><c>abc</c></a>
#       <a><b>MORE DATA</b><c>more data</c></a>
#       <a><b>XYZ</b><c>xyz</c></a>
#     </root>''')
# for _, element in etree.iterparse(xml_file, tag='a'):
#     print('%s --%s' % (element.findtext('b'), element.findtext('c')))
#     element.clear()

# class ParserTarget:
#     events = []
#     close_count = 0
#     def start(self, tag, attrib):
#         self.events.append(("start", tag, attrib))
#     def close(self):
#         events, self.events = self.events, []
#         self.close_count += 1
#         return events

# parser_target = ParserTarget()

# parser = etree.XMLParser(target=parser_target)
# events = etree.fromstring('<root test="true"/>', parser)

# print(parser_target.close_count)
# for event in events:
#     print('event: %s - tag: %s' %(event[0], event[1]))
#     for attr, value in event[2].items():
#         print(' * %s = %s' %(attr, value))

# events = etree.fromstring('<root test="true"/>', parser)
# print(parser_target.close_count)

# events = etree.fromstring('<root test="true"/>', parser)
# print(parser_target.close_count)

# events = etree.fromstring('<root test="true"/>', parser)
# print(parser_target.close_count)

# print(parser_target.close_count)
# for event in events:
#     print('event: %s - tag: %s' %(event[0], event[1]))
#     for attr, value in event[2].items():
#         print(' * %s = %s' %(attr, value))

# xhtml = etree.Element("{http://w")
# value = []

# def tst(value_origin):
#     value_origin.append(2)

# tst(value)

# print value





# try:
#     from lxml import etree as ET
# except:
#     import xml.etree.ElementTree as ET

# def change_fullpath(xml_path):
#     tree = ET.parse(xml_path)
#     root = tree.getroot()
#     inst_nodes=root.xpath('//description')
#     origin_full_path = inst_nodes[0].attrib['Full_Path']
#     print origin_full_path
#     origin_full_path = filter(lambda c: not c.isdigit(),origin_full_path)
#     print origin_full_path
#     inst_nodes[0].attrib['Full_Path'] =  origin_full_path
#     # change_word = (origin_full_path.split('|')[4]).split('_')[1]
#     # print change_word
#     tree.write(xml_path)

# change_fullpath('/home/jiayi/Desktop/tst.xml')
# import sys
# sys.path.append('/mnt/proj/software/lib/lib64/python2.6/site-packages')
# from argparse import ArgumentParser

# parser = ArgumentParser(usage='just used for tst')
# parser.add_argument("-f", "--fruit",help="it is a kind of fruit", default="orange")
# parser.add_argument("-n", "--number",help="it means the number of the fruit",type=int, default=0)
# parser.add_argument("-he", "--heroes",help="it is a kind of ability", default="superman")
# parser.add_argument("-t", "--type",help="it is all kinds of number", choices=[1,2,3],type=int,default=0)

# parser.add_argument("-p", "--proj",help="project name,default god", default="tpr")

# # parser.add_argument("-py", "--python",help="python script file to exectue in set file",default="")
# parser.add_argument("-fa", "--farm",help="send build and render to farm",default=0,type=int)

# parser.add_argument('-ipath','--imagepath',help='output image path folder,put it with katana file if None',default="")
# parser.add_argument('-ipng','--imagepng',help='convert first frame to png,and put it in this folder',default="")
# parser.add_argument('-kpath','--katanapath',help='output katana file path folder,use set task folder if None',default="")
# parser.add_argument('-kexe','--katanaexe',help='use custom katana exe',default="")

# parser.add_argument("-aa", "--aasamples",help="render settings AA_samples",default=5,type=int)
# parser.add_argument("-sf", "--singleframe",help="render single frame or multi frame,10 frames at most if in multi frame mode",default=1,type=int)

# parser.add_argument('-s','--status',help='set status,0: Rough Set,1: Better Set,2: Final Set',choices=[0,1,2],type=int,default=0)
# parser.add_argument("-pub", "--publish",help="publish or not,if -vz 1,publish will be 1",default=1,type=int)
# parser.add_argument('-vz','--vzero',help='publish to v000 or new set vesion',choices=[0,1],type=int,default=0)

# parser.add_argument('-u','--user',help='send message to user via pidgin',default="huangxin")
# parser.add_argument("-msg", "--message",help="send msg to user",default=0,type=int)
# parser.add_argument("-d", "--debug",help="yingjie debug mode",default=0,type=int)
# parser.add_argument("-des", "--description",help="set description",default="")

# parser.add_argument('-shot',"--shot",help='shot name,f70030',default="")

# temp_args,unknow = parser.parse_known_args()
# args=vars(temp_args)
# extra_args=''
# for k,v in args.items():
#     if k not in ['proj','shot','farm']:
#         if str(v):
#             extra_args+='--'+k+' '+str(v)+' '

#     print 'extra_args is '+ extra_args

# extra_args is --shot  --farm 0 --number 0 --fruit orange --proj tpr --heroes superman --type 0

# extra_args is --number 0 --fruit orange --heroes superman --type 0 

# tst = 17+15+50+7+7+3+14+17+7+13+15+5+4+6+4+12+7+20+4+6+23
# print tst

# def tst():
#     debug = 1
#     if debug ==1:
#         print "Yes"
#         # return

#     try:
#         print "No"
#     except:
#         print "No No"

# tst()

# import subprocess 

# subprocess.call(["ls","-l"])
# from os import fork,execlp,wait

# pid = fork()
# if pid == 0:
#     execlp("ls","ls","-1",None)
# else:
#     retval = wait(pid)

# subprocess.check_output("ls")

# parser = ArgumentParser(usage='Set dressing v000')
# parser.add_argument("-p", "--proj",help="project name,default god", default="tpr")

# parser.add_argument("-py", "--python",help="python script file to exectue in set file",default="")
# parser.add_argument("-f", "--farm",help="send build and render to farm",default=0,type=int)

# parser.add_argument('-ipath','--imagepath',help='output image path folder,put it with katana file if None',default="")
# parser.add_argument('-ipng','--imagepng',help='convert first frame to png,and put it in this folder',default="")
# parser.add_argument('-kpath','--katanapath',help='output katana file path folder,use set task folder if None',default="")
# parser.add_argument('-kexe','--katanaexe',help='use custom katana exe',default="")

# parser.add_argument("-aa", "--aasamples",help="render settings AA_samples",default=5,type=int)
# parser.add_argument("-sf", "--singleframe",help="render single frame or multi frame,10 frames at most if in multi frame mode",default=1,type=int)

# parser.add_argument('-s','--status',help='set status,0: Rough Set,1: Better Set,2: Final Set',choices=[0,1,2],type=int,default=0)
# parser.add_argument("-pub", "--publish",help="publish or not,if -vz 1,publish will be 1",default=1,type=int)
# parser.add_argument('-vz','--vzero',help='publish to v000 or new set vesion',choices=[0,1],type=int,default=0)

# parser.add_argument('-u','--user',help='send message to user via pidgin',default="huangxin")
# parser.add_argument("-msg", "--message",help="send msg to user",default=0,type=int)
# parser.add_argument("-d", "--debug",help="yingjie debug mode",default=0,type=int)
# parser.add_argument("-des", "--description",help="set description",default="")

# parser.add_argument('shot',help='shot name,f70030')

# args=None

# temp_args,unknow = parser.parse_known_args()
# print temp_args
# args=vars(temp_args)

# extra_args=''
# for k,v in args.items():
#     if k not in ['proj','shot','farm']:
#         if str(v):
#             extra_args+='--'+k+' '+str(v)+' '
#             print extra_args

# python /mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts/auto_set/auto_set_vz_cmd.py -p tst -pub 1 -u jiayi -s 0 -f 1 -aa 1   a10080


# /mnt/work/software/k2/katana2.1v1b4/ktoa --script=/mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts/auto_set/auto_set_vz_v1.py /tmp/xiaos_render_.22480.config

# import subprocess

# cmd = 'python /home/jiayi/Desktop/tst_pipe.py'
# pp=subprocess.Popen(cmd, shell=True,stdout = subprocess.PIPE)
# line ='\nStart testing...'

# while line != "":
#     line = pp.stdout.readline()
#     print 'the output pipe is ' + line


# args = {'status': '0', 'imagepath': '', 'imagepng': '',
#  'description': 'nihao', 'python': '', 'endframe': '1',
#   'katana': '/mnt/work/software/k2/katana2.1v1b4/ktoa',
#    'aasamples': '1', 'publish': '1', 'farm': '0',
#     'singleframe': '1', 'user': 'jiayi', 'katanaexe': '',
#      'debug': '0', 'vzero': '0', 'message': '0', 'katanapath': '',
#       'shot': 'k80450', 'proj': 'tst'}


# if int(args['endframe'])==1:
#     args['description'] += " \n渲染最后一帧 "
# if args['description']:
#     print "Yes"
#     print args['description']
# else:
#     print args['description']
# # print args.get('python')

# print args.get('aasamples',5)





# description = str(self.deslineEditbel.text())

# x=5
# print type(x)

# def setProj(proj,connect_shotgun=False):
#     if connect_shotgun:
#         print "Yes"
#     else:
#         print "No"

# setProj(args['proj'])
# import sys,os
# class lcProdProj:
#     def __init__(self):
#         rootDir = {'linux2': '/mnt/proj/projects', 'win32':
#                         'z:/projects', 'darwin': '/Volumes/publish/projects'} 
#         self.rootDir = {'local':os.environ.get('LC_PROJ_PATH',rootDir[sys.platform])}
#     def setProj(self,proj):
#         self.proj = proj
#         self.projRoot = self.rootDir['local'] + '/' +self.proj
#         self.assetRoot = self.projRoot + '/asset'

#         self.all_asset_type = []
#         if os.path.isdir(self.assetRoot):
#             for v in os.listdir(self.assetRoot):
#                 if '.' not in v:
#                     self.all_asset_type.append(v)
#         print self.all_asset_type

# # lcProdProj_instance = lcProdProj()
# # lcProdProj_instance.setProj(args['proj'])
# def getshotNextVersionFolder():


# def __get_export_katana_files(set_args,pub_f,shot):
#     export_katana_files=[]

#     v0

# f = '/mnt/proj/projects/tst/shot/a10/a10080/set/publish'
# __get_export_katana_files(args,f,'a10080',)

# exp_file = '/mnt/work/projects/tst/shot/a10/a10080/set/task/katana/a10080.set.set_dressing.v287/a10080.katana'
# out_set_path = '/mnt/proj/projects/tst/shot/a10/a10080/set/publish/a10080.set.set_dressing.v276'
# v0_folder = '/mnt/proj/projects/tst/shot/a10/a10080/set/publish/a10080.set.set_dressing.v270' 
# pub_f = '/mnt/proj/projects/tst/shot/a10/a10080/set/publish'

# import os,re,string
# version_dirs = os.listdir(pub_f)
# versions = sorted(version_dirs)
# # print versions
# version_num = re.findall('\.v(\d*$)',versions[-1])
# print version_num

# a10080.set.set_dressing.v275
# import re

# v_num = int(version_num[0])
# # # publish_version_name = 'a10080'+'.set.set_dressing.v'+string.zfill(v_num+1,3)
# publish_version_name = 'a10080'+'.set.set_dressing.v'+string.zfill(v_num,3)

# # print publish_version_name
# v0_folder=pub_f+'/'+publish_version_name
# # print v0_folder

# export_katana_files=[]
# export_katana_files.append(v0_folder)
# export_katana_files.append(out_set_path)
# # for f in export_katana_files:
# #     if f == os.path.dirname('/mnt/work/projects/tst/shot/a10/a10080/set/task/katana/a10080.set.set_dressing.v287/a10080_ani_sg.xml'):
# #         print os.path.dirname('/mnt/work/projects/tst/shot/a10/a10080/set/task/katana/a10080.set.set_dressing.v287/a10080_ani_sg.xml')
# print export_katana_files
# render_katana_file=export_katana_files[-1]+'/'+'a10080'+'.render.katana'



# print render_katana_file

# publish_version_folder = export_katana_files[0]+'/preview'
# print publish_version_folder

# tag=os.path.basename(render_katana_file)+' -- '+args['user']
# print tag

# from PyQt4.QtGui import *  
# from PyQt4.QtCore import *  
# import sys  
  
# QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
  
# class MainWindow(QMainWindow):  
#     def __init__(self,parent=None):  
#         super(MainWindow,self).__init__(parent)  
#         # f=QFont("ZYSong18030",120)  
#         # self.setFont(f)  
		  
#         self.setWindowTitle("Image Processor")  
#         self.imageLabel=QLabel()  
#         self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)   
#         self.imageLabel.setScaledContents(True)  
		  
#         self.setCentralWidget(self.imageLabel)  
#         self.image=QImage()  

#         self.createActions()  
#         self.createMenus()  
#         self.createToolBars()  
		  
#     def createActions(self):  
#         self.zoominAction=QAction(QIcon("/mnt/public/Share/zhaojiayi/photos/pokecoin.png"),self.tr("+"),self)  
#         self.zoominAction.setShortcut("Ctrl+P")  
#         self.zoominAction.setStatusTip(self.tr("="))  
#         self.connect(self.zoominAction,SIGNAL("triggered()"),self.slotZoomin)  
		  
#         self.deflateAction=QAction(QIcon("/home/huazhuo/Pictures/icon/Minus.png"),self.tr("-"),self)  
#         self.deflateAction.setShortcut("Ctrl+A")  
#         self.deflateAction.setStatusTip(self.tr("-"))  
#         self.connect(self.deflateAction,SIGNAL("triggered()"),self.slotDeflate)  
		  
#         self.circumgyrate=QAction(QIcon("/home/huazhuo/Pictures/icon/rotate.png"),self.tr("*"),self)  
#         self.circumgyrate.setShortcut("Ctrl+B")  
#         self.circumgyrate.setStatusTip(self.tr("*"))  
#         self.connect(self.circumgyrate,SIGNAL("triggered()"),self.slotCircumgyrate)  
		  
#     def createMenus(self):  
#         PrintMenu=self.menuBar().addMenu(self.tr("+-"))  
#         PrintMenu.addAction(self.zoominAction)  
#         PrintMenu.addAction(self.deflateAction)  
#         circumgyrateMenu=self.menuBar().addMenu(self.tr("*"))  
#         circumgyrateMenu.addAction(self.circumgyrate)  
		  
#     def createToolBars(self):  
#         fileToolBar=self.addToolBar("Print")  
#         fileToolBar.addAction(self.zoominAction)  
#         fileToolBar.addAction(self.deflateAction)  
#         fileToolBar.addAction(self.circumgyrate)  
	  
#     def slotZoomin(self):  
#         if self.image.isNull():  
#             return  
#         martix = QMatrix()  
#         martix.scale(2,2)  
#         self.image=self.image.transformed(martix);  
#         self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  
#         self.resize(self.image.width(),self.image.height())   
	  
#     def slotDeflate(self):  
#         if self.image.isNull():  
#             return  
#         martix = QMatrix()  
#         martix.scale(0.5,0.5)  
#         self.image=self.image.transformed(martix);  
#         self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  
#         self.resize(self.image.width(),self.image.height())   
	  
#     def slotCircumgyrate(self):  
#         if self.image.isNull():  
#             return  
#         martix = QMatrix()  
#         martix.rotate(90)  
#         self.image=self.image.transformed(martix);  
#         self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  
#         self.resize(self.image.width(),self.image.height())   
				  
# app=QApplication(sys.argv)  
# window=MainWindow()  
# window.show()  
# app.exec_()  

# start_frame = 1001.0
# # start_frame = 1261
# render_image = '/mnt/work/projects/tst/shot/k80/k80450/set/task/katana/k80450.set.set_dressing.v014/render/k80450.####.exr'
# render_image_new = render_image.replace('.####.','.'+str(start_frame).zfill(4)+'.')
# print render_image
# print render_image_new

# publish_id=ppj.send_job(PYTHON_SCRIPT_ROOT+'/applications/katana/Scripts/auto_set/publish_set.py',
#             args=' -p '+proj+' -v '+export_katana_files[0]+' -i '+out_mov+' -d '+descriptons+' -u '+set_args['user'],
#             proj=set_args['proj'].upper(),
#             job_name_prefix='[Xiaos Publish Set] -- '+os.path.basename(export_katana_files[0]),
#             step='SET',
#             depends=','.join([str(i) for i in job_id if i!=-1]),
#             msg='[ Xiaos Publish Set]: '+pplu.lca_path_platform(export_katana_files[0]),
#             user=set_args['user'],
#             pools='rv',
#             url=FARMTEMPLATE_ID
#             )

# out_mov = '/mnt/public/Share/zhaojiayi/tst/task/a10080.set.set_dressing.v288/a10080.mov'
# set_args['user'] = 'jiayi'
# descriptons = '/mnt/proj/trash/setdescriptons/a10080tst20161028165431.txt'
# export_katana_files[0] = '/mnt/public/Share/zhaojiayi/tst/publish'
# args=' -p '+proj+' -v '+export_katana_files[0]+' -i '+out_mov+' -d '+descriptons+' -u '+set_args['user']

# args['version'] = export_katana_files[0]
# args['image'] = out_mov
# args['proj'] = 'tst'
# args['status'] = 0
# args['descriptons'] = descriptons
# args['user'] = 'jiayi'
# publish_set(args['version'], args['image'],proj=args['proj'],status=int(args['status']),descriptons=args['descriptons'],user=args['user'])

# python /mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts/auto_set/publish_set.py ' -p '+'tst'+' -v '+'/mnt/proj/projects/tst/shot/a10/a10080/set/publish/a10080.set.set_dressing.v271/a10080.katana'+' -i '+'/mnt/proj/projects/tst/shot/a10/a10080/set/publish/a10080.set.set_dressing.v271/preview/a10080.set.set_dressing.v271.mov'+' -d '+'/mnt/proj/trash/setdescriptons/a10080tst20161028165431.txt'+' -u '+'jiayi'

# /mnt/utility/toolset/applications/katana/Scripts/auto_set/get_render_info.py 
# /mnt/work/projects/tst/shot/k80/k80450/set/task/katana/k80450.set.set_dressing.v023/render/k80450.1261.exr 
# /mnt/proj/projects/tst/shot/k80/k80450/set/publish/k80450.set.set_dressing.v022/k80450.katana 
# /mnt/work/projects/tst/shot/k80/k80450/set/task/katana/k80450.set.set_dressing.v023/k80450.katana 
# /mnt/proj/projects/tst/shot/k80/k80450/set/publish/k80450.set.set_dressing.v022/k80450.katana 
# /mnt/work/projects/tst/shot/k80/k80450/set/task/katana/k80450.set.set_dressing.v023/k80450.katana 
# maincall

# /mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts/auto_set/get_render_info.py /mnt/work/projects/tst/shot/k80/k80450/set/task/katana/k80450.set.set_dressing.v023/render/k80450.1261.exr /mnt/proj/projects/tst/shot/k80/k80450/set/publish/k80450.set.set_dressing.v022/k80450.katana /mnt/work/projects/tst/shot/k80/k80450/set/task/katana/k80450.set.set_dressing.v023/k80450.katana /mnt/proj/projects/tst/shot/k80/k80450/set/publish/k80450.set.set_dressing.v022/k80450.katana /mnt/work/projects/tst/shot/k80/k80450/set/task/katana/k80450.set.set_dressing.v023/k80450.katana maincall
# import os,string
# path = '/mnt/proj/trash/setdescriptons'
# all_files_list = os.listdir(path)
# required_files_list = []
# # for f in all_files_list:
# #     if f.find('cat20170822') and f.find('r30'):
# #         print f
# for f in all_files_list:
#     if 'cat20170822' in f :
#         required_files_list.append(f)

# required_files_list.sort()
# for f in required_files_list:
#     print f
# import time
# ISOTIMEFORMAT="%Y%m%d"
# print time.strftime( ISOTIMEFORMAT, time.localtime() )
# setdescriptonsPath = '/mnt/proj/trash/setdescriptons/r30055cat20170822142135.txt'
# f = open(setdescriptonsPath,'w')
# descriptons = 'this is tst'
# f.write(descriptons)
# f.flush()
# f.close()
# shotText ="['a10010', 'a10012', 'a10020', 'a10030', 'a10040', 'a10050', 'a10060', 'a10080']"
# print eval(shotText)
# from PySide.QtCore import *
# from PySide.QtGui import *

# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(180, 320)
#         self.label = QLabel(Form)
#         self.label.setGeometry(QRect(20, 10, 201, 41))
#         self.label.setObjectName("label")
#         self.pushButton = QPushButton(Form)
#         self.pushButton.setGeometry(QRect(70, 60, 93, 27))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton.setStyleSheet("color:black; background-color: rgb(131, 239, 255, 0);border-style:outset; border-width:0.1px; border-radius:100px; border-color:beige")
#         self.retranslateUi(Form)
#         QMetaObject.connectSlotsByName(Form)

#     def retranslateUi(self, Form):
#         Form.setWindowTitle(QApplication.translate("Form", "Form", None, QApplication.UnicodeUTF8))
#         self.label.setText(QApplication.translate("Form", "tstststststst", None, QApplication.UnicodeUTF8))
#         self.pushButton.setText(QApplication.translate("Form", "select", None, QApplication.UnicodeUTF8))


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     # QApplication.setStyleSheet("background-color: rgb(131, 239, 255, 0)")
#     Form = QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.setStyleSheet("background-image: url(/mnt/public/Share/zhaojiayi/photos/pokecoin.png);background-position:center")
#     Form.show()
#     sys.exit(app.exec_())

# import sys
# sys.path.insert(0,'/mnt/public/Share/zhaojiayi/gitrepo/lcatools/tools/srf/turntable_muster/')

# import srf_katana_submit
# reload(srf_katana_submit)

# srf_katana_submit.start()

# # # node=NodegraphAPI.GetNode('RenderSettings')

# # # producer = Nodes3DAPI.GetGeometryProducer(node, 0)

# # # t=producer.getFirstChild()

# # # t.getFullName()

# l_locations=[]
# node=NodegraphAPI.GetNode('RenderSettings')
# producer = Nodes3DAPI.GetGeometryProducer(node, 0)
# def sceneGraph_walk_cam(producer, l_locations):
#     if producer.getType()=='camera':
#         l_locations.append(producer.getFullName())
#     print producer.getType()
#     child = producer.getFirstChild()
#     while child:
#         sceneGraph_walk(child, l_locations)
#         child = child.getNextSibling()
# sceneGraph_walk(producer, l_locations)
# for l in l_locations:
#     if 'cam/' in l:
#         l_cam.append(l)

# import PySide.QtCore as QtCore
# import PySide.QtGui as QtGui

# class cBox( QtGui.QComboBox ):
#     def __init__( self, *args, **kwargs ):
#         super( cBox, self ).__init__( *args, **kwargs)


# class TestTable( QtGui.QWidget ):
#     def __init__( self, parent=None ):
#         QtGui.QWidget.__init__( self, parent )

#         self.setLayout( QtGui.QVBoxLayout() )
#         self.resize( 600, 300 )

#         self.myTable = QtGui.QTableWidget()
#         self.myTable.setColumnCount( 3 )
#         self.myTable.setRowCount( 5 )    

#         self.setTable()  

#         self.layout().addWidget(self.myTable)
#         self.myTable.cellChanged.connect(self.update) 

#     def setTable(self):

#         for i in range( 0, self.myTable.rowCount() ):
#             item = "row " + str(i)
#             self.myTable.setItem(i, 0, QtGui.QTableWidgetItem(item))

#             box = cBox()
#             nameList = ("sss","aaa","qqq")
#             box.addItems(nameList)

#             self.myTable.setCellWidget( i,1,box)   
#             box.currentIndexChanged.connect(self.tmp)

#     def tmp(self,i):
#         row = 1 # this I need change for actual row ,now just set to row 1 
#         item = "item " + str(i)
#         self.myTable.setItem(row, 2, QtGui.QTableWidgetItem(item)) #set item to 3 column by selected item form combo box


# if __name__ == "__main__":
#     tableView = TestTable()
#     tableView.show()



# if ($selMesh != ""){
#                 $aSelVerts = abCheckSym($selMesh, $axisSel, $tol, false, $usePiv);
#                 if (size($aSelVerts) > 0){
#                     selectMode -component;
#                     select $aSelVerts;
#                     print (size($aSelVerts)+" asymmetric vert(s)");
#                 }else{
#                     select $selMesh;
#                     print ($selMesh+" is symmetrical");
#                 }
#             }

# import maya.mel as mel 
# import sys

# mel.eval('source "/mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/maya/scripts/abSymMesh.mel"')
# mel.eval('string $baseObj = "pCube1"')
# mel.eval('abSymCtl(\"favBn\")')

# myPythonVariable = maya.mel.eval ('global $myMELvariable; $temp=$myMELvariable;' )
# output = mel.eval('global $output')

# import maya.mel as mel 
# import sys

# mel.eval('source "/mnt/public/Share/zhaojiayi/gitrepo/lcatools/tools/mod/abSymMesh_new.mel"')
# output = mel.eval('abSymCtl(\"favBn\");')
# if output>1:
#     print 'it is not symmetrical'
# else:
#     print 'it is symmetrical'



# # l_render = 'what'
# # # l_render = {
# list_1 = [1,2,4]
# list_2 = [1,2,4]
# list_3 = [1,2,4]
# # # l_render['a'] = list_1
# # # l_render['b'] = list_2
# # # l_render['c'] = list_3
# # print l_render

# tst_list = []
# for i in range(3):
#     tst_list[i] = 
#     tst_list[i].append(1)

# print tst_list

# cam = '/root/hello'
# print cam.split('/')[-1]
# list_tst = [0,1,2,4]
# key_num = 3
# what_num = 2
# for i in range(key_num):
#     print i
#     for j in list_tst:
#         if j/what_num == i:
#             print 'when i is ' + str(i) + ' j is ' + str(j)

# file:///output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.v013/indoor_day_portico/chair_b.defaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefault.mov
# file:///output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.v013/indoor_day_portico/chair_b.defaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefaultdefault.mov
# import sys
# sys.path.insert(0,'/mnt/public/Share/zhaojiayi/gitrepo/lcatools/tools/srf/turntable_muster/')

# import srf_katana_submit
# reload(srf_katana_submit)
# srf_katana_submit.start()
# # /mnt/public/Share/zhaojiayi/gitrepo/lcatools/tools/srf/project_loader/set_output_path.py
# # /mnt/public/Share/zhaojiayi/gitrepo/lcatools/tools/srf/project_loader/set_output_path.py
# # '/output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.v013/'+
# # str(getParam("SRF_PBR_RIG2.user.Current_Rig")).lower() 
# # + (('/'+str(getParam("RenderOutputDefine_Stack2.user.custom_path"))) if getParam("RenderOutputDefine_Stack2.user.custom_path") else '')

# # '/output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.v013/'+str(getParam("SRF_PBR_RIG1.user.Current_Rig")).lower() +"/default"


# '/output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.v013/'+
# str(getParam("SRF_PBR_RIG2.user.Current_Rig")).lower() 
# + (('/'+str(getParam("RenderOutputDefine_Stack2.user.custom_path"))) if getParam("RenderOutputDefine_Stack2.user.custom_path") else '') 

# import NodegraphAPI as ngapi
# stack_nodes=ngapi.GetAllNodesByType('GroupStack')
# for n in stack_nodes:
#     if n.getName().startswith('RenderOutputDefine_Stack'):
#         number = n.getName()[-1]
#         param1 = 'SRF_PBR_RIG' + number + '.user.Current_Rig'
#         param2 = 'RenderOutputDefine_Stack' + number + '.user.custom_path'
#         new_exp ="'/output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.v013/'+str(getParam( '" + param1 + \
#                  "')).lower()+(('/'+str(getParam('" + param2 + "'))) if getParam('" + param2 + "') else '')" + \
#                  " + '/' + (str(getParam(" "'RenderSettings.args.renderSettings.cameraName.value'" "))).split('/')[-1] " 
#         n.getParameter('user.path').setExpression(new_exp)
#         # print param1
#         # print str(getParam(param1)).lower()




# new_exp="'"+asset_path+"'+"+'+'.join(exp_sp[1:4]) + " + '/' + (str(getParam(" "'RenderSettings.args.renderSettings.cameraName.value'" "))).split('/')[-1] " + (('+"/'+custom_folder+'"') if custom_folder else '')




# new_exp ="'/output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.v013/'+str(getParam( '" + param1 + \
#          "')).lower()+(('/'+str(getParam('" + param2 + "'))) if getParam('" + param2 + "') else '')" + \
#          " + '/' + (str(getParam(" "'RenderSettings.args.renderSettings.cameraName.value'" "))).split('/')[-1] "


# new_exp="'"+asset_path+"'+"+'+'.join(exp_sp[1:4]) + " + '/' + (str(getParam(" "'RenderSettings.args.renderSettings.cameraName.value'" "))).split('/')[-1] "















# asset_path = '/output/projects/tst/asset/prp/chair_b/srf/output/render'
# exp_sp = ['a','b','c']
# print exp_sp[1:3]
# custom_folder = 'default'
# new_exp="'"+asset_path+"'+"+'+'.join(exp_sp[1:])+(('+"/'+custom_folder+'"') if custom_folder else '')

# '/output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.v013/'+
# str(getParam("SRF_PBR_RIG2.user.Current_Rig")).lower() 
# + (('/'+str(getParam("RenderOutputDefine_Stack2.user.custom_path"))) if getParam("RenderOutputDefine_Stack2.user.custom_path") else '') 

# # '/output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.chair_b/'+str(getParam("SRF_PBR_RIG3.user.Current_Rig")).lower()+ (('/'+str(getParam("RenderOutputDefine_Stack3.user.custom_path"))) if getParam("RenderOutputDefine_Stack3.user.custom_path") else '')

# # /output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.chair_b/indoor_day_portico/camera1504606783default/beauty.####.exr
# # /output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.chair_b/indoor_day_portico/chair_b.camera1504606783default.mov

# # /output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.chair_b/indoor_day_portico/camera1504606783/default/beauty.####.exr
# print new_exp
# '/output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.chair_b/'+\
# str(getParam("SRF_PBR_RIG3.user.Current_Rig")).lower()+ \
# (('/'+str(getParam("RenderOutputDefine_Stack3.user.custom_path"))) if getParam("RenderOutputDefine_Stack3.user.custom_path") else '')+
# ('/'+(str(getParam("RenderSettings.args.renderSettings.cameraName.value"))).split('/')[-1])
# ('/'+(str(getParam("RenderSettings.args.renderSettings.cameraName.value"))).split('/')[-1])
# new_exp="'"+asset_path+"'+"+exp_sp[1]+('+"/'+custom_folder+'"') 
# new_exp= "'" + asset_path + "'+" + '+'.join(exp_sp[1:3]) \
# + " + '/' + (str(getParam("RenderSettings.args.renderSettings.cameraName.value"))).split('/')[-1] " 

# 'getParam("' + spec_center_node.getName() + '.parameters.gain.value")'
# exp_sp = NodegraphAPI.GetNode('RenderOutputDefine_Stack1').getParameter('user.path').getExpression()

# new_exp=  exp_sp \
# + " + '/' + (str(getParam(" "'RenderSettings.args.renderSettings.cameraName.value'" "))).split('/')[-1] " 

# NodegraphAPI.GetNode('RenderOutputDefine_Stack1').getParameter('user.path').setExpression(new_exp)

# '/output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.v013/' + \
# str(getParam("SRF_PBR_RIG1.user.Current_Rig")).lower()+ (('/'+str(getParam("RenderOutputDefine_Stack2.user.custom_path"))) \
#     if getParam("RenderOutputDefine_Stack2.user.custom_path") else '') + '/' + \
# (str(getParam('RenderSettings.args.renderSettings.cameraName.value'))).split('/')[-1] 


# '/output/projects/tst/asset/prp/chair_b/srf/output/render/chair_b.srf.render.katana/'+ \
# str(getParam("SRF_PBR_RIG2.user.Current_Rig")).lower()+\
# (('/'+'/'+(str(getParam('RenderSettings.args.renderSettings.cameraName.value'))).split('/')[-1] 

# exp_sp = NodegraphAPI.GetNode('RenderOutputDefine_Stack1').getParameter('user.path').getExpression()
# new_exp=  exp_sp \
# + " + '/' + (str(getParam(" "'RenderSettings.args.renderSettings.cameraName.value'" "))).split('/')[-1] "
# NodegraphAPI.GetNode('RenderOutputDefine_Stack1').getParameter('user.path').setExpression(new_exp)

# import re 
# s = "adfad asdfasdf asdfas asdfawef asd adsfas "
# reObj1 = re.compile()
# import sys
# sys.path.append('/mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts')
# import macro.lgtShotMaker as mlsm


# import sys
# sys.path.insert(0,'/mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts/macro')
# import lgtShotMaker as mlsm
# import NodegraphAPI as ngapi
# proj = 'tst'
# shot = 'a10080'
# out_set_path = '/mnt/proj/projects/tst/shot/a10/a10080/set/publish/a10080.set.set_dressing.v276'
# st_mk = ngapi.CreateNode('LgtShotMaker_Lc')
# st_mk.getParameter('user.proj').setValue(proj,0)
# st_mk.getParameter('user.shot').setValue(shot,0)
# st_mk.getParameter('user.exportTo').setValue(out_file,0)
# reload(mlsm)
# mlsm.build_set(st_mk)

# def valid_color_id(asset):
#     if isinstance(asset['sg_color_id'], (str, unicode)):
#         tokens = asset['sg_color_id'].split(' ')
#         if len(tokens) == 3 and tokens[0].isdigit() and tokens[1].isdigit() and tokens[2].isdigit():
#             return True
#     return False

# asset = {}
# asset['sg_color_id'] = '0 0 0'

# print valid_color_id(asset)

# from production import shotgun_connection
# sg = shotgun_connection.Connection('get_shot_info').get_sg()


# proj_name = 'cat'
# shot = 'g50010'

# # task = sg.find_one('Tasks', [['project', 'is', proj],['shot','is',shot]], ['content', 'code', 'sg_color_id'])

# asset_name = 'camera_inhand'
# proj = sg.find_one('Project', [['name', 'is', proj_name]], [])
# # print proj
# color_id = sg.find_one('Asset', [['project', 'is', proj],['code','is',asset_name]], ['sg_asset_type', 'code', 'sg_color_id'])
# color_id = sg.find_one('Asset', [['project', 'is', proj],['code','is',asset_name]], ['sg_color_id'])

# task = sg.find_one('Shot', [['project', 'is', proj],['code','is',shot],['step','is','plt']], ['content'])
# shot = sg.find_one('Shot', [['project', 'is', proj],['code','is',shot]])
# print task 
# print color_id
# # print shot
# task = sg.find_one('Task',[['project', 'is', proj],['entity.Shot.code','is',shot],['content','is','stereo']],['id','content','step'])
# task = sg.find('Task',[['project', 'name_is', 'CAT'],['entity.Shot.code','is',shot],['step','name_is','plt']],['id','content','sg_status_list'])
# print task
# print len(task)

# def sgTask(self, fields=None):
#     """
#     corresponding shotgun task.
#     """
#     if self.args['entity_type'] == self.kEntityTypeShot:
#         filters = [['content', 'is', self.name()],
#                   ['entity.Shot.code', 'is', self.entity_name],
#                   ['project', 'name_is', self.proj]]

#     else:
#         filters = [['code', 'is', self.entity_name],
#                   ['sg_asset_type', 'is', 'efx'],
#                   ['project', 'name_is', self.proj]]
#         asset = SG.find_one('Asset', filters)
#         if not asset:
#             return None

#         filters = [['content', 'is','efx'],
#                   ['entity.Asset.code', 'is', self.entity_name],
#                   ['project', 'name_is', self.proj]]
#     if fields == None:
#         fields = ['id', 'content']

#     return SG.find_one('Task', filters, fields)



# stack_nodes=ngapi.GetAllNodesByType('GroupStack')
# for n in stack_nodes:
#     if n.getName().startswith('k50460'):
#         print n.getName()


# def get_plantshot(self):
#     from production.shotgun_connection import Connection
#     self.shot_list = []
#     sg = Connection('get_project_info').get_sg()
#     selected_rows = self.__selected_rows()
#     project_name = ngapi.GetNode('CamShotsGroup_Lc').getParameter('user.proj').getValue(0)
#     for r in selected_rows:
#         shot = str(self.ui.tableWidget.item(r,0).text())
#         tasks = sg.find('Task',[['project', 'name_is', project_name],['entity.Shot.code','is',shot],['step','name_is','plt']],['content','sg_status_list'])
#         for t in tasks:
#             if t['content'] != 'plant_edit':
#                 if t['sg_status_list'] == 'da':
#                     self.shot_list.append(shot)
#     set_plant_task()

# def set_plant_task(self):
#     stack_nodes=ngapi.GetAllNodesByType('GroupStack')
#     for n in stack_nodes:
#         for shot in self.shot_list:
#             if n.getName().startswith(shot):
#                 print n.getName()

# def set_node_position(node, parent_node):
#     old_pos=NodegraphAPI.GetNodePosition(parent_node)
#     NodegraphAPI.SetNodePosition(node,(old_pos[0],old_pos[1]-50))


# shot_list = ['k50460','k50480']
# asset_name = NodegraphAPI.GetNode('AssetXmlIn_Lc').getParameter('user.assetName').getValue(0)
# prune_path = '/root/world/geo/assets/asb/' + str(asset_name) +'/master/plant'
# stack_nodes=NodegraphAPI.GetAllNodesByType('GroupStack')
# Var_nodes=NodegraphAPI.GetAllNodesByType('VariableSet')
# shotrender_nodes = NodegraphAPI.GetAllNodesByType('Group')
# for s in shotrender_nodes:
#     if s.getName().startswith('ShotRenderGroup'):
#         shotrender_node = s

# for n in stack_nodes:
#     for shot in shot_list:
#         if n.getName().startswith(shot):
#             plantcache_node = NodegraphAPI.CreateNode('PlantCacheIn_Lc',shotrender_node)
#             plantcache_node.getParameter('user.asset_shot').setValue(shot,0)
#             NodegraphAPI.UserParameters.ExecuteButton(plantcache_node, 'getplatn')
#             merge_node = NodegraphAPI.CreateNode('Merge',shotrender_node)
#             prune_node = NodegraphAPI.CreateNode('Prune',shotrender_node)
#             prune_node.getParameter('cel').setValue(prune_path,0)
#             n.getOutputPortByIndex(0).connect(prune_node.getInputPortByIndex(0))
			
#             inputPort0 = merge_node.addInputPort('i0')
#             inputPort1 = merge_node.addInputPort('i1')
#             plantcache_node.getOutputPortByIndex(0).connect(inputPort0)
			
#             prune_node.getOutputPortByIndex(0).connect(inputPort1)
#             for v in Var_nodes:
#                 if v.getName().startswith(shot):
#                     merge_node.getOutputPortByIndex(0).connect(v.getInputPortByIndex(0))
#                     set_node_position(prune_node,n)
#                     set_node_position(merge_node,prune_node)
#                     set_node_position(v,merge_node)
#                     cku.node_layout_katana([prune_node,plantcache_node],True)

# plantcache_node = NodegraphAPI.CreateNode('PlantCacheIn_Lc')
# plantcache_node = NodegraphAPI.CreateNode('PlantCacheIn_Lc')
# merge_node = NodegraphAPI.CreateNode('Merge',NodegraphAPI.GetNode('rootNode'))
# prune_node = NodegraphAPI.CreateNode('Prune',NodegraphAPI.GetNode('rootNode'))

# # Group_node = NodegraphAPI.CreateNode('GroupStack',NodegraphAPI.GetNode('rootNode'))
# # varible_node = NodegraphAPI.CreateNode('VariableSet',NodegraphAPI.GetNode('rootNode'))
# plantcache_node = NodegraphAPI.CreateNode('PlantCacheIn_Lc')
# merge = NodegraphAPI.CreateNode('Merge',NodegraphAPI.GetNode('rootNode'))
# prune_node = NodegraphAPI.CreateNode('Prune',NodegraphAPI.GetNode('rootNode'))
# Group_node.getOutputPortByIndex(0).connect(prune_node.getInputPortByIndex(0))
# inputPort0 = merge_node.addInputPort('i0')
# inputPort1 = merge_node.addInputPort('i1')
# plantcache_node.getOutputPortByIndex(0).connect(inputPort0)
# prune_node.getOutputPortByIndex(0).connect(inputPort1)
# merge_node.getOutputPortByIndex(0).connect(varible_node.getInputPortByIndex(0))
# import os
# orgin_path='/mnt/proj/trash/srf_uvs/train_data/orgin/'
# i=0
# all_uv_file_list = [u'apartment_corridor_b.wall_b_tilesShape.2007.npz', u'apartment_corridor_b.wall_a_tilesShape4Shape.81.npz', u'apartment_corridor_b.wall_b_waistlineShape.4906.npz', u'apartment_corridor_b.wall_dShape.1381.npz', u'apartment_corridor_b.wall_b_waistline1Shape.660.npz', u'apartment_corridor_b.wall_b_baseboard1Shape.154.npz', u'apartment_corridor_b.ground_tile_aShape.44826.npz', u'apartment_corridor_b.ground_tile_bShape.18511.npz', u'apartment_corridor_b.ground_plane_PLYShape.484.npz', u'apartment_corridor_b.ceiling_bShape35Shape.405.npz', u'apartment_corridor_b.wall_a_waistlineShape.5786.npz', u'apartment_corridor_b.wall_b_baseboardShape.1430.npz', u'apartment_corridor_b.wall_b_tiles1Shape.180.npz', u'apartment_corridor_b.wall_b_PLYShape.124.npz', u'apartment_corridor_b.wall_a_tilesShape.2124.npz', u'apartment_corridor_b.slidingwindowhook_bShape.1597.npz', u'apartment_corridor_b.slidingwindowglass_bShape.234.npz', u'apartment_corridor_b.ceiling_aShape.2957.npz', u'apartment_corridor_b.wall_a_baseboardShape.1166.npz', u'apartment_corridor_b.wall_a_PLYShape.88.npz', u'apartment_corridor_b.slidingwindowknob_aShape.907.npz', u'apartment_corridor_b.wall_cShape.413.npz', u'apartment_corridor_b.slidingwindowscrew_aShape.769.npz', u'apartment_corridor_b.trackShape.4836.npz', u'apartment_corridor_b.wall_c_baseboardShape.209.npz', u'apartment_corridor_b.slidingwindowbase_aShape.806.npz', u'apartment_corridor_b.ceiling_bShape29Shape.405.npz', u'apartment_corridor_b.slidingwindowglass_aShape.234.npz', u'apartment_corridor_b.wall_d1Shape.162.npz', u'apartment_corridor_b.wall_c_waistlineShape.946.npz', u'apartment_corridor_b.staircase_wall_PLYShape.230.npz', u'apartment_corridor_b.ceiling_bShape34Shape.405.npz']
# def check_cross(uvs):

#     uv_file = os.path.join(orgin_path, uvs)
#     print uv_file
#     all_uvs_data = np.load(uv_file)

	#print all_uvs_data.keys()
	# UV_list = all_uvs_data['UV_list']
	# UVIndices=all_uvs_data['UVIndices']

	# edge_list=all_uvs_data['edge_list']
	# uv_edge_list=[]
	# for i in range(len(edge_list)):
	#     point_a_index=edge_list[i][0]
	#     point_b_index=edge_list[i][1]

	#     point_a_Indices=UVIndices[point_a_index]
	#     point_b_Indices=UVIndices[point_b_index]
	#     a_uv=None
	#     b_uv=None
	#     if uv_not_cut(point_a_Indices):
	#         a_uv=UV_list[point_a_index]
	#     if uv_not_cut(point_b_Indices):

	#         b_uv = UV_list[point_b_index]

	#     if  a_uv is not None and b_uv is not None:

	#         a_uv_point=[a_uv[0][0],a_uv[1][0]]
	#         b_uv_point=[b_uv[0][0],b_uv[1][0]]

	#         uv_edge_list.append([a_uv_point,b_uv_point])

	# uv_edge_len=len(uv_edge_list)
	# for i  in range(uv_edge_len-1):
	#     for j in range(i+1 ,uv_edge_len):
	#         if cross_2Seg.seg_intersect(uv_edge_list[i][0],uv_edge_list[i][1],uv_edge_list[j][0],uv_edge_list[j][1]):

	#             return True

	# return False

# for uvs in all_uv_file_list[i:]:
#     # print i
#     i+=1
#     print uvs
#     # print int(uvs.split('.')[-2])
#     try:
#         if 500<int(uvs.split('.')[-2])<1000:
#             print 'Yes'
#             print uvs
#             if check_cross(uvs) :
#                 uvs_snapshot=os.path.join(snapshot_path,uvs.replace('.npz','.jpg'))
#                 new_uvs_snapshot=os.path.join(check_snapshot_path,uvs.replace('.npz','.jpg'))

#                 shutil.copy(uvs_snapshot,new_uvs_snapshot)
#                 print 'is error ', uvs

#             else:
#                 print 'is ok'
#         # else:
#         #     print 'is point to many'
#     except:
#         print 'check except'


# import numpy as np
# uv_file = '/mnt/proj/trash/srf_uvs/train_data/orgin/apartment_corridor_b.wall_b_waistline1Shape.660.npz'
# all_uvs_data = np.load(uv_file)
# print all_uvs_data
# # print all_uvs_data['connect_edge_list']
# # print all_uvs_data['connect_vtx_list']
# print all_uvs_data['edge_list']
# # print all_uvs_data['point_list']
# print all_uvs_data['UV_list']
# print all_uvs_data['UVIndices']
# uvs = 'apartment_corridor_b.wall_b_waistline1Shape.660.npz'
# check_cross(uvs)
# import sys
# sys.path.append('/mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts')
# import common.lcProdProj as lcp
# reload(lcp)
# localP = lcp.lcProdProj()
# localP.setProj('pws')
# print localP.lcGetLayXml('z88725')
# print localP.get_shot_version_folder('z88725','ani')

# aniasset = localP.getAniAsset('z88725','xiaoqing_girl_snake')
# empty = localP.getAniAsset('z88726','xiaoqing_girl_snake')
# print aniasset
# print empty
# self.ppinfo.setProj('pws')
# self.ppinfo.getAniAsset('z88725','xiaoqing_girl_snake')
# camPath = localP.lcGetLayCam('z88725')
# version = localP.getPathVersion(camPath)
# print camPath
# print version
# localP.get_shot_version_folder('z88725','ani')
# lay_task = '/mnt/proj/projects/pws/shot/z88/z88725/ani/publish/z88725.ani.animation.v002'
# print lay_task.get('ani',lay_task.get('layout'))


# sys.path.append('/mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts/macro/camAlembicIn.py')
# import camAlembicIn as cai
# reload(cai)
# cai.GetLayCam('pws')
# import os
# anipath = '/mnt/proj/projects/pws/shot/z88/z88725/ani/publish/z88725.ani.animation.v002/cache/xiaoqing_girl_snake/geo/xiaoqing_girl_snake.xml'
# # ani_re = '/'.join(anipath.split('/')[:-1])
# path = os.path.join('/'.join(anipath.split('/')[:-1]) , 'geo_hi.abc')
# ani_list = anipath.split('/')[:-1]
# print ani_list
# ani_re = '/'.join(ani_list)
# print ani_re
# path = os.path.join(ani_re , 'geo_hi.abc')
# print path
# string_1 = 'asdfg'
# string_2 = 'qwer'
# new_string = os.path.join(string_1 , string_2)
# print new_string
# import sys
# sys.path.insert(0,'/mnt/public/Share/zhaojiayi/tst/')

# import alsurf_to_arnold5
# reload(alsurf_to_arnold5)

# PORT_DICT = {
#     'diffuseStrength': 'base',
#     'diffuseColor': 'base_color',
#     'diffuseRoughness': 'diffuse_roughness',
#     'emissionStrength': 'emission',
#     'emissionColor': 'emission_color',
#     'specular1Strength': 'specular',
#     'specular1Color': 'specular_color',
#     'specular1Roughness': 'specular_roughness',
#     'specular1Anisotropy': 'specular_anisotropy',
#     'specular1Rotation': 'specular_rotation',
#     'transmissionStrength': 'transmission',
#     'transmissionColor': 'transmission_color',
#     'sssMix': 'subsurface',
#     'sssDensityScale': 'subsurface_scale',
#     'opacity': 'opacity'}

# all_arnold_shading_nodes = NodegraphAPI.GetAllNodesByType('ArnoldShadingNode')
# all_alsurface = []
# for al in all_arnold_shading_nodes:
#     if al.getParameter('nodeType').getValue(0) == 'alSurface':
#         all_alsurface.append(al)
#         print al.getName()
# for all in all_alsurface:
#     mtl_grp = all.getParent()
#     alsurf_name = all.getName()
#     new_name = alsurf_name
#     if 'alSurface' in alsurf_name:
#         new_name = alsurf_name.replace('alSurface','_std_srf')
#     else:
#         new_name += '_std_srf'
#     print new_name
#     new_arnold = NodegraphAPI.CreateNode('ArnoldShadingNode', mtl_grp)
#     new_arnold.getParameter('nodeType').setValue('standard_surface', 0)
#     new_arnold.getParameter('name').setValue(new_name, 0)
#     new_arnold.checkDynamicParameters()
#     new_arnold.setName(new_name)
#     new_arnold = NodegraphAPI.GetNode(new_name)
	
#     alsurf_node = all
#     std_srf_node = new_arnold
#     switch_out_ports(alsurf_node,std_srf_node)
	# curr_dict = PORT_DICT
	# all_ports_in = alsurf_node.getInputPorts()
	# print alsurf_name
	# for port_in in all_ports_in:
	#     port_conn = port_in.getConnectedPorts()
	#     if port_conn:
	#         port_n = port_in.getName()
	#         print 'the port name is '
	#         print port_n
	#         if port_n in curr_dict:
	#             print 'alsurf inport name: ', port_n
	#             NodegraphAPI.SetNodeEdited(std_srf_node, 1, 1)
	#             new_port_in = std_srf_node.getInputPort(curr_dict[port_n])
	#             print 'arnold 5 new import name', new_port_in
	#             for each_conn in port_conn:
	#                 print each_conn.getName()
	#                 each_conn.connect(new_port_in)


# def switch_out_ports(alsurf_node, std_srf_node):
#     alsurf_out_port = alsurf_node.getOutputPort('out')
#     print 'the output port name is: '
#     print alsurf_out_port.getName()
#     connected_port = alsurf_out_port.getConnectedPorts()
#     if not connected_port:
#         print 'no port is connected to alsurf node, skipping ...'
#         return
#     connected_port = connected_port[0]
#     next_node = connected_port.getNode()
#     print 'the next node name is:'
#     print next_node.getName()
#     if next_node.getType() == 'ArnoldShadingNode':
#         next_node_type = next_node.getParameter('nodeType').getValue(0)
#         print 'the next node type is:'
#         print next_node_type
#         if not next_node_type:
#             print 'cannot find nodeType, skipping ...'
#             return
#         if next_node_type in ['bump2d', 'bump3d', 'mayaBump2D']:
#             print 'detecting bump connection on ', alsurf_node.getName()
#             #switch connected_port one node down
#             bump_out = next_node.getOutputPort('out')
#             connected_port = bump_out.getConnectedPorts()
#             if not connected_port:
#                 print 'no port is connected to bump node, skipping ...'
#                 return
#             connected_port = connected_port[0]
#             std_srf_bump_in = std_srf_node.getInputPort('normal')
#             bump_out.connect(std_srf_bump_in)
#             print 'bump1 '
#             std_coat_bump = std_srf_node.getInputPort('coat_normal')
#             bump_out.connect(std_coat_bump)
#             print 'bump2'
#     conn_rst = std_srf_node.getOutputPort('out').connect(connected_port)
#     if not conn_rst:
#         print 'unsuccessful connection, skipping ...'
#         return
#     return True


# from production.shotgun_connection import Connection
# sg = Connection('get_project_info').get_sg()
# project_name = 'cat'
# shot = 'r50360'
# # tasks = sg.find('Task',[['project', 'name_is', project_name],['entity.Shot.code','is',shot],['step','name_is','plt']],['content','sg_last_version.sg_version_type'])
# # tasks = sg.find('Task',[['project', 'name_is', project_name],['entity.Shot.code','is',shot],['step','name_is','plt']],['content','sg_last_version',])
# # for t in tasks:
# #     if t['content'] != 'plant_edit':
# #         print t['sg_last_version']['name']
# #         version = sg.find('Version',[['project', 'name_is', project_name],['entity.Shot.code','is',shot],['code','contain','plt']],['sg_version_type'])
# #         print version
#         # if version[0]['sg_version_type'] == 'Downstream':
#         #     print 'Yes'
#         # version = sg.find('Version',[['project', 'name_is', project_name],['entity.Shot.code','is',shot]],['code','sg_version_type'])
# # for t in tasks:
# #     if 'plt' in t['code'] and 'plant_edit' not in t['code']:
# #         print t

# version = sg.find('Version',[['project', 'name_is', project_name],['entity.Shot.code','is',shot],['code','contains','plt']],['sg_version_type'])
# versionEntity = sg.find('Version',[['project','name_is',project_name],['entity.Shot.code','is',shot],['code','contains','_plant'],['sg_version_type','is','Downstream']],['code','sg_version_type'])
# if versionEntity:
#     print 'Yes'
# print versionEntity

# import sys
# sys.path.append('/mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts/macro')
# node = NodegraphAPI.GetNode('ShotRenderGroup')
# import cam_shots_group as mcsg
# reload(mcsg)
# mcsg.shot_editor(node)
# def switch_out_ports(alsurf_node, std_srf_node):
#     alsurf_out_port = alsurf_node.getOutputPort('out')
#     connected_port = alsurf_out_port.getConnectedPorts()
#     if not connected_port:
#         print 'no port is connected to alsurf node, skipping ...'
#         return
#     connected_port = connected_port[0]
#     next_node = connected_port.getNode()
#     if next_node.getType() == 'ArnoldShadingNode':
#         next_node_type = next_node.getParameter('nodeType').getValue(0)
#         if not next_node_type:
#             print 'cannot find nodeType, skipping ...'
#             return
#         if next_node_type in ['bump2d', 'bump3d', 'mayaBump2D']:
#             print 'detecting bump connection on ', alsurf_node.getName()
#             bump_out = next_node.getOutputPort('out')
#             connected_port = bump_out.getConnectedPorts()
#             if not connected_port:
#                 print 'no port is connected to bump node, skipping ...'
#                 return
#             connected_port = connected_port[0]
#             std_srf_bump_in = std_srf_node.getInputPort('normal')
#             bump_out.connect(std_srf_bump_in)
#             std_coat_bump = std_srf_node.getInputPort('coat_normal')
#             bump_out.connect(std_coat_bump)
#     conn_rst = std_srf_node.getOutputPort('out').connect(connected_port)
#     if not conn_rst:
#         print 'unsuccessful connection, skipping ...'
#         return

# def disconnect_previous_connection(alsurf_node):
#     for ip in alsurf_node.getInputPorts():
#         ip_conns = ip.getConnectedPorts()
#         if ip_conns:
#             for each_ip_conn in ip_conns:
#                 ip.disconnect(each_ip_conn)
#     for op in alsurf_node.getOutputPorts():
#         op_conns = op.getConnectedPorts()
#         if op_conns:
#             for each_op_conn in op_conns:
#                 op.disconnect(each_op_conn)
# for alsurf_node in all_alsurface:
#     disconnect_previous_connection(alsurf_node)

# def get_self_defined_attrs(curr_node, curr_dict):
#     self_defined_attrs = {}
#     for p in curr_node.getParameter('parameters').getChildren():
#         p_name = p.getName()
#         if curr_node.getParameterValue('parameters.'+p_name+'.enable',0) and p_name in curr_dict:
#             print p_name 
#             value = curr_node.getParameter('parameters.'+p_name+'.value')
#             sub_value = value.getChildren()
#             if not sub_value:
#                 rst = value.getValue(0)
#             else:
#                 values = []
#                 for val in sub_value:
#                     values.append(val.getValue(0))
#                 rst = tuple(values)
#             print rst


# PORT_DICT = {
#     'diffuseStrength': 'base',
#     'diffuseColor': 'base_color',
#     'diffuseRoughness': 'diffuse_roughness',
#     'emissionStrength': 'emission',
#     'emissionColor': 'emission_color',
#     'specular1Strength': 'specular',
#     'specular1Color': 'specular_color',
#     'specular1Roughness': 'specular_roughness',
#     'specular1Anisotropy': 'specular_anisotropy',
#     'specular1Rotation': 'specular_rotation',
#     'transmissionStrength': 'transmission',
#     'transmissionColor': 'transmission_color',
#     'sssMix': 'subsurface',
#     'sssDensityScale': 'subsurface_scale',
#     'opacity': 'opacity'}


# all_arnold_shading_nodes = NodegraphAPI.GetAllNodesByType('ArnoldShadingNode')
# all_alsurface = []
# all_stdsurface = []
# replace_node = {}
# import sys, os
# for ar_sn in all_arnold_shading_nodes:
#     if ar_sn.getParameter('nodeType').getValue(0) == 'alSurface':
#         all_alsurface.append(ar_sn)
# for alsurf_node in all_alsurface:
#     mtl_grp = alsurf_node.getParent()
#     alsurf_name = alsurf_node.getName()
#     new_name = alsurf_name
#     if 'alSurface' in alsurf_name:
#         new_name = alsurf_name.replace('alSurface','_std_srf')
#     else:
#         new_name += '_std_srf'
#     new_arnold = NodegraphAPI.CreateNode('ArnoldShadingNode', mtl_grp)
#     new_arnold.getParameter('nodeType').setValue('standard_surface', 0)
#     new_arnold.getParameter('name').setValue(new_name, 0)
#     new_arnold.checkDynamicParameters()
#     new_arnold.setName(new_name)
#     new_arnold = NodegraphAPI.GetNode(new_name)
#     alName = alsurf_node.getName()
#     stdName = new_name
#     replace_node[alName] = stdName
#     print new_name 
#     # all_stdsurface.append(new_arnold)
# curr_dict = PORT_DICT
# # alsurf_node = new_arnold
# for alsurf_node in all_alsurface:
#     al_name = alsurf_node.getName()
#     stdName = replace_node[al_name]
#     std_srf_node = NodegraphAPI.GetNode(stdName)
#     all_ports_in = alsurf_node.getInputPorts()
#     for port_in in all_ports_in:
#         port_conn = port_in.getConnectedPorts()
#         if port_conn:
#             port_n = port_in.getName()
#             if port_n in curr_dict:
#                 print 'alsurf inport name: ', port_n
#                 NodegraphAPI.SetNodeEdited(std_srf_node, 1, 1)
#                 new_port_in = std_srf_node.getInputPort(curr_dict[port_n])
#                 print 'arnold 5 new import name', new_port_in
#                 for each_conn in port_conn:
#                     print each_conn.getName()
#                     each_conn.connect(new_port_in)

# for alsurf_node in all_alsurface:

#     al_name = alsurf_node.getName()
#     stdName = replace_node[al_name]
#     std_srf_node = NodegraphAPI.GetNode(stdName)
#     switch_out_ports(alsurf_node, std_srf_node)
#     self_defined_attrs = get_self_defined_attrs(alsurf_node, curr_dict)

# import sys
# sys.path.insert('/mnt/public/Share/zhaojiayi/tst')
# import untitled as utt
# reload(utt)
# utt.main()

# import macro.lgtShotMaker as mlsm
# import traceback
# try:
#    win=mlsm.updatePlant(node)
# except:
#    raise Exception(traceback.format_exc())


# nodes = NodegraphAPI.GetAllNodesByType('GroupMerge')


# list_1 = ['b','bsgdf','a']
# if 'd' not in list_1:
#     print 'Yes'
# else:
#     print 'No'
# list_1.sort()
# print list_1
# import sys,os
# # path = '/mnt/work/projects/itt/asset'
# # path_1 = '/mnt/work/projects/cat/asset'
# # print os.path.isdir(path)
# # print os.path.isdir(path_1)
#         # proj_path = '/mnt/work/projects'

#         # l_proje = os.listdir(proj_path)
#         # l_proje.sort()
#         # for proj in l_proj:
#         #     assett_path = '/mnt/work/projects/%s/asset'%proj
#         #     if not os.path.isdir(assett_path):
#         #         print proj
#         #         l_proj.remove(proj)
# list_tst = ['cat', 'deepstereo', 'gby', 'god', 'itt', 'lcl', 'lib', 'pws', 'shot', 'tap', 'tec', 'tnk', 'tpr', 'tst', 'vrc']
# print list_tst
# for l in list_tst:
#     print l
# print '.........................'
# for proj in list_tst:
#     print proj
#     assett_path = '/mnt/work/projects/%s/asset'% proj
#     if not os.path.isdir(assett_path):
#         # print assett_path
#         list_tst.remove(proj)
#     # else:
#     #     print ''
# print list_tst
# for l in list_tst:
#     print l

#!/usr/bin/python
# -*- coding: utf-8 -*-

# import sys
# from PyQt4 import QtGui


# def main():

#     app = QtGui.QApplication(sys.argv)

#     w = QtGui.QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('Simple')
#     w.show()

#     # sys.exit(app.exec_())

#     app.exec_()
#     sys.exit(0)

# if __name__ == '__main__':
#     main()

# class Icon(QtGui.QWidget):
#     def __init__(self,parent=None):
#         QtGui.QWidget.__init__(self,parent)
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Icon')
#         self.setWindowIcon(QtGui.QIcon('icons/web.png'))
# app = QtGui.QApplication(sys.argv)
# icon = Icon()
# icon.show()
# sys.exit(app.exec_())
# from xml.etree import ElementTree as ET
# import sys
# def readXml(xml):
#     assetList=[]
#     aniAssetDict={}
#     floAssetDict={}

#     root = ET.parse(xml)
#     for asset in root.findall('asset'):
#         namespace=asset.get('namespace')
#         type=asset.get('type')
#         if asset.get('status') == 'edited':
#             if type in ['chr', 'crd','veh']:
#                 aniAssetDict.setdefault(type,[]).append(namespace)
#             else:
#                 floAssetDict.setdefault(type,[]).append(namespace)
#         else:
#             aniAssetDict.setdefault(type,[]).append(namespace)
	
#     assetList=[aniAssetDict, floAssetDict]
#     print aniAssetDict
#     print floAssetDict
#     print assetList
#     return assetList

# xml_path = '/mnt/proj/projects/cat/shot/c10/c10360/flo/publish/c10360.flo.final_layout.v002/ani_assets.xml'
# readXml(xml_path)

# print sys.platform
# from shotgun_connection import Connection
# import os,sys
# sys.path.append('/mnt/utility/toolset/applications/katana/Scripts')
# sys.path.append('/mnt/utility/toolset/lib')
# from lxml import etree as ET
# from production import shotgun_connection
# import traceback
# xml_file = '/mnt/proj/projects/cat/shot/h70/h70180/ani/publish/h70180.ani.animation.v008/cache/duck_leg3/geo/duck_leg3.xml'


# # cache_path = '/mnt/proj/projects/cat/shot/h70/h70180/ani/publish/h70180.ani.animation.v008/cache'
# # caches = os.listdir(cache_path)
# # for cache in caches:
# #     cache_name = cache.split('/')[-1]
# #     if cache_name.startswith('duck_leg'):
# #         print cache
# def GetCacheModVersionFromXml(xml,Asset_name=None):
#     if os.path.isfile(xml):
#         tree = ET.parse(xml)
#         root = tree.getroot()
#         arb_list = root.getiterator('arbitraryList')
#         for ab in arb_list:
#             ats = ab.getiterator('attribute')
#             for at in ats:
#                 if at.attrib.get('name', '') == 'modVersion':
#                     return at.attrib.get('value', '')
#         # print arb_list

# # GetCacheModVersionFromXml(xml_file)
# tst_list = ['a','b','c','d']
# tst_list[0] = {'a':'b'}
# tst_list[0]['x'] = 'y'
# print tst_list[0].getName()

# import os,sys

# from PyQt4 import QtGui, QtCore

# class assetVersionUI( QtGui.QWidget):
#     def __init__(self):
#         QtGui.QWidget.__init__(self)
# import os,sys
# sys.path.append('/mnt/utility/toolset/applications/katana/Scripts')
# sys.path.append('/mnt/utility/toolset/lib')
# # from lxml import etree as ET
# from production import shotgun_connection
# # import traceback
# sg = shotgun_connection.Connection('get_shot_info').get_sg()

# assetEntity=sg.find('Asset',[['project','name_is','pws'],["code",'is','taoist_priest_little']],['id'])[-1]
# sg_info = sg.find_one(assetEntity['type'], [['id', 'is', assetEntity['id']]], ['sg_status_list'])
# print assetEntity
# print sg_info
# version_list = assetEntitylist['sg_versions']
# for ver in assetEntitylist
# print assetEntitylist
# print assetEntity
# asset_list = assetEntity['sg_versions']
# ver_list = []
# print assetEntity['sg_versions']
# for ass in asset_list:
#     if 'mod' in ass['name']:
#         ver_list.append(ass['name'].split('.')[-1])
# print ver_list

# mod = 'v002'
# tst = '002'
# print mod[1:]
# if mod[1:] != tst:
#     print 'No'
# else:
#     print 'Yes'

# shotEntity = sg.find('Shot',[['project','name_is','cat'],['code', 'is', 'e80140']],['id'])[0]
# versionEntity = sg.find('Version',[['project','name_is','cat'],['entity','is',shotEntity],['sg_version_type','is','Downstream'],['code','contains','ani.animation']],['sg_version_folder'])[-1]
# ver_fo = versionEntity['sg_version_folder']['local_path_linux']
# print ver_fo

# def readXml(xml):
#     assetList=[]
#     aniAssetDict={}
#     floAssetDict={}

#     root = ET.parse(xml)
#     for asset in root.findall('asset'):
#         namespace=asset.get('namespace')
#         type=asset.get('type')
#         if asset.get('status') == 'edited':
#             if type in ['chr', 'crd','veh']:
#                 aniAssetDict.setdefault(type,[]).append(namespace)
#             else:
#                 floAssetDict.setdefault(type,[]).append(namespace)
#         else:
#             aniAssetDict.setdefault(type,[]).append(namespace)
	
#     assetList=[aniAssetDict, floAssetDict]
#     return assetList

# # xml = ver_fo + 'ani_assets.xml'
# # print readXml(xml)
# string_tst = 'asn'
# # print type(string_tst[-1])
# # if string_tst.endswith('1'):
# #     print 'u'
# # import re
# # print re.search('.*([0-9]+).*', string_tst)
# import re
 
# pattern = re.compile(r'.*\d')
# # str = 'Abc12d'
# print pattern.match(string_tst)

# self.ModVerTableWidget.setRowCount(2)
# self.ModVerListWidget.clear()
# self.addTableWidget()
# proj = str(self.comboBox.currentText())
# shot = str(self.shotText_shot.text())
# init =  ca.checkShotAsset(proj,shot)
# self.initListTile_shot()

# AniCache_list = init.GetAniCachesFromXml()
# aniPublish_folder = init.GetLatestAniFileByShot()
# anicacheMod_dict = init.GetCacheModVersion('ani')
# ani_info = (init.GetLatestAniFileByShot()).split('/')[-2]
# AniItem=QtGui.QListWidgetItem(ani_info)
# AniItem.setStatusTip('miss')
# AniItem.setFont(self.myFont)
# self.ModVerListWidget.addItem(AniItem)

# FloCache_list = init.GetFloCachesFromXml()
# floPublish_folder = init.GetLatestFloFileByShot()
# flocacheMod_dict = init.GetCacheModVersion('flo')
# flo_info = (init.GetLatestFloFileByShot()).split('/')[-2]
# FloItem=QtGui.QListWidgetItem(flo_info)
# FloItem.setStatusTip('miss')
# FloItem.setFont(self.myFont)
# self.ModVerListWidget.addItem(FloItem)

# RowNum = len(AniCache_list) + len(FloCache_list)
# self.ModVerTableWidget.setRowCount(RowNum)
# Ani_item = QtGui.QTableWidgetItem(ani_info)
# Flo_item = QtGui.QTableWidgetItem(flo_info)
# self.ModVerTableWidget.setHorizontalHeaderItem(0,Ani_item)
# self.ModVerTableWidget.setHorizontalHeaderItem(len(AniCache_list),Flo_item)

# for cache in AniCache_list:
#     cache_file = aniPublish_folder +'cache/'+ cache + '/geo/geo_hi.abc'
#     latestModVer = init.GetLastestModVersion(cache)
#     cacheModInfo = cache + ':' + anicacheMod_dict[cache] + ':' + latestModVer[1:]
#     subItem_cache = QtGui.QListWidgetItem(cacheModInfo)
#     subItem_cache.setStatusTip(shot)
#     if os.path.isfile(cache_file):
#         if anicacheMod_dict[cache] == latestModVer[1:]:
#             subItem_cache.setIcon(self.likeIcon)
#         else:
#             subItem_cache.setIcon(self.down_arrowIcon)
#     else:
#         subItem_cache.setIcon(self.exclamationIcon)
#     self.ModVerListWidget.addItem(subItem_cache)
# for cache in FloCache_list:
#     cache_file = floPublish_folder +'cache/'+ cache + '/geo/geo_hi.abc'
#     latestModVer = init.GetLastestModVersion(cache)
#     cacheModInfo = cache + ':' + flocacheMod_dict[cache] + ':' + latestModVer[1:]
#     subItem_cache = QtGui.QListWidgetItem(cacheModInfo)
#     subItem_cache.setStatusTip(shot)
#     if os.path.isfile(cache_file):
#         if flocacheMod_dict[cache] == latestModVer[1:]:
#             subItem_cache.setIcon(self.likeIcon)
#         else:
#             subItem_cache.setIcon(self.down_arrowIcon)
#     else:
#         subItem_cache.setIcon(self.exclamationIcon)
#     self.ModVerListWidget.addItem(subItem_cache)
# import re
# shot = 'h708170'
# if re.match(r'^\w{1}\d{5}$', shot):
#     print 'Yes'
# else:
#     print 'No'

# import sys
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *

# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.setWindowTitle('Network Automation')
#         self.lb_device_list = QLabel('Device Type')
#         self.cb_device_list = QComboBox()
#         self.cb_device_list.addItem('cisco_ios')
#         self.cb_device_list.addItem('cisco_s300')

#         self.vbox = QVBoxLayout()
#         self.vbox.addWidget(self.lb_device_list)
#         self.vbox.addWidget(self.cb_device_list)

#         self.layout = QGridLayout()
#         self.layout.addLayout(self.vbox,0,0)
#         self.setLayout(self.layout)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myapp = Window()
#     myapp.show()
#     sys.exit(app.exec_())

# from lxml import etree as ET
# import shutil
# import sys,os
# sys.path.append('/mnt/utility/toolset/lib')
# sys.path.append('/mnt/utility/toolset/applications/katana/Scripts')

# import common.lcProdProj as lcpp
# from production import shotgun_connection
# sg = shotgun_connection.Connection('get_shot_info').get_sg()

# correctList = []

# def change_xform(xml,shot):
#     global key_transform
#     tree = ET.parse(xml)
#     root = tree.getroot()
#     inst_nodes=root.xpath('//instance')
#     correct = False
#     changeform=[0.0,0.0,0.0]
#     # transform = t_dict[shot]
#     print shot,transform
#     for i in inst_nodes:
#         if i.attrib['name']=="assets":
#             xform = i.xpath('./xform')[0].attrib['value']
#             # if key_transform != xform:
#             #     print xform
#             #     key_transform = xform
#             xtr = transform[0]
#             ytr = transform[1]
#             ztr = transform[2]
#             changeform=[xtr-float(xform.split(' ')[-4]), ytr-float(xform.split(' ')[-3]), ztr-float(xform.split(' ')[-2])]
#             if xform.split(' ')[-4] == str(xtr) and xform.split(' ')[-3] == str(ytr) and xform.split(' ')[-2] == str(ztr):
#                 correct = True
#                 correctList.append(xml.split('/')[-1].split('.')[0]) 
#             else:
#                 newvalue = ' '.join(xform.split(' ')[:12])+' '+str(xtr)+' '+str(ytr)+' '+str(ztr)+' '+xform.split(' ')[-1]
#                 i.xpath('./xform')[0].attrib['value'] = newvalue
#                 print i.attrib['name'], i.xpath('./xform')[0].attrib['value']

#         elif i.attrib['type'] == "reference":
#             ast_wform= i.xpath('./wform')[0].attrib['value']
#             newvalue = ' '.join(ast_wform.split(' ')[:12])+' '+str(float(ast_wform.split(' ')[-4])+changeform[0]) \
#             +' '+str(float(ast_wform.split(' ')[-3])+changeform[1])+' '+str(float(ast_wform.split(' ')[-2])+changeform[2]) \
#             +' '+ast_wform.split(' ')[-1]
#             i.xpath('./wform')[0].attrib['value'] = newvalue
#             # print i.attrib['name'],i.xpath('./wform')[0].attrib['value']

#     if not correct:
#         # oldlist=[f for f in os.listdir(os.path.dirname(xml)) if '.xml.old' in f]
#         # if oldlist:
#         #     new_path = xml + '.old'+str(len(oldlist))
#         # else:
#         #     new_path = xml + '.old'
#         # shutil.copyfile(xml,new_path)
#         tree.write(xml)
# xml = '/mnt/public/Share/zhaojiayi/code/xml/h70170.xml'
# tree = ET.parse(xml)
# root = tree.getroot()
# inst_nodes=root.xpath('//instance')

# for i in inst_nodes:

#     if i.attrib['name']=="assets":
#         xform = i.xpath('./xform')[0].attrib['value']
#     elif i.attrib['type'] == "reference": # now we r in the node of real asset
#         ast_wform= i.xpath('./wform')[0].attrib['value']
#         print ast_wform

# class modifyXml():

#     def __init__(self,proj,shot,step):
#         self.proj=proj
#         self.shot=shot
#         self.step = step
#         self.folder = self.get_latest_version()

#     def change_shot_xform(self,transform):
#         if self.folder:
#             xml = self.folder+'scene_graph_xml/'+self.shot+'.xml'
#             print xml

#     def get_latest_version(self):
#         """
#         """
#         root_path = '/mnt/proj/projects/%s/shot/%s/%s/%s/publish' % (self.proj,self.shot[:3], self.shot, self.step)
#         if os.path.exists(root_path):
#             if self.step == 'flo':
#                 vers = sorted([ver for ver in os.listdir(root_path) if 'final_layout' in ver])
#             else:
#                 vers = sorted(os.listdir(root_path))
#             if vers:
#                 last_ver = vers[-1]
#                 latest_version = root_path + '/%s/' %(last_ver)
#                 if os.path.exists(latest_version):
#                     return latest_version
#                 else:
#                     print last_ver + 'xml does not exists.' 
#             else:
#                 print 'no version:', self.shot
#         return None

# init = modifyXml('cat','h70170','flo')
# init.change_shot_xform('  ')
# def GetDownstreamVersion(proj,shot,step):
#     if step == 'flo':
#         dep = 'flo.final_layout.'
#         shotEntity = sg.find('Shot',[['project','name_is',proj],['code', 'is', shot]],['id'])[0]
#         versionEntity = sg.find('Version',[['project','name_is',proj],['entity','is',shotEntity],['code','contains',dep]],['sg_version_folder','sg_version_type'])
#         if versionEntity and versionEntity[-1]['sg_version_type'] == 'Downstream':
#             latest = versionEntity[-1]['sg_version_folder']['local_path_linux']
#             return latest
#         else:
#             return None
# proj = 'tst'
# shot = 'c30007'
# step = 'flo'

# print GetDownstreamVersion(proj,shot,step)
# h80_city.river_asb.river

# tst = 'a b c d'
# tst_list = tst.split(' ')
# print tst_list
# def get_latest_version(proj,shot,step):
#     root_path = '/mnt/proj/projects/%s/shot/%s/%s/%s/publish' % (proj,shot[:3], shot, step)
#     if os.path.exists(root_path):
#         if step == 'flo':
#             vers = sorted([ver for ver in os.listdir(root_path) if 'final_layout' in ver])
#         else:
#             vers = sorted(os.listdir(root_path))
#         if vers:
#             last_ver = vers[-1]
#             latest_version = root_path + '/%s/' %(last_ver)
#             if os.path.exists(latest_version):
#                 return latest_version
#             else:
#                 print last_ver + 'xml does not exists.' 
#         else:
#             print 'no version:', self.shot
#     else: 
#         print '[Error] : No Such Publish File' 
#     return None

# print get_latest_version('tst','a10010','flo')
# asset = "r50_city.peach_garden_true_asb.peach_tree_big6"
# if 'peach_tree_big' in asset:
#     print 'Yes'
# from xml.etree import ElementTree as ET
# from lxml import etree as ET
# def solve_asset_hidden(xml,assetNamespace): # asset name with namespace means that the asset is in the 'scn' level
#     tree = ET.parse(xml)
#     root = tree.getroot()
#     inst_nodes=root.xpath('//instance')
#     for i in inst_nodes:
#         if i.attrib['name'] == assetNamespace:
#             v_node = i
#     if v_node is not None: 
#         print 'the changed asset name is ' + str(v_node.attrib['name'])
#         attList=v_node.xpath('.//attribute')
#         for v in attList:
#             print v.attrib['name']
#             if v.attrib['name'] == 'hidden':
#                 v.attrib['name'] = 'viewable'
#                 v.attrib['value'] = "yes"
#                 print 'change state'
#             if v.attrib['name'] == 'angle':
#                 if v.attrib['value'] == "0.0":
#                     v.attrib['value'] = "2.0"
#                     print 'change angle'                        
#             print "Change the asset %s from hidden to viewable" %assetNamespace
#             break
#     # tree.write(xml)
#     return 1

# assetNamespace = 'h80_city.south_area_b.asphodel100'
# xml = '/mnt/proj/projects/tst/shot/a10/a10010/flo/publish/a10010.flo.final_layout.v002/scene_graph_xml/a10010.xml'

# solve_asset_hidden(xml,assetNamespace)

# tst_list = ['a','b','c']
# tst_list = []
# # index = tst_list.index('c')
# # tst_list.pop(index)
# print tst_list
# value = 100.00
# v = int(value)
# print v
# tst_dict = {'soldier_norm_a': None, 'soldier_norm': None, 'axuan': ['frozen', 'scratch']}
# tst_dict = {}
# print tst_dict

# ['man_norm', 'soldier_norm', 'soldier_norm_a']
# ['man_norm', 'man_stro', 'soldier_norm', 'soldier_stro', 'soldier_stro_a']
# ['man_norm', 'soldier_norm', 'man_norm', 'man_stro', 'soldier_norm', 'soldier_stro', 'soldier_stro_a', 'soldier_norm_a']

# import sys,os
# import traceback
# sys.path.append('/mnt/public/Share/zhaojiayi/gitrepo/lcatools/lib/production')
# import shotgun_connection
# sg = shotgun_connection.Connection('get_shot_info').get_sg()
# sys.path.append('/mnt/utility/toolset/lib/production')
# import pipeline.ShotGunProj as psgp
# reload(psgp)
# proj = 'pws'

# def GetLastestSrfVersion(proj,asset_name):
#     assetEntity=sg.find('Asset',[['project','name_is',proj],["code",'is',asset_name]],['id'])[0]
#     look_pass = []
#     try:
#         versionEntity = sg.find('Version',[['project','name_is',proj],['entity','is',assetEntity],['sg_version_type','is','Downstream'],['code','contains','srf.surfacing']],['sg_version_folder'])[-1]
#     except:
#         return None

#     lookpass_info = sg.find_one('Asset', [['project', 'name_is', proj], ['code', 'is', asset_name]], ['sg_look_passes_1'])['sg_look_passes_1']
#     if lookpass_info:
#         for dic in lookpass_info:
#             look_pass.append(dic['name'])
#         return look_pass
#     else:
#         return 'No Pass'

# def get_parent_asset_list(proj,asset_name):
#     init = psgp.ShotGunProj(proj)
#     asset_list = init.get_klf_asset_list(asset_name)
#     return asset_list

# asset_list =  get_parent_asset_list('pws','soldier_norm_a')
# print asset_list
# for ass in asset_list:
#     print GetLastestSrfVersion('pws',ass)

# assetEntity=sg.find('Asset',[['project','name_is','pws'],["code",'is','xiaobai_girl']],['sg_versions'])[-1]

# assetversion_list = assetEntity['sg_versions']
# print assetversion_list
# print GetLastestSrfVersion('pws','man_norm')

# assetId=sg.find('Asset',[['project','name_is',proj],["code",'is','citizen_on_horse']],['id'])[0]['id']
# print assetId
# # chr_list = []
# # for ch in List:
# #     chr_list.append(ch['code'])
# # print chr_list
# tst_list = [{'LookPass': None, 'asset': 'citizen_rich_woman_norm', 'LookColor': ['min: 0', 'max: 0']}, {'LookPass': None, 'asset': 'woman_thin', 'LookColor': ['min: 0', 'max: 0']}, {'LookPass': None, 'asset': 'citizen_on_horse', 'LookColor': ['min: 0', 'max: 0']}, {'LookPass': ['makeup'], 'asset': 'woman_norm', 'LookColor': ['min: 0', 'max: 0']}, {'LookPass': None, 'asset': 'citizen_rich_woman_thin', 'LookColor': ['min: 0', 'max: 0']}]
# def type_to_string(element_list):
#     dict_string = '['
#     for ele in element_list:
#         LookPass_string = '\'LookPass\': ['
#         asset_string = '{\'asset\': '
#         LookColor_string = '\'LookColor\': ['
#         if ele['LookPass'] != None:
#             if len(ele['LookPass'])>1:
#                 for i in range(len(ele['LookPass'])-1):
#                     LookPass_string += "\'%s\'," %ele['LookPass'][i]
#             LookPass_string +=  "\'%s\']," %ele['LookPass'][-1]
#         else:
#             LookPass_string = '\'LookPass\' : None,'
#         asset_string += '\'%s\',' %ele['asset']
#         LookColor_string += '\'%s\', \'%s\']}' % (ele['LookColor'][0],ele['LookColor'][-1])
#         dict_string += ((asset_string + LookPass_string + LookColor_string) + ',')
#     dict_string += ']'
#     return dict_string
# string = type_to_string(tst_list)
# print eval(string)




# def dict_to_string(d):
#     d_string = '{'
#     for key, value in d.items():
#        d_string += "\"%s\":\"%s\"" % (key, value)
#        d_string += ','
#     d_string += '}'
#     return d_string
# d = {'a': 'b','c':'d'}
# d_string =  dict_to_string(d)
# print eval(d_string)
# a = '/mnt/proj/projects/pws/shot/h20/h20293/ani/publish/h20293.ani.animation.v023/'
# cache_path = a+'cache'
# if os.path.isfile(cache_path):
#     print 'Yes'
#     
# tst = []
# print tst
# if tst:
#     print 'YEs'
# else:
#     print 'N'

# def get_all_asm_asset(proj):
#     chr_asset_list = sg.find('Asset',[['project','name_is',proj],["sg_asset_type",'is','chr']],['code'])
#     chr_list = []
#     asm_list = []
#     for ch in chr_asset_list:
#         chr_list.append(ch['code'])
#         if ch['code'].startswith('w'):
#             print ch['code']
	# print chr_list
	# init = psgp.ShotGunProj(proj)
	# for c in chr_list:
	#     if init.parent_is_asm(c):
	#         asm_list.append(c)
	# return asm_list


# def parent_is_asm(asset):
#     asset_sg = sg.find_one('Asset', [['project', 'name_is', 'pws'], ['code', 'is', asset]], ['code', 'parents'])
#     if asset_sg and len(asset_sg['parents'])>0:
#         for p in asset_sg['parents']:
#             pa=sg.find_one('Asset',[['project','name_is','pws'],['code','is',p['name']]],['sg_asset_type'])
#             if pa and pa['sg_asset_type']=='asm':
#                 return True
#     return False

# # get_all_asm_asset('pws')
# # print parent_is_asm('soldier_norm_a')

# def get_cloth_parent_pass(proj,asset):
#     parent_close = sg.find_one('Asset', [['project', 'name_is', proj], ['code', 'is', asset]], ['code', 'parents'])['parents'][0]['name']
#     lookpass_info = sg.find_one('Asset', [['project', 'name_is', proj], ['code', 'is', parent_close]], ['sg_look_passes_1'])['sg_look_passes_1']
#     lookpass_info.append('default')
#     return lookpass_info

# print get_cloth_parent_pass('pws','soldier_norm_a')

# def get_parent_pass(proj,asset,flag = None):
#     lookpass_info = []
#     parent_asset = sg.find_one('Asset', [['project', 'name_is', proj], ['code', 'is', asset]], ['code', 'parents'])['parents'][0]['name']
#     if flag == 'body':
#         parent_asset = sg.find_one('Asset', [['project', 'name_is', proj], ['code', 'is', parent_asset]], ['code', 'parents'])['parents'][0]['name']
#     remark_info = sg.find_one('Asset', [['project', 'name_is', proj], ['code', 'is', parent_asset]], ['sg_remark'])['sg_remark']
#     if remark_info:
#         lookpass_info.append(eval(remark_info)['klf'])
#     else:
#         lookpass_info = sg.find_one('Asset', [['project', 'name_is', proj], ['code', 'is', parent_asset]], ['sg_look_passes_1'])['sg_look_passes_1']
#     lookpass_info.append('default')
#     return lookpass_info

# def get_parent_pass_info(proj,asset):
#     cloth_pass_list = get_parent_pass(proj,asset)
#     body_pass_list = get_parent_pass(proj,asset,'body')
#     return cloth_pass_list,body_pass_list

# print get_parent_pass('pws','soldier_stro_a')
# get_parent_pass('pws','soldier_stro_a','body')

# task_list=sg.find('Task',[['project', 'name_is', 'pws'],['step','name_is','art']],['code'])
# for task in task_list:
#     version_list = sg.find('Version',[['project', 'name_is', 'pws'],['sg_task.Task.id','is',task['id']]],['code','sg_version_folder'])
#     print version_list
# file_path = '/mnt/proj/projects/pws/preproduction/f30/story/art/publish/f30.art.design_c.v000'
# print os.access(file_path,os.F_OK) # whether exists
# print os.access(file_path,os.R_OK)
# print os.access(file_path,os.W_OK)
# print os.access(file_path,os.X_OK)
# import subprocess
# subprocess.call("ls -l /mnt/proj/projects/pws/preproduction/f30/story/art/publish >/mnt/public/Share/zhaojiayi/tst/mode.txt", shell=True)
# subprocess.call("ls -l /mnt/proj/projects/pws/preproduction/b70/story/art/publish >>/mnt/public/Share/zhaojiayi/tst/mode.txt", shell=True)

# ts = '/mnt/proj/projects/pws/asset/chr/xiaobai_girl/art/publish/xiaobai_girl.art.design_c.v011/'
# # tst = ts.split('publish')[0]
# # print tst + 'publish'
# print ts.rstrip('publish')

# def convert_file(self, src, dst):
# import subprocess
# def convert_file():
#     p = subprocess.Popen('"' + '/usr/local/rv/rv-Linux-x86-64-4.0.10/bin/rvls' + '" -l ' + '/home/jiayi/Downloads/pokeball.png', shell=True, stdin= subprocess.PIPE, stdout= subprocess.PIPE)
#     tokens = p.communicate()[0].split('\n')[1].split(' ')
#     # print tokens
#     tokens = [i for i in tokens if i != '']
#     print tokens
#     # self.dialog.print_log(tokens)
#     if not (tokens[0].isdigit() and tokens[2].isdigit()):
#         return

#     img_w = int(tokens[0])
#     img_h = int(tokens[2])

#     if img_w == 0 or img_h ==0:
#         return

#     ratio = min(900/float(float(img_w)), 600/float(img_h))
#     cmd = '"'+ self.dialog.rvio_path +'" ' +src  + ' -scale ' + str(ratio) + ' -o ' + dst

#     ext_src = src.lower().split('.')[-1]
#     if ext_src == 'exr':
#         cmd += ' -outsrgb'

#     os.system(cmd)
#     return

# convert_file()
# version_dir = '/mnt/proj/projects/tst/asset/asb/park/art/publish/park.art.design_c.v022'
# l_preview_files = ['/mnt/proj/projects/tst/asset/asb/park/art/publish/park.art.design_c.v000/buckup/pokeball.20171103141813.png','/mnt/proj/projects/tst/asset/asb/park/art/publish/park.art.design_c.v000/buckup/haidao.1501730339.jpg']
# version_name = '/mnt/proj/projects/tst/asset/asb/park/art/publish/park.art.design_c.v022/preview/park.art.design_c.v022'
# def create_version_preview():
#     # create preview folder
#     preview_dir = version_dir + '/preview/'
#     if not os.path.isdir(preview_dir):
#         os.makedirs(preview_dir)

#     # images - copy and convert
#     # mov - copy
#     for i in range(len(l_preview_files)):
#         l_preview_files[i]=str(l_preview_files[i])
#     if len(l_preview_files) == 1 and l_preview_files[0].endswith('.mov'):
#         self.dialog.v_preview = preview_dir + self.dialog.version_name +'.mov'
#         cmdStr = ' '.join(['Copy', self.dialog.l_preview_files[0], self.dialog.v_preview])
#         shutil.copyfile( self.dialog.l_preview_files[0], self.dialog.v_preview)
#         self.dialog.v_pdf = ''
#     else:
#         l_copied_files = []
#         self.dialog.l_preview_files.sort()
#         for i in range(len(self.dialog.l_preview_files)):
#             dst = preview_dir + (self.dialog.version_name + ('.%04d.' % i) + 'jpg' )
#             self.copy_file(self.dialog.l_preview_files[i], dst)
#             l_copied_files.append(dst )

#         self.dialog.v_preview = preview_dir + self.dialog.version_name +'.mov'
#         cmdStr = '"'+ self.dialog.rvio_path +'" [ ' + preview_dir + self.dialog.version_name + '.%04d.jpg -pa 1.0 ] -o ' + self.dialog.v_preview
#         os.system(cmdStr)
#         #self.dialog.print_log(cmdStr)

#         self.dialog.v_pdf = preview_dir + self.dialog.version_name +'.pdf'
#         cmdStr = '"' + self.dialog.pdf_tool + '" -density 72 ' + preview_dir + '*.jpg ' + self.dialog.v_pdf
#         os.system(cmdStr)
#         #self.dialog.print_log(cmdStr)

#         # clean jpg files
#         for file_path in l_copied_files:
#             os.remove(file_path)

#     return cmdStr

# class FooParent(object):
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print ('Parent')
	
#     def bar(self,message):
#         print ("%s from Parent" % message)
 
# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
#         super(FooChild,self).__init__()    
#         print ('Child')
		
#     def bar(self,message):
#         super(FooChild, self).bar(message)
#         print ('Child bar fuction')
#         print (self.parent)
 
# if __name__ == '__main__':
#     fooChild = FooChild()
#     fooChild.bar('HelloWorld')
# import subprocess
# import os
# rvls_path = '/usr/local/rv/rv-Linux-x86-64-4.0.10/bin/rvls'
# rvio_path = '/usr/local/rv/rv-Linux-x86-64-4.0.10/bin/rvio'
# src = '/mnt/proj/projects/tst/asset/asb/park/art/publish/park.art.design_c.v000/3toy_02.jpg'
# dst = '/mnt/proj/projects/tst/asset/asb/park/art/publish/park.art.design_c.v000/preview/park.art.design_c.v000.0000.jpg'
# p = subprocess.Popen('"' + rvls_path + '" -l ' + src, shell=True, stdin=subprocess.PIPE,
#                              stdout=subprocess.PIPE)
# tokens = p.communicate()[0].split('\n')[1].split(' ')
# print tokens
# tokens = [i for i in tokens if i != '']
# string = tokens
# string = '-'.join(string)
# print string
# print tokens
# img_w = int(tokens[0])
# img_h = int(tokens[2])
# ext_src = src.lower().split('.')[-1]

# if max(img_w, img_h) > 2048:
#     ratio = str(2048.0 / float(max(img_w, img_h)))
#     cmd = '"' + rvio_path + '" ' + src + ' -scale ' + ratio + ' -o ' + dst
#     if ext_src == 'exr':
#         cmd += ' -outsrgb'
#     print cmd
#     os.system(cmd)
# elif ext_src != 'jpg':
#     cmd = '"' + rvio_path + '" ' + src + ' -o ' + dst
#     if ext_src == 'exr':
#         cmd += ' -outsrgb'
#     print cmd
#     # os.system(cmd)
# else:
#     shutil.copyfile(src, dst)
# print 'Done!'
# tst_list = ['absdjhf;ishf','n','v']
# for t in tst_list:
#     if 'a' in t:
#         continue
#     print t

# num_list = [1,2,3,4]
# i = 0
# value_list = []
# for h in num_list:
#     for t in num_list:
#         for s in num_list:
#             if h != t and t != s:
#                 if h!=s:
#                     value = h*100 + t*10 +s
#                     value_list.append(value)
#                     i = i+1
# print value_list 
# print i

# def get_node_children_by_type(node, node_type, parm_name=None, operation=None):
#     result = []
#     for c in node.getChildren():
#         if c.getType() == node_type:
#             if not parm_name:
#                 result.append(c)
#             else:
#                 if c.getParameter(parm_name):
#                     result.append(c)
#     if operation and result:
#         filter(operation, result)
#     return result
# try:
#    network = srfMtlMerge.SrfNodesNetwork(node)
#    base = network.createBase(node)
#    info = network.gatherInfo(node,shader_name='standard_surface')
#    network.buildNetwork_a5(info, base)
#    network.createMtlAssign()

# except:
#    raise Exception(traceback.format_exc())
# mtl_name = 'skin_body'
# shader_name = 'standard_surface'
# info = {'layer1': [mtl_name + '_' + shader_name, {}]}
# print info
# name_list = ['bump_map','spec2Clr_map']
# path= '/mnt/work/projects/tst/asset/prp/camera_inhand/srf/task/images/tex/'

# for n in name_list:
#     info['layer1'][1][n] = path

# print info
# node_name = info['layer1'][0]
# maps = info['layer1'][1]
# print 'node_name:' + node_name
# print maps
# print maps.keys()

# def createAsnNode(self, node_type, node_name, root, root_pos, offset=[0, 0]):
#     node = NodegraphAPI.CreateNode('ArnoldShadingNode', root)
#     node.getParameter('nodeType').setValue(node_type, 0)
#     node.setName(node_name)
#     node.getParameter('name').setValue(node_name, 0)
#     node.checkDynamicParameters()
#     NodegraphAPI.SetNodePosition(node, (root_pos[0] - offset[0], root_pos[1] + offset[1]))
#     return node


# {'layer1': ['skin_body_standard_surface', {'spec2Clr_map': '/mnt/work/projects/tst/asset/prp/camera_inhand/srf/task/images/tex/', 'bump_map': '/mnt/work/projects/tst/asset/prp/camera_inhand/srf/task/images/tex/'}]}
# info = {'layer2': ['skin_body_spec_only_standard_surface', {'coat_map': '/mnt/work/projects/tst/asset/prp/camera_inhand/srf/task/images/tex/'}], \
#  'layer1': ['skin_body_standard_surface', {'normal_map': '/mnt/work/projects/tst/asset/prp/camera_inhand/srf/task/images/tex/'}]}

# for key in info.keys():
#     print key
#     print info[key][0]

# def get_render_nodes_from_muster(shot):
#     for muster_dispacher in muster_dispacher_list:
#         print 'search jobs in', muster_dispacher
#         print '-' * 50
#         conn = MySQLdb.connect(
#             host=muster_dispacher, user='xiaom', passwd='000000', db='muster', cursorclass=MySQLdb.cursors.DictCursor)
#         cu = conn.cursor()
#         sql = 'select * from db_jobs where engine in ("953","950") and instr(job_name, "%s") and is_locked = "1"' % shot
#         # print sql
#         cu.execute(sql)
#         r = cu.fetchall()
#         if not r:
#             print 'damn, found nothing...'
#         else:
#             node_names = []
#             for i in r:
#                 print i['job_name']
#                 node_names.append(i['job_name'].split('-')[1])
#         cu.close()
#         conn.close()
#         print '-' * 50
#         print 'count: %d' % len(r)
#         print '-' * 50
#         if r:
#             print 'nodes: %s' % ';'.join(node_names)
#         print '\n'
# import sys
# def abort_tst():
#     print 'abort'
#     # return 0
#     sys.exit()

# def main():
#     print 'step1'
#     abort_tst()
#     print 'step2'

# value = main()
# print 'nnnnnn'
# print value

# file_path = '/mnt/public/Share/zhaojiayi/code/muster/logs_job_id_972244/render3193.txt'
# fo = open(file_path, "r+")
# line_count = 0
# # str = fo.read(100);
# line = fo.readline()
# while line != "":
#     line = fo.readline()
#     if '--------file---------' in line:
#         print line
#         break
#     line_count +=1
# print line_count
# fo.close()

# fo = open(file_path, "r+")
# line = fo.readline()
# for i in range(90):
#     line = fo.readline()
#     if i == 89 or i == 88:
#         print line

# fo.close()

# instance_list = ['render3062','render3193','render3034','render3130']

# def record_log(str_app):
#     record_file = '/mnt/public/Share/zhaojiayi/code/muster/logs_job_id_972244/render_cap.txt'
#     fo = open(record_file, "rw+")
#     ori_str = fo.read()
#     fo.write(str_app)
#     fo.close()

# # record_log('what')

# for ins in instance_list:
#     file_path = '/mnt/public/Share/zhaojiayi/code/muster/logs_job_id_972244/%s.txt'%ins
#     fo = open(file_path, "r+")
#     line_count = 0
#     line = fo.readline()
#     while line != "":
#         line = fo.readline()
#         if '--------file---------' in line:
#             si_flag = 1
#             break
#         line_count +=1
#     fo.close()
#     if si_flag == 1:
#         fo = open(file_path, "r+")
#         line = fo.readline()
#         for i in range(line_count):
#             line = fo.readline()
#             if i == (line_count-1):
#                 if 'Done' in line :
#                     # print ('Instance %s is ok'%ins)
#                     fo.close()
#                     str_app = ins + ' ok\n'
#                     # return flag,'ok'
#                 else:
#                     # print ('Instance %s is wrong'%ins)
#                     fo.close()
#                     str_app = ins + ' wrong\n'  
#                 record_log(str_app)
#                     # return flag,'wrong'
#         fo.close()

# file_path = FarmAPI.GetKatanaFileName()

# file_path = FarmAPI.GetKatanaFileName()
# print file_path
# file_path = file_path.replace(file_path.split('/')[-1], '')[:-7] + 'images/tex/'
# node.getParameter('user.texture_path').setValue(file_path, 0)

# node.getParameter('user.control_maps.disp_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.bump_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.normal_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.diffClr_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.diffInt_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.spec1Clr_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.spec1Int_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.spec1Rough_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.coatClr_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.coat_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.coatRough_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.emissionClr_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.control_maps.emission_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)

# node.getParameter('user.layers.layer2.control_maps.bump_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.layers.layer2.control_maps.normal_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.layers.layer2.control_maps.diffClr_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.layers.layer2.control_maps.diffInt_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.layers.layer2.control_maps.spec1Clr_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.layers.layer2.control_maps.spec1Int_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.layers.layer2.control_maps.spec1Rough_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.layers.layer2.control_maps.coatClr_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.layers.layer2.control_maps.coat_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.layers.layer2.control_maps.coatRough_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.layers.layer2.control_maps.emissionClr_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# node.getParameter('user.layers.layer2.control_maps.emission_map.file_path').setExpression('getParam("srf_mtl_Merge.user.texture_path")', True)
# import datetime as dt
# st = 1509602250
# starting_time_dt = dt.datetime.fromtimestamp(st)
# time_now = dt.datetime.now()
# elaps_time = time_now - starting_time_dt
# delta_time = dt.timedelta(seconds=60 * 6000) 
# print starting_time_dt
# print time_now
# print elaps_time
# print delta_time
# from ssh_cmd import ssh_cmd
# print ssh_cmd

# node3_list = range(12,21) + range(28,210) + [254]
# print node3_list
# import subprocess
# # # gnome-terminal -e "/mnt/public/Share/zhaojiayi/gitrepo/lca_rez/launchers/pws/linux/katana" hold
# # # subprocess.call(gnome-terminal -e "/mnt/public/Share/zhaojiayi/gitrepo/lca_rez/launchers/pws/linux/katana" hold)
# # # t = subprocess.Popen(['gnome-terminal'])
# # # subprocess.call(['gnome-terminal', '-x', '/mnt/public/Share/zhaojiayi/gitrepo/lca_rez/launchers/pws/linux/katana'])
# # # script_py = '/mnt/public/Share/zhaojiayi/gitrepo/lcatools/tools/plt/plt_tools_shelf/katana_exec.py'
# # # subprocess.call(['gnome-terminal', '-x', '/mnt/public/Share/zhaojiayi/gitrepo/lca_rez/launchers/pws/linux/katana --script='\
# # #                   + script_py + ' '+ 'shpt'])
# import os
# proj = 'tst'
# shot = 'a10010'
# script_py = '/mnt/utility/toolset/tools/plt/plt_tools_shelf/katana_exec.py'
# p1 = subprocess.call(['gnome-terminal', '-e', '/mnt/public/Share/zhaojiayi/gitrepo/lca_rez/launchers/pws/linux/katana --script=/mnt/public/Share/zhaojiayi/gitrepo/lcatools/tools/plt/plt_tools_shelf/katana_exec.py %s %s'%(proj,shot)])
# p1.wait()'gnome-terminal', '-e','/mnt/public/Share/zhaojiayi/gitrepo/lca_rez/launchers/pws/linux/katana %s'%real_path
# print '.................'
# # real_path'/mnt/work/projects/tst/shot/a10/a10010/plt/task/katana'
#           # /mnt/work/projects/tst/shot/a10/a10010/plt/task/katana
# seq = shot[:-3]
# path = '/mnt/work/projects/%s/shot/%s/%s/plt/task/katana'%(proj,seq,shot)
# print len(os.listdir(path))

# print path
# real_path = path + '/' +os.listdir(path)[-1]
# print real_path
# p_o = subprocess.call(['gnome-terminal', '-e','/mnt/public/Share/zhaojiayi/gitrepo/lca_rez/launchers/pws/linux/katana %s'%real_path])
# get_path = '/output/projects/tst/shot/a10/a10010/plt/output/render_images/a10010.plt.render.v005'
# export_path = '/mnt/work/projects/tst/shot/a10/a10010/plt/task/katana'
# '/mnt/work/projects/tst/shot/a10/a10010/plt/task/katana/a10010.plt.render.v005.katana'
# '/mnt/work/projects/tst/shot/a10/a10010/plt/task/katana/a10010.plt.render.v005.katana'

# export_path = NodegraphAPI.GetNode('PltCheckCache_Lc').getParameter('user.export_to').getValue(0)
# get_path = NodegraphAPI.GetNode('PltCheckCache_Lc').getParameter('user.render_set.render_output').getValue(0)
# real_path = export_path +'/' + get_path.split('/')[-1] + '.katana'
# print real_path
# shot = 'ASB'
# # sh = lower(shot)
# print shot.lower()
# cmdStr = '/mnt/utility/linked_tools/lca_rez/launchers/pws/linux/katana --script=%s %s %s' %(script_py, proj,shot)
# os.system(cmdStr)

# p = '/mnt/work/projects/pws/shot/h20/h20090/plt/task/katana'
# p_list = os.listdir(p)
# f_list = []
# # print p_list
# # p_list.sort()
# # print p_list
# for f in os.listdir(p):
#     if 'plt.render' in f:
#         f_list.append(f)

# print f_list 
# f_list.sort()
# print f_list

# import os
# # cmd_str = '/mnt/utility/lca_launchers/python/python27 /mnt/utility/lca_sgtk_apps/tk-lca-shot-player/python/tk_lca_shot_player/main.py'
# # os.system(cmd_str)
# # cmd_str = 'python /mnt/utility/toolset/tools/cfx/kan/cmd.py pws h20090 plt'
# # cmd_1984 = '/mnt/utility/lca_launchers/python/python27 /mnt/utility/lca_sgtk_apps/tk-lca-shot-player/python/tk_lca_shot_player/main.py'
# # os.system(cmd_1984)
# cmd_str = 'python /mnt/utility/toolset/tools/cfx/kan/cmd.py pws h20090 plt'
# os.system(cmd_str)

# import os
# import subprocess
# # mov_list = []
# # proj = 'pws'
# # shot = 'h20040'
# # # if shot == None:
# # #     print 'Please Input Shot Number'
# # #     return
# # # step = str(comboBox_step.currentText())
# # # cmd_str = 'python /mnt/utility/toolset/tools/cfx/kan/cmd.py %s %s %s' %(proj, shot, step)
# # # os.system(cmd_str)
# # step = 'plt'
# # mov_path = '/mnt/output/projects/%s/shot/%s/%s/%s/output/render_images'%(proj,shot[:-3],shot,step)
# # print mov_path
# # for o in os.listdir(mov_path):
# #     if '.mov' in o and 'plt.render' in o:
# #         mov_list.append(o)
# # mov_list.sort()
# # mov_file = mov_path + '/' + mov_list[-1]
# # print mov_file
# # cmd_kan = '/usr/local/rv/rv-Linux-x86-64-4.0.10/bin/rv %s'% mov_file
# # subprocess.call(['gnome-terminal','-e', cmd_kan])

# tst_list = []
# # if tst_list == None:
# #     print 'Yes'
# print len(tst_list)
# if len(tst_list) == 0:
#     print 'Yes'

# mov_dir = '/mnt/output/projects/pws/shot/h20/h20040/plt/output/render_images'

# for o in os.listdir(mov_dir):
# tst_list = ['a','a','a','b','c']
# print set(tst_list)
# print list(set(tst_list))
# get_camera

# cam_list = ['/mnt/proj/projects/cat/shot/r30/r30620/cam/publish/r30620.cam.camera.v001','/mnt/proj/projects/cat/shot/r30/r30620/cam/publish/r30620.cam.camera.v002',\
#             '/mnt/proj/projects/cat/shot/r30/r30620/cam/publish/r30620.cam.camera.v003','/mnt/proj/projects/cat/shot/r30/r30620/cam/publish/r30620.cam.camera.v004',\
#             '/mnt/proj/projects/cat/shot/r30/r30620/cam/publish/r30620.cam.camera.v005']

# def get_camera(shot):
#     """
#     get camera abc file for specified shot
#     """
#     cam_folder = cam_list
#     if not cam_folder:
#         return

#     result=''
#     stereo_abc=''
#     for f in cam_folder.get('camera',[]):
#         print f
#         # cam_abc=f+'/'+shot+'_cam.abc'
#         # if os.path.isfile(cam_abc):
#         #     abc_real_path=os.path.realpath(cam_abc)
#         #     if '.flo.stereo.' in abc_real_path:
#         #         stereo_abc=abc_real_path
#         #     result=abc_real_path

#     # return stereo_abc if stereo_abc else result

# get_camera('r30620')

# import sys
# import os
# sys.path.insert(0,'/mnt/public/Share/zhaojiayi/gitrepo/lcatools/applications/katana/Scripts/')
# import common.lcProdProj as lcp
# reload(lcp)
# localP=lcp.lcProdProj()
# localP.setProj('cat')
# # print localP.get_camera('r30620')
# cam_path = '/mnt/proj/projects/cat/shot/r30/r30620/cam/publish/r30620.cam.camera.v003/r30620_cam.abc'
# abc_real_path=os.path.realpath(cam_path)
# print abc_real_path

# import macro.lgtShotMaker as mlsm
# import traceback
# try:
#    mlsm.getExistingKatana(node)
# except:
#    raise Exception(traceback.format_exc())

# import macro.lgtShotMaker as mlsm
# import traceback
# try:
#    mlsm.getExistingKatana(node,True)
# except:
#    raise Exception(traceback.format_exc())
# import os
# abc = '/mnt/proj/projects/cat/asset/env/lake_bottom_env/mod/publish/lake_bottom_env.mod.model.v031/scene_graph_xml/hi.abc'
# print os.path.dirname(abc).getData()
# tst_list = ['a']
# tst_list += 'b'
# print tst_list
# /mnt/proj/projects/cat/shot/r30/r30620/plt/publish/r30620.plt.lake_bottom_env_plant.v006/cache/lake_bottom_env/xgen/collections/and_al_col/and_al_col.xgen -palette and_al_col -geom /mnt/proj/projects/cat/shot/r30/r30620/plt/publish/r30620.plt.lake_bottom_env_plant.v006/cache/lake_bottom_env/xgen/collections/and_al_col/patches/and_al_col.abc 
# /efxcache/projects/cat/asset/efx/water_smoke_lakebottom/efx/publish/water_smoke_lakebottom.efx.efx.v001/smoke_general10/vdb/smoke_general10.vdb
# /efxcache/projects/cat/shot/r30/r30620/efx/publish/r30620.efx.water_deep.v003/particle_volume11/abc/particle_volume11.1088.abc
# import sys
# sys.path.append('/mnt/utility/toolset/lib/production')
# import shotgun_connection
# sg = shotgun_connection.Connection('get_shot_info').get_sg()

# asm_list = ['soldier_norm_a',  'soldier_norm_cavalry', 'soldier_thin_a', 'soldier_stro_a', 'citizen_richman_norm_a',\
#             'citizen_richman_stro_a', 'citizen_rich_woman_thin_a', 'citizen_rich_woman_fat_a', 'citizen_poor_man_thin_a', \
#             'citizen_poor_woman_norm_a', 'citizen_poor_woman_norm_b', 'citizen_poor_oldman_norm_a', 'citizen_poor_oldwoman_norm_a',\
#             'villager_man_norm_catcher', 'villager_man_stro_catcher', 'villager_man_thin_a', 'villager_man_thin_b', 'villager_man_thin_c', \
#             'villager_woman_norm_catcher', 'villager_woman_norm_a', 'villager_woman_norm_b', 'villager_boy_norm_a', 'villager_girl_norm_a', \
#             'maid_thin_a', 'maid_norm_a', 'villager_man_norm_b', 'villager_man_norm_c', 'villager_oldman_norm_b', 'villager_oldman_norm_c', \
#             'villager_woman_thin_a', 'villager_woman_thin_b', 'villager_oldwoman_norm_a', 'villager_oldwoman_norm_b', 'soldier_stro_senior', \
#             'citizen_poor_man_norm_a', 'citizen_poor_woman_thin_a', 'citizen_poor_woman_thin_b','villager_man_norm_a', 'villager_oldman_norm_a']

# # asm_list = ['citizen_poor_woman_norm_a']


# def get_asm_info(asset):
#     proj = sg.find_one('Project', [['name', 'is', 'pws']], [])
#     asset_sg = sg.find_one('Asset', [['project', 'is', proj], ['code', 'is', asset]], ['code', 'parents','sg_remark'])
#     if asset_sg['sg_remark']:
#         return eval(asset_sg['sg_remark'])
#     else:
#         return {'bodyPass': ['default'],'bodyColor': ['min: 0.0', 'max: 1.0'],'clothPass': ['default'],'clothColor': ['min: 0.0', 'max: 1.0']}

# def get_asm_pass_info(asset):
#     asm_pass_info = {}
#     cloth_pass_list = []
#     body_pass_list = []
#     asm_info = get_asm_info(asset)
#     # print asm_info
#     cloth_asset = asm_info['clothPass']
#     body_asset = asm_info['bodyPass']
#     parent_asset = sg.find_one('Asset', [['project', 'name_is', 'pws'], ['code', 'is', asset]], ['code', 'parents'])['parents'][0]['name']
#     if len(cloth_asset)>1:
#         for c in cloth_asset:
#             if c != 'default':
#                 lookPass_list = sg.find_one('Asset', [['project', 'name_is', 'pws'], ['code', 'is', c]], ['sg_look_passes_1'])['sg_look_passes_1']
#                 if lookPass_list:
#                     for l in lookPass_list:
#                         asm_pass_info.setdefault('clothPass',[]).append(l['name'])
#     else:        
#         lookPass_list = sg.find_one('Asset', [['project', 'name_is', 'pws'], ['code', 'is', parent_asset]], ['sg_look_passes_1'])['sg_look_passes_1']
#         # print lookPass_list
#         if lookPass_list:
#             for l in lookPass_list:
#                 asm_pass_info.setdefault('clothPass',[]).append(l['name'])
#     asm_pass_info.setdefault('clothPass',[]).append('default')
#     if len(cloth_asset)>1:
#         for b in body_asset:
#             if b!= 'default':
#                 lookPass_list = sg.find_one('Asset', [['project', 'name_is', 'pws'], ['code', 'is', b]], ['sg_look_passes_1'])['sg_look_passes_1']
#                 if lookPass_list:
#                     for l in lookPass_list:
#                         asm_pass_info.setdefault('bodyPass',[]).append(l['name'])
#     else:
#         parent_asset = sg.find_one('Asset', [['project', 'name_is', 'pws'], ['code', 'is', parent_asset]], ['code', 'parents'])['parents'][0]['name']
#         lookPass_list = sg.find_one('Asset', [['project', 'name_is', 'pws'], ['code', 'is', parent_asset]], ['sg_look_passes_1'])['sg_look_passes_1']
#         if lookPass_list:
#             for l in lookPass_list:
#                 asm_pass_info.setdefault('bodyPass',[]).append(l['name'])
#     asm_pass_info.setdefault('bodyPass',[]).append('default')
#     return asm_pass_info

# for a in asm_list:
#     print a
#     print get_asm_pass_info(a)

#     /mnt/proj/projects/pws/shot/c90/c90520/cam/publish/c90520.cam.camera.v006/c90520_cam_anim.ma

# import pipeline.ShotGunProj as csgp
# def get_asm_info(asset):
#     # sg = Connection('get_project_info').get_sg()
#     proj = sg.find_one('Project', [['name', 'is', 'pws']], [])
#     asset_sg = sg.find_one('Asset', [['project', 'is', proj], ['code', 'is', asset]], ['code', 'parents','sg_remark'])
#     if asset_sg['sg_remark']:
#         return eval(asset_sg['sg_remark'])
#     else:
#         return {'bodyPass': ['default'],'bodyColor': ['min: 0.0', 'max: 1.0'],'clothPass': ['default'],'clothColor': ['min: 0.0', 'max: 1.0']}

# def convert_pass_info(chr_name,pass_dict,proj='pws'):
#     shotgunProj=csgp.ShotGunProj(proj)
#     asset_parents=shotgunProj.get_srf_parent_asset_list(chr_name)
#     print asset_parents
#     pass_dict['set']['bodyPass']=(pass_dict['set']['bodyPass'],[])
#     pass_dict['set']['clothPass']=(pass_dict['set']['clothPass'],[])
#     for asset in asset_parents:
#         tag_list=shotgunProj.get_info_from_name(asset,'tag_list')
#         if tag_list and 'body' in tag_list:
#             pass_dict['set']['bodyPass'][1].append(asset)
#         else:
#             pass_dict['set']['clothPass'][1].append(asset)
#     return pass_dict



# asset = 'citizen_rich_woman_thin_a'
# pass_dict = get_asm_info(asset)
# print pass_dict
# print convert_pass_info(asset,pass_dict)
# {'bodyPass': ['default','makeup'],'clothPass': ['default'],}
# {'clothPass': ['citizen_rich_woman_norm', 'default'], 'bodyPass': ['woman_norm', 'default']}


# {'set': {'bodyColor': 0.28353, 'clothColor': 0, 'clothPass': ('default', ['soldier_norm', 'soldier_thin']), 'bodyPass': ('default', ['man_norm', 'man_thin'])}, 'cfx': {'beard_toggle': 0, 'brow_toggle': 2}}
# import sys
# sys.path.append('/mnt/utility/toolset/applications/katana/Scripts')
# lay_xml = ['/tmp/jiayi_shot_xml/c90040.xml', '/mnt/proj/projects/pws/shot/c90/c90040/ani/publish/c90040.ani.animation.v027/scene_graph_xml/c90040.xml']
# import common.lcProdProj as lcpp
# import production.pipeline.asset_node_base as ppan
# xml_file = lay_xml[0]
# pnode = ppan.AssetNodeBase(xml_file)
# all_assets = pnode.get_all_asset_children()

# for ast in all_assets:

#     print ast.name.split('.')[-1]

# ppInfo = lcpp.lcProdProj()
# ppInfo.setProj('pws')
# lay_xml = ppInfo.lcGetLayXml('c90040')
# print lay_xml
# xml_file = lay_xml[0]
# print xml_file

# value = '1.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0'
# value_list = value.split(' ')
# new_list = []
# print value_list
# for v in value_list:
#     new_list.append(float(v))
# print new_list
# string = '060  160  254  250  330  347   380  510  620  630  670   680  700  770  775  790  795  815  820'
# s_list = string.split('  ')
# n_list = []
# for s in s_list:
#     n_list.append('f30'+s)
# print n_list

# import os
# from lxml import etree as ET
# shot_list = ['f30060', 'f30160', 'f30245', 'f30250', 'f30330', 'f30347', 'f30380', 'f30510', 'f30620', 'f30630', 'f30670', 'f30680', 'f30700', 'f30770', 'f30775', 'f30790', 'f30795', 'f30815', 'f30820']

# # path = '/mnt/proj/projects/pws/shot/f30/%s/lay/publish/f30060.lay.rough_layout.v047/scene_graph_xml/f30060.xml'
# for shot in shot_list:
#     dir_path = '/mnt/proj/projects/pws/shot/f30/%s/lay/publish/'%shot
#     lay_list=os.listdir(dir_path)
#     lay_list.sort()
#     latest_version = lay_list[-1]
#     xml = dir_path + latest_version + '/scene_graph_xml/%s.xml'%shot
#     # print os.path.isfile(file_path)
#     # print file_path
#     tree = ET.parse(xml)
#     root = tree.getroot()
#     inst_nodes=root.xpath('//instance')
#     for i in inst_nodes:
#         # if i.attrib['type'] == 'reference' and i.attrib['name'] == 'f30_river.river_asb.river_env' :
#         if i.attrib['type'] == 'reference' and 'river_env' in i.attrib['name']:
#             wform = i.xpath('./wform')[0].attrib['value']
#             wform_list = wform.split(' ')
#             if wform_list[-4] == '0.0' and wform_list[-3] == '0.0' and wform_list[-2] == '0.0':
#                 print wform
			# print wform_list[-4] + " " + wform_list[-3] + " " + wform_list[-2]

# shot 
# f30630
# f30700
# f30380
# f30815
# f30330
# f30510
# f30250
# f30620
# f30245
# f30347
# f30060
# f30680
# f30670
# f30775
# f30790
# f30160
# f30795
# f30820

# shot = 'f20360'
# print shot[0:3]
# versions = sg.find('Version',[['project', 'name_is', 'pws'],['entity.Shot.code','is',shot],['code','contains','ani']],['sg_version_type'])
# for v in versions:
#     print v['sg_version_type']
#     if v['sg_version_type'] == 'Downstream':
#         print 'YES'
# print version

# in_folder = '/mnt/output/projects/pws/shot/h20/h20080/plt/output/h20080.plt.baoqing_store_outside_terrain_plant.v001/cache/baoqing_store_outside_terrain/xgen/collections'
# latest_folder = 'output'.join(in_folder.split('output')[:-1])
# print latest_folder
# import os
# in_folder = '/mnt/output/projects/pws/shot/h20/h20080/plt/output/h20080.plt.baoqing_store_outside_terrain_plant.v001/cache/baoqing_store_outside_terrain/xgen/collections'
# output_folder = 'output'.join(in_folder.split('output')[:-1]) + 'output/'
# ver_list = []
# print output_folder
# file_list=os.listdir(output_folder)
# for f in file_list:
#     if 'v00' in f:
#         ver_list.append(f)
# ver_list.sort()
# latest = ver_list[-1]
# latest_folder = output_folder + latest
# print latest_folder 

# /mnt/output/projects/pws/shot/h20/h20080/plt/output/h20080.plt.baoqing_store_outside_terrain_plant.v001/cache/baoqing_store_outside_terrain/xgen/collections
# /mnt/output/projects/pws/shot/h20/h20080/plt/output/h20080.plt.baoqing_store_outside_terrain_plant.v002/cache/baoqing_store_outside_terrain/xgen/collections
# import glob
# to_folder = '/mnt/output/projects/pws/shot/h20/h20080/plt/output/h20080.plt.baoqing_store_outside_terrain_plant.v001/cache/baoqing_store_outside_terrain/xgen/collections'
# # print to_folder.split['cache'][-2]
# to_folder_real = to_folder.split('cache')[-2]
# # print to_folder_real
# xml_f='cache/*/*/*/*/*/*/*.xml'
# xg_f='cache/*/*/*/*/*.xgen'
# all_files=[]
# all_files.extend(glob.glob(to_folder_real+xml_f))
# xgen_files=glob.glob(to_folder_real+xg_f)
# # for f in all_files:
# #     # print f
# #     if to_folder in f:
# #         print '.....................'
# #         print f
# for x in xgen_files:
#     if to_folder in x:
#         print x
# print all_files
# import os
# in_folder = '/mnt/output/projects/pws/shot/h20/h20080/plt/output/h20080.plt.baoqing_store_outside_terrain_plant.v001/cache/baoqing_store_outside_terrain/xgen/collections'
# def get_to_folder(in_folder):
#     folder_cache = 'output'.join(in_folder.split('output')[:-1]) + 'output'
#     ver_list = []
#     for v in os.listdir(folder_cache):
#         if 'plt.' in v:
#             ver_list.append(v)
#     ver_list.sort()
#     # print ver_list
#     latest_version = ver_list[-1]
#     in_folder_list = in_folder.split('/')
#     for i in in_folder_list:
#         if '.plt.' in i:
#             curren_version = i
#             break 
#     to_folder = in_folder.replace(curren_version,ver_list[-1])
#     print in_folder
#     print to_folder

# get_to_folder(in_folder)
# import sqlite3
# import getpass

# def getUserFullFromDB(username=None):
#     cx = sqlite3.connect('/mnt/public/Share/chengshun/db/user.db')
#     cu = cx.cursor()
#     if username:
#         current_user = username
#     else:
#         current_user = getpass.getuser()
#     print current_user
#     sql = 'select * from user where wrong_name="%s"' % current_user
#     print sql
#     r = cu.execute(sql)
#     m_list = r.fetchall()
#     print m_list
#     if len(m_list) == 0:
#         print 'Do not find user! Please contact chengshun.'
#         result = None
#     elif len(m_list) == 1:
#         result = {'full_name': str(m_list[0][1]), 'password': str(
#             m_list[0][3]), 'department': str(m_list[0][2])}
#     else:
#         print 'More than one user found! Please contact chengshun.'
#         result = None
#     cu.close()
#     cx.close()
#     return result

# print getUserFullFromDB('yiming')
# import re
# # mayaFile = '/mnt/work/projects/pws/shot/f40/f40080/cfx/task/maya/f40080.cfx.cloth.v001.ma.lock'
# # re_group=re.search('/projects/.{3}/', mayaFile).group()
# # tst = str(re_group[-4:-1]).upper()
# # tst_l = str(re_group[-4:-1])
# # print tst
# # print tst_l
# name = 'h30060'
# # name = 'fer_a'
# print re.match(r'^[a-z]\d{5}',name)
# import os
# unlock_path = '/mnt/work/projects/pws/asset/flg/fern_d/mod/task'
# cmd_str = 'chmod -R 777 %s' %unlock_path
# print os.system(cmd_str)
# local indexvalue = Interface.GetAttr('geometry.poly.vertexList')
# local uv_num = Interface.GetAttr('geometry.arbitrary.st.indexedValue'):getNumberOfValues()
# print (uv_num)
# uv_value = {}
# for i = 1,uv_num do
#  uv_value[i] = 0
# end
# Interface.SetAttr('geometry.arbitrary.st_efx.scope',StringAttribute('vertex'))
# Interface.SetAttr('geometry.arbitrary.st_efx.inputType',StringAttribute('point2'))
# Interface.SetAttr('geometry.arbitrary.st_efx.index', indexvalue)
# Interface.SetAttr('geometry.arbitrary.st_efx.indexedValue',DoubleAttribute(uv_value, 2))

# def tst_args(usr,msg,depends=1,job_name = 'sdhf',proj='None'):
#     print usr
#     print msg
#     print depends
#     print job_name
#     print proj

# tst_args('jiayi','what',depends=2,proj='pws')
# 759    class ShotEditor:
# 1111    def set_assets_postion():
#             send_msg
# /mnt/utility/git_publish/lcatools/log
# import os
# import sys
# sys.path.append('/mnt/utility/toolset/applications/katana/Scripts')
# import common.lcProdProj as lcpp
# ppinfo=lcpp.lcProdProj()
# ppinfo.setProj('cat')

# def get_lgt_katana_full_path(shot,version):
#     path=ppinfo.getShotWorkFolder(shot,dep='lgt',progress='task',software='katana')
#     katana_file=os.path.join(path,shot+'.lgt.lighting.'+version+'.katana')
#     if os.path.isfile(katana_file):
#         return katana_file

# import sys
# file_path = '/home/jiayi/Desktop/note.txt'
# shotVersion = {}
# f = open(file_path, "r+")
# line = f.readline()
# while line:
#     line = f.readline()
#     line = line.split('\n')[0]
#     line = line.split('   ')[0]
#     if 'i50' in line:
#         shot = line.split('  ')[0]
#         version = line.split('  ')[1]
#         # print shot + '  ' + version
#         shotVersion[shot] = version

# # print shotVersion
# shot_list = shotVersion.keys()
# shot_list.sort()
# for s in shot_list:
#     filePath = get_lgt_katana_full_path(s,shotVersion[s])
#     cmd = '/mnt/work/software/k2/katana2.1v1/ktoa --script=/mnt/public/Share/zhaojiayi/code/muster/katana_scan_cat.py %s'%filePath
#     # print filePath
# #     print cmd
# def dic_j():
#     job = {
#         'url' : '10.0.3.11',
#         'department' : 'sdfgks;lg',
#         'name' : '-',
#         'file' : 'filepath,',
#         'f_start' :'fstart'
#         }
#     p_j(job)

# def p_j(job):
#     job.get('project','')

# print dic_j()
# import os
# def get_asset(proj,type):
#     type_folder = '/mnt/proj/projects/%s/asset/%s'%(proj,type)
#     print os.listdir(type_folder)
# get_asset

# filepath = '/mnt/work/projects/pws/shot/c90/c90010/efx/task'
# if 'efxcache' in filepath:
#    proj = filepath.split("/")[3]
# else:
#    proj = filepath.split("/")[4]

# print proj
# file_path = '/mnt/work/projects/cat/shot/i50/i50020/lgt/task/katana/i50020.lgt.lighting.v014.katana.txt'

# def move_jobs_to_ucloud(shot):
#     session_u = connection_farmer(farm_ip)
#     for muster_dispacher in muster_dispacher_list:
#         print 'search jobs in', muster_dispacher
#         print '-' * 50
#         count = 0
#         conn = MySQLdb.connect(
#             host=muster_dispacher, user='xiaom', passwd='000000', db='muster', cursorclass=MySQLdb.cursors.DictCursor)
#         cu = conn.cursor()
#         sql = 'select * from db_jobs where engine in ("953", "950") and instr(job_name, "%s") and job_pool = "ucloud" and is_paused=0' % shot
#         # print sql
#         cu.execute(sql)
#         r = cu.fetchall()
#         if not r:
#             print 'damn, found nothing...'
#         else:
#             session = connection_farmer(muster_dispacher)
#             node_names = []
#             job = MClientAPI.MJob()
#             for i in r:
#                 print i['job_name'], i['id']
#                 # node_names.append(i['job_name'].split('-')[1])
#                 MClientAPI.GetJob(session, job, i['id'])
#                 owner = job.getOwner()
#                 sql = 'select * from db_jobs_data where job_id = %d and key_name = "job_file"' % i[
#                     'id']
#                 cu.execute(sql)
#                 r = cu.fetchall()
#                 if len(r) == 1:
#                     count += 1
#                     if 'projcache' in r[0]['key_value']:
#                         ucloud_katana_file = os.path.dirname(os.path.dirname(r[0]['key_value'].replace(
#                             'projcache', 'work'))) + '/' + '.'.join(os.path.basename(r[0]['key_value']).split('.')[1:])
#                         job.attributeSetString('job_file', ucloud_katana_file)
#                         job.setTemplateID(950)
#                         job.setIncludedPools('')
#                         job.setLocked(0)
#                         job.setDepends('')
#                         job.setPriority(5)
#                         job.setMaximumNodes(50)
#                         err = MClientAPI.ActionSendJob(session_u, job)
#                         new_id = job.getJobId()
#                         MClientAPI.JobActionSetOwner(session_u, new_id, owner)
#                         total_frames = job.attributeGetInt('total_frames')
#                         #MClientAPI.ChunkActionSetCompleted(
#                         #    session_u, new_id, range(1, total_frames))
#                         MClientAPI.JobActionLock(session, i['id'])

#             MClientAPI.Disconnect(session)
#             MClientAPI.Disconnect(session_u)
#         cu.close()
#         conn.close()
#         print '-' * 50
#         print 'count: %d' % count
#     MClientAPI.Disconnect(session_u)
# def tst(v):
#     if v == 1:
#         return True
#     elif v == 0:
#         return False
# r = tst(0)
# if r:
#     print r
# else :
#     print '...'
#     print r
# import logging

# def tst_log():
#     logger = logging.getLogger('Tst_Logging')
#     logger.setLevel(logging.DEBUG)
#     ch = logging.StreamHandler()
#     ch.setLevel(logging.DEBUG)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     ch.setFormatter(formatter)
#     logger.addHandler(ch)
#     logger.info('************[ssh_cmd] start*************')
#     logger.info('connecting to ' + 'Tst_Logging')

# tst_log()

# import os,sys
# sys.path.append('/mnt/utility/toolset/applications/katana/Scripts')
# sys.path.append('/mnt/utility/toolset/lib')
# from lxml import etree as ET
# from production import shotgun_connection
# import traceback
# import re
# sg = shotgun_connection.Connection('get_shot_info').get_sg()

# assetEntity=sg.find_one('Asset',[['project','name_is','pws'],["code",'is','diaper']],['sg_versions'])
# list_1 = sg.find('Asset',[['project','name_is','pws'],["code",'is','diaper']],['sg_versions'])
# print assetEntity
# print list_1
# import sys
# sys.path.insert(0,'/mnt/public/Share/zhaojiayi/gitrepo/lcatools/tools/render/muster_functions/')

# from muster_connection import connection_farmer
# import MySQLdb
# import MySQLdb.cursors
# import MClientAPI
# import os

# def setChunkCompleted(shot):
#     aliyun_muster = '39.104.78.122'
#     count = 0
#     conn = MySQLdb.connect(
#         host=aliyun_muster, user='xiaom', passwd='000000', db='muster', cursorclass=MySQLdb.cursors.DictCursor)
#     cu = conn.cursor()
#     sql = 'select * from db_jobs where engine in ("953", "950") and instr(job_name, "%s") and is_paused=0 and is_locked=0' % shot
#     cu.execute(sql)
#     r = cu.fetchall()
#     if not r:
#         print 'damn, found nothing...'
#     else:
#         session_ali = connection_farmer(aliyun_muster)
#         node_names = []
#         job = MClientAPI.MJob()
#         for i in r:
#             print i['job_name'], i['id']
#             MClientAPI.GetJob(session_ali, job, i['id'])
#             total_frames = job.attributeGetInt('total_frames')
#             print total_frames
#             MClientAPI.ChunkActionSetCompleted(session_ali, i['id'], range(1, total_frames-1))
#     MClientAPI.Disconnect(session_ali)
#     cu.close()
#     conn.close()

# setChunkCompleted('i50245')

# def create_completed_signal(shot):
#     signal_file = '/home/jiayi/Desktop/shot_signal.txt'
#     f = open(signal_file, 'a')
#     f.write(shot+'\n')
#     f.close()
# shot_list = ['i50010','i50005']
# for s in shot_list:
#     create_completed_signal(s)


# import os
# import sys
# sys.path.append('/mnt/utility/toolset/applications/katana/Scripts')
# import common.lcProdProj as lcpp
# import subprocess
# ppinfo=lcpp.lcProdProj()
# ppinfo.setProj('cat')
# sys.path.insert(0,'/mnt/public/Share/zhaojiayi/gitrepo/lcatools/tools/render/muster_functions/')
# from muster_connection import connection_farmer
# import MySQLdb
# import MySQLdb.cursors
# import MClientAPI

# def get_seq_job_version(seq):
#     shot_version_dict = {}
#     # muster_dispacher = '10.0.3.10'
#     muster_dispacher = '39.104.78.122'
#     session_tmp = connection_farmer(muster_dispacher)
#     count = 0
#     conn = MySQLdb.connect(
#         host=muster_dispacher, user='xiaom', passwd='000000', db='muster', cursorclass=MySQLdb.cursors.DictCursor)
#     cu = conn.cursor()
#     sql = 'select * from db_jobs where engine in ("953", "950") and instr(job_name, "%s") and is_paused=0 and is_locked=1' % seq
#     cu.execute(sql)
#     r = cu.fetchall()
#     if not r:
#         print 'damn, found nothing...'
#     else:
#         job = MClientAPI.MJob()
#         for i in r:
#             shot = (i['job_name']).split('.')[0]
#             version = (i['job_name']).split('.')[3]
#             if shot not in shot_version_dict.keys():
#                 shot_version_dict[shot] = version
#             # print i['job_name'], i['id']
#             # print shot
#             # print version
#         shot_list = shot_version_dict.keys()
#         shot_list.sort()
#         # print shot_list
#         return shot_version_dict

# def get_lgt_katana_full_path(shot,version):
#     path=ppinfo.getShotWorkFolder(shot,dep='lgt',progress='task',software='katana')
#     katana_file=os.path.join(path,shot+'.lgt.lighting.'+version+'.katana')
#     # if os.path.isfile(katana_file):
#     #     return katana_file
#     return katana_file

# def get_katana_txt(shot,version):
#     file_path = '/mnt/work/projects/cat/shot/%s/%s/lgt/task/katana/%s.lgt.lighting.%s.katana.txt'%(shot[0:3],shot,shot,version)
#     # print file_path
#     # return file_path
#     if os.path.isfile(file_path):
#         return file_path
#     else:
#         return 'Error'

# shotVersion = get_seq_job_version('r50')
# shot_list = shotVersion.keys()
# shot_list.sort()
# print shot_list
# for s in shot_list:
#     print get_katana_txt(s,shotVersion[s])
# print get_katana_txt('r50010','cat')
# print get_lgt_katana_full_path('r50010','cat')

# def get_chunks_status(shot):
#     aliyun_muster = '39.104.78.122'
#     conn = MySQLdb.connect(
#         host=aliyun_muster, user='xiaom', passwd='000000', db='muster', cursorclass=MySQLdb.cursors.DictCursor)
#     cu = conn.cursor()
#     sql = 'select * from db_jobs where engine in ("953", "950") and instr(job_name, "%s") and is_paused=0 and is_locked=0' % shot
#     cu.execute(sql)
#     r = cu.fetchall()
#     if not r:
#         print 'damn, found nothing...'
#     else:
#         session_ali = connection_farmer(aliyun_muster)
#         job = MClientAPI.MJob()
#         for i in r:
#             print i['job_name']
#             # MClientAPI.GetJob(session_ali, job, i['id'])
#             chunks = MClientAPI.MChunks()
#             MClientAPI.GetChunks(session_ali, i['id'], 4, chunks)
#             completed_chunk_ids = [chunk.getChunkId() for chunk in chunks]
#             print completed_chunk_ids

# import sys
# import os
# import shutil
# import sqlite3
# import random
# import datetime as dt
# global sg
# sg=None

# def init_shotgun():
#     global sg
#     if not sg:
#         from production.shotgun_connection import Connection
#         sg = Connection('get_project_info').get_sg()

# def uninit_shotgun():
#     if sg:sg.close()


# def get_people():
#     init_shotgun()
#     userEntity_cs = sg.find('HumanUser',[['login','is','chengshun']],['id','name'])[0]
#     print userEntity_cs
# #     userEntity=sg.find('Group',[['code','is','LGT_Leader']],['id','code'])[0]
#     userEntity_yy = sg.find('HumanUser',[['login','is','yangyang']],['id','name'])[0]
#     print userEntity_yy
	
#     uninit_shotgun()
# def get_frame_num():
	

# get_people()

# tst_list = []
# if not tst_list :
#     print '1'
# from production import shotgun_connection
# sg = shotgun_connection.Connection('get_shot_info').get_sg()
# proj = 'pws'
# shot = 'h90508'
# # shotEntity = sg.find('Shot',[['project','name_is',proj],['code', 'is', shot]],['sg_cut_in'],['sg_cut_out'])[0]
# shotEntity = sg.find('Shot',[['project','name_is',proj],['code', 'is', shot]],['sg_cut_in','sg_cut_out'])[0]
# print shotEntity
# print shotEntity['sg_cut_in']
# print shotEntity['sg_cut_out']

# print shotEntity


# def GetshotlistFromShotGun(proj,sequence,priority=None):
#     #sg_priority
#     if priority:
#         shotEntitylist=sg.find('Shot',[['project','name_is',proj],["sg_sequence",'name_is',sequence],["sg_priority",'is',priority],["sg_status_list","is_not","omt"]],['code'])
#     else:
#         shotEntitylist=sg.find('Shot',[['project','name_is',proj],["sg_sequence",'name_is',sequence],["sg_status_list","is_not","omt"]],['code'])
#     if shotEntitylist:
#         shotlist=[x["code"] for x  in shotEntitylist if x]
#         shotlist.sort()
#         return shotlist

# def GetLgtRigShotList(proj,sequence,priority):
#     shotlist = GetshotlistFromShotGun(proj,sequence,priority=priority)
#     lgtrig_list = []
	
#     for shot in shotlist:
#         filter_data=[
#             ['entity', 'name_is', shot],
#             ['entity', 'type_is', 'shot'],
#             ['step', 'name_is','lgt'],
#             ['project', 'name_is', proj],
#             ['content','is', 'lgt_rig']
#             ]
#         taskEntity = sg.find('Task', filter_data, ['id'])
#         if taskEntity:
#             lgtrig_list.append(shot)
#     lgtrig_list.sort()
#     return lgtrig_list

# print GetLgtRigShotList('pws','f20',' ')


# print __file__
# import production.CacheUtils.CacheXml as cx

# tst = '/mnt/proj/projects/pws/shot/b70/b70420/ani/publish/b70420.ani.animation.v026/b70420.ani.animation.v026.ma'
# print tst.split('/')[-8]
# print tst

# tst = ['snake_catcher', 'xiaobai_girl_snake']
# print tst
# print type(tst)
# tst_string = str(tst)
# print tst_string
# print type(tst_string)
# tst_s = eval(tst_string)
# print tst_s
# print type(tst_s)
# print len(tst)

# import datetime
# import os,sys
# sys.path.append('/mnt/utility/toolset/applications/katana/Scripts')
# sys.path.append('/mnt/utility/toolset/lib')
# # from lxml import etree as ET
# from production import shotgun_connection
# # import traceback
# sg = shotgun_connection.Connection('get_shot_info').get_sg()
# id_list = []
# # eventEntity=sg.find('EventLogEntry',[['id','is',83886661]],['meta','user','created_at','event_type'])
# # eventEntity=sg.find('EventLogEntry',[['user','name_is','Cai Nina'],['event_type','is','Shotgun_Asset_Change'],['created_at','is',datetime.datetime(2018,2,2, 14, 17, 56)]],['id'])
# # eventEntity_1=sg.find('EventLogEntry',[['user','name_is','Cai Nina'],['event_type','is','Shotgun_Asset_Change'],['created_at','is',datetime.datetime(2018,2,2, 14, 17, 55)]],['id'])
# # eventEntity_2=sg.find('EventLogEntry',[['user','name_is','Cai Nina'],['event_type','is','Shotgun_Asset_Change'],['created_at','is',datetime.datetime(2018,2,2, 14, 17, 57)]],['id'])
# # for e in eventEntity:
# #     id_list.append(e['id'])
# # for e in eventEntity_1:
# #     id_list.append(e['id'])
# # for e in eventEntity_2:
# #     id_list.append(e['id'])
# # eventEntity=sg.find('EventLogEntry',[['user','name_is','Cai Nina'],['event_type','is','Shotgun_Asset_Change'],['created_at','is',datetime.datetime(2018,2,2, 14, 17)]],['id'])

# # sg_info = sg.find_one(assetEntity['type'], [['id', 'is', assetEntity['id']]], ['sg_status_list'])
# # print assetEntity
# # print sg_info
# # print eventEntity
# # print id_list

# # print sg.schema_entity_read()

# # id_list = [83886552, 83886553, 83886555, 83886557, 83886559, 83886560, 83886562, 83886564, 83886566, 83886567, 83886569, 83886571, 83886572, 83886574, 83886576, 83886577, 83886579, 83886580, 83886582, 83886583, 83886585, 83886588, 83886590, 83886593, 83886595, 83886597, 83886598, 83886601, 83886602, 83886605, 83886607, 83886608, 83886611, 83886613, 83886614, 83886617, 83886618, 83886620, 83886621, 83886623, 83886624, 83886626, 83886627, 83886628, 83886630, 83886631, 83886632, 83886634, 83886635, 83886637, 83886639, 83886640, 83886642, 83886643, 83886645, 83886647, 83886648, 83886650, 83886651, 83886652, 83886653, 83886655, 83886656, 83886658, 83886659, 83886660, 83886662, 83886664, 83886665, 83886666, 83886668, 83886670, 83886672, 83886674, 83886675, 83886678, 83886680, 83886682, 83886683]
# id_list = [83886530, 83886531, 83886533, 83886534, 83886536, 83886539, 83886541, 83886544, 83886545, 83886546, 83886548, 83886549, 83886551, 83886552, 83886553, 83886555, 83886557, 83886559, 83886560, 83886562, 83886564, 83886566, 83886567, 83886569, 83886571, 83886572, 83886574, 83886576, 83886577, 83886579, 83886580, 83886582, 83886583, 83886585, 83886588, 83886590, 83886593, 83886595, 83886597, 83886598, 83886601, 83886602, 83886605, 83886607, 83886608, 83886611, 83886613, 83886614, 83886617, 83886618, 83886620, 83886621, 83886623, 83886624, 83886626, 83886627, 83886628, 83886630, 83886631, 83886632, 83886634, 83886635, 83886637, 83886639, 83886640, 83886642, 83886643, 83886645, 83886647, 83886648, 83886650, 83886651, 83886652, 83886653, 83886655, 83886656, 83886658, 83886659, 83886660, 83886662, 83886664, 83886665, 83886666, 83886668, 83886670, 83886672, 83886674, 83886675, 83886678, 83886680, 83886682, 83886683, 83886684, 83886686, 83886688, 83886689, 83886691, 83886693, 83886694, 83886696]
# id_list.sort()
# # sg.update('Asset', assetId, {'sg_remark':info_string})
# # print id_list
# # print len(id_list)
# for id in id_list:
#     eventEntity=sg.find('EventLogEntry',[['id','is',id]],['meta','user','event_type','entity'])[0]
#     asset_Id = eventEntity['entity']['id']
#     asset_name = eventEntity['entity']['name']
#     old_status = eventEntity['meta']['old_value']
#     new_status = eventEntity['meta']['new_value']
#     # print asset_Id, assetName, old_status, new_value
#     # print asset_Id
#     # print asset_name
#     # print old_status
#     # print new_status
#     # assetEntity = sg.find_one('Asset',[['code','name_is',id]],['sg_status_list'])
#     # assetEntity=sg.find('Asset',[['project','name_is','pws'],["code",'is','taoist_priest_little']],['id'])[-1]
#     assetEntity=sg.find('Asset',[['project','name_is','pws'],["code",'is',asset_name]],['sg_status_list'])[-1]['sg_status_list']
#     # print asset_name
#     # print asset_name
#     # print old_status
#     # print assetEntity
#     if assetEntity != old_status:
#         print asset_name
#         print assetEntity
#         print old_status
#     # if assetEntity == None:
#     #     print asset_name
#     #     print new_status
#     #     sg.update('Asset', asset_Id, {'sg_status_list':old_status})
#     # sg.update('Asset', asset_Id, {'sg_status_list':new_status})
#     # # if 
#     # if new_status != None:
#     #     print '...................'
#     # else:
#     #     print ',,'

# # sg.update('Asset', 10927, {'sg_status_list':'rdy'})

# /mnt/public/Share/zhaojiayi/gitrepo/lcatools/tools/gene/sgXmlParser/sgXml_parser.py


# ma_path = '/mnt/proj/projects/pws/shot/i20/i20200/flo/publish/i20200.flo.final_layout.v001/i20200.flo.final_layout.v001.ma'
# # ma_path = '/mnt/proj/projects/pws/shot/i20/i20240/flo/publish/i20240.flo.final_layout.v001/i20240.flo.final_layout.v001.ma'
# with open(ma_path) as f:
#     data = f.readlines()
# if 'select -ne :defaultResolution;\n' in data:
#     print 'yes'
# ln = data.index('select -ne :defaultResolution;\n')
# print ln
# w = int(data[ln+1].split()[2][:-1])
# # w_tst = data[ln+1].split()[2][:-1]
# # print data[ln+1]
# h = int(data[ln+2].split()[2][:-1])
# # h_tst = data[ln+2].split()[2][:-1]
# # print data[ln+2]
# print w
# print h
# # print w_tst
# # print h_tst
# import traceback
# import production.pipeline.color_log as ppcl
# lca_logger=ppcl.init_logger('TST ERROR')
# try:
#     with open(tst_file) as f:
#         data = f.readlines()
# except:
#     lca_logger.exception('Failed to open file')
# lca_logger.info('continue')

# cacheDict = [{'chr': ['axuan', 'xiaobai_girl'], 'prp': ['flying_parasol', 'snake_catcher']}, {'flg': ['maple_tree_a1', 'maple_tree_a', 'maple_tree_b'], 'env': ['c90_snake_wood_area.snake_wood_area.snake_wood_area_env']}]
# for va in cacheDict[0].values():
#     print va
# from pxr import Usd, UsdGeom

# stage = Usd.Stage.CreateNew('HelloWorld.usda')
# xfromPrim = UsdGeom.Xform.Define(stage,'/hello')
# spherePrim = UsdGeom.Sphere.Define(stage,'/hello/world')
# stage.GetRootLayer().Save()

# import os
# import re
# import sys
# import copy
# import itertools
# import uuid
# import copy
# import itertools
# import pprint
# import openpyxl
# import maya.cmds as cmds
# import string
# sys.path.append('D:\\zhaojiayi\\Documents\\coco')
# from cocoPipeline.lib.python.shotLib import getShotMessage
# from cocoPipeline.lib.python.assetLib import asset
# from cocoPipeline.bin.assetInShot import Function
# from cocoPipeline.lib.python.shotLib import castingLib
# from cocoPipeline.lib.python.assetLib import asset
# reload(getShotMessage)
# reload(asset)
# reload(castingLib)
# import cocoPipeline.lib.python.ftrackLib.ftrackSession as ftrackSession
# reload(ftrackSession)



# def get_shotinfo(project,shot,sets=False):
#   shotinfo_list = castingLib.casting_from_excl(project,shot,sets)
#   return shotinfo_list

# def get_shot_asset_srf(proj,shot,sets=False):
#   shotinfo_list = get_shotinfo(project,shot)
#   srfpath_list = []
#   for shotinfo in shotinfo_list:
#       srfpath = "Z:\\%s\\assets\\char\\%s\\surface\\look\\%s\\ok\\%s_look_%s.ma"%(proj,shotinfo.asset_id,shotinfo.var['look'],shotinfo.asset_id,shotinfo.var['look'])
#       if os.path.isfile(srfpath):
#           srfpath_list.append(srfpath)
#   return srfpath_list

# def get_shot_ani(proj,shot):
#   shotinfo_list = get_shotinfo(proj,shot)
#   anipath_list = []
#   for shotinfo in shotinfo_list:
#       anipath = "Z:\\%s\\shots\\ep001\\%s\\%s\\cache\\geocache\\%s\\%s_geocache_%s.abc"%(proj,shot[0:3],shot,shotinfo.asset_name,shot,shotinfo.asset_name)
#       if os.path.isfile(anipath):
#           anipath_list.append(anipath)
#   return anipath_list

# def get_cam_abc(proj,shot):
#   campath = "Z:\\%s\\shots\\ep001\\%s\\%s\\cache\\camcache\\cam\\%s_camcache_cam.abc"%(proj,shot[0:3],shot,shot)
#   if os.path.isfile(campath):
#       return campath
#   else:
#       print 'No such file'
#       return None,None

# def get_shot_sets(proj,shot):
#   shotinfo_list = get_shotinfo(project,shot,sets=True)
#   sets_list = []
#   for shotinfo in shotinfo_list:
#       asset_id = shotinfo.asset_id
#       if asset_id[0] == 's':
#           sets_list.append(shotinfo)
#   return sets_list

# def get_shot_time(proj,shot):
#   xlsx_path = "Z:\\%s\\database\\casting\\main.xlsx"%proj
#   shotinfo = Function.getShot(xlsx_path, shot)
#   timeRange = shotinfo['frameRange']
#   return timeRange

# def auto_copy_uv(asset_name):
#   d_uvset = 'map1'
#   mesh_list =  cmds.listRelatives('%s:Root_grp'%asset_name,ad= True,type= ['geometryShape'])
#   cmds.listRelatives(['%s:Root_grp'%asset_name],c=True,type= 'geometryShape')
#   for mesh in mesh_list:
#       if not cmds.polyEvaluate(mesh,uvcoord = True):
#           print "%s has No Uvs"%mesh
#       else:
#           cmds.select(mesh)
#           uvsets_list = cmds.polyUVSet( query=True, currentUVSet=True)
#           if uvsets_list:
#               if d_uvset not in uvsets_list:
#                   cmds.polyCopyUV(mesh,uvSetNameInput = uvsets_list[0],uvSetName= d_uvset)

# def check_errorUv_asset():
#   char_path = 'Z:\\smxm\\assets\\char'
#   asset_list = os.listdir(char_path)
#   print asset_list
#   srfpathList = []
#   for asset in asset_list:
#       srf_path = 'Z:\\smxm\\assets\\char\\%s\\surface\\look\\main\\ok\\%s_look_main.ma'%(asset,asset)
#       if os.path.isfile(srf_path):
#           srfpathList.append(srf_path)
#           cmds.file(srf_path,r = True,type = 'mayaAscii',namespace = asset)
#           print '--------------------------------------------'
#           auto_copy_uv(asset)
#           print '----------------------------------------------'

# assetName = 'c002001xiongmaoc'
# print assetName[7:-1]





# def get_proj_fps(proj):
#   session = ftrackSession.createSession()
#   projects = session.query('Project where name is "{0}"'.format(proj)).first()
#   GetFps = projects['custom_attributes']['fps']
#   time_dict = {
#   15:"gama",
#   24:"film",
#   25:"pal",
#   30:"ntsc",
#   48:"show",
#   50:"half",
#   60:"ntscf"
#   }
#   time_str = time_dict[GetFps]
#   return time_str

# def get_shot_info(proj,shot):
#   xlsx_path = "Z:\\%s\\database\\casting\\main.xlsx"%proj
#   print xlsx_path
#   # xlsx_path = "C:\\Users\\zhaojiayi\\Desktop\\tstfile\\main.xlsx"
#   shotinfo = Function.getShot(xlsx_path, shot)
#   return shotinfo

# def get_shot_assets(type,shotinfo):
#   info_list = shotinfo[type]
#   typeAssetlist = []
#   for info in info_list:
#       assetName = info['name'] + (str(info['id']) if info['id'] else '')
#       typeAssetlist.append(assetName)
#   return typeAssetlist

# def get_asset_outline(proj,shot):
#   shotinfo = get_shot_info(proj,shot)
#   prp_list = get_shot_assets('prop',shotinfo)
#   char_list = get_shot_assets('char',shotinfo)
#   set_list = get_shot_assets('set',shotinfo)
#   for prp in prp_list:
#       print 'root/prp/%s'%prp
#   for char in char_list:
#       print 'root/char/%s'%char
#   for sets in set_list:
#       print 'root/set/%s'%char

# def ref_asset_srf(proj,shot,assetType,asset_name,look):
#   # if assetType == 'set':
#   #   setPath = 'Z:\\%s\\shots\\ep001\\%s\\%s\\set\\scene\\ok\\%s_scene_ok.ma'%(proj,shot[0:3],shot,shot)
#   #   if os.path.isfile(setPath):
#   #       cmds.file(setPath,r = True,type = 'mayaAscii',gr =True,gn = 'set')
#   #       # file -r -type "mayaAscii" -gr  -ignoreVersion -gn "tsts" -loadReferenceDepth "all" -mergeNamespacesOnClash false -namespace "dhd067_scene_ok" 
#   #       print '---------------------------------'
#   #       print setPath
#   #       # parent_group = '%s_%s'%(asset_name,assetType)
#   #       # cmds.group( em=True, name=parent_group )
#   #       # cmds.parent('%s:Root_grp'%asset_name,parent_group)
#   if assetType != 'set':
#       assetName = asset_name.rstrip(string.digits)
#       srfpath = "Z:\\%s\\assets\\%s\\%s\\surface\\look\\%s\\ok\\%s_look_%s.ma"%(proj,assetType,assetName,look,assetName,look)
#       if os.path.isfile(srfpath):
#           cmds.file(srfpath,r = True,type = 'mayaAscii',namespace = asset_name)
#           parent_group = '%s_%s'%(asset_name,assetType) 
#           cmds.group( em=True, name=parent_group )
#           cmds.parent('%s:Root_grp'%asset_name,parent_group)

# def ref_asset_set(proj,shot):
#   setPath = 'Z:\\%s\\shots\\ep001\\%s\\%s\\set\\scene\\ok\\%s_scene_ok.ma'%(proj,shot[0:3],shot,shot)
#   if os.path.isfile(setPath):
#       cmds.file(setPath,r = True,type = 'mayaAscii',gr =True,gn = 'set')
#       if not cmds.objExists('|root'):
#           cmds.group(em=True,name = 'root')
#       cmds.parent('set','root')

# def group_type_asset(assetType,assetName):
#   if assetType != 'set':
#       if cmds.objExists('%s_%s'%(assetName,assetType)):
#           if not cmds.objExists('|root'):
#               cmds.group(em=True,name = 'root')
#           if not cmds.objExists('|root|%s'%assetType):
#               cmds.group(em=True,name = assetType)
#               cmds.parent(assetType,'root')
#           cmds.parent('%s_%s'%(assetName,assetType),assetType)

# def merge_cache(proj,shot,assetName,hair=False):
#   anipath = "Z:\\%s\\shots\\ep001\\%s\\%s\\cache\\geocache\\%s\\%s_geocache_%s.abc"%(proj,shot[0:3],shot,assetName,shot,assetName)
#   cmds.AbcImport(anipath, mode= True, connect ='%s:Root_grp' %(assetName))
#   if hair:
#       hairPath = 'Z:/%s/shots/ep001/%s/%s/cache/haircache/%s/geom/{%s}_geom.abc'%(proj,shot[0:3],shot,assetName,assetName)
#       if os.path.isfile(hairPath):
#           cmds.AbcImport(hairPath, mode= True, connect ='%s:Root_grp' %(assetName))

# def ref_cam_cache(proj,shot):
#   cam_path = get_cam_abc(proj,shot)
#   if cam_path:
#       namespace_cam = '%s_cam'%shot
#       cmds.file(cam_path,type = "Alembic",r= True,namespace = namespace_cam)
#   else:
#       print "No such camera File"

# def set_time_range(proj,shot):
#   fps = get_proj_fps(proj)
#   timeRange = get_shot_time(proj,shot)
#   cmds.currentUnit(time=fps)
#   cmds.playbackOptions(minTime=int(timeRange[0])-2)
#   cmds.playbackOptions(maxTime=int(timeRange[1])+2)

# # dhd067
# # if __name__ == "__main__":
# #     app = QtWidgets.QApplication(sys.argv)
# #     app.setQuitOnLastWindowClosed(False)
# #     ex = MainSystem()
# #     ex.hide()
# #     sys.exit(app.exec_())
#   # proj = 'smxm'
#   # shot = 'xuz003'
#   # shotinfo = get_shot_info(proj,shot)


# # 'Z:/smxm/shots/ep001/xuz/xuz003/cache/haircache/c001001xiongmaox/geom/'
# # timeRange = get_shot_time(proj,shot)
# # count = 1 
# # shotinfo_list = get_shotinfo(proj,shot)
# # for shotinfo in shotinfo_list:
# #     count -= 1
# #     srfpath = "Z:\\%s\\assets\\char\\%s\\surface\\look\\%s\\ok\\%s_look_%s.ma"%(proj,shotinfo.asset_id,shotinfo.var['look'],shotinfo.asset_id,shotinfo.var['look'])
# #     anipath = "Z:\\%s\\shots\\ep001\\%s\\%s\\cache\\geocache\\%s\\%s_geocache_%s.abc"%(proj,shot[0:3],shot,shotinfo.asset_name,shot,shotinfo.asset_name)
# #     if os.path.isfile(srfpath) and os.path.isfile(anipath):
# #         cmds.file(srfpath,r = True,type = 'mayaAscii',namespace = shotinfo.asset_name)
# #         cmds.reorder( '%s:Root_grp'%shotinfo.asset_name, r=count )
# #         cmds.AbcImport(anipath, mode= True, connect ='%s:Root_grp' %(shotinfo.asset_name))
# #         auto_copy_uv(shotinfo.asset_name)
# # cam_path = get_cam_abc(proj,shot)
# # if cam_path:
# #     cmds.file(cam_path,type = "Alembic",r= True)
# # else:
# #     print "No such camera File"
# # fps = get_proj_fps(proj)
# # cmds.currentUnit(time=fps)
# # cmds.playbackOptions(minTime=int(timeRange[0])-2)
# # cmds.playbackOptions(maxTime=int(timeRange[1])+2)

# # import os
# # import glob
# # projPath = 'Z:\\smxm\\shots\\ep001'
# # print os.listdir(projPath)
# # print os.path.dirname(projPath)

# # # "Z:\\smxm\\shots\\ep001\\ccj\\ccj004\\set\\"
# # searchPath = 'Z:\\smxm\\shots\\ep001\\ccj\\ccj004\\set\\'

# # get_shot_info(proj,shot)
# # mel.eval('group -n -c001001xiongmaox c001001xiongmaox_look_main:Root_grp')
# # parent c007002xniujiaol_char char

# # 'Z:\smxm\shots\ep001\xuz\xuz003\set\scene\ok'
# # import glob

# # # for fileName in glob.glob( r'Z:\\smxm\\shots\\ep001\\*\\set\\scene\\ok\\*.abc'):
# # # for fileName in glob.glob(r"Z:/smxm/shots/ep001/*/*/cache/geocache/*/*.abc"):
# # #   print fileName
# # for fileName in glob.glob(r"Z:/smxm/shots/ep001/*/*/set/scene/ok/*.abc"):
# #     print fileName

# # f= glob.iglob(r'../*.py')
# # print f
# # "Z:\smxm\shots\ep001\xuz\xuz003\cache\geocache\c011001zhushu\xuz003_geocache_c011001zhushu.abc"
# import os
# import maya.OpenMayaUI as omui
# # import shiboken2 as shiboken
# from Qt import QtWidgets, QtCore,QtGui
# from PySide2 import QtWidgets, QtCore 
# try:
#     from PySide2.QtWidgets import *
# except:
#     from PyQt5.QtWidgets import *
	
# from Qt.QtCore import *
# from Qt.QtGui import *
# from Qt.QtWidgets import *

# import time
# import threading

# class Form(QtWidgets.QMainWindow):

#   _signal = QtCore.Signal(str,str)

#   def __init__(self,parent=None):
#       super(Form,self).__init__(parent)
#       self.initUI()

#   def initUI(self):
#       # self.addLabel()
#       # self.addLine()
#       self.setInitdata()
#       self.addcombBox()
#       # self.addtextEdit()
#       self.addpushButton()
#       self.currentTime = time.time()
#       self.setSignal()
#       self.setWindowTitle("Light Shot Maker")
#       self.slot_initCurrentTask(0)
#       self.resize(500,80)
#       self.move(500,200)
#       self.run = False
#       # self.show()

#   def setInitdata(self):
#       self.serverRoot = os.environ['SERVER_ROOT'].capitalize()
#       self.currentTime = time.time()


#   def addLabel(self):
#       labelProj = QLabel('PROJECT',self)
#       labelProj.resize = (100,100)
#       labelProj.move(20,10)
#       labelSeq = QLabel('SEQ',self)
#       labelSeq.resize = (100,100)
#       labelSeq.move(20,30)
#       labelShot = QLabel('SHOT',self)
#       labelShot.resize = (100,100)
#       labelShot.move(20,50)

#   def addLine(self):
#       lineProj = QFrame(self)
#       lineProj.setGeometry(QRect(65,9,10,14))
#       lineProj.setFrameShape(QFrame.VLine)
#       lineProj.setFrameShadow(QFrame.Raised)
#       lineSeq = QFrame(self)
#       lineSeq.setGeometry(QRect(65,29,10,14))
#       lineSeq.setFrameShape(QFrame.VLine)
#       lineSeq.setFrameShadow(QFrame.Raised)
#       lineShot = QFrame(self)
#       lineShot.setGeometry(QRect(65,49,10,14))
#       lineShot.setFrameShape(QFrame.VLine)
#       lineShot.setFrameShadow(QFrame.Raised)
#       lineShot = QFrame(self)
#       lineShot.setGeometry(QRect(65,49,10,14))
#       lineShot.setFrameShape(QFrame.VLine)
#       lineShot.setFrameShadow(QFrame.Raised)

#   def addcombBox(self):
#       self.cBoxProj = QComboBox(self)
#       self.cBoxProj.setGeometry(QRect(20,9,80,20))
#       self.cBoxSeq = QComboBox(self)
#       self.cBoxSeq.setGeometry(QRect(110,9,80,20))
#       self.cBoxShots = QComboBox(self)
#       self.cBoxShots.setGeometry(QRect(200,9,80,20))
#       self.cBoxShot = QComboBox(self)
#       self.cBoxShot.setGeometry(QRect(290,9,80,20))

#   def addtextEdit(self):
#       tEditShot = QLineEdit(self)
#       tEditShot.setGeometry(QRect(90,49,80,20))

#   def addpushButton(self):
#       self.pButtonGet = QPushButton('Get',self)
#       self.pButtonGet.setGeometry(QRect(380,29,80,20))

#   def setSignal(self):
#       self.cBoxProj.currentTextChanged.connect(lambda: self.slot_initCurrentTask(1))
#       self.cBoxSeq.currentTextChanged.connect(lambda: self.slot_initCurrentTask(2))
#       self.cBoxShots.currentTextChanged.connect(lambda: self.slot_initCurrentTask(3))
#       self.pButtonGet.clicked.connect(self.popWindow)

#   def slot_initCurrentTask(self, order):
#       time_start = time.time()
#       time_space = time_start - self.currentTime

#       if time_space > 0.6 and self.run == False:
#           thread = threading.Thread(target=self.call_reloadCurrentFunction)
#           thread.start()
#       if order == 0:
#           self.cBoxProj.clear()
#           ignoreProjectList = ['smxm']
#           for item in os.listdir(self.serverRoot+'/'):
#               if item in ignoreProjectList:
#                   self.cBoxProj.addItem(item) 
#       if order == 1:
#           self.projectName = self.cBoxProj.currentText()
#           self.cBoxSeq.clear()
#           self.projPath = self.serverRoot+'/' + self.projectName + '/shots/' 
#           for item in sorted(os.listdir(self.projPath)):
#               self.cBoxSeq.addItem(item)
#       if order == 2:
#           self.seq = self.cBoxSeq.currentText()
#           self.cBoxShots.clear()
#           self.seqPath = self.projPath + self.seq + '/'
#           for item in sorted(os.listdir(self.seqPath)):
#               self.cBoxShots.addItem(item)
#       if order == 3:
#           self.shots = self.cBoxShots.currentText()
#           self.cBoxShot.clear()
#           self.shotPath = self.seqPath + self.shots + '/'
#           for item in sorted(os.listdir(self.shotPath)):
#               self.cBoxShot.addItem(item)
#       self.currentTime = time.time()

#   def call_reloadCurrentFunction(self):
#       self.run = True
#       time.sleep(0.6)
#       self.run = False
#       self.move(500,200)

#   def popWindow(self):
#       self.proj = self.cBoxProj.currentText()
#       self.seq = self.cBoxSeq.currentText()
#       self.shots = self.cBoxShots.currentText()
#       self.shot = self.cBoxShot.currentText()
#       self.ui2 = Ui_Form()
#       self.ui2.getData(self.proj,self.seq,self.shots,self.shot)
#       self.ui2.show()

#   def set_param(self):
#       proj = self.cBoxProj.currentText()
#       seq = self.cBoxSeq.currentText()
#       shots = self.cBoxShots.currentText()
#       shot = self.cBoxShot.currentText()

# class Ui_Form(QtWidgets.QWidget):

#   def __init__(self,parent = None):
#       super(Ui_Form,self).__init__(parent)
#       self.initUI() 
		

#   def initUI(self):
#       self.resize(500,500)
#       self.addtreeWidget()
#       self.addpushButton()
#       self.set_signal()

#   def addtreeWidget(self):
#       self.treeMain = QTreeWidget(self)
#       self.treeMain.setGeometry(QRect(10,10,400,400))
#       self.treeMain.itemChanged.connect(self.autoCheckable)

#   def addpushButton(self):
#       self.pButtonBuild = QPushButton('BUILD',self)
#       self.pButtonBuild.setGeometry(QRect(420,430,70,20))

#   def set_signal(self):
#       self.pButtonBuild.clicked.connect(self.buildScene)

#   def settreeWidget(self):
#       self.treeMain.setColumnCount(2)
#       self.headerList = ['TYPE','NAME']
#       self.treeMain.setHeaderLabels(self.headerList)
#       self.root_char = QTreeWidgetItem(self.treeMain)
#       self.root_char.setText(0,'char')
#       self.root_char.setCheckState(0,Qt.Checked)
#       self.root_prop = QTreeWidgetItem(self.treeMain)
#       self.root_prop.setText(0,'prop')
#       self.root_prop.setCheckState(0,Qt.Checked)
#       self.root_set = QTreeWidgetItem(self.treeMain)
#       self.root_set.setText(0,'set')
#       self.root_set.setCheckState(0,Qt.Checked)
#       shotinfo = self.get_assets()
#       char_list = shotinfo['char']
#       set_list = shotinfo['set']
#       prop_list = shotinfo['prop']
#       if char_list:           
#           for char in char_list:
#               assetnameItem = char['name'] + (str(char['id']) if char['id'] else '')
#               child = QTreeWidgetItem()
#               child.setText(1,assetnameItem)
#               child.setCheckState(1,Qt.Checked)
#               self.root_char.addChild(child)              
#       # if set_list:
#       #   for sets in set_list:
#       #       assetnameItem = sets['name'] + (str(sets['id']) if sets['id'] else '')
#       #       child = QTreeWidgetItem()
#       #       child.setText(1,assetnameItem)
#       #       child.setCheckState(1,Qt.Checked)
#       #       self.root_set.addChild(child)
#       if prop_list:
#           for prop in prop_list:
#               assetnameItem = prop['name'] + (str(prop['id']) if prop['id'] else '')
#               child = QTreeWidgetItem()
#               child.setText(1,assetnameItem)
#               child.setCheckState(1,Qt.Checked)
#               self.root_prop.addChild(child)

#   def autoCheckable(self,item,column):
#       if item and column == 0 and item.text(0)!='set':
#           topitemState = item.checkState(0)
#           for i in range(item.childCount()):
#               childItem = item.child(i)
#               childItem.setCheckState(1,topitemState)
#       # if item.parent():
#       #   if item.parent().text(0) == 'set':
#       #       itemState = item.checkState(0)
#       #       for i in range(item.parent().childCount()):
#       #           broItem = item.parent().child(i)
#       #           broItem.setCheckState(1,itemState)

#   def get_assets(self):
#       print self.proj
#       print self.shot
#       shotinfo = get_shot_info(self.proj,self.shot)
#       return shotinfo

#   def getData(self,proj='1',seq= '1',shots = '1',shot = '1'):
#       self.proj = proj
#       self.seq = seq
#       self.shots = shots
#       self.shot = shot
#       self.settreeWidget()

#   def buildScene(self):
#       look = 'main'
#       asset_dict = self.get_checked_asset()
#       print asset_dict
#       for asset_name in asset_dict.keys():
#           ref_asset_srf(self.proj,self.shot,str(asset_dict[asset_name]),str(asset_name),look)
#           group_type_asset(asset_dict[asset_name],asset_name)
#           merge_cache(self.proj,self.shot,asset_name,True)
#       if self.root_set.checkState(0):
#           ref_asset_set(self.proj,self.shot)
#       if not cmds.objExists('%s_cam'%(self.shot)):
#           ref_cam_cache(self.proj,self.shot)
#       set_time_range(self.proj,self.shot)
		
#   def get_checked_asset(self):
#       asset_dict = {}
#       for i in range(self.root_char.childCount()):
#           item = self.root_char.child(i)
#           if item.checkState(1):
#               asset_dict[item.text(1)] = 'char'
#       # for i in range(self.root_set.childCount()):
#       #   item = self.root_set.child(i)
#       #   if item.checkState(1):
#       #       asset_dict[item.text(1)] = 'set'
#       for i in range(self.root_prop.childCount()):
#           item = self.root_prop.child(i)
#           if item.checkState(1):
#               asset_dict[item.text(1)] = 'prop'
#       return asset_dict

# def get_shot_assets(proj,seq,shots,shot):
#   print proj,seq,shots,shot
#   app = QtWidgets.QApplication.instance()
#   uiSide = assetList()
#   uiSide.show()


# def main():
#   app = QtWidgets.QApplication.instance()
#   if app == None:
#       app = QtWidgets.QApplication(sys.argv)
#   ui = Form()
#   ui.show()
#   app.exec_()

# import sys
# sys.path.append(r"D:\zhaojiayi\TST\tstcode\GitTsT")
# import tst
# reload(tst)
# tst.main()
# "Z:\\smxm\\shots\\ep001\\dhd\\dhd067\\cache\\haircache\\c023001lang\\curves\\{c023001lang}_bozi_cangmao.abc"
# ${DESC}/guides.abc

# Z:/smxm/shots/ep001/dhd/dhd067/cache/haircache/c023001lang/curves/\{c023001lang\}_{DESC}.abc
# 'Z:/smxm/shots/ep001/dhd/dhd067/cache/haircache/c023001lang/curves/\{c023001lang\}_${DESC}.abc'
# ${DESC}/guides.abc
# import xgenm.xgGlobal as xgg
# import xgenm as xg
# xg.palettes()
# xg.descriptions('')
# xg.palette('c023001lang1:bozi_chang')
# xg.getActive('c023001lang1:Lang_HairCol','c023001lang1:dupi_changmao','Primitive')
# xg.objects('c023001lang1:Lang_HairCol','c023001lang1:dupi_changmao',False)

# xg.getActive('c023001lang1:Lang_HairCol','c023001lang1:bozi_chang','Preview/Output')
# xg.setActive('c023001lang1:Lang_HairCol','c023001lang1:tou_duanmao', 'GLRenderer',True)
# xg.setActive('c023001lang1:Lang_HairCol','c023001lang1:tou_duanmao', 'RandomGenerator',False)
# xg.attrs('c023001lang1:Lang_HairCol','c023001lang1:tou_duanmao','NullRenderer' )
# xg.attrs('c023001lang1:Lang_HairCol','c023001lang1:tou_duanmao','RendermanRenderer' )
# xg.attrs('c023001lang1:Lang_HairCol','c023001lang1:tou_duanmao','RandomGenerator' )
# xg.attrs('c023001lang1:Lang_HairCol','c023001lang1:tou_duanmao','GLRenderer' )
# xg.allAttrs('c023001lang1:Lang_HairCol','c023001lang1:tou_duanmao','RandomGenerator' )

# 16:03:55 (1) GLRenderer made active previewer.
# 16:03:55 (1) Initialize c023001lang1:bozi_chang description 
# 16:04:10 (1) RandomGenerator made active.

# import xgenm as xg
# import xgenm.xgGlobal as xgg
# import xgenm.XgExternalAPI as xge
# print xg.palettes()
# descriptions =  xg.descriptions('c023001lang:Lang_HairCol')
# for description in descriptions:
#     print "Description:" + description
#     objects = xg.objects('c023001lang:Lang_HairCol',description,True)
#     for object in objects:
#         print "Object:" + object
#         attrs = xg.allAttrs('c023001lang:Lang_HairCol',description,object)
#         for attr in attrs:
#             print 'Attribute:' + attr + ", Value:" + xg.getAttr(attr,'c023001lang:Lang_HairCol',description,object)
# import os
# for description in descriptions:
#     des = description.split(":")[-1]
#     filePath = "Z:\smxm\shots\ep001\dhd\dhd067\cache\haircache\c023001lang\curves\{c023001lang}_%s.abc"%(description.split(":")[-1])
#     print os.path.isfile(filePath)
#     xgen.setAttr('cacheFileName',filePath,'c023001lang:Lang_HairCol',description,'SplinePrimitive')
#     xgen.setAttr('liveMode','True','c023001lang:Lang_HairCol',description,'SplinePrimitive')
# import xgenm.xgGlobal as xgg
# de = xgg.DescriptionEditor
# de.refresh("Full")
# -------------------------------------------------------------------------------------
# import xgenm as xgen
# import xgenm.xgGlobal as xgg
# de = xgg.DescriptionEditor
# palettesList = xg.palettes()
# for palette in palettesList:
#   descriptions =  xgen.descriptions(palette)
#   for description in descriptions:
#       des = description.split(":")[-1]
#       filePath = "Z:\smxm\shots\ep001\dhd\dhd067\cache\haircache\c023001lang1\curves\{c023001lang1}_%s.abc"%(description.split(":")[-1])
#       if os.path.isfile(filePath):
#           xgen.setAttr('cacheFileName',filePath,palette,description,'SplinePrimitive')
#           xgen.setAttr('liveMode','False',palette,description,'SplinePrimitive')
#   for description in descriptions:
#       cmds.xgmPreview(description)
#       de.previewer.execute()

# de.refresh("Full")
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# import maya.cmds as cmds

# cmds.setAttr("defaultArnoldRenderOptions.autotx",False)
# cmds.setAttr("defaultArnoldRenderOptions.use_existing_tiled_textures",False)
# aiString = cmds.createNode('aiStringReplace')
# cmds.setAttr(aiString+".enable",True )
# cmds.setAttr(aiString+'.selection',"*.(@node=='image')",type = 'string')
# cmds.setAttr(aiString+".os",0)
# cmds.setAttr(aiString+".match","\\.(png|exr|hdr)",type = 'string')
# cmds.setAttr(aiString+".replace",".tx",type = 'string')
# -------------------------------------------------------------------------------------
# import sys
# sys.path.append(r"D:\zhaojiayi\Documents\coco\cocoPipeline\dcc\maya\scripts\python\pipelineTool\lgt")
# import lgtshotmay
# reload(lgtshotmay)
# lgtshotmay.main()
# import os

# rvPath = r'"C:/Program Files/Shotgun/RV-7.2.0/bin/rv.exe"'
# filePath = r"Z:\\smxm\\shots\\ep001\\dhd\\dhd067\\animation\\lay\\ok\\dhd067_lay_ok.mov"
# cmd = rvPath + ' ' + filePath
# print cmd
# os.system(cmd)

# "Z:\\smxm\\shots\\ep001\\xuz\\xuz003\animation\\lay\\ok\\xuz003_lay_ok.mov"
# "Z:\\smxm\\shots\\ep001\\dhd\\dhd067\\set\\scene\\ok\\dhd067_scene_ok.mov"
# signal = 'lay'
# signal = 'set'
# projPath = 'Z:\\smxm\\shots\\ep001'
# shotsList = os.listdir(projPath)
# filepathList = []
# for shots in shotsList:
#   shotsPath = os.path.join(projPath,shots)
#   shotList = os.listdir(shotsPath)
#   for shot in shotList:
#       if signal == 'lay':
#           shotPath = os.path.join(shotsPath,shot,'animation\\lay\\ok')
#           if os.path.isdir(shotPath):
#               filePath = shotPath + '\\' + shot + '_lay_ok.mov'
#               if os.path.isfile(filePath):
#                   filepathList.append(filePath)
#       elif signal == 'set':
#           shotPath = os.path.join(shotsPath,shot,'set\\scene\\ok')
#           if os.path.isdir(shotPath):
#               filePath = shotPath + '\\' + shot + '_scene_ok.mov'
#               if os.path.isfile(filePath):
#                   filepathList.append(filePath)
# cmdPath = ' '.join(filepathList)
# cmd = rvPath + ' ' + cmdPath
# os.system(cmd)

# def get_shot_info(proj,shot):
#   xlsx_path = "Z:\\%s\\database\\casting\\main.xlsx"%proj
#   shotinfo = Function.getShot(xlsx_path, shot)
#   return shotinfo

# proj = 'smxm'
# shot = 'dhd066'
# print '------------'
# print get_shot_info(proj,shot)
# import os
# import ftrack
# print ftrack.getProjects()

# new session 
# ERROR: com.ftrack.recipes.customise_structure.location.custom_location_plugin:Disk prefix location variable does not exist. 
# INFO: ftrack_api._centralized_storage_scenario.ActivateCentralizedStorageScenario:Storage scenario activated. Configured from {u'data': {u'location_id': u'f10b5013-50e2-4cfb-b659-16c86f27375b', u'location_name': u'studio.central-storage-location', u'accessor': {u'mount_points': {u'windows': u'z:', u'osx': u'', u'linux': u''}}}, u'scenario': u'ftrack.centralized-storage'} 
# INFO: received URL 'rvlink://baked/202d666c616773204d6f64654d616e616765725072656c6f61643d66747261636b2066747261636b55726c3d687474703a2f2f666b2e6363632e6e657420706172616d733d277b22656e746974794964223a5b2264386533396434382d616663302d313165622d383937342d303031353564303162663037225d2c22617574685f746f6b656e223a5b2264386539646139362d616663302d313165622d613837312d303031353564303162663037225d2c22656e7469747954797065223a5b2274656d7064617461225d7d27' 
# INFO: decoded URL 'rvlink:// -flags ModeManagerPreload=ftrack ftrackUrl=http://fk.ccc.net params='{"entityId":["d8e39d48-afc0-11eb-8974-00155d01bf07"],"auth_token":["d8e9da96-afc0-11eb-a871-00155d01bf07"],"entityType":["tempdata"]}'' 
# INFO: received URL 'rvlink://baked/202d666c616773204d6f64654d616e616765725072656c6f61643d66747261636b2066747261636b55726c3d687474703a2f2f666b2e6363632e6e657420706172616d733d277b22656e746974794964223a5b2264386533396434382d616663302d313165622d383937342d303031353564303162663037225d2c22617574685f746f6b656e223a5b2264386539646139362d616663302d313165622d613837312d303031353564303162663037225d2c22656e7469747954797065223a5b2274656d7064617461225d7d27' 
# INFO: decoded URL 'rvlink:// -flags ModeManagerPreload=ftrack ftrackUrl=http://fk.ccc.net params='{"entityId":["d8e39d48-afc0-11eb-8974-00155d01bf07"],"auth_token":["d8e9da96-afc0-11eb-a871-00155d01bf07"],"entityType":["tempdata"]}'' 
# INFO: eval returned: 
# INFO: eval returned: 
# import ftrack_api

# -------------------------------density shrink---------------------------------------------------
# import xgenm as xg
# import xgenm.xgGlobal as xgg
# import xgenm.XgExternalAPI as xge
# palettes = xg.palettes()
# for palette in palettes:
# 	descriptions = xg.descriptions(palette)
# 	for description in descriptions:
# 		objects = xg.objects(palette, description, True)
# 		for object in objects:
# 			attrs = xg.allAttrs(palette, description, object)
# 			for attr in attrs:
# 				if "ensity" in attr:
# 					_value = xg.getAttr(attr, palette, description, object)
# 					print(_value,float(_value)/10)
# 					xg.setAttr(attr,str(float(_value)/10),palette, description, object)
# -------------------------------------------------------------------------------------------------

# import sys
# sys.path.append('D:\\zhaojiayi\\Documents\\coco')
# import os
# import getpass
# from cocoPipeline.lib.python import resource
# from cocoLib.python.configLib import confParser
# reload(confParser)
# reload(resource)
# import cocoPipeline.lib.python.ftrackLib.ftrackSession as ftrackSession
# reload(ftrackSession)
# import cocoPipeline.lib.python.ftrackLib.ftrackQuery as ftrackQuery
# reload(ftrackQuery)
# from cocoPipeline.lib.python.dataLib import entityObject

# getUserName = getpass.getuser()
# session = ftrackSession.createSession()
# print session.types.keys()
# projectName = 'TDtest'
# projectName = 'Goodbye_Monster'
# getUserName = getpass.getuser()
# projects = session.query('Project where name is "{0}"'.format(projectName)).first()
# getUserName = os.environ['USER']
# UserMessage = session.query('User where username is "{0}"'.format(getUserName)).one()
# entity = entityObject.Project().objects(projectName)
# print type(entity)
# location = session.query('Location where name is "{0}"'.format(entity.ftrack_pipeline_location)).one()
# serverRoot = os.path.abspath(location.get_accessor_prefix())
# mapAttrDicView['taskName'] = 'surface'
# mapAttrDicView['subTaskName'] = 'view'
# mapAttrDicView['assetFile'] = 'sourceimages'
# def get_entity():
#     entity_template = os.path.realpath(os.path.join(resource.get_config(), 'mapping.yml'))
#     print entity_template
#     cp = confParser.DeepYamlParser(entity_template)
#     return cp.parse()
# # print get_entity()

# Dir = "Z:\\smxm\\assets\\char\\c001001xiongmaox\\surface\\look\\main\\ok\\c001001xiongmaox_look_main.ma"
# Dir =       'Z:/         smxm/           shots/    ep001/       dhd/dhd067/       lgt/     lighting/workarea/xm_shots_dhd067_lgt_deep_2019_v001.mb'
# '{projectRoot}/{projectName}/{productionType}/{episode}/{sequence}/{shot}/{taskName}/{subTaskName}/{assetFile}'
# folderList[-1], folderList[-2], folderList[-3], folderList[-4], folderList[-5], folderList[-8]
# folderList[-2], folderList[-3], folderList[-4], folderList[-5], folderList[-8]

# --------------------------

# import sys
# sys.path.append('D:\\zhaojiayi\\Documents\\coco')
# import os
# import getpass
# import cocoPipeline.lib.python.ftrackLib.ftrackSession as ftrackSession
# reload(ftrackSession)
# import cocoPipeline.lib.python.ftrackLib.ftrackQuery as ftrackQuery
# reload(ftrackQuery)
# from cocoPipeline.lib.python.dataLib import entityObject
# from cocoPipeline.lib.python.dataLib import getEntity
# projectName = 'TDtest'
# session = ftrackSession.createSession()
# entity = entityObject.Project().objects(projectName)
# location = session.query('Location where name is "{0}"'.format(entity.ftrack_pipeline_location)).one()
# serverRoot = os.path.abspath(location.get_accessor_prefix())
# serverRoot = os.environ['SERVER_ROOT'].capitalize()
# task = session.query(
# 			'Task where parent.name is "{0}" \
# 			 and parent.parent.name is "{1}" \
# 			 and parent.parent.parent.name is "{2}" \
# 			 and parent.parent.parent.parent.name is "{3}" \
# 			 and project.name is "{4}"'\
# 			 .format('comp', 'cmp', 'hdd', 'ep001', 'TDtest')
# 		)
# asset = session.query(
# 			'Asset where name is "{0}" \
# 			 and parent.name is "{1}" \
# 			 and parent.parent.name is "{2}" \
# 			 and parent.parent.parent.name is "{3}" \
# 			 and parent.parent.parent.parent.name is "{4}" \
# 			 and project.name is "{5}"'\
# 			 .format('comp', 'cmp', 'cmp', 'hdd','ep001', 'TDtest')
# 		)

# print task[0]
# print asset[0]
# 		王者荣耀_澜/shots/ep001/hdd/hdd076/animation/ani/ani
# 'TDtest/shots/ep001/hdd/cmp/comp/comp'
# project = session.query('Project').first()
# print project['task_templates']
# print session.types.keys()
# projects = session.query('Project')
# for proj in projects:
# 	print proj['name']
# active_projects = session.query('Project where status is active')
# for proj in active_projects:
# 	print proj['name']
# projects[0].keys()
# --------------------------

# import json
# jsonFile = "C:/Users/zhaojiayi/Desktop/tstfile/p006001shu_look_main.json"
# assetName = 'p006001shu'
# with open(jsonFile) as dataFile:
# 	jsonData = json.load(dataFile)
# 	shapeDicts = jsonData['geoProperty']
# 	shapeList = shapeDicts.keys() 	
# 	for shape in shapeList:
# 		shapyDict = shapeDicts[shape]
# 		print shapyDict['uv_link']
# 		node = assetName + ':' + shape.split('|')[-1]
# 		if cmds.objExists(node):
# 			cmds.select(node)
# 			indices = cmds.polyUVSet(node, query=True, allUVSetsIndices=True)
# 			for k,v in shapyDict['uv_link'].items():
# 				texture = assetName+ ':' + k
# 				for i in indices[:]:
# 					uvSetName = cmds.getAttr(node+".uvSet["+str(i)+"].uvSetName")
# 					if uvSetName == v:
# 						cmds.uvLink(make=True,uvSet =node+".uvSet["+str(i)+"].uvSetName",texture = texture )



# cmds.select(mesh)
# import os
# filePath = 'Z:/smxm/shots/ep001/dhd/dhd071/cache/haircache/c023001lang1/patches'
# fileName = os.listdir(filePath)
# cmds.file('Z:/smxm/assets/prop/p006001shu/surface/look/main/ok/p006001shu_look_main.ma',loadReferenceDepth = 'asPrefs',loadReference = 'p006001shuRN')
# import time 
# import os
# import re
# ticks = time.time()
# print ticks
# a =  "Thu May 13 19:24:00 2021"
# b =  "Thu May 13 19:24:24 2021"
# print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
# fullPath = "Z:/smxm/assets/char/c001001xiongmaox/surface/look/main/sst/c001001xiongmaox_look_main_render.ma"
# mtime = os.stat(fullPath).st_mtime
# print mtime

# fPath = 'Z:/smxm/assets/char/c001001xiongmaox/surface/look/main/ok'
# b = "Z:/smxm/assets/char/c001001xiongmaox/surface/look/main/ok/c001001xiongmaox_look_main.ma"
# pattern = r'(surface/look/main/ok*)'
# print re.match(pattern,b)
# for root, dirs,files in os.walk(fPath,topdown = False):
# 	# print 'root'
# 	# print root
# 	# print 'dirs'
# 	# print dirs
# 	# print 'files'
# 	# print files
# 	# for name in files:
# 	# 	if '/surface/look/main/ok/' in root and 'v0' not in root and 'ma' in name:
# 	# 		print (os.path.join(root,name))
# 	# for name in dirs:
# 	# 	print (os.path.join(root,name))	
# 	# for name in files:
# 	# 	print '--------------------------------'
# 	# 	# print (os.path.join(root,name))
# 	# 	if '/surface/look/main/ok' in root:
# 	# 		print (os.path.join(root,name))
# 	# 		if 'v0' not in root:
# 	# 			print (os.path.join(root,name))
# 	# 			if '.ma' in name:
# 	# 				print (os.path.join(root,name))
# 	# 	print '--------------------------------'
# 	print root
# 	for name in files:
# 		if '/surface/look/main/ok' in root:
# 			if 'v0' not in root and '.ma' in name:
# 				print (os.path.join(root,name))
# fPath = 'Z:/smxm/assets/char/'
# fPath = 'Z:/smxm/assets/prop/'

# charList = os.listdir(fPath)
# # print charList
# for char in charList:
#     srfPath = fPath + char + '/surface/look/main/ok/'
#     if os.path.isdir(srfPath):
#         fileList =  os.listdir(srfPath)
#         for file in fileList:
#             if '_render.ma' in file:
#                 rederFile = srfPath + file
#                 fileTime = os.stat(rederFile).st_mtime
#                 # print fileTime,type(fileTime)
#                 chuo = time.ctime(fileTime)
#                 print rederFile,chuo



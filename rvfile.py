# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# from Qt import QtWidgets, QtCore,QtGui
import time

from Qt import QtWidgets, QtCore
from Qt.QtCore import *
import threading
# from Qt.QtGui import *
# from Qt.QtWidgets import *



rvPath = r'"C:/Program Files/Shotgun/RV-7.2.0/bin/rv.exe"'
signal = 'set'
projPath = 'Z:\\smxm\\shots\\ep001'
shotsList = os.listdir(projPath)
filepathList = []
for shots in shotsList:
	shotsPath = os.path.join(projPath,shots)
	shotList = os.listdir(shotsPath)
	for shot in shotList:
		if signal == 'lay':
			shotPath = os.path.join(shotsPath,shot,'animation\\lay\\ok')
			if os.path.isdir(shotPath):
				filePath = shotPath + '\\' + shot + '_lay_ok.mov'
				if os.path.isfile(filePath):
					filepathList.append(filePath)
		elif signal == 'set':
			shotPath = os.path.join(shotsPath,shot,'set\\scene\\ok')
			if os.path.isdir(shotPath):
				filePath = shotPath + '\\' + shot + '_scene_ok.mov'
				if os.path.isfile(filePath):
					filepathList.append(filePath)
cmdPath = ' '.join(filepathList)
# ------------------------------------------
cmd = rvPath + ' ' + cmdPath
print cmd
# os.system(cmd)
# ------------------------------------------

class Form(QtWidgets.QMainWindow):

	def __init__(self,parent=None):
		super(Form,self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.mainLayout = QtWidgets.QVBoxLayout(self)
		self.setInitData()
		self.addcombBox()
		self.addLayout()
		self.addpushButton()
		self.currentTime = time.time()
		self.setSignal()
		self.setWindowTitle("Quick Open File in RV")
		self.slot_initCurrentTask(0)
		self.resize(500,80)
		self.run = False

	def setInitData(self):
		departmentList = ['lay','ani']
		self.serverRoot = "Z:"
		self.currentTime = time.time()

	def addLayout(self):
		self.searchLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addChildLayout(self.searchLayout)
		self.searchLayout.addWidget(self.cBoxProj)
		# self.searchLayout.addWidget(self.cBoxSeq)
		# self.searchLayout.addWidget(self.cBoxShots)
		# self.searchLayout.addWidget(self.cBoxShot)

	def addcombBox(self):
		self.cBoxProj = QtWidgets.QComboBox()
		# self.cBoxProj.setGeometry(QtCore.QRect(20,9,80,20))
		self.cBoxSeq = QtWidgets.QComboBox()
		# self.cBoxSeq.setGeometry(QtCore.QRect(110,9,80,20))
		self.cBoxShots = QtWidgets.QComboBox()
		# self.cBoxShots.setGeometry(QtCore.QRect(200,9,80,20))
		self.cBoxShot = QtWidgets.QComboBox()
		# self.cBoxShot.setGeometry(QtCore.QRect(290,9,80,20))

	def addpushButton(self):
		self.pButtonSearch = QtWidgets.QPushButton('SEARCH',self)
		self.pButtonSearch.setGeometry(QtCore.QRect(420,430,70,20))

	def setSignal(self):
		self.cBoxProj.currentIndexChanged.connect(lambda: self.slot_initCurrentTask(1))
		# self.cBoxSeq.currentIndexChanged.connect(lambda: self.slot_initCurrentTask(2))
		# self.cBoxShots.currentIndexChanged.connect(lambda: self.slot_initCurrentTask(3))	
		self.pButtonSearch.clicked.connect(self.get_shotList)

	def slot_initCurrentTask(self, order):
		time_start = time.time()
		time_space = time_start - self.currentTime

		if time_space > 0.6 and self.run == False:
			thread = threading.Thread(target=self.call_reloadCurrentFunction)
			thread.start()
		if order == 0:
			self.cBoxProj.clear()
			ignoreProjectList = ['smxm']
			for item in ignoreProjectList:
				self.cBoxProj.addItem(item) 
		if order == 1:
			self.projectName = self.cBoxProj.currentText()
			self.cBoxSeq.clear()
			self.projPath = self.serverRoot+'/' + self.projectName + '/shots/' 
			# for item in sorted(os.listdir(self.projPath)):
			# 	self.cBoxSeq.addItem(item)
			# self.cBoxSeq.addItem('ALL')
			self.cBoxSeq.addItem('ep001')
		if order == 2:
			self.seq = self.cBoxSeq.currentText()
			self.cBoxShots.clear()
			self.cBoxShots.addItem('ALL')
			self.seqPath = self.projPath + self.seq + '/'
			for item in sorted(os.listdir(self.seqPath)):
				self.cBoxShots.addItem(item)
		if order == 3:
			self.shots = self.cBoxShots.currentText()
			self.cBoxShot.clear()
			if self.shots == 'ALL':
				self.cBoxShot.addItem('ALL')
			else:
				self.cBoxShot.addItem('ALL')
				self.shotPath = self.seqPath + self.shots + '/'
				for item in sorted(os.listdir(self.shotPath)):
					self.cBoxShot.addItem(item)

		self.currentTime = time.time()

	def call_reloadCurrentFunction(self):
		self.run = True
		time.sleep(0.6)
		self.run = False
		# self.move(500,200)

	def get_shotList(self):
		pass




# if __name__=='__main__':
# 	app = QtWidgets.QApplication.instance()
# 	if app == None:
# 		app = QtWidgets.QApplication(sys.argv)
# 	ui = Form()
# 	ui.show()
# 	app.exec_()	

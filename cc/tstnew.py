# !/usr/bin/env python
# -*- coding: utf-8 -*-

# from PySide2 import QtWidgets, QtCore 
# try:
# 	from PySide2.QtWidgets import *
# except:
# 	from PyQt5.QtWidgets import *
	
# from Qt.QtCore import *
# from Qt.QtGui import *
# from Qt.QtWidgets import *
import sys
from Qt import QtCore, QtWidgets


class Form(QtWidgets.QMainWindow):

	def __init__(self,parent=None):
		super(Form,self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.setWindowTitle("JI ZHANG XI TONG")
		self.resize(1000,700)
		self.addTab()
		self.addtabWidget()
		self.addCoustomLayout()
		# self.addLayout()
		# self.addpushButton()

	def addTab(self):
		self.mainTab = QtWidgets.QWidget()
		self.billTab = QtWidgets.QWidget()
		self.storageTab = QtWidgets.QWidget()

	def addtabWidget(self):
		self.tabWidgetMain = QtWidgets.QTabWidget(self)
		self.tabWidgetMain.resize(1000,700)
		self.tabWidgetMain.setStyleSheet('font-size:30pt;')
		# self.tabWidgetMain.setStyleSheet('font-size:30pt;')
		self.tabWidgetMain.addTab(self.mainTab, 'MAIN')
		self.tabWidgetMain.addTab(self.billTab, 'BILL')
		self.tabWidgetMain.addTab(self.storageTab, 'STORAGE')


	def addpushButton(self):
		self.pButtonplus = QtWidgets.QPushButton('+',self)
		self.pButtonplus.setGeometry(QtCore.QRect(20,20,100,100))
		self.pButtonplus.setStyleSheet("font-size: 100pt;")
		self.pButtonplus.clicked.connect(self.plus_bill)

	def addCoustomLayout(self):
		self.mainLayout = QtWidgets.QVBoxLayout(self.tabWidgetMain)
		self.newbillsLayout = QtWidgets.QGridLayout()
		self.currentMenuLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.newbillsLayout)
		self.mainLayout.addLayout(self.currentMenuLayout)

	def plus_bill(self):
		self.pButtonbill = QtWidgets.QPushButton('+',self)


if __name__ == '__main__':
	app = QtWidgets.QApplication.instance()
	if app == None:
		app = QtWidgets.QApplication(sys.argv)
	ui = Form()
	ui.show()
	app.exec_()

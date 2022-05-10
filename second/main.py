from turtle import setx
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic,QtGui,QtWidgets

from PyQt5.QtGui import QPixmap


import sys
#1 = 남자
sex = 1

class preset(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("preset.ui",self)
        
        if sex==1:
            self.img_preset_1.setPixmap(QPixmap("ref/male/1.png"))
            self.img_preset_2.setPixmap(QPixmap("ref/male/2.png"))
            self.img_preset_3.setPixmap(QPixmap("ref/male/3.png"))
        else:
            self.img_preset_1.setPixmap(QPixmap("ref/fem/1.png"))
            self.img_preset_2.setPixmap(QPixmap("ref/fem/2.png"))
            self.img_preset_3.setPixmap(QPixmap("ref/fem/3.png"))
        
        self.show()
        self.merge.clicked.connect(self.home)
        self.select_src.clicked.connect(self.fileopen_src)
        
    def fileopen_src(self):
        srcimg = QFileDialog.getOpenFileName(self,'Open file','./')
        self.img_src.setPixmap(QtGui.QPixmap(srcimg[0]))
    
    def home(self):
        self.close()

class custom_hair(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("custom.ui",self)
        self.show()
        self.merge.clicked.connect(self.home)
        self.select_src.clicked.connect(self.fileopen_src)
        self.select_ref.clicked.connect(self.fileopen_ref)
    
    def fileopen_src(self):

        srcimg = QFileDialog.getOpenFileName(self,'Open file','./')
        self.img_src.setPixmap(QtGui.QPixmap(srcimg[0]))
        
    def fileopen_ref(self):
        refimg = QFileDialog.getOpenFileName(self,'Open file','./')
        self.img_ref.setPixmap(QtGui.QPixmap(refimg[0]))
        
        
    def home(self):
        self.close()

class custom_dye(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("custom.ui",self)
        self.show()
        self.merge.clicked.connect(self.home)
        self.select_src.clicked.connect(self.fileopen_src)
        self.select_ref.clicked.connect(self.fileopen_ref)
    
    def fileopen_src(self):

        srcimg = QFileDialog.getOpenFileName(self,'Open file','./')
        self.img_src.setPixmap(QtGui.QPixmap(srcimg[0]))
    def fileopen_ref(self):
        refimg = QFileDialog.getOpenFileName(self,'Open file','./')
        self.img_ref.setPixmap(QtGui.QPixmap(refimg[0]))
        
    def home(self):
        self.close()

class initialwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("sex_select.ui",self)
        self.male.clicked.connect(self.homewindow_1)
        self.female.clicked.connect(self.homewindow_2)
        self.show()

    def homewindow_1(self):
        window_home = home()

    def homewindow_2(self):
        sex = 0
        window_home = home()
        


class home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("main.ui",self)
        self.custom_hair.clicked.connect(self.customwindow_1)
        self.custom_dye.clicked.connect(self.customwindow_2)
        self.preset.clicked.connect(self.presetwindow_1)
        self.show()
    
    def customwindow_1(self):
        window_1 = custom_hair()

    def customwindow_2(self):
        window_2 = custom_dye()

    def presetwindow_1(self):
        window_3 = preset()
        


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = initialwindow()
    window.show()
    app.exec_()

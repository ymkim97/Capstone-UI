import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('proto1.ui') #메인 윈도우
form_class = uic.loadUiType(form)[0]

form_second = resource_path('btn1_window.ui') #hairstyle
form_secondwindow = uic.loadUiType(form_second)[0]

form_third = resource_path('btn2_window.ui') #dye   
form_thirdwindow = uic.loadUiType(form_third)[0]

form_fourth = resource_path('btn3_window.ui') #preset
form_fourthwindow = uic.loadUiType(form_fourth)[0]



form_error1 = resource_path('error1.ui') #error1
form_errorwindow1 = uic.loadUiType(form_error1)[0]

form_error3 = resource_path('error3.ui') #error3
form_errorwindow3 = uic.loadUiType(form_error3)[0]


class WindowClass(QMainWindow, form_class): #메인 윈도우
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButtonMale.clicked.connect(self.RadioButton)
        self.radioButtonFemale.clicked.connect(self.RadioButton)

    def btn_main_to_second(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = secondwindow()    
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐
    
    def btn_main_to_third(self):
        self.hide()                    
        self.third = thirdwindow()    
        self.third.exec()              
        self.show()
    
    def btn_main_to_fourth(self):
        self.hide()                    
        self.fourth = fourthwindow()    
        self.fourth.exec()              
        self.show()

    def RadioButton(self):
        global gender
        if self.radioButtonMale.isChecked():
            gender = 'male'

        elif self.radioButtonFemale.isChecked():
            gender = 'female'
    
	

    #여기에 시그널-슬롯 연결 설정 및 함수 설정



class secondwindow(QDialog,QWidget,form_secondwindow): #hairstyle
    def __init__(self):
        super(secondwindow,self).__init__()
        self.initUi()
        self.show()


    def initUi(self):
        self.setupUi(self)
        self.isPic1 = 0
        self.isPic2 = 0
        self.hairstyleOriginalUpload.clicked.connect(self.fileopen1)
        self.hairstyleUpload.clicked.connect(self.fileopen2)
        self.hairstyleResult.clicked.connect(self.addimageRes)

    def fileopen1(self):
        global hairstyleOriginal_file
        hairstyleOriginal_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        
        if(hairstyleOriginal_file):
            self.addimage1()
            self.isPic1 = 1
        
    
    def fileopen2(self):
        global hairStyle_file
        hairStyle_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if(hairStyle_file):
            self.addimage2()
            self.isPic2 = 1

    def addimage1(self):
        qpixmap = QPixmap(hairstyleOriginal_file[0])
        self.originalLabel.setPixmap(qpixmap)
    
    def addimage2(self):
        qpixmap = QPixmap(hairStyle_file[0])
        self.originalLabel_2.setPixmap(qpixmap)

    def addimageRes(self):
        if(self.isPic1 and self.isPic2):
            pass
        else:
            self.error3 = errorwindow3() #원본 또는 스타일 이미지 없이 합성 누를때
    
    def btn_second_to_main(self):
        self.close()


    
class thirdwindow(QDialog,QWidget,form_thirdwindow): #dye
    def __init__(self):
        super(thirdwindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)
        self.isPic1 = 0
        self.isPic2 = 0
        self.dyeOriginalUpload.clicked.connect(self.fileopen1)
        self.dyeStyleUpload.clicked.connect(self.fileopen2)
        self.dyeResult.clicked.connect(self.addimageRes)
        

    def fileopen1(self):
        global dyeOriginal_file
        dyeOriginal_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if(dyeOriginal_file):
            self.addimage1()
            self.isPic1 = 1
        
    def fileopen2(self):
        global dyeStyle_file
        dyeStyle_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if(dyeStyle_file):
            self.addimage2()
            self.isPic2 = 1

    def addimage1(self):
        qpixmap = QPixmap(dyeOriginal_file[0])
        self.originalLabel.setPixmap(qpixmap)
    
    def addimage2(self):
        qpixmap = QPixmap(dyeStyle_file[0])
        self.originalLabel_2.setPixmap(qpixmap)

    def addimageRes(self):
        if(self.isPic1 and self.isPic2):
            pass
        else:
            self.error3 = errorwindow3() #원본 또는 스타일 이미지 없이 합성 누를때
    
    def btn_third_to_main(self):
        self.close()



class fourthwindow(QDialog,QWidget,form_fourthwindow): #preset
    def __init__(self):
        super(fourthwindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)
        self.isPic = 0
        self.presetUpload.clicked.connect(self.fileopen)
        self.presetSyn.clicked.connect(self.addimageRes)
        

    def fileopen(self):
        global preset_file
        preset_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if(preset_file):
            self.addimage()
            self.isPic = 1

    def addimage(self):
        qpixmap = QPixmap(preset_file[0])
        self.originalLabel.setPixmap(qpixmap)

    def addimageRes(self):
        if(self.isPic):
            pass
        else:
            self.error3 = errorwindow3() #원본 또는 스타일 이미지 없이 합성 누를때
    
    def btn_fourth_to_main(self):
        self.close()

###에러 창 모음
class errorwindow1(QDialog,QWidget,form_errorwindow1): #error1
    def __init__(self):
        super(errorwindow1,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

    def okay(self):
        self.close()

class errorwindow3(QDialog,QWidget,form_errorwindow3): #error1
    def __init__(self):
        super(errorwindow3,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)
    
    def okay(self):
        self.close()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
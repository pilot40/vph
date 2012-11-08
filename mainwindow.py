# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from datetime import *
import math

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.center()
        self.connect(self.ui.butRasch, SIGNAL('clicked()'), SLOT('fuel()'))
        self.connect(self.ui.butRaschVes, SIGNAL('clicked()'), SLOT('ves()'))
        
      #Размещение окна по центру экрана  
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        
    #Закрытие приложения   
    @pyqtSignature("")
    def on_exit_triggered(self):
        #self.close()
        exit = QMessageBox.information(self,
                                       u'Выход...',
                                       u'Вы хотите выйти?',
                                       u'&Да', 
                                       u'&Нет', 
                                       '', 0, 1)
        if exit==0:
            return self.close()
        else:
            return 0
        
    #О программе    
    @pyqtSignature("")
    def on_about_triggered(self):
        QMessageBox.information(self, u'О программе', u'Расчёт ВПХ для Як-40\n ООО "СКОЛ"')
        
    #О Qt    
    @pyqtSignature("")
    def on_about_Qt_triggered(self):
        QMessageBox.information(self, qApp.aboutQt())
        
    #Расчёт топлива и времени
    @pyqtSignature("")
    def fuel(self):
        #self.dial.setValue(self.spinbox.value())
        #S = ui.spinBoxG.value()
        #self.ui.lineEditG.setText(u"Ух ты получилось!")
        dt = datetime.now()
        S = self.ui.spinBoxS.value()
        Salt = self.ui.spinBoxSalt.value()
        W = 420 # Скорость
        Q = 1200 #Расход топлива
        Tpsum = (S+Salt)/W #Время полета для общего топлива
        Tp = float(S)/float(W) #Время полета до ап
        Hh = int(Tp)
        Mm = int((Tp- Hh)*60)
        n = QTime()
        n.setHMS(Hh,Mm,00,00)        
        Gf = int((((((float(S)+float(Salt))/W)*Q)*1.03)+600))
        self.ui.lineEditG.setText(str(Gf))#Вывод общего топлива
        self.ui.lineEditG_2.setText(str(Gf))#Вывод общего топлива для загрузки
        self.ui.timeEdit.setTime(n)#Вывод времени полёта
     
    #Расчёт веса 
    @pyqtSignature("")
    def ves(self):
        Gpust = 11245
        Gsl = 80
        Gfull = int(self.ui.lineEditG_2.text())
        vEk = 80
        vPr = 75
        vTeh = 75
        vPass = 75
        Gvzl = Gpust+Gsl+Gfull+(self.ui.spinEk.value()*vEk)+(self.ui.spinPr.value()*vPr)+(self.ui.spinTeh.value()*vTeh)+(self.ui.spinZagr.value()*vPass)-65
        self.ui.lineVzl.setText(str(Gvzl))
        
    #Завершение
    def __del__ ( self ):
     self.ui = None
     


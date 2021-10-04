# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random
import resources
from os import path
from intersections import *
from scipy import optimize

steps = 0
gde_mag = []
gde_susc = []
gde_spec = []
gde_binder = []
mag_l = []
susc_l = []
spec_l = []
binder_l = []
values_mag_temp = []
values_mag = []
values_mag_err = []
values_susc_temp = []
values_susc = []
values_susc_err = []
values_spec_temp = []
values_spec = []
values_spec_err = []
values_binder_temp = []
values_binder = []
values_binder_err = []

xmin = -0.1
xmax = 0.1
ymin = 0.9
ymax = 1.25
     
class MatplotlibWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("guialps.ui",self)
        self.setWindowTitle("MCgui")
        #self.addToolBar(NavigationToolbar(self.widget.canvas, self))
        #self.addToolBar(NavigationToolbar(self.widget_2.canvas, self))
        self.loader_button.clicked.connect(self.loaddata)
        self.pushButton.clicked.connect(self.grafici)
        self.comboBox.addItems(['Magnetizacija',u'Specifična toplota','Susceptibilnost','Binderov kumulant'])
        self.pushButton_2.clicked.connect(self.procenatc)
        self.pushButton_3.clicked.connect(self.zoom)
        self.pushButton_4.clicked.connect(self.tcfit)
        self.pushButton_5.clicked.connect(self.nu)
        self.pushButton_6.clicked.connect(self.gama)
        self.pushButton_7.clicked.connect(self.alfa)
        self.pushButton_8.clicked.connect(self.beta)


    def loaddata(self):
        global steps,gde_mag,gde_susc,gde_spec,gde_binder,mag_l,susc_l,spec_l,binder_l,values_mag_temp,values_mag,values_mag_err
        global values_susc_temp,values_susc,values_susc_err,values_spec_temp,values_spec,values_spec_err,values_binder_temp,values_binder,values_binder_err
        def search_string_in_file(file_name, string_to_search):
            line_number = -1
            list_of_results = []
            with open(file_name, 'r') as read_obj:
                for line in read_obj:
                    line_number += 1
                    if string_to_search in line:
                        list_of_results.append((line_number, line.rstrip()))
            return list_of_results

        if path.exists("podaci.txt") == True:
            self.label_4.setText(u"Dokument podaci.txt je uspešno učitan!\nMožete preći na analizu i vizuelizaciju rezultata\nMonte Karlo simulacije.")
            self.label_4.setStyleSheet("background-color: green; border: 1px solid black;")
            self.updatelabel1()
            with open('podaci.txt') as f:
                lines = f.readlines()
            
            steps = int(lines[0].split(' ')[3]) # koraci temperature
            
            for i in range(len(search_string_in_file('podaci.txt','|Magnetization|'))):
                gde_mag.append(search_string_in_file('podaci.txt','|Magnetization|')[i][0])

            for i in range(len(search_string_in_file('podaci.txt','Susceptibility'))):
                gde_susc.append(search_string_in_file('podaci.txt','Susceptibility')[i][0])

            
            for i in range(len(search_string_in_file('podaci.txt','Specific'))):
                gde_spec.append(search_string_in_file('podaci.txt','Specific')[i][0])

            
            for i in range(len(search_string_in_file('podaci.txt','Binder'))):
                gde_binder.append(search_string_in_file('podaci.txt','Binder')[i][0])


            for i in range(len(gde_mag)):
                mag_l.append(float(lines[gde_mag[i]-2].split(' = ')[1]))

            for i in range(len(gde_susc)):
                susc_l.append(float(lines[gde_susc[i]-2].split(' = ')[1]))

            for i in range(len(gde_spec)):
                spec_l.append(float(lines[gde_spec[i]-2].split(' = ')[1]))

            for i in range(len(gde_binder)):
                binder_l.append(float(lines[gde_binder[i]-2].split(' = ')[1]))

            # MAGNETIZACIJA

            for j in range(len(gde_mag)):
                for i in range(steps):
                    values_mag_temp.append(float(lines[gde_mag[j]+1+i].split(' ')[0].split('\t')[0]))    

            for j in range(len(gde_mag)):
                for i in range(steps):
                    values_mag.append(float(lines[gde_mag[j]+1+i].split(' ')[0].split('\t')[1]))

            for j in range(len(gde_mag)):
                for i in range(steps):
                    values_mag_err.append(float(lines[gde_mag[j]+1+i].split('+/- ')[1]))

            # SUSCEPTIBILNOST

            for j in range(len(gde_susc)):
                for i in range(steps):
                    values_susc_temp.append(float(lines[gde_susc[j]+1+i].split(' ')[0].split('\t')[0]))    

            for j in range(len(gde_susc)):
                for i in range(steps):
                    values_susc.append(float(lines[gde_susc[j]+1+i].split(' ')[0].split('\t')[1]))

            for j in range(len(gde_susc)):
                for i in range(steps):
                    values_susc_err.append(float(lines[gde_susc[j]+1+i].split('+/- ')[1]))

            # SPECIFICNA TOPLOTA

            for j in range(len(gde_spec)):
                for i in range(steps):
                    values_spec_temp.append(float(lines[gde_spec[j]+1+i].split(' ')[0].split('\t')[0]))    

            for j in range(len(gde_spec)):
                for i in range(steps):
                    values_spec.append(float(lines[gde_spec[j]+1+i].split(' ')[0].split('\t')[1]))

            for j in range(len(gde_spec)):
                for i in range(steps):
                    values_spec_err.append(float(lines[gde_spec[j]+1+i].split('+/- ')[1]))

            # BINDEROV KUMULANT

            for j in range(len(gde_binder)):
                for i in range(steps):
                    values_binder_temp.append(float(lines[gde_binder[j]+1+i].split(' ')[0].split('\t')[0]))

            for j in range(len(gde_binder)):
                for i in range(steps):
                    values_binder.append(float(lines[gde_binder[j]+1+i].split(' ')[0].split('\t')[1]))

            for j in range(len(gde_binder)):
                for i in range(steps):
                    values_binder_err.append(float(lines[gde_binder[j]+1+i].split('+/- ')[1]))
        else:
            self.label_4.setText("Dokument podaci.txt se ne nalazi u folderu!")
            self.label_4.setStyleSheet("background-color: red; border: 1px solid black;")
            self.updatelabel1()

    def updatelabel1(self):
        self.label_4.adjustSize()

    

    def grafici(self):
        global steps,gde_mag,gde_susc,gde_spec,gde_binder,mag_l,susc_l,spec_l,binder_l,values_mag_temp,values_mag,values_mag_err
        global values_susc_temp,values_susc,values_susc_err,values_spec_temp,values_spec,values_spec_err,values_binder_temp,values_binder,values_binder_err
        vrednost=self.comboBox.currentText()
        if vrednost == 'Magnetizacija':
            self.widget.canvas.axes.clear()
            for k in range(len(mag_l)):
                self.widget.canvas.axes.errorbar(values_mag_temp[k*steps:(k+1)*steps],values_mag[k*steps:(k+1)*steps],yerr=values_mag_err[k*steps:(k+1)*steps],label='L = %.1f'%(mag_l[k]))
            self.widget.canvas.axes.set_title(u"Temperaturska zavisnost magnetizacije")
            self.widget.canvas.axes.set_xlabel(r'$T$')
            self.widget.canvas.axes.set_ylabel(ur"Magnetizacija $|M|$")
            self.widget.canvas.axes.legend(loc='best')
            self.widget.canvas.draw()
        elif vrednost == u'Specifična toplota':
            self.widget.canvas.axes.clear()
            for k in range(len(spec_l)):
                self.widget.canvas.axes.errorbar(values_spec_temp[k*steps:(k+1)*steps],values_spec[k*steps:(k+1)*steps],yerr=values_spec_err[k*steps:(k+1)*steps],label='L = %.1f'%(spec_l[k]))
            self.widget.canvas.axes.set_title(u"Temperaturska zavisnost specifične toplote")
            self.widget.canvas.axes.set_xlabel(r'$T$')
            self.widget.canvas.axes.set_ylabel(ur"Specifična toplota $C_{V}$")
            self.widget.canvas.axes.legend(loc='best')
            self.widget.canvas.draw()
        elif vrednost == 'Susceptibilnost':
            self.widget.canvas.axes.clear()
            for k in range(len(susc_l)):
                self.widget.canvas.axes.errorbar(values_susc_temp[k*steps:(k+1)*steps],values_susc[k*steps:(k+1)*steps],yerr=values_susc_err[k*steps:(k+1)*steps],label='L = %.1f'%(susc_l[k]))
            self.widget.canvas.axes.set_title(u"Temperaturska zavisnost susceptibilnosti")
            self.widget.canvas.axes.set_xlabel(r'$T$')
            self.widget.canvas.axes.set_ylabel(ur"Susceptibilnost $\chi$")
            self.widget.canvas.axes.legend(loc='best')
            self.widget.canvas.draw()
        elif vrednost == 'Binderov kumulant':
            self.widget.canvas.axes.clear()
            for k in range(len(binder_l)):
                self.widget.canvas.axes.errorbar(values_binder_temp[k*steps:(k+1)*steps],values_binder[k*steps:(k+1)*steps],yerr=values_binder_err[k*steps:(k+1)*steps],label='L = %.1f'%(binder_l[k]))
            self.widget.canvas.axes.set_title(u"Temperaturska zavisnost Binderovog kumulanta")
            self.widget.canvas.axes.set_xlabel(r'$T$')
            self.widget.canvas.axes.set_ylabel(ur"Binderov kumulant $U_{4}$")
            self.widget.canvas.axes.legend(loc='best')
            self.widget.canvas.draw()
        else:
            pass
        
    def procenatc(self):
        global steps,gde_mag,gde_susc,gde_spec,gde_binder,mag_l,susc_l,spec_l,binder_l,values_mag_temp,values_mag,values_mag_err
        global values_susc_temp,values_susc,values_susc_err,values_spec_temp,values_spec,values_spec_err,values_binder_temp,values_binder,values_binder_err
        tc = float(self.lineEdit.text())
        x = (np.array(values_binder_temp)-tc)/(tc)
        y = np.array(values_binder)
        z = np.array(values_binder_err)
        self.widget_2.canvas.axes.clear()
        for k in range(len(binder_l)):
            self.widget_2.canvas.axes.errorbar(x[k*steps:(k+1)*steps],y[k*steps:(k+1)*steps],yerr=z[k*steps:(k+1)*steps],label='L = %.1f'%(binder_l[k]))
        self.widget_2.canvas.axes.set_title(u"Zavisnost Binderovog kumulanta od redukovane temperature")
        self.widget_2.canvas.axes.set_xlabel(r'$(T-T_{C})/T_{C}$')
        self.widget_2.canvas.axes.set_ylabel(r"$U_{4}$")
        self.widget_2.canvas.axes.legend(loc='best')
        self.widget_2.canvas.draw()

    def zoom(self):
        global steps,gde_mag,gde_susc,gde_spec,gde_binder,mag_l,susc_l,spec_l,binder_l,values_mag_temp,values_mag,values_mag_err
        global values_susc_temp,values_susc,values_susc_err,values_spec_temp,values_spec,values_spec_err,values_binder_temp,values_binder,values_binder_err
        global xmin,xmax,ymin,ymax
        tc = float(self.lineEdit.text())
        if self.lineEdit_3.text() == '':
            xmin = xmin
        else:
            xmin = float(self.lineEdit_3.text())
        
        if self.lineEdit_2.text()=='':
            xmax = xmax
        else:
            xmax = float(self.lineEdit_2.text())

        if self.lineEdit_5.text() == '':
            ymin = ymin
        else:
            ymin = float(self.lineEdit_5.text())

        if self.lineEdit_4.text() == '':
            ymax = ymax
        else:
            ymax = float(self.lineEdit_4.text())

        x = (np.array(values_binder_temp)-tc)/(tc)
        y = np.array(values_binder)
        z = np.array(values_binder_err)
        self.widget_3.canvas.axes.clear()
        for k in range(len(binder_l)):
            self.widget_3.canvas.axes.errorbar(x[k*steps:(k+1)*steps],y[k*steps:(k+1)*steps],yerr=z[k*steps:(k+1)*steps],label='L = %.1f'%(mag_l[k]))
        self.widget_3.canvas.axes.set_title(u"Zoom")
        self.widget_3.canvas.axes.set_xlabel(r'$(T-T_{C})/T_{C}$')
        self.widget_3.canvas.axes.set_ylabel(r"$U_{4}$")
        self.widget_3.canvas.axes.set_xlim(xmin,xmax)
        self.widget_3.canvas.axes.set_ylim(ymin,ymax)
        self.widget_3.canvas.axes.legend(loc='best')
        self.widget_3.canvas.draw()

    def tcfit(self):
        global steps,gde_mag,gde_susc,gde_spec,gde_binder,mag_l,susc_l,spec_l,binder_l,values_mag_temp,values_mag,values_mag_err
        global values_susc_temp,values_susc,values_susc_err,values_spec_temp,values_spec,values_spec_err,values_binder_temp,values_binder,values_binder_err
        l=float(self.lineEdit_7.text())
        tstart = float(self.lineEdit_8.text())
        tstop = float(self.lineEdit_9.text())
        for i in range(0,len(binder_l)):
            exec("x%d = values_binder_temp[i*steps:i*steps+steps]" % (int(binder_l[i])))
        for i in range(0,len(binder_l)):
            exec("y%d = values_binder[i*steps:i*steps+steps]" % (int(binder_l[i])))
        nova = []
        for i in range(len(binder_l)):
            nova.append(int(binder_l[i]))

        nova.remove(int(l))
        listaintersceptsx=[]
        listaintersceptsy=[]
        for i in range(len(nova)):
            xprvi = []
            xdrugi = []
            yprvi = []
            ydrugi = []
            exec('xprvi = x%d'% (int(l)))
            exec('yprvi = y%d'% (int(l)))
            exec('xdrugi = x%d'% (nova[i]))
            exec('ydrugi = y%d'% (nova[i]))
            xintercept, yintercept = intersection(xprvi,yprvi,xdrugi,ydrugi)
            for j in range(0,len(xintercept)):
                if tstart<= xintercept[j] <= tstop:
                    listaintersceptsx.append(xintercept[j])
                    listaintersceptsy.append(yintercept[j])

        lodnosi=[(float(i)/l) for i in nova]

        xosa=1/np.log(lodnosi)
        def test_funk(x,a,b):
            return a*x+b
        params, params_cov=optimize.curve_fit(test_funk,xosa,listaintersceptsx)
        greskatc = np.sqrt(np.diag(params_cov))[1]

        self.widget_4.canvas.axes.clear()
        self.widget_4.canvas.axes.scatter(xosa,listaintersceptsx,label='Podaci',color='blue')
        self.widget_4.canvas.axes.plot(xosa,test_funk(xosa,params[0],params[1]),label='Linear fit',color='black')
        self.widget_4.canvas.axes.set_xlabel(r'$1/ln(L\'/L)$')
        self.widget_4.canvas.axes.set_ylabel(r"$T_{C}$")
        self.widget_4.canvas.axes.legend(loc='best')
        self.widget_4.canvas.draw()

        self.label_18.setText("T<sub>C</sub>="+str(params[1])+'±'+str(greskatc))
        self.updatelabel2()

    def updatelabel2(self):
        self.label_18.adjustSize()


    def nu(self):
        global steps,gde_mag,gde_susc,gde_spec,gde_binder,mag_l,susc_l,spec_l,binder_l,values_mag_temp,values_mag,values_mag_err
        global values_susc_temp,values_susc,values_susc_err,values_spec_temp,values_spec,values_spec_err,values_binder_temp,values_binder,values_binder_err
        tc = float(self.lineEdit_10.text())
        nu = float(self.lineEdit_6.text())
        x = (np.array(values_binder_temp)-tc)/(tc)
        y = np.array(values_binder)
        z = np.array(values_binder_err)
        self.widget_5.canvas.axes.clear()
        for k in range(len(binder_l)):
            self.widget_5.canvas.axes.errorbar(x[k*steps:(k+1)*steps]*binder_l[k]**(nu),y[k*steps:(k+1)*steps],yerr=z[k*steps:(k+1)*steps],label='L = %.1f'%(binder_l[k]))
        self.widget_5.canvas.axes.set_title(ur"Zavisnost $U_{4}=f(L^{1/\nu}(T-T_{C})/T_{C})$")
        self.widget_5.canvas.axes.set_xlabel(r'$L^{1/\nu}(T-T_{C})/T_{C}$')
        self.widget_5.canvas.axes.set_ylabel(r"$U_{4}$")
        self.widget_5.canvas.axes.legend(loc='best')
        self.widget_5.canvas.draw()

    def gama(self):
        global steps,gde_susc,susc_l
        global values_susc_temp,values_susc,values_susc_err
        xlista = []
        ylista = []
        for i in range(0,len(susc_l)):
            lista_temp = [] 
            for k in range(len(values_susc[i*steps:i*steps+steps])):
                lista_temp.append(values_susc[i*steps:i*steps+steps][k])
            nova_list = []
            for item in lista_temp:
                if str(item) != 'nan':
                    nova_list.append(item)
            maksimum = max(nova_list)
            ylista.append(maksimum)
            xlista.append(susc_l[i])

        def test_funk(x,a,b):
            return a*x**b

        paramsg,params_covarianceg=optimize.curve_fit(test_funk,xlista,ylista)
        greskanu = np.sqrt(np.diag(params_covarianceg))[1]

        self.widget_6.canvas.axes.clear()
        self.widget_6.canvas.axes.scatter(xlista,ylista,label='Podaci',color='blue')
        self.widget_6.canvas.axes.plot(xlista,test_funk(xlista,paramsg[0],paramsg[1]),label='Fit',color='black')
        self.widget_6.canvas.axes.set_xlabel(r'$L$')
        self.widget_6.canvas.axes.set_ylabel(r"$\chi(T_{C})\equiv \chi^{max}$")
        self.widget_6.canvas.axes.legend(loc='best')
        self.widget_6.canvas.draw()

        self.label_25.setText(str(paramsg[1])+'±'+str(greskanu))
        self.updatelabel3()

    def updatelabel3(self):
        self.label_25.adjustSize()

    def alfa(self):
        global steps,gde_spec,spec_l
        global values_spec_temp,values_spec,values_spec_err
        xlista = []
        ylista = []
        for i in range(0,len(spec_l)):
            lista_temp = [] 
            for k in range(len(values_spec[i*steps:i*steps+steps])):
                lista_temp.append(values_spec[i*steps:i*steps+steps][k])
            nova_list = []
            for item in lista_temp:
                if str(item) != 'nan':
                    nova_list.append(item)
            maksimum = max(nova_list)
            ylista.append(maksimum)
            xlista.append(susc_l[i])

        def test_funk(x,a,b):
            return a*x**b

        paramsa,params_covariancea=optimize.curve_fit(test_funk,xlista,ylista)
        greskaalfa = np.sqrt(np.diag(params_covariancea))[1]

        self.widget_7.canvas.axes.clear()
        self.widget_7.canvas.axes.scatter(xlista,ylista,label='Podaci',color='blue')
        self.widget_7.canvas.axes.plot(xlista,test_funk(xlista,paramsa[0],paramsa[1]),label='Fit',color='black')
        self.widget_7.canvas.axes.set_xlabel(r'$L$')
        self.widget_7.canvas.axes.set_ylabel(r"$C_{V}(T_{C})\equiv \chi_{V}^{max}$")
        self.widget_7.canvas.axes.legend(loc='best')
        self.widget_7.canvas.draw()

        self.label_27.setText(str(paramsa[1])+'±'+str(greskaalfa))
        self.updatelabel4()

    def updatelabel4(self):
        self.label_27.adjustSize()


    def beta(self):
        global steps,gde_mag,mag_l,values_mag_temp,values_mag,values_mag_err
        tc = float(self.lineEdit_12.text())
        nu = float(self.lineEdit_11.text())
        betanu = float(self.lineEdit_13.text())
        x = (np.array(values_mag_temp)-tc)/(tc)
        y = np.array(values_mag)
        self.widget_8.canvas.axes.clear()
        for k in range(len(mag_l)):
            self.widget_8.canvas.axes.errorbar(x[k*steps:(k+1)*steps]*pow(mag_l[k],nu),y[k*steps:(k+1)*steps]/pow(mag_l[k],-betanu),label='L = %.1f'%(mag_l[k]))
        self.widget_8.canvas.axes.set_title(ur"Zavisnost $|M|=L^{-\beta/\nu}f(L^{1/\nu}(T-T_{C})/T_{C})$")
        self.widget_8.canvas.axes.set_xlabel(r'$L^{1/\nu}(T-T_{C})/T_{C}$')
        self.widget_8.canvas.axes.set_ylabel(r"$|M|$")
        self.widget_8.canvas.axes.legend(loc='best')
        self.widget_8.canvas.draw()


app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()
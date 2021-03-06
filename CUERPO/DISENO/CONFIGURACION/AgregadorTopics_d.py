# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregadorTopics_d.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(375, 355)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(300, 40))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_actualizarTopcis = QtWidgets.QPushButton(Dialog)
        self.btn_actualizarTopcis.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_actualizarTopcis.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_actualizarTopcis.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_actualizarTopcis.setBaseSize(QtCore.QSize(30, 30))
        self.btn_actualizarTopcis.setStyleSheet("QPushButton {\n"
"border-image: url(:/main/IMAGENES/cargar_off.png);\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/main/IMAGENES/cargar_on.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/main/IMAGENES/cargar_off.png);\n"
"}\n"
"")
        self.btn_actualizarTopcis.setText("")
        self.btn_actualizarTopcis.setObjectName("btn_actualizarTopcis")
        self.verticalLayout_2.addWidget(self.btn_actualizarTopcis)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setMinimumSize(QtCore.QSize(35, 35))
        self.label_11.setMaximumSize(QtCore.QSize(30, 30))
        self.label_11.setBaseSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(200, 40))
        self.label_4.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.listWidget_topicsTareasProgramas = QtWidgets.QListWidget(Dialog)
        self.listWidget_topicsTareasProgramas.setMinimumSize(QtCore.QSize(200, 0))
        self.listWidget_topicsTareasProgramas.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget_topicsTareasProgramas.setObjectName("listWidget_topicsTareasProgramas")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_topicsTareasProgramas.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_topicsTareasProgramas.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_topicsTareasProgramas.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_topicsTareasProgramas.addItem(item)
        self.verticalLayout.addWidget(self.listWidget_topicsTareasProgramas)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.btn_agregar = QtWidgets.QPushButton(Dialog)
        self.btn_agregar.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_agregar.setMaximumSize(QtCore.QSize(150, 60))
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout_2.addWidget(self.btn_agregar)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Selecciona segun corresponda"))
        self.label_11.setText(_translate("Dialog", "Refrescar"))
        self.label_4.setText(_translate("Dialog", "Topic tareas programas"))
        __sortingEnabled = self.listWidget_topicsTareasProgramas.isSortingEnabled()
        self.listWidget_topicsTareasProgramas.setSortingEnabled(False)
        item = self.listWidget_topicsTareasProgramas.item(0)
        item.setText(_translate("Dialog", "hola"))
        item = self.listWidget_topicsTareasProgramas.item(1)
        item.setText(_translate("Dialog", "como"))
        item = self.listWidget_topicsTareasProgramas.item(2)
        item.setText(_translate("Dialog", "estas"))
        item = self.listWidget_topicsTareasProgramas.item(3)
        item.setText(_translate("Dialog", "miNombre"))
        self.listWidget_topicsTareasProgramas.setSortingEnabled(__sortingEnabled)
        self.btn_agregar.setText(_translate("Dialog", "Agregar"))
import img_rc

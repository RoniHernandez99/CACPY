# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CargadorCrendencial_d.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 414)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(350, 120))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.bel_nombreArchivoSelec = QtWidgets.QLabel(self.centralwidget)
        self.bel_nombreArchivoSelec.setMinimumSize(QtCore.QSize(300, 40))
        self.bel_nombreArchivoSelec.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bel_nombreArchivoSelec.setFont(font)
        self.bel_nombreArchivoSelec.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_nombreArchivoSelec.setObjectName("bel_nombreArchivoSelec")
        self.horizontalLayout_5.addWidget(self.bel_nombreArchivoSelec)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_abrirExploradorArchivos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abrirExploradorArchivos.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_abrirExploradorArchivos.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_abrirExploradorArchivos.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_abrirExploradorArchivos.setBaseSize(QtCore.QSize(30, 30))
        self.btn_abrirExploradorArchivos.setStyleSheet("QPushButton {\n"
"\n"
"border-image: url(:/main/IMAGENES/subir_off.png);\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/main/IMAGENES/subir_on.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/main/IMAGENES/subir_off.png);\n"
"}\n"
"")
        self.btn_abrirExploradorArchivos.setText("")
        self.btn_abrirExploradorArchivos.setObjectName("btn_cargarArchivos")
        self.verticalLayout_2.addWidget(self.btn_abrirExploradorArchivos)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMinimumSize(QtCore.QSize(35, 35))
        self.label_11.setMaximumSize(QtCore.QSize(30, 30))
        self.label_11.setBaseSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.btn_finalizar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_finalizar.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_finalizar.setMaximumSize(QtCore.QSize(120, 70))
        self.btn_finalizar.setObjectName("btn_finalizar")
        self.horizontalLayout.addWidget(self.btn_finalizar)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Instrucciones:Antes de iniciar el programa, debes cargar el archivo que contiene tus credenciales,una vez cargado dicho archivo da clic sobre el boton cuya  leyenda es: <<Validar archivo>>, si el archivo de credenciales cargado es correcto, el programa te avisara que se ha cargado con exito y que ya puedes cerrar esta ventana."))
        self.label_2.setText(_translate("MainWindow", "Arhicivo cargado:"))
        self.bel_nombreArchivoSelec.setText(_translate("MainWindow", "Ningun archivo seleccionado"))
        self.label_11.setText(_translate("MainWindow", "Cargar archivo"))
        self.btn_finalizar.setText(_translate("MainWindow", "Validar archivo"))
import img_rc

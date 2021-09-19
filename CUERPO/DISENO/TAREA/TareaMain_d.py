# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TareaMain_d.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 526)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setMinimumSize(QtCore.QSize(60, 50))
        self.label_8.setMaximumSize(QtCore.QSize(50, 50))
        self.label_8.setBaseSize(QtCore.QSize(40, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.bel_nombreCurso = QtWidgets.QLabel(Form)
        self.bel_nombreCurso.setMinimumSize(QtCore.QSize(200, 50))
        self.bel_nombreCurso.setMaximumSize(QtCore.QSize(16777215, 50))
        self.bel_nombreCurso.setBaseSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bel_nombreCurso.setFont(font)
        self.bel_nombreCurso.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.bel_nombreCurso.setObjectName("bel_nombreCurso")
        self.horizontalLayout_10.addWidget(self.bel_nombreCurso)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setMinimumSize(QtCore.QSize(60, 50))
        self.label_9.setMaximumSize(QtCore.QSize(50, 50))
        self.label_9.setBaseSize(QtCore.QSize(40, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.bel_nombreTopic = QtWidgets.QLabel(Form)
        self.bel_nombreTopic.setMinimumSize(QtCore.QSize(200, 50))
        self.bel_nombreTopic.setMaximumSize(QtCore.QSize(16777215, 50))
        self.bel_nombreTopic.setBaseSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bel_nombreTopic.setFont(font)
        self.bel_nombreTopic.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.bel_nombreTopic.setObjectName("bel_nombreTopic")
        self.horizontalLayout_11.addWidget(self.bel_nombreTopic)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.listWidget = QtWidgets.QStackedWidget(Form)
        self.listWidget.setToolTipDuration(0)
        self.listWidget.setStyleSheet("padding:0px;\n"
"margin:0px;\n"
"\n"
"")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setObjectName("listWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_2 = QtWidgets.QWidget(self.page)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setMinimumSize(QtCore.QSize(0, 18))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_importarTarea = QtWidgets.QPushButton(self.widget_2)
        self.btn_importarTarea.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_importarTarea.setMaximumSize(QtCore.QSize(35, 35))
        self.btn_importarTarea.setBaseSize(QtCore.QSize(30, 30))
        self.btn_importarTarea.setStyleSheet("\n"
"QPushButton {\n"
"border-image: url(:/main/IMAGENES/plus_off.png);\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/main/IMAGENES/plus_on.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/main/IMAGENES/plus_off.png);\n"
"}\n"
"")
        self.btn_importarTarea.setText("")
        self.btn_importarTarea.setObjectName("btn_importarTarea")
        self.verticalLayout_3.addWidget(self.btn_importarTarea)
        self.bel_agregar_or_guardar_apar = QtWidgets.QLabel(self.widget_2)
        self.bel_agregar_or_guardar_apar.setMinimumSize(QtCore.QSize(35, 35))
        self.bel_agregar_or_guardar_apar.setMaximumSize(QtCore.QSize(35, 35))
        self.bel_agregar_or_guardar_apar.setBaseSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.bel_agregar_or_guardar_apar.setFont(font)
        self.bel_agregar_or_guardar_apar.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_agregar_or_guardar_apar.setWordWrap(True)
        self.bel_agregar_or_guardar_apar.setObjectName("bel_agregar_or_guardar_apar")
        self.verticalLayout_3.addWidget(self.bel_agregar_or_guardar_apar)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, 20, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_crearTarea = QtWidgets.QPushButton(self.widget_2)
        self.btn_crearTarea.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_crearTarea.setMaximumSize(QtCore.QSize(35, 35))
        self.btn_crearTarea.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_crearTarea.setBaseSize(QtCore.QSize(30, 30))
        self.btn_crearTarea.setStyleSheet("QPushButton {\n"
"    border-image: url(:/main/IMAGENES/crear_off.png);\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/main/IMAGENES/crear_on.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/main/IMAGENES/crear_off.png);\n"
"}\n"
"")
        self.btn_crearTarea.setText("")
        self.btn_crearTarea.setObjectName("btn_crearTarea")
        self.verticalLayout_5.addWidget(self.btn_crearTarea)
        self.bel_agregar_or_guardar_apar_2 = QtWidgets.QLabel(self.widget_2)
        self.bel_agregar_or_guardar_apar_2.setMinimumSize(QtCore.QSize(35, 35))
        self.bel_agregar_or_guardar_apar_2.setMaximumSize(QtCore.QSize(35, 35))
        self.bel_agregar_or_guardar_apar_2.setBaseSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.bel_agregar_or_guardar_apar_2.setFont(font)
        self.bel_agregar_or_guardar_apar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_agregar_or_guardar_apar_2.setWordWrap(True)
        self.bel_agregar_or_guardar_apar_2.setObjectName("bel_agregar_or_guardar_apar_2")
        self.verticalLayout_5.addWidget(self.bel_agregar_or_guardar_apar_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_8.addWidget(self.tableWidget)
        self.verticalLayout_9.addWidget(self.widget_2)
        self.listWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_3 = QtWidgets.QWidget(self.page_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setMinimumSize(QtCore.QSize(100, 30))
        self.label_4.setMaximumSize(QtCore.QSize(70, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.bel_nombre = QtWidgets.QLabel(self.widget_3)
        self.bel_nombre.setMinimumSize(QtCore.QSize(200, 30))
        self.bel_nombre.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bel_nombre.setStyleSheet("border: 2px solid   black;\n"
"border-radius:5px\n"
"")
        self.bel_nombre.setText("")
        self.bel_nombre.setObjectName("bel_nombre")
        self.horizontalLayout_7.addWidget(self.bel_nombre)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setMinimumSize(QtCore.QSize(100, 30))
        self.label_5.setMaximumSize(QtCore.QSize(70, 30))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.bel_fechaCreacion = QtWidgets.QLabel(self.widget_3)
        self.bel_fechaCreacion.setMinimumSize(QtCore.QSize(200, 30))
        self.bel_fechaCreacion.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bel_fechaCreacion.setStyleSheet("border: 2px solid   black;\n"
"border-radius:5px\n"
"")
        self.bel_fechaCreacion.setText("")
        self.bel_fechaCreacion.setObjectName("bel_fechaCreacion")
        self.horizontalLayout_8.addWidget(self.bel_fechaCreacion)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setMinimumSize(QtCore.QSize(70, 30))
        self.label_3.setMaximumSize(QtCore.QSize(70, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.bel_noTareasCalificadas = QtWidgets.QLabel(self.widget_3)
        self.bel_noTareasCalificadas.setMinimumSize(QtCore.QSize(30, 30))
        self.bel_noTareasCalificadas.setMaximumSize(QtCore.QSize(40, 40))
        self.bel_noTareasCalificadas.setStyleSheet("border: 2px solid   black;\n"
"border-radius:5px\n"
"")
        self.bel_noTareasCalificadas.setText("")
        self.bel_noTareasCalificadas.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_noTareasCalificadas.setObjectName("bel_noTareasCalificadas")
        self.horizontalLayout_2.addWidget(self.bel_noTareasCalificadas)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.widget_3)
        self.label_14.setMinimumSize(QtCore.QSize(70, 30))
        self.label_14.setMaximumSize(QtCore.QSize(70, 30))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.bel_noTareasPorCalificar = QtWidgets.QLabel(self.widget_3)
        self.bel_noTareasPorCalificar.setMinimumSize(QtCore.QSize(30, 30))
        self.bel_noTareasPorCalificar.setMaximumSize(QtCore.QSize(40, 40))
        self.bel_noTareasPorCalificar.setStyleSheet("border: 2px solid   black;\n"
"border-radius:5px\n"
"")
        self.bel_noTareasPorCalificar.setText("")
        self.bel_noTareasPorCalificar.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_noTareasPorCalificar.setObjectName("bel_noTareasPorCalificar")
        self.horizontalLayout_4.addWidget(self.bel_noTareasPorCalificar)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.widget_3)
        self.label_18.setMinimumSize(QtCore.QSize(70, 30))
        self.label_18.setMaximumSize(QtCore.QSize(70, 30))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.bel_noTareasPorEntregar = QtWidgets.QLabel(self.widget_3)
        self.bel_noTareasPorEntregar.setMinimumSize(QtCore.QSize(30, 30))
        self.bel_noTareasPorEntregar.setMaximumSize(QtCore.QSize(40, 40))
        self.bel_noTareasPorEntregar.setStyleSheet("border: 2px solid   black;\n"
"border-radius:5px\n"
"")
        self.bel_noTareasPorEntregar.setText("")
        self.bel_noTareasPorEntregar.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_noTareasPorEntregar.setObjectName("bel_noTareasPorEntregar")
        self.horizontalLayout_6.addWidget(self.bel_noTareasPorEntregar)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_13.setSpacing(50)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.widget_3)
        self.label_13.setMinimumSize(QtCore.QSize(120, 50))
        self.label_13.setMaximumSize(QtCore.QSize(120, 50))
        self.label_13.setBaseSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_13.addWidget(self.label_13)
        self.btn_calificarPendientes = QtWidgets.QPushButton(self.widget_3)
        self.btn_calificarPendientes.setMinimumSize(QtCore.QSize(120, 100))
        self.btn_calificarPendientes.setMaximumSize(QtCore.QSize(120, 100))
        self.btn_calificarPendientes.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_calificarPendientes.setBaseSize(QtCore.QSize(30, 30))
        self.btn_calificarPendientes.setStyleSheet("QPushButton {\n"
"border-image: url(:/main/IMAGENES/calificar_off.png);\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/main/IMAGENES/calificar_on.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/main/IMAGENES/calificar_off.png);\n"
"}")
        self.btn_calificarPendientes.setText("")
        self.btn_calificarPendientes.setObjectName("btn_calificarPendientes")
        self.verticalLayout_13.addWidget(self.btn_calificarPendientes)
        self.horizontalLayout_13.addLayout(self.verticalLayout_13)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.btn_regresar = QtWidgets.QCommandLinkButton(self.widget_3)
        self.btn_regresar.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_regresar.setMaximumSize(QtCore.QSize(120, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/IMAGENES/regresar_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/main/IMAGENES/regresar_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_regresar.setIcon(icon)
        self.btn_regresar.setCheckable(False)
        self.btn_regresar.setObjectName("btn_regresar")
        self.horizontalLayout_14.addWidget(self.btn_regresar)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.verticalLayout_7.addWidget(self.widget_3)
        self.listWidget.addWidget(self.page_2)
        self.verticalLayout_4.addWidget(self.listWidget)

        self.retranslateUi(Form)
        self.listWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Clase:"))
        self.bel_nombreCurso.setText(_translate("Form", "Python pre-intermedio"))
        self.label_9.setText(_translate("Form", "Topic:"))
        self.bel_nombreTopic.setText(_translate("Form", "Python pre-intermedio"))
        self.label_7.setText(_translate("Form", "Tareas asignadas"))
        self.bel_agregar_or_guardar_apar.setText(_translate("Form", "Importar\n"
"apartado"))
        self.bel_agregar_or_guardar_apar_2.setText(_translate("Form", "Crear\n"
"tarea"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Fecha creacion"))
        self.label_4.setText(_translate("Form", "Nombre:"))
        self.label_5.setText(_translate("Form", "Fecha emision:"))
        self.label_3.setText(_translate("Form", "Calificadas:"))
        self.label_14.setText(_translate("Form", "Por calificar:"))
        self.label_18.setText(_translate("Form", "Por entregar:"))
        self.label_13.setText(_translate("Form", "Calificar tareas"))
        self.btn_regresar.setText(_translate("Form", "Regresar "))
import img_rc

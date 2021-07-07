# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalificadorEnDirecto_d.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 486)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(100, 30))
        self.label_4.setMaximumSize(QtCore.QSize(70, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.bel_nombre = QtWidgets.QLabel(Dialog)
        self.bel_nombre.setMinimumSize(QtCore.QSize(200, 30))
        self.bel_nombre.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bel_nombre.setStyleSheet("border: 2px solid   black;\n"
"border-radius:5px\n"
"")
        self.bel_nombre.setText("")
        self.bel_nombre.setObjectName("bel_nombre")
        self.horizontalLayout_7.addWidget(self.bel_nombre)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setMinimumSize(QtCore.QSize(100, 30))
        self.label_5.setMaximumSize(QtCore.QSize(70, 30))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.bel_fechaCreacion = QtWidgets.QLabel(Dialog)
        self.bel_fechaCreacion.setMinimumSize(QtCore.QSize(200, 30))
        self.bel_fechaCreacion.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bel_fechaCreacion.setStyleSheet("border: 2px solid   black;\n"
"border-radius:5px\n"
"")
        self.bel_fechaCreacion.setText("")
        self.bel_fechaCreacion.setObjectName("bel_fechaCreacion")
        self.horizontalLayout_8.addWidget(self.bel_fechaCreacion)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(70, 30))
        self.label_3.setMaximumSize(QtCore.QSize(70, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.bel_noTareasCalificadas = QtWidgets.QLabel(Dialog)
        self.bel_noTareasCalificadas.setMinimumSize(QtCore.QSize(30, 30))
        self.bel_noTareasCalificadas.setMaximumSize(QtCore.QSize(40, 40))
        self.bel_noTareasCalificadas.setStyleSheet("border: 2px solid   black;\n"
"border-radius:5px\n"
"")
        self.bel_noTareasCalificadas.setText("")
        self.bel_noTareasCalificadas.setObjectName("bel_noTareasCalificadas")
        self.horizontalLayout.addWidget(self.bel_noTareasCalificadas)
        self.horizontalLayout_10.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setMinimumSize(QtCore.QSize(70, 30))
        self.label_14.setMaximumSize(QtCore.QSize(70, 30))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.bel_noTareasPorCalificar = QtWidgets.QLabel(Dialog)
        self.bel_noTareasPorCalificar.setMinimumSize(QtCore.QSize(30, 30))
        self.bel_noTareasPorCalificar.setMaximumSize(QtCore.QSize(40, 40))
        self.bel_noTareasPorCalificar.setStyleSheet("border: 2px solid   black;\n"
"border-radius:5px\n"
"")
        self.bel_noTareasPorCalificar.setText("")
        self.bel_noTareasPorCalificar.setObjectName("bel_noTareasPorCalificar")
        self.horizontalLayout_4.addWidget(self.bel_noTareasPorCalificar)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setMinimumSize(QtCore.QSize(70, 30))
        self.label_18.setMaximumSize(QtCore.QSize(70, 30))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.bel_noTareasPorEntregar = QtWidgets.QLabel(Dialog)
        self.bel_noTareasPorEntregar.setMinimumSize(QtCore.QSize(30, 30))
        self.bel_noTareasPorEntregar.setMaximumSize(QtCore.QSize(40, 40))
        self.bel_noTareasPorEntregar.setStyleSheet("border: 2px solid   black;\n"
"border-radius:5px\n"
"")
        self.bel_noTareasPorEntregar.setText("")
        self.bel_noTareasPorEntregar.setObjectName("bel_noTareasPorEntregar")
        self.horizontalLayout_6.addWidget(self.bel_noTareasPorEntregar)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CALIFICACION EN DIRECTO"))
        self.label_4.setText(_translate("Dialog", "Nombre:"))
        self.label_5.setText(_translate("Dialog", "Fecha emision:"))
        self.label_3.setText(_translate("Dialog", "Calificadas:"))
        self.label_14.setText(_translate("Dialog", "Por calificar:"))
        self.label_18.setText(_translate("Dialog", "Por entregar:"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles\Automat.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Automat(object):
    def setupUi(self, Automat):
        Automat.setObjectName("Automat")
        Automat.resize(420, 529)
        self.gridLayout_3 = QtWidgets.QGridLayout(Automat)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(0, 0, 0, -1)
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_9 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.label_2 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_11 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_11)
        self.line_field_size_x = QtWidgets.QLineEdit(Automat)
        self.line_field_size_x.setObjectName("line_field_size_x")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.line_field_size_x)
        self.line_disturbance_start_x = QtWidgets.QLineEdit(Automat)
        self.line_disturbance_start_x.setObjectName("line_disturbance_start_x")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_disturbance_start_x)
        self.label_3 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_12 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_12)
        self.line_field_size_y = QtWidgets.QLineEdit(Automat)
        self.line_field_size_y.setObjectName("line_field_size_y")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.line_field_size_y)
        self.line_disturbance_start_y = QtWidgets.QLineEdit(Automat)
        self.line_disturbance_start_y.setObjectName("line_disturbance_start_y")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.line_disturbance_start_y)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.label_13 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_13)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.line_disturbance_size_dx = QtWidgets.QLineEdit(Automat)
        self.line_disturbance_size_dx.setObjectName("line_disturbance_size_dx")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.line_disturbance_size_dx)
        self.label_4 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_14 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_14)
        self.line_density = QtWidgets.QLineEdit(Automat)
        self.line_density.setObjectName("line_density")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.line_density)
        self.line_disturbance_size_dy = QtWidgets.QLineEdit(Automat)
        self.line_disturbance_size_dy.setObjectName("line_disturbance_size_dy")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.line_disturbance_size_dy)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(10, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.label_15 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.line_averaging = QtWidgets.QLineEdit(Automat)
        self.line_averaging.setObjectName("line_averaging")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.line_averaging)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(13, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(14, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.label_5 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.line_obstacle_center_x = QtWidgets.QLineEdit(Automat)
        self.line_obstacle_center_x.setObjectName("line_obstacle_center_x")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.line_obstacle_center_x)
        self.label_7 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.line_obstacle_center_y = QtWidgets.QLineEdit(Automat)
        self.line_obstacle_center_y.setObjectName("line_obstacle_center_y")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.line_obstacle_center_y)
        self.label_8 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.line_obstacle_radius = QtWidgets.QLineEdit(Automat)
        self.line_obstacle_radius.setObjectName("line_obstacle_radius")
        self.formLayout_2.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.line_obstacle_radius)
        self.label_10 = QtWidgets.QLabel(Automat)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(31, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.btn_startdisturbance = QtWidgets.QPushButton(Automat)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_startdisturbance.setFont(font)
        self.btn_startdisturbance.setObjectName("btn_startdisturbance")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.btn_startdisturbance)
        self.btn_start = QtWidgets.QPushButton(Automat)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")
        self.formLayout_2.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.btn_start)
        self.btn_stop = QtWidgets.QPushButton(Automat)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName("btn_stop")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.btn_stop)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Automat)
        QtCore.QMetaObject.connectSlotsByName(Automat)

    def retranslateUi(self, Automat):
        _translate = QtCore.QCoreApplication.translate
        Automat.setWindowTitle(_translate("Automat", "Form"))
        self.label.setText(_translate("Automat", "Размеры плоскости"))
        self.label_2.setText(_translate("Automat", "X"))
        self.line_field_size_x.setText(_translate("Automat", "400"))
        self.label_3.setText(_translate("Automat", "Y"))
        self.line_field_size_y.setText(_translate("Automat", "400"))
        self.label_4.setText(_translate("Automat", "Плотность"))
        self.line_density.setText(_translate("Automat", "0.2"))
        self.label_15.setText(_translate("Automat", "Усреднение (клеток)"))
        self.line_averaging.setText(_translate("Automat", "4"))
        self.label_5.setText(_translate("Automat", "Препятствие"))
        self.label_6.setText(_translate("Automat", "Центр x"))
        self.line_obstacle_center_x.setText(_translate("Automat", "250"))
        self.label_7.setText(_translate("Automat", "Центр y"))
        self.line_obstacle_center_y.setText(_translate("Automat", "150"))
        self.label_8.setText(_translate("Automat", "Радиус"))
        self.line_obstacle_radius.setText(_translate("Automat", "80"))
        self.label_9.setText(_translate("Automat", "Возмущение"))
        self.label_11.setText(_translate("Automat", "X"))
        self.line_disturbance_start_x.setText(_translate("Automat", "200"))
        self.label_12.setText(_translate("Automat", "Y"))
        self.line_disturbance_start_y.setText(_translate("Automat", "40"))
        self.label_13.setText(_translate("Automat", "dx"))
        self.line_disturbance_size_dx.setText(_translate("Automat", "140"))
        self.btn_startdisturbance.setText(_translate("Automat", "Пуск возмущения"))
        self.label_14.setText(_translate("Automat", "dy"))
        self.btn_stop.setText(_translate("Automat", "Стоп"))
        self.line_disturbance_size_dy.setText(_translate("Automat", "30"))
        self.btn_start.setText(_translate("Automat", "Старт"))

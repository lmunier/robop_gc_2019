# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'int_command.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 230)
        Form.setMinimumSize(QtCore.QSize(900, 230))
        Form.setMaximumSize(QtCore.QSize(900, 230))
        self.button_start_all = QtWidgets.QPushButton(Form)
        self.button_start_all.setGeometry(QtCore.QRect(700, 200, 89, 25))
        self.button_start_all.setObjectName("button_start_all")
        self.button_refresh = QtWidgets.QPushButton(Form)
        self.button_refresh.setGeometry(QtCore.QRect(800, 200, 89, 25))
        self.button_refresh.setObjectName("button_refresh")
        self.button_next = QtWidgets.QPushButton(Form)
        self.button_next.setGeometry(QtCore.QRect(580, 200, 89, 25))
        self.button_next.setObjectName("button_next")
        self.button_previous = QtWidgets.QPushButton(Form)
        self.button_previous.setGeometry(QtCore.QRect(480, 200, 89, 25))
        self.button_previous.setObjectName("button_previous")
        self.slider_gym = QtWidgets.QSlider(Form)
        self.slider_gym.setGeometry(QtCore.QRect(580, 150, 121, 21))
        self.slider_gym.setMaximum(4)
        self.slider_gym.setPageStep(1)
        self.slider_gym.setOrientation(QtCore.Qt.Horizontal)
        self.slider_gym.setObjectName("slider_gym")
        self.label_score_gym = QtWidgets.QLabel(Form)
        self.label_score_gym.setGeometry(QtCore.QRect(763, 150, 41, 20))
        self.label_score_gym.setObjectName("label_score_gym")
        self.label_score_tchoukball = QtWidgets.QLabel(Form)
        self.label_score_tchoukball.setGeometry(QtCore.QRect(763, 100, 41, 20))
        self.label_score_tchoukball.setObjectName("label_score_tchoukball")
        self.slider_tchoukball = QtWidgets.QSlider(Form)
        self.slider_tchoukball.setGeometry(QtCore.QRect(580, 100, 121, 21))
        self.slider_tchoukball.setMaximum(4)
        self.slider_tchoukball.setPageStep(1)
        self.slider_tchoukball.setOrientation(QtCore.Qt.Horizontal)
        self.slider_tchoukball.setObjectName("slider_tchoukball")
        self.label_score_ski = QtWidgets.QLabel(Form)
        self.label_score_ski.setGeometry(QtCore.QRect(763, 70, 41, 20))
        self.label_score_ski.setObjectName("label_score_ski")
        self.slider_ski = QtWidgets.QSlider(Form)
        self.slider_ski.setGeometry(QtCore.QRect(580, 70, 121, 21))
        self.slider_ski.setMaximum(4)
        self.slider_ski.setPageStep(1)
        self.slider_ski.setOrientation(QtCore.Qt.Horizontal)
        self.slider_ski.setObjectName("slider_ski")
        self.table_matchs = QtWidgets.QTableWidget(Form)
        self.table_matchs.setGeometry(QtCore.QRect(10, 10, 461, 211))
        self.table_matchs.setObjectName("table_matchs")
        self.table_matchs.setColumnCount(0)
        self.table_matchs.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(755, 10, 131, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layout_timer = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.layout_timer.setContentsMargins(0, 0, 0, 0)
        self.layout_timer.setObjectName("layout_timer")
        self.lcd_min = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcd_min.setMinimumSize(QtCore.QSize(20, 20))
        self.lcd_min.setMaximumSize(QtCore.QSize(20, 60))
        self.lcd_min.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_min.setDigitCount(1)
        self.lcd_min.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_min.setObjectName("lcd_min")
        self.layout_timer.addWidget(self.lcd_min)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(5, 50))
        self.label_5.setObjectName("label_5")
        self.layout_timer.addWidget(self.label_5)
        self.lcd_sec = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcd_sec.setMinimumSize(QtCore.QSize(30, 30))
        self.lcd_sec.setMaximumSize(QtCore.QSize(40, 60))
        self.lcd_sec.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_sec.setDigitCount(2)
        self.lcd_sec.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_sec.setObjectName("lcd_sec")
        self.layout_timer.addWidget(self.lcd_sec)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(5, 50))
        self.label_6.setObjectName("label_6")
        self.layout_timer.addWidget(self.label_6)
        self.lcd_millis = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcd_millis.setMinimumSize(QtCore.QSize(20, 30))
        self.lcd_millis.setMaximumSize(QtCore.QSize(40, 60))
        self.lcd_millis.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_millis.setDigitCount(2)
        self.lcd_millis.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_millis.setObjectName("lcd_millis")
        self.layout_timer.addWidget(self.lcd_millis)
        self.label_time_ski = QtWidgets.QLabel(Form)
        self.label_time_ski.setGeometry(QtCore.QRect(820, 70, 61, 20))
        self.label_time_ski.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_time_ski.setObjectName("label_time_ski")
        self.label_time_tchoukball = QtWidgets.QLabel(Form)
        self.label_time_tchoukball.setGeometry(QtCore.QRect(820, 100, 61, 20))
        self.label_time_tchoukball.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_time_tchoukball.setObjectName("label_time_tchoukball")
        self.label_time_gym = QtWidgets.QLabel(Form)
        self.label_time_gym.setGeometry(QtCore.QRect(820, 150, 61, 20))
        self.label_time_gym.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_time_gym.setObjectName("label_time_gym")
        self.button_ski = QtWidgets.QPushButton(Form)
        self.button_ski.setGeometry(QtCore.QRect(490, 70, 89, 25))
        self.button_ski.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_ski.setStyleSheet("Text-align:left")
        self.button_ski.setAutoDefault(False)
        self.button_ski.setDefault(False)
        self.button_ski.setFlat(True)
        self.button_ski.setObjectName("button_ski")
        self.button_tchoukball = QtWidgets.QPushButton(Form)
        self.button_tchoukball.setGeometry(QtCore.QRect(490, 100, 89, 25))
        self.button_tchoukball.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_tchoukball.setStyleSheet("Text-align:left")
        self.button_tchoukball.setAutoDefault(False)
        self.button_tchoukball.setDefault(False)
        self.button_tchoukball.setFlat(True)
        self.button_tchoukball.setObjectName("button_tchoukball")
        self.button_gym = QtWidgets.QPushButton(Form)
        self.button_gym.setGeometry(QtCore.QRect(490, 150, 89, 25))
        self.button_gym.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_gym.setStyleSheet("Text-align:left")
        self.button_gym.setAutoDefault(False)
        self.button_gym.setDefault(False)
        self.button_gym.setFlat(True)
        self.button_gym.setObjectName("button_gym")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(800, 70, 2, 111))
        self.line.setMinimumSize(QtCore.QSize(2, 0))
        self.line.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line.setStyleSheet("border: none;\n"
"background: gray;")
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.button_stop = QtWidgets.QPushButton(Form)
        self.button_stop.setGeometry(QtCore.QRect(480, 10, 89, 25))
        self.button_stop.setObjectName("button_stop")
        self.check_dance = QtWidgets.QCheckBox(Form)
        self.check_dance.setGeometry(QtCore.QRect(580, 120, 121, 21))
        self.check_dance.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_dance.setObjectName("check_dance")
        self.spin_penalty_ski = QtWidgets.QSpinBox(Form)
        self.spin_penalty_ski.setGeometry(QtCore.QRect(710, 70, 41, 26))
        self.spin_penalty_ski.setObjectName("spin_penalty_ski")
        self.spin_penalty_tchoukball = QtWidgets.QSpinBox(Form)
        self.spin_penalty_tchoukball.setGeometry(QtCore.QRect(710, 100, 41, 26))
        self.spin_penalty_tchoukball.setObjectName("spin_penalty_tchoukball")
        self.spin_penalty_gym = QtWidgets.QSpinBox(Form)
        self.spin_penalty_gym.setGeometry(QtCore.QRect(710, 150, 41, 26))
        self.spin_penalty_gym.setObjectName("spin_penalty_gym")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_start_all.setText(_translate("Form", "Start all"))
        self.button_refresh.setText(_translate("Form", "Refresh"))
        self.button_next.setText(_translate("Form", "Next"))
        self.button_previous.setText(_translate("Form", "Previous"))
        self.label_score_gym.setText(_translate("Form", "0"))
        self.label_score_tchoukball.setText(_translate("Form", "0"))
        self.label_score_ski.setText(_translate("Form", "0"))
        self.label_5.setText(_translate("Form", ":"))
        self.label_6.setText(_translate("Form", ":"))
        self.label_time_ski.setText(_translate("Form", "-.--.--"))
        self.label_time_tchoukball.setText(_translate("Form", "-.--.--"))
        self.label_time_gym.setText(_translate("Form", "-.--.--"))
        self.button_ski.setText(_translate("Form", "Ski"))
        self.button_tchoukball.setText(_translate("Form", "Tchoukball"))
        self.button_gym.setText(_translate("Form", "Gym"))
        self.button_stop.setText(_translate("Form", "Stop"))
        self.check_dance.setText(_translate("Form", "Victory dance"))



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Evaluate(object):
    def setupUi(self, Evaluate):
        Evaluate.setObjectName("Evaluate")
        Evaluate.resize(799, 560)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Evaluate)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.h1 = QtWidgets.QHBoxLayout()
        self.h1.setObjectName("h1")
        self.team = QtWidgets.QLabel(Evaluate)
        self.team.setObjectName("team")
        self.h1.addWidget(self.team)
        self.lineEdit_team = QtWidgets.QLineEdit(Evaluate)
        self.lineEdit_team.setObjectName("lineEdit_team")
        self.h1.addWidget(self.lineEdit_team)
        self.verticalLayout_3.addLayout(self.h1)
        self.h2 = QtWidgets.QHBoxLayout()
        self.h2.setObjectName("h2")
        self.matchNum = QtWidgets.QLabel(Evaluate)
        self.matchNum.setObjectName("matchNum")
        self.h2.addWidget(self.matchNum)
        self.lineEdit_matchNum = QtWidgets.QLineEdit(Evaluate)
        self.lineEdit_matchNum.setObjectName("lineEdit_matchNum")
        self.h2.addWidget(self.lineEdit_matchNum)
        self.verticalLayout_3.addLayout(self.h2)
        self.h3 = QtWidgets.QHBoxLayout()
        self.h3.setObjectName("h3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.players = QtWidgets.QLabel(Evaluate)
        self.players.setObjectName("players")
        self.verticalLayout.addWidget(self.players)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.p1 = QtWidgets.QLabel(Evaluate)
        self.p1.setObjectName("p1")
        self.verticalLayout.addWidget(self.p1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.p2 = QtWidgets.QLabel(Evaluate)
        self.p2.setObjectName("p2")
        self.verticalLayout.addWidget(self.p2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.p3 = QtWidgets.QLabel(Evaluate)
        self.p3.setObjectName("p3")
        self.verticalLayout.addWidget(self.p3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.p4 = QtWidgets.QLabel(Evaluate)
        self.p4.setObjectName("p4")
        self.verticalLayout.addWidget(self.p4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.p5 = QtWidgets.QLabel(Evaluate)
        self.p5.setObjectName("p5")
        self.verticalLayout.addWidget(self.p5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.p6 = QtWidgets.QLabel(Evaluate)
        self.p6.setObjectName("p6")
        self.verticalLayout.addWidget(self.p6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.p7 = QtWidgets.QLabel(Evaluate)
        self.p7.setObjectName("p7")
        self.verticalLayout.addWidget(self.p7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.p8 = QtWidgets.QLabel(Evaluate)
        self.p8.setObjectName("p8")
        self.verticalLayout.addWidget(self.p8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.p9 = QtWidgets.QLabel(Evaluate)
        self.p9.setObjectName("p9")
        self.verticalLayout.addWidget(self.p9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.p10 = QtWidgets.QLabel(Evaluate)
        self.p10.setObjectName("p10")
        self.verticalLayout.addWidget(self.p10)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.p11 = QtWidgets.QLabel(Evaluate)
        self.p11.setObjectName("p11")
        self.verticalLayout.addWidget(self.p11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.h3.addLayout(self.verticalLayout)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h3.addItem(spacerItem13)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.points = QtWidgets.QLabel(Evaluate)
        self.points.setObjectName("points")
        self.verticalLayout_2.addWidget(self.points)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem15)
        self.point1 = QtWidgets.QLineEdit(Evaluate)
        self.point1.setObjectName("point1")
        self.verticalLayout_2.addWidget(self.point1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)
        self.point2 = QtWidgets.QLineEdit(Evaluate)
        self.point2.setObjectName("point2")
        self.verticalLayout_2.addWidget(self.point2)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem17)
        self.point3 = QtWidgets.QLineEdit(Evaluate)
        self.point3.setObjectName("point3")
        self.verticalLayout_2.addWidget(self.point3)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)
        self.point4 = QtWidgets.QLineEdit(Evaluate)
        self.point4.setObjectName("point4")
        self.verticalLayout_2.addWidget(self.point4)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem19)
        self.point5 = QtWidgets.QLineEdit(Evaluate)
        self.point5.setObjectName("point5")
        self.verticalLayout_2.addWidget(self.point5)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem20)
        self.point6 = QtWidgets.QLineEdit(Evaluate)
        self.point6.setObjectName("point6")
        self.verticalLayout_2.addWidget(self.point6)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem21)
        self.point7 = QtWidgets.QLineEdit(Evaluate)
        self.point7.setObjectName("point7")
        self.verticalLayout_2.addWidget(self.point7)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem22)
        self.point8 = QtWidgets.QLineEdit(Evaluate)
        self.point8.setObjectName("point8")
        self.verticalLayout_2.addWidget(self.point8)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem23)
        self.point9 = QtWidgets.QLineEdit(Evaluate)
        self.point9.setObjectName("point9")
        self.verticalLayout_2.addWidget(self.point9)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem24)
        self.point10 = QtWidgets.QLineEdit(Evaluate)
        self.point10.setObjectName("point10")
        self.verticalLayout_2.addWidget(self.point10)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem25)
        self.point11 = QtWidgets.QLineEdit(Evaluate)
        self.point11.setObjectName("point11")
        self.verticalLayout_2.addWidget(self.point11)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem26)
        self.h3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.h3)
        self.h4 = QtWidgets.QHBoxLayout()
        self.h4.setObjectName("h4")
        self.bInsert = QtWidgets.QPushButton(Evaluate)
        self.bInsert.setObjectName("bInsert")
        self.h4.addWidget(self.bInsert)
        self.bEvaluate = QtWidgets.QPushButton(Evaluate)
        self.bEvaluate.setObjectName("bEvaluate")
        self.h4.addWidget(self.bEvaluate)
        self.bOK = QtWidgets.QPushButton(Evaluate)
        self.bOK.setObjectName("bOK")
        self.h4.addWidget(self.bOK)
        self.verticalLayout_3.addLayout(self.h4)

        self.retranslateUi(Evaluate)
        QtCore.QMetaObject.connectSlotsByName(Evaluate)

    def retranslateUi(self, Evaluate):
        _translate = QtCore.QCoreApplication.translate
        Evaluate.setWindowTitle(_translate("Evaluate", "Evaluate"))
        self.team.setText(_translate("Evaluate", "TEAM"))
        self.matchNum.setText(_translate("Evaluate", "MATCH NUMBER"))
        self.players.setText(_translate("Evaluate", "PLAYERS"))
        self.p1.setText(_translate("Evaluate", "P1"))
        self.p2.setText(_translate("Evaluate", "P2"))
        self.p3.setText(_translate("Evaluate", "P3"))
        self.p4.setText(_translate("Evaluate", "P4"))
        self.p5.setText(_translate("Evaluate", "P5"))
        self.p6.setText(_translate("Evaluate", "P6"))
        self.p7.setText(_translate("Evaluate", "P7"))
        self.p8.setText(_translate("Evaluate", "P8"))
        self.p9.setText(_translate("Evaluate", "P9"))
        self.p10.setText(_translate("Evaluate", "P10"))
        self.p11.setText(_translate("Evaluate", "P11"))
        self.points.setText(_translate("Evaluate", "POINTS"))
        self.bInsert.setText(_translate("Evaluate", "INSERT"))
        self.bEvaluate.setText(_translate("Evaluate", "EVALUATE"))
        self.bOK.setText(_translate("Evaluate", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Evaluate = QtWidgets.QWidget()
    ui = Ui_Evaluate()
    ui.setupUi(Evaluate)
    Evaluate.show()
    sys.exit(app.exec_())

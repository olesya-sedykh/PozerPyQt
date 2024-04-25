# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adddialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtGui import QIntValidator, QFont

from PyQt5.QtWidgets import (
    QDialog, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QSpacerItem, QSizePolicy, QHBoxLayout, QLayout
)

from PyQt5.QtCore import QSize, QMetaObject, Qt, QRect


class SetDialog(QDialog):
    def __init__(self, parent=None, current_node=None):
        super().__init__(parent)
        self.setObjectName("Dialog")
        self.resize(230, 150)
        self.setMinimumSize(QSize(230, 150))
        self.setMaximumSize(QSize(230, 150))
        self.setStyleSheet("QDialog {\n"
        "    background-color: #e5e5e5;\n"
        "    border: 1px solid black;\n"
        "}")
        self.current_node = current_node
        self.int_validator = QIntValidator(-1000, 1000, self)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)

        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 211, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)

        self.label = QLabel(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_2 = QLabel(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMaximumSize(QSize(100, 25))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(self.int_validator)
        self.lineEdit.setPlaceholderText("A")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setMaximumSize(QSize(100, 25))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setValidator(self.int_validator)
        self.lineEdit_2.setPlaceholderText("B")
        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.check_and_set_costs)
        self.lineEdit.editingFinished.connect(self.change_costs)
        self.lineEdit_2.editingFinished.connect(self.change_costs)
        self.horizontalLayout_2.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setModal(True)

        self.label.setText("Введите выигрыши:")
        self.label_2.setText("(")
        self.label_3.setText(";")
        self.label_4.setText(")")
        self.pushButton.setText("OK")

        self.lineEdit.setFocus()
        QMetaObject.connectSlotsByName(self)

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.move(x, y)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.check_and_set_costs()
        elif event.key() == Qt.Key_Up:
            self.lineEdit_2.setFocus()
        elif event.key() == Qt.Key_Down:
            self.lineEdit.setFocus()
        elif event.key() == Qt.Key_Escape:
            self.close()

    def change_costs(self):
        a, b = self.lineEdit.text(), self.lineEdit_2.text()
        # if self.lineEdit.textChanged() or self.lineEdit_2.textChanged():
        if (not self.current_node.getChildren()
                or not self.current_node.checkChildrenCosts()
                or (a, b) in self.current_node.findBestCosts()):
            pass
        else:
            if (a != '' and any(tup[0] == int(a) for tup in self.current_node.findBestCosts())):
                self.lineEdit.setStyleSheet('background-color:  #ffffff;')
            elif (a != '' and any(int(tup[0]) != int(a)  for tup in self.current_node.findBestCosts())):
                self.lineEdit.setStyleSheet('background-color:  #d9746c;')
            if (b != '' and any(tup[1] == int(b) for tup in self.current_node.findBestCosts())):
                self.lineEdit_2.setStyleSheet('background-color:  #ffffff;')
            elif (b != '' and any(int(tup[1]) != int(b) for tup in self.current_node.findBestCosts())):
                self.lineEdit_2.setStyleSheet('background-color:  #d9746c;')
    
    # def set_error_a(self):
    #     style1 = 'background-color:  #d9746c;'
    #     style2 = 'background-color:  #ffffff;'
    #     self.lineEdit.setStyleSheet(style1)
    #     self.lineEdit_2.setStyleSheet(style2)
        
    # def set_error_b(self):
    #     style1 = 'background-color:  #d9746c;'
    #     style2 = 'background-color:  #ffffff;'
    #     self.lineEdit.setStyleSheet(style2)
    #     self.lineEdit_2.setStyleSheet(style1)

    # def set_error_both(self):
    #     style = 'background-color:  #d9746c;'
    #     self.lineEdit.setStyleSheet(style)
    #     self.lineEdit_2.setStyleSheet(style)

    def check_and_set_costs(self):
        a, b = self.lineEdit.text(), self.lineEdit_2.text()
        if a != '' and b != '':
            a, b = int(a), int(b)
            if (not self.current_node.getChildren()
                or not self.current_node.checkChildrenCosts()
                or (a, b) in self.current_node.findBestCosts()):
                    self.parent().set_node_cost(self.current_node, (a, b))
                    self.parent().update()
                    self.close()
            # elif (any(tup[0] != a for tup in self.current_node.findBestCosts())) and (any(tup[1] == b for tup in self.current_node.findBestCosts())):
            #     self.set_error_a()
            # elif (any(tup[1] != b for tup in self.current_node.findBestCosts())) and (any(tup[0] == a for tup in self.current_node.findBestCosts())):
            #     self.set_error_b()
            # else:
            #     self.set_error_both()
            # else:
            #     self.change_costs(a, b)
        #elif a == '' and b != '':
        #    self.set_error_a()
        #elif a != '' and b == '':
        #    self.set_error_b()
        #else:
        #    self.set_error_both()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adddialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class SetDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, current_node=None):
        super().__init__(parent)
        self.setObjectName("Dialog")
        self.resize(230, 150)
        self.setMinimumSize(QtCore.QSize(230, 150))
        self.setMaximumSize(QtCore.QSize(230, 150))
        self.setStyleSheet("QDialog {\n"
"    background-color: #e5e5e5;\n"
"    border: 1px solid black;\n"
"}")
        self.current_node = current_node
        self.int_validator = QtGui.QIntValidator(-1000, 1000, self)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 211, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 25))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(self.int_validator)
        self.lineEdit.setPlaceholderText("A")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 25))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setValidator(self.int_validator)
        self.lineEdit_2.setPlaceholderText("B")
        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.check_and_set_costs)
        self.horizontalLayout_2.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setModal(True)

        self.label.setText("Введите выигрыши:")
        self.label_2.setText("(")
        self.label_3.setText(";")
        self.label_4.setText(")")
        self.pushButton.setText("OK")

        QtCore.QMetaObject.connectSlotsByName(self)

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.move(x, y)

    def set_error(self):
        style = 'border: 1px solid red;'
        self.lineEdit.setStyleSheet(style)
        self.lineEdit_2.setStyleSheet(style)

    def check_and_set_costs(self):
        a, b = self.lineEdit.text(), self.lineEdit_2.text()
        if a != '' and b != '':
            a, b = int(a), int(b)
            if (not self.current_node.getChildren()
                or not self.current_node.checkChildrenCosts()
                or (a, b) == self.current_node.findBestCosts()):
                self.parent().set_node_cost(self.current_node, (a, b))
                self.parent().update()
                self.close()
            else:
                self.set_error()
        else:
            self.set_error()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = SetDialog()
    dialog.show()
    sys.exit(app.exec())

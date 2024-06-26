from PyQt5.QtGui import QFont, QIntValidator

from PyQt5.QtCore import Qt, QSize, QRect, QMetaObject

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QDesktopWidget,
    QGridLayout, QLayout, QMessageBox,
    QLineEdit, QRadioButton, QSizePolicy,
    QPushButton, QMenuBar, QStatusBar
)


class ModeWindow(QMainWindow):
    """
    Окно выбора режима ввода. По умолчанию выбран ввод вручную.
    При выборе режима загрузки варианта открывается поле ввода номера варианта.
    Если вариант введет верно (число от 1 до 100), в главном окне появляется
    соответствующее задание, а окно выбора ввода закрывается.
    """
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setObjectName("MainWindow")
        self.setWindowTitle("Режим ввода")
        self.setFixedSize(320, 180)
        font = QFont()
        font.setPointSize(10)
        self.center()

        self.centralwidget = QWidget(self)
        self.centralwidget.setMaximumSize(QSize(400, 350))
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 291, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setMaximumSize(QSize(150, 30))
        self.lineEdit.setMaxLength(3)
        self.int_validator = QIntValidator(1, 100, self)
        self.lineEdit.setValidator(self.int_validator)
        self.lineEdit.setPlaceholderText("1-100")
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setDisabled(True)
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.radioButton = QRadioButton(self.gridLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setFont(font)
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setText("Вариант")
        self.radioButton.toggled.connect(self.change_mode)
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.gridLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setText("Ввод вручную")
        self.radioButton_2.setChecked(True)
        self.radioButton_2.toggled.connect(self.change_mode)
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)

        self.ok = QPushButton(self.centralwidget)
        self.ok.setGeometry(QRect(180, 120, 120, 28))
        self.ok.setMaximumSize(QSize(120, 30))
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.ok.setText("OK")
        self.ok.clicked.connect(self.handle_mode)

        self.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 320, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        QMetaObject.connectSlotsByName(self)
    
    def center(self) -> None:
        """
        Устанавливает окно по центру экрана.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, event) -> None:
        """
        Обработчик нажатия на клавиши во время открытого окна.
        Обрабатывает Enter, стрелки вверх-вниз.
        """
        if event.key() == Qt.Key_Return:
            self.handle_mode()
        elif event.key() == Qt.Key_Up:
            self.radioButton.setFocus()
        elif event.key() == Qt.Key_Down:
            self.radioButton_2.setFocus()

    def change_mode(self) -> None:
        """
        Включает возможность ввода в поле ввода, если выбрано "Вариант"
        и отключает в противном случае.
        """
        if self.radioButton.isChecked():
            self.lineEdit.setDisabled(False)
        else:
            self.lineEdit.setDisabled(True)

    def show_warning(self, title: str, message: str) -> None:
        """
        Выводит окно с сообщением об ошибке ввода.
        """
        self.lineEdit.setStyleSheet('border: 1px solid red;')
        QMessageBox.warning(self, title, message)

    def handle_mode(self) -> None:
        """
        Если выбрано "Вариант", проверяет ввод на правильность
        и открывает задания введенного варианта в случае правильно введенного значения варианта.
        После открытия задания окно закрывается.
        """
        if self.radioButton.isChecked():
            if len(self.lineEdit.text().strip()) == 0:
                self.show_warning(
                    'Пропущено значение',
                    'Введите номер варианта'
                )
            else:
                if int(self.lineEdit.text().strip()) > 100:
                    self.show_warning(
                        'Неправильный вариант',
                        'Значение варианта должно быть между 1 и 100 включительно'
                    )
                else:
                    self.parent().set_task_number(int(self.lineEdit.text().strip()))
                    self.parent().clearField()
                    self.parent().get_task_tree()
                    self.close()
        else:
            self.parent().set_task_number(-1)
            self.parent().clearField()
            self.close()

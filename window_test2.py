
from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QTabWidget, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1920, 1015)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(58, 58, 58);\n"
"color: rgb(98, 223, 185);")
        MainWindow.setDocumentMode(False)
        self.actionNew_Project = QAction(MainWindow)
        self.actionNew_Project.setObjectName(u"actionNew_Project")
        self.actionSplash = QAction(MainWindow)
        self.actionSplash.setObjectName(u"actionSplash")
        self.actionTutorial = QAction(MainWindow)
        self.actionTutorial.setObjectName(u"actionTutorial")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionComing_soon = QAction(MainWindow)
        self.actionComing_soon.setObjectName(u"actionComing_soon")
        self.actionComing_soon_2 = QAction(MainWindow)
        self.actionComing_soon_2.setObjectName(u"actionComing_soon_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_background = QWidget(self.centralwidget)
        self.widget_background.setObjectName(u"widget_background")
        self.widget_background.setGeometry(QRect(0, 0, 1920, 1020))
        self.widget_background.setStyleSheet(u"background-color: rgb(20, 8, 39);")
        self.tabWidget_3 = QTabWidget(self.widget_background)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(0, 0, 1920, 980))
        font = QFont()
        font.setPointSize(12)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget_3.setStyleSheet(u"#tabWidget_3::pane {\n"
"    border-radius: 8px;\n"
"    background: #180a2f;\n"
"}\n"
"\n"
"#tabWidget_3 QTabBar::tab {\n"
"    background-color: #001f4d; /* Dark Blue */\n"
"    color: rgb(180, 161, 255);\n"
"    padding: 2px 20px;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    margin-left: 8px;\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"#tabWidget_3 QTabBar::tab:selected {\n"
"    background: #5fd9b4; /* Light Green */\n"
"    color: black;\n"
"    border: 1px solid #56458f;\n"
"    border-bottom-color: #5fd9b4;\n"
"}\n"
"\n"
"#tabWidget_3 QTabBar::tab:hover {\n"
"    background: #003366; /* Slightly lighter blue on hover */\n"
"    color: rgb(180, 161, 255);\n"
"}\n"
"")
        self.tabWidget_3.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget_3.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget_3.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidget_3.setUsesScrollButtons(False)
        self.tabWidget_3.setDocumentMode(False)
        self.tabWidget_3.setTabsClosable(True)
        self.tabWidget_3.setMovable(True)
        self.tabWidget_3.setTabBarAutoHide(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.widget_8 = QWidget(self.tab_1)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 0, 1920, 951))
        self.widget_8.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(5, 50, 1910, 891))
        self.widget_9.setStyleSheet(u"background-color: rgb(58, 58, 58);")
        self.label = QLabel(self.widget_9)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 5, 1600, 880))
        font1 = QFont()
        font1.setPointSize(28)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"#label {\n"
"   \n"
"	background-color: #140827;\n"
"    border: 1px solid #7f67d5;\n"
"    border-radius: 10px;\n"
"	\n"
"	color: rgb(56, 48, 86);\n"
"}\n"
"\n"
"#label:hover {\n"
"    border: 2px solid #5424a7; /* red border on hover */\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.label.setPixmap(QPixmap(u"banner3.jpg"))
        self.label.setScaledContents(True)
        self.label.setMargin(7)
        self.widget = QWidget(self.widget_9)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(1612, 7, 292, 100))
        self.widget.setStyleSheet(u"#widget {\n"
"   \n"
"	background-color: rgb(39, 39, 39);\n"
"    border: 1px solid #7f67d5;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#widget:hover {\n"
"    border: 1px solid #1abc9c; /* red border on hover */\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.pushButton_generate_single_btn = QPushButton(self.widget)
        self.pushButton_generate_single_btn.setObjectName(u"pushButton_generate_single_btn")
        self.pushButton_generate_single_btn.setGeometry(QRect(5, 63, 281, 25))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton_generate_single_btn.setFont(font2)
        self.pushButton_generate_single_btn.setStyleSheet(u"#pushButton_generate_single_btn{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #62dfb9;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"\n"
"\n"
"}\n"
"\n"
"#pushButton_generate_single_btn:hover {\n"
"    background-color: rgb(134, 255, 215);\n"
"}\n"
"\n"
"#pushButton_generate_single_btn:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_generate_single_btn:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.pushButton_select_cutouts_btn = QPushButton(self.widget)
        self.pushButton_select_cutouts_btn.setObjectName(u"pushButton_select_cutouts_btn")
        self.pushButton_select_cutouts_btn.setGeometry(QRect(145, 30, 139, 25))
        self.pushButton_select_cutouts_btn.setFont(font2)
        self.pushButton_select_cutouts_btn.setStyleSheet(u"#pushButton_select_cutouts_btn {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #eab88f;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"\n"
"\n"
"}\n"
"\n"
"#pushButton_select_cutouts_btn:hover {\n"
"    background-color: #ffd7a7;\n"
"}\n"
"\n"
"#pushButton_select_cutouts_btn:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_select_cutouts_btn:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.pushButton_select_background_btn = QPushButton(self.widget)
        self.pushButton_select_background_btn.setObjectName(u"pushButton_select_background_btn")
        self.pushButton_select_background_btn.setGeometry(QRect(7, 30, 132, 25))
        self.pushButton_select_background_btn.setFont(font2)
        self.pushButton_select_background_btn.setStyleSheet(u"#pushButton_select_background_btn {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #8ac8ef;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"#pushButton_select_background_btn:hover {\n"
"    background-color: #b4f9ff;\n"
"}\n"
"\n"
"#pushButton_select_background_btn:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_select_background_btn:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(2, 2, 288, 24))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"#label_6 {\n"
"    color: rgb(180, 161, 255);\n"
"    background-color: rgb(20, 8, 39);\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.widget_2 = QWidget(self.widget_9)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(1612, 495, 292, 100))
        self.widget_2.setStyleSheet(u"#widget_2 {\n"
"   \n"
"	background-color: #433048;\n"
"    border: 1px solid #7f67d5;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#widget_2:hover {\n"
"    border: 1px solid #1abc9c; /* red border on hover */\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.pushButton_generate_btn = QPushButton(self.widget_2)
        self.pushButton_generate_btn.setObjectName(u"pushButton_generate_btn")
        self.pushButton_generate_btn.setGeometry(QRect(5, 68, 281, 25))
        self.pushButton_generate_btn.setFont(font2)
        self.pushButton_generate_btn.setStyleSheet(u"#pushButton_generate_btn{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #d9b8ff;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"\n"
"}\n"
"\n"
"#pushButton_generate_btn:hover {\n"
"    background-color: #edd3ff;\n"
"}\n"
"\n"
"#pushButton_generate_btn:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_open_folder:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.toolButton_open_box_folder = QToolButton(self.widget_2)
        self.toolButton_open_box_folder.setObjectName(u"toolButton_open_box_folder")
        self.toolButton_open_box_folder.setGeometry(QRect(258, 33, 25, 25))
        self.toolButton_open_box_folder.setStyleSheet(u"background-color: rgb(255, 214, 180);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_box_location = QLineEdit(self.widget_2)
        self.lineEdit_box_location.setObjectName(u"lineEdit_box_location")
        self.lineEdit_box_location.setGeometry(QRect(77, 33, 174, 26))
        self.lineEdit_box_location.setStyleSheet(u"#lineEdit_box_location {\n"
"    background-color: #1e1e2f;\n"
"    color: #ffffff;\n"
"    border: 1px solid #56458f;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#lineEdit_box_location:focus {\n"
"    border: 1px solid #8ae6c3;\n"
"    background-color: #2a2a40;\n"
"    color: #ffffff;\n"
"}\n"
"")
        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(9, 28, 66, 31))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: #433048")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(2, 2, 288, 24))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"#label_5 {\n"
"    color: rgb(180, 161, 255);\n"
"    background-color: rgb(20, 8, 39);\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.widget_3 = QWidget(self.widget_9)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(1612, 606, 292, 140))
        self.widget_3.setStyleSheet(u"#widget_3 {\n"
"   \n"
"	background-color: #22313f;\n"
"    border: 1px solid #7f67d5;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#widget_3:hover {\n"
"    border: 1px solid #1abc9c; /* red border on hover */\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.pushButton_segmentation_button = QPushButton(self.widget_3)
        self.pushButton_segmentation_button.setObjectName(u"pushButton_segmentation_button")
        self.pushButton_segmentation_button.setGeometry(QRect(5, 105, 281, 25))
        self.pushButton_segmentation_button.setFont(font2)
        self.pushButton_segmentation_button.setStyleSheet(u"#pushButton_segmentation_button {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #8ac8ef;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"\n"
"}\n"
"\n"
"#pushButton_segmentation_button:hover {\n"
"    background-color: #b4f9ff;\n"
"}\n"
"\n"
"#pushButton_segmentation_button:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_segmentation_button:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.toolButton_toolButton_open_segment_folder = QToolButton(self.widget_3)
        self.toolButton_toolButton_open_segment_folder.setObjectName(u"toolButton_toolButton_open_segment_folder")
        self.toolButton_toolButton_open_segment_folder.setGeometry(QRect(258, 68, 25, 25))
        self.toolButton_toolButton_open_segment_folder.setStyleSheet(u"background-color: rgb(255, 214, 180);\n"
"color: rgb(0, 0, 0);")
        self.spinBox_resolution_epsilon = QSpinBox(self.widget_3)
        self.spinBox_resolution_epsilon.setObjectName(u"spinBox_resolution_epsilon")
        self.spinBox_resolution_epsilon.setGeometry(QRect(130, 34, 91, 26))
        self.spinBox_resolution_epsilon.setStyleSheet(u"background-color: rgb(86, 69, 143);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";")
        self.spinBox_resolution_epsilon.setMinimum(1)
        self.spinBox_resolution_epsilon.setMaximum(100)
        self.spinBox_resolution_epsilon.setSingleStep(5)
        self.spinBox_resolution_epsilon.setValue(10)
        self.spinBox_resolution_epsilon.setDisplayIntegerBase(10)
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(7, 31, 121, 31))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: #22313f")
        self.pushButton_default_res = QPushButton(self.widget_3)
        self.pushButton_default_res.setObjectName(u"pushButton_default_res")
        self.pushButton_default_res.setGeometry(QRect(225, 34, 61, 26))
        self.pushButton_default_res.setFont(font)
        self.pushButton_default_res.setStyleSheet(u"background-color: rgb(255, 174, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 65, 77, 31))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: #22313f")
        self.lineEdit_segment_location = QLineEdit(self.widget_3)
        self.lineEdit_segment_location.setObjectName(u"lineEdit_segment_location")
        self.lineEdit_segment_location.setGeometry(QRect(77, 68, 174, 26))
        self.lineEdit_segment_location.setStyleSheet(u"#lineEdit_segment_location {\n"
"    background-color: #1e1e2f;\n"
"    color: #ffffff;\n"
"    border: 1px solid #56458f;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#lineEdit_segment_location:focus {\n"
"    border: 1px solid #8ae6c3;\n"
"    background-color: #2a2a40;\n"
"    color: #ffffff;\n"
"}\n"
"")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(2, 2, 288, 24))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"#label_7 {\n"
"    color: rgb(180, 161, 255);\n"
"    background-color: rgb(20, 8, 39);\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.widget_4 = QWidget(self.widget_9)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(1612, 343, 292, 140))
        self.widget_4.setStyleSheet(u"#widget_4 {\n"
"   \n"
"	background-color: rgb(39, 39, 39);\n"
"    border: 1px solid #7f67d5;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#widget_4:hover {\n"
"    border: 1px solid #1abc9c; /* red border on hover */\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(2, 2, 288, 24))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"#label_9 {\n"
"    color: rgb(180, 161, 255);\n"
"    background-color: rgb(20, 8, 39);\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.spinBox_height = QSpinBox(self.widget_4)
        self.spinBox_height.setObjectName(u"spinBox_height")
        self.spinBox_height.setGeometry(QRect(174, 35, 107, 26))
        self.spinBox_height.setStyleSheet(u"background-color: rgb(86, 69, 143);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";")
        self.spinBox_height.setMinimum(200)
        self.spinBox_height.setMaximum(3840)
        self.spinBox_height.setSingleStep(40)
        self.spinBox_height.setValue(1024)
        self.spinBox_height.setDisplayIntegerBase(10)
        self.spinBox_width = QSpinBox(self.widget_4)
        self.spinBox_width.setObjectName(u"spinBox_width")
        self.spinBox_width.setGeometry(QRect(62, 35, 107, 26))
        self.spinBox_width.setStyleSheet(u"background-color: rgb(86, 69, 143);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";")
        self.spinBox_width.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox_width.setMinimum(200)
        self.spinBox_width.setMaximum(3840)
        self.spinBox_width.setSingleStep(40)
        self.spinBox_width.setValue(1024)
        self.spinBox_width.setDisplayIntegerBase(10)
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(15, 35, 38, 21))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.pushButton_default = QPushButton(self.widget_4)
        self.pushButton_default.setObjectName(u"pushButton_default")
        self.pushButton_default.setGeometry(QRect(208, 104, 73, 26))
        self.pushButton_default.setFont(font)
        self.pushButton_default.setStyleSheet(u"background-color: rgb(255, 174, 193);\n"
"color: rgb(0, 0, 0);")
        self.horizontalSlider_quality = QSlider(self.widget_4)
        self.horizontalSlider_quality.setObjectName(u"horizontalSlider_quality")
        self.horizontalSlider_quality.setGeometry(QRect(74, 75, 110, 18))
        self.horizontalSlider_quality.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.horizontalSlider_quality.setMinimum(10)
        self.horizontalSlider_quality.setMaximum(100)
        self.horizontalSlider_quality.setSingleStep(5)
        self.horizontalSlider_quality.setValue(90)
        self.horizontalSlider_quality.setSliderPosition(90)
        self.horizontalSlider_quality.setOrientation(Qt.Orientation.Horizontal)
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(16, 65, 56, 31))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.spinBox_num_quality = QSpinBox(self.widget_4)
        self.spinBox_num_quality.setObjectName(u"spinBox_num_quality")
        self.spinBox_num_quality.setGeometry(QRect(190, 70, 90, 26))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.spinBox_num_quality.setFont(font3)
        self.spinBox_num_quality.setStyleSheet(u"background-color: rgb(86, 69, 143);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";")
        self.spinBox_num_quality.setMinimum(10)
        self.spinBox_num_quality.setMaximum(100)
        self.spinBox_num_quality.setSingleStep(5)
        self.spinBox_num_quality.setValue(90)
        self.checkBox = QCheckBox(self.widget_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 104, 201, 24))
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.checkBox.setChecked(True)
        self.widget_5 = QWidget(self.widget_9)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(1612, 758, 292, 126))
        self.widget_5.setStyleSheet(u"#widget_5 {\n"
"   \n"
"	background-color: rgb(39, 39, 39);\n"
"    border: 1px solid #7f67d5;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#widget_5:hover {\n"
"    border: 1px solid #1abc9c; /* red border on hover */\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.label_19 = QLabel(self.widget_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 61, 141, 22))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.toolButton_Select_image_folder = QToolButton(self.widget_5)
        self.toolButton_Select_image_folder.setObjectName(u"toolButton_Select_image_folder")
        self.toolButton_Select_image_folder.setGeometry(QRect(150, 61, 25, 25))
        self.toolButton_Select_image_folder.setStyleSheet(u"background-color: rgb(255, 214, 180);\n"
"color: rgb(0, 0, 0);")
        self.toolButton_Select_label_folder = QToolButton(self.widget_5)
        self.toolButton_Select_label_folder.setObjectName(u"toolButton_Select_label_folder")
        self.toolButton_Select_label_folder.setGeometry(QRect(150, 89, 25, 25))
        self.toolButton_Select_label_folder.setStyleSheet(u"background-color: rgb(255, 214, 180);\n"
"color: rgb(0, 0, 0);")
        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 89, 141, 22))
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.pushButton_force_split = QPushButton(self.widget_5)
        self.pushButton_force_split.setObjectName(u"pushButton_force_split")
        self.pushButton_force_split.setGeometry(QRect(186, 90, 102, 25))
        self.pushButton_force_split.setFont(font2)
        self.pushButton_force_split.setStyleSheet(u"#pushButton_force_split{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #62dfb9;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"\n"
"\n"
"}\n"
"\n"
"#pushButton_force_split:hover {\n"
"    background-color: rgb(134, 255, 215);\n"
"}\n"
"\n"
"#pushButton_force_split:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_generate_single_btn:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.label_17 = QLabel(self.widget_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 32, 81, 22))
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"color: rgb(180, 161, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.comboBox_split = QComboBox(self.widget_5)
        self.comboBox_split.addItem("")
        self.comboBox_split.addItem("")
        self.comboBox_split.addItem("")
        self.comboBox_split.addItem("")
        self.comboBox_split.addItem("")
        self.comboBox_split.addItem("")
        self.comboBox_split.setObjectName(u"comboBox_split")
        self.comboBox_split.setGeometry(QRect(90, 31, 193, 24))
        self.comboBox_split.setStyleSheet(u"background-color: rgb(86, 69, 143);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";")
        self.pushButton_splitter_default = QPushButton(self.widget_5)
        self.pushButton_splitter_default.setObjectName(u"pushButton_splitter_default")
        self.pushButton_splitter_default.setGeometry(QRect(223, 58, 61, 26))
        self.pushButton_splitter_default.setFont(font)
        self.pushButton_splitter_default.setStyleSheet(u"background-color: rgb(255, 174, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_11 = QLabel(self.widget_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(2, 2, 288, 24))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"#label_11 {\n"
"    color: rgb(180, 161, 255);\n"
"    background-color: rgb(20, 8, 39);\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.listWidget = QListWidget(self.widget_9)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(1612, 118, 292, 215))
        self.listWidget.setStyleSheet(u"#listWidget {\n"
"    font: 12pt \"Segoe UI\";\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid #7f67d5;\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"    outline: none;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Hover effect for the entire list widget */\n"
"#listWidget:hover {\n"
"    border: 1px solid #1abc9c;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"/* Style for each item inside the list */\n"
"#listWidget::item {\n"
"    border-radius: 10px;\n"
"    padding: 4px 6px;\n"
"    margin: 2px 0;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Hover effect for each individual list item */\n"
"#listWidget::item:hover {\n"
"    background-color: #1abc9c;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Selected item style */\n"
"#listWidget::item:selected {\n"
"    background-color: #7f67d5;\n"
"    color: white;\n"
"}\n"
"")
        self.listWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget.setLineWidth(1)
        self.listWidget.setMidLineWidth(-3)
        self.listWidget.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.listWidget.setSortingEnabled(True)
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(5, 5, 1910, 40))
        self.widget_10.setStyleSheet(u"#widget_10 {\n"
"   \n"
"	background-color: #56458f;\n"
"    border: 1px solid #140827;\n"
"	color: rgb(121, 98, 203);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.label_1 = QLabel(self.widget_10)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(19, 8, 113, 21))
        font4 = QFont()
        font4.setPointSize(11)
        self.label_1.setFont(font4)
        self.label_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")
        self.label_2 = QLabel(self.widget_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(244, 8, 115, 21))
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")
        self.label_3 = QLabel(self.widget_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(715, 8, 182, 21))
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")
        self.pushButton_open_folder = QPushButton(self.widget_10)
        self.pushButton_open_folder.setObjectName(u"pushButton_open_folder")
        self.pushButton_open_folder.setGeometry(QRect(1688, 7, 115, 25))
        self.pushButton_open_folder.setFont(font2)
        self.pushButton_open_folder.setStyleSheet(u"#pushButton_open_folder{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #8ac8ef;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"#pushButton_open_folder:hover {\n"
"    background-color: #edd3ff;\n"
"}\n"
"\n"
"#pushButton_open_folder:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_open_folder:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.spinBox_min_size_input = QSpinBox(self.widget_10)
        self.spinBox_min_size_input.setObjectName(u"spinBox_min_size_input")
        self.spinBox_min_size_input.setGeometry(QRect(132, 7, 100, 26))
        self.spinBox_min_size_input.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.spinBox_min_size_input.setMaximum(1000)
        self.spinBox_min_size_input.setValue(50)
        self.spinBox_max_size_input = QSpinBox(self.widget_10)
        self.spinBox_max_size_input.setObjectName(u"spinBox_max_size_input")
        self.spinBox_max_size_input.setGeometry(QRect(360, 7, 100, 26))
        self.spinBox_max_size_input.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.spinBox_max_size_input.setMaximum(1000)
        self.spinBox_max_size_input.setValue(150)
        self.spinBox_num_images_input = QSpinBox(self.widget_10)
        self.spinBox_num_images_input.setObjectName(u"spinBox_num_images_input")
        self.spinBox_num_images_input.setGeometry(QRect(895, 7, 100, 26))
        self.spinBox_num_images_input.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.spinBox_num_images_input.setMaximum(10000)
        self.spinBox_num_images_input.setValue(10)
        self.spinBox_starting_image_input = QSpinBox(self.widget_10)
        self.spinBox_starting_image_input.setObjectName(u"spinBox_starting_image_input")
        self.spinBox_starting_image_input.setGeometry(QRect(600, 7, 100, 26))
        self.spinBox_starting_image_input.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.spinBox_starting_image_input.setMaximum(10000)
        self.spinBox_starting_image_input.setValue(1)
        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(474, 8, 127, 21))
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")
        self.toolButton_prev = QToolButton(self.widget_10)
        self.toolButton_prev.setObjectName(u"toolButton_prev")
        self.toolButton_prev.setGeometry(QRect(1809, 5, 45, 30))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.toolButton_prev.setFont(font5)
        self.toolButton_next = QToolButton(self.widget_10)
        self.toolButton_next.setObjectName(u"toolButton_next")
        self.toolButton_next.setGeometry(QRect(1858, 5, 45, 30))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setItalic(False)
        self.toolButton_next.setFont(font6)
        self.toolButton_next.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_background_src = QLabel(self.widget_10)
        self.label_background_src.setObjectName(u"label_background_src")
        self.label_background_src.setGeometry(QRect(1009, 8, 111, 21))
        self.label_background_src.setFont(font4)
        self.label_background_src.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")
        self.lineEdit_background_src = QLineEdit(self.widget_10)
        self.lineEdit_background_src.setObjectName(u"lineEdit_background_src")
        self.lineEdit_background_src.setGeometry(QRect(1120, 5, 281, 30))
        self.lineEdit_background_src.setStyleSheet(u"#lineEdit_background_src {\n"
"    background-color: #140827;\n"
"    color: #ffffff;\n"
"    border: 1px solid #56458f;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#lineEdit_background_src:focus {\n"
"    border: 1px solid #8ae6c3;\n"
"    background-color: #2a2a40;\n"
"    color: #ffffff;\n"
"}\n"
"")
        self.lineEdit_background_src.setReadOnly(True)
        self.comboBox_profile = QComboBox(self.widget_10)
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.setObjectName(u"comboBox_profile")
        self.comboBox_profile.setGeometry(QRect(1459, 7, 215, 25))
        self.comboBox_profile.setStyleSheet(u"#comboBox_profile {\n"
"    color: #000000;\n"
"    background-color: #d9b8ff;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"#comboBox_profile::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 5px;\n"
"    border-left: 1px solid rgba(0, 0, 0, 0.1);\n"
"    background-color: rgb(180, 161, 255);\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#comboBox_profile:hover {\n"
"    background-color: #7feccc;\n"
"}\n"
"\n"
"\n"
"#comboBox_profile:disabled {\n"
"    background-color: #cccccc;\n"
"    color: #666666;\n"
"}\n"
"\n"
"\n"
"\n"
"#comboBox_profile::down-arrow {\n"
"    width: 8px;\n"
"    height: 12px;\n"
"    image: url(:/icons/down-arrow.png); /* Optional: replace or remove */\n"
"}\n"
"\n"
"/* Dropdown list view */\n"
"#comboBox_profile QAbstractItemView {\n"
"    color: #b7a9ff;\n"
"    background-color: #140827;\n"
"    border: "
                        "1px solid #dddddd;\n"
"    selection-background-color: #5c2d91; /* Optional: active selection color */\n"
"    selection-color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Red background on hover inside dropdown items */\n"
"#comboBox_profile QAbstractItemView::item:hover {\n"
"    background-color: #d9b8ff;\n"
"    color: black;\n"
"}\n"
"")
        self.label_background_src_2 = QLabel(self.widget_10)
        self.label_background_src_2.setObjectName(u"label_background_src_2")
        self.label_background_src_2.setGeometry(QRect(1409, 8, 51, 21))
        self.label_background_src_2.setFont(font4)
        self.label_background_src_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 69, 143);")
        self.tabWidget_3.addTab(self.tab_1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget_editor = QWidget(self.tab)
        self.widget_editor.setObjectName(u"widget_editor")
        self.widget_editor.setGeometry(QRect(0, 0, 1931, 961))
        self.widget_editor.setStyleSheet(u"#widget_editor {\n"
"   \n"
"	background-color: #140827;\n"
"    border: 2px solid #5fd9b4;\n"
"    \n"
"}\n"
"\n"
"#widget_editor:hover {\n"
"    border: 2px solid #1abc9c; /* red border on hover */\n"
"    \n"
"}\n"
"")
        self.webEngineView = QWebEngineView(self.widget_editor)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(0, 2, 2231, 940))
        self.webEngineView.setStyleSheet(u"background-color: rgb(103, 103, 103);\n"
"color: rgb(255, 255, 255);")
        self.webEngineView.setUrl(QUrl(u"https://www.photopea.com/#%7B%22files%22%3A%5B%22https%3A%2F%2Fwww.photopea.com%2Fapi%2Fimg2%2Fpug.png%22%5D%2C%22environment%22%3A%7B%7D%7D"))
        self.webEngineView.setZoomFactor(1.000000000000000)
        self.pushButton_show_in_browser = QPushButton(self.widget_editor)
        self.pushButton_show_in_browser.setObjectName(u"pushButton_show_in_browser")
        self.pushButton_show_in_browser.setGeometry(QRect(600, 10, 110, 20))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(9)
        font7.setBold(False)
        font7.setItalic(False)
        self.pushButton_show_in_browser.setFont(font7)
        self.pushButton_show_in_browser.setStyleSheet(u"#pushButton_show_in_browser{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #62dfb9;\n"
"    font: 9pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"}\n"
"\n"
"#pushButton_show_in_browser:hover {\n"
"    background-color: rgb(134, 255, 215);\n"
"}\n"
"\n"
"#pushButton_show_in_browser:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_show_in_browser:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.tabWidget_3.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget_graph_3 = QWidget(self.tab_2)
        self.widget_graph_3.setObjectName(u"widget_graph_3")
        self.widget_graph_3.setGeometry(QRect(0, 0, 1920, 945))
        self.widget_graph_3.setStyleSheet(u"background-color: rgb(29, 24, 49);")
        self.widget_box = QWidget(self.widget_graph_3)
        self.widget_box.setObjectName(u"widget_box")
        self.widget_box.setGeometry(QRect(0, 0, 1918, 940))
        self.widget_box.setStyleSheet(u"#widget_box {\n"
"   \n"
"	background-color: #140827;\n"
"    border: 2px solid #5fd9b4;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#widget_box:hover {\n"
"    border: 2px solid #1abc9c; /* red border on hover */\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.pushButton_btn_select_label = QPushButton(self.widget_graph_3)
        self.pushButton_btn_select_label.setObjectName(u"pushButton_btn_select_label")
        self.pushButton_btn_select_label.setGeometry(QRect(1725, 44, 180, 25))
        self.pushButton_btn_select_label.setFont(font2)
        self.pushButton_btn_select_label.setStyleSheet(u"#pushButton_btn_select_label {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #8ac8ef;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"\n"
"}\n"
"\n"
"#pushButton_btn_select_label:hover {\n"
"    background-color: #b4f9ff;\n"
"}\n"
"\n"
"#pushButton_btn_select_label:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_btn_select_label:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.pushButton_btn_select_image = QPushButton(self.widget_graph_3)
        self.pushButton_btn_select_image.setObjectName(u"pushButton_btn_select_image")
        self.pushButton_btn_select_image.setGeometry(QRect(1725, 10, 180, 25))
        self.pushButton_btn_select_image.setFont(font2)
        self.pushButton_btn_select_image.setStyleSheet(u"#pushButton_btn_select_image{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #d9b8ff;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"\n"
"}\n"
"\n"
"#pushButton_btn_select_image:hover {\n"
"    background-color: #edd3ff;\n"
"}\n"
"\n"
"#pushButton_btn_select_image:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_btn_select_image:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.tabWidget_3.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.widget_graph_4 = QWidget(self.tab_3)
        self.widget_graph_4.setObjectName(u"widget_graph_4")
        self.widget_graph_4.setGeometry(QRect(0, 0, 1920, 951))
        self.widget_graph_4.setStyleSheet(u"background-color:#140827;")
        self.widget_segment = QWidget(self.widget_graph_4)
        self.widget_segment.setObjectName(u"widget_segment")
        self.widget_segment.setGeometry(QRect(0, 0, 1918, 940))
        self.widget_segment.setStyleSheet(u"#widget_segment {\n"
"   \n"
"	background-color: #140827;\n"
"    border: 2px solid #5fd9b4;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#widget_segment:hover {\n"
"    border: 2px solid #1abc9c; /* red border on hover */\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.pushButton_btn_image2 = QPushButton(self.widget_graph_4)
        self.pushButton_btn_image2.setObjectName(u"pushButton_btn_image2")
        self.pushButton_btn_image2.setGeometry(QRect(1725, 10, 180, 25))
        self.pushButton_btn_image2.setFont(font2)
        self.pushButton_btn_image2.setStyleSheet(u"#pushButton_btn_image2{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #d9b8ff;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"\n"
"}\n"
"\n"
"#pushButton_btn_image2:hover {\n"
"    background-color: #edd3ff;\n"
"}\n"
"\n"
"#pushButton_btn_image2:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_btn_image2:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.pushButton_btn_txt2 = QPushButton(self.widget_graph_4)
        self.pushButton_btn_txt2.setObjectName(u"pushButton_btn_txt2")
        self.pushButton_btn_txt2.setGeometry(QRect(1725, 44, 180, 25))
        self.pushButton_btn_txt2.setFont(font2)
        self.pushButton_btn_txt2.setStyleSheet(u"#pushButton_btn_txt2 {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #8ac8ef;\n"
"    font: 11pt \"Segoe UI\";\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"\n"
"}\n"
"\n"
"#pushButton_btn_txt2:hover {\n"
"    background-color: #b4f9ff;\n"
"}\n"
"\n"
"#pushButton_btn_txt2:pressed {\n"
"    background-color: #ad98ff;\n"
"    padding-left: 3px;\n"
"	padding-top: 2px;\n"
"  \n"
"\n"
"}\n"
"\n"
"#pushButton_btn_txt2:disabled {\n"
"    background-color: rgb(180, 180, 180);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.tabWidget_3.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 41))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"    background-color: #140827;\n"
"    color: white;\n"
"    font: 11pt \"Segoe UI\";\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    padding: 6px 14px;\n"
"    margin: 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background: #56458f;\n"
"    color: white;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #5fd9b4;\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    padding: 6px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 6px 18px;\n"
"    background-color: transparent;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #3a9ff5;\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 5px;\n"
"    background: #555;\n"
"    margin: 2px 8px;\n"
"}\n"
"")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuForm = QMenu(self.menubar)
        self.menuForm.setObjectName(u"menuForm")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuForm.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionComing_soon_2)
        self.menuForm.addAction(self.actionComing_soon)
        self.menuHelp.addAction(self.actionTutorial)
        self.menuAbout.addAction(self.actionSplash)

        self.retranslateUi(MainWindow)

        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Label-Blend v1.1 Synthetic image studio", None))
        self.actionNew_Project.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.actionSplash.setText(QCoreApplication.translate("MainWindow", u"Splash", None))
        self.actionTutorial.setText(QCoreApplication.translate("MainWindow", u"Coming soon..", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionComing_soon.setText(QCoreApplication.translate("MainWindow", u"Coming soon..", None))
        self.actionComing_soon_2.setText(QCoreApplication.translate("MainWindow", u"Coming soon..", None))
        self.label.setText("")
        self.pushButton_generate_single_btn.setText(QCoreApplication.translate("MainWindow", u"Random Roll", None))
#if QT_CONFIG(shortcut)
        self.pushButton_generate_single_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+G", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_select_cutouts_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Add Object to environment", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_select_cutouts_btn.setText(QCoreApplication.translate("MainWindow", u"Add PNG Cutouts", None))
#if QT_CONFIG(shortcut)
        self.pushButton_select_cutouts_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_select_background_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select Environment</p><p>ShortCut: Ctrl+O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_select_background_btn.setText(QCoreApplication.translate("MainWindow", u"Add Backgrounds", None))
#if QT_CONFIG(shortcut)
        self.pushButton_select_background_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"                   Image Settings", None))
        self.pushButton_generate_btn.setText(QCoreApplication.translate("MainWindow", u"Save Bounding Box Dataset", None))
#if QT_CONFIG(shortcut)
        self.pushButton_generate_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.toolButton_open_box_folder.setToolTip(QCoreApplication.translate("MainWindow", u"Open Box Folder", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_open_box_folder.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_box_location.setText("")
        self.lineEdit_box_location.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Location...", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Location:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"            Bounding Box Annotation", None))
        self.pushButton_segmentation_button.setText(QCoreApplication.translate("MainWindow", u"Save Mask Segment Dataset", None))
#if QT_CONFIG(shortcut)
        self.pushButton_segmentation_button.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.toolButton_toolButton_open_segment_folder.setToolTip(QCoreApplication.translate("MainWindow", u"Open Segment folder", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_toolButton_open_segment_folder.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.spinBox_resolution_epsilon.setToolTip(QCoreApplication.translate("MainWindow", u"Polygon Vertices Epsilon Value", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Vertices Distance:", None))
        self.pushButton_default_res.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Location:", None))
        self.lineEdit_segment_location.setText("")
        self.lineEdit_segment_location.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Location...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"            Mask Polygons Annotation", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"                   Image Settings", None))
#if QT_CONFIG(tooltip)
        self.spinBox_height.setToolTip(QCoreApplication.translate("MainWindow", u"Polygon Vertices Epsilon Value", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_height.setSuffix(QCoreApplication.translate("MainWindow", u" px", None))
        self.spinBox_height.setPrefix("")
#if QT_CONFIG(tooltip)
        self.spinBox_width.setToolTip(QCoreApplication.translate("MainWindow", u"Polygon Vertices Epsilon Value", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_width.setSuffix(QCoreApplication.translate("MainWindow", u" px", None))
        self.spinBox_width.setPrefix("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.pushButton_default.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Quality:", None))
        self.spinBox_num_quality.setSuffix(QCoreApplication.translate("MainWindow", u" %", None))
        self.spinBox_num_quality.setPrefix("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Data Splitting Train / Val", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Select Image Folder", None))
#if QT_CONFIG(tooltip)
        self.toolButton_Select_image_folder.setToolTip(QCoreApplication.translate("MainWindow", u"Open Box Folder", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_Select_image_folder.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolButton_Select_label_folder.setToolTip(QCoreApplication.translate("MainWindow", u"Open Box Folder", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_Select_label_folder.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Select Label Folder", None))
        self.pushButton_force_split.setText(QCoreApplication.translate("MainWindow", u"Force Split", None))
#if QT_CONFIG(shortcut)
        self.pushButton_force_split.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+G", None))
#endif // QT_CONFIG(shortcut)
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Train / Val", None))
        self.comboBox_split.setItemText(0, QCoreApplication.translate("MainWindow", u"95 : 15 OverFit", None))
        self.comboBox_split.setItemText(1, QCoreApplication.translate("MainWindow", u"90 : 10 Biased", None))
        self.comboBox_split.setItemText(2, QCoreApplication.translate("MainWindow", u"80 : 20 Recommended", None))
        self.comboBox_split.setItemText(3, QCoreApplication.translate("MainWindow", u"70 : 30 Standard", None))
        self.comboBox_split.setItemText(4, QCoreApplication.translate("MainWindow", u"50 : 50 Scarcity", None))
        self.comboBox_split.setItemText(5, QCoreApplication.translate("MainWindow", u"30 : 70 UnderFit", None))

        self.pushButton_splitter_default.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"    Manual Dataset Splitter   <Optional>", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"No Backgrounds Added", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Min Cutout Size:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max Cutout Size:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"No. of Images to Generate:", None))
        self.pushButton_open_folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
#if QT_CONFIG(shortcut)
        self.pushButton_open_folder.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+O", None))
#endif // QT_CONFIG(shortcut)
        self.spinBox_min_size_input.setSuffix(QCoreApplication.translate("MainWindow", u" px", None))
        self.spinBox_max_size_input.setSuffix(QCoreApplication.translate("MainWindow", u" px", None))
        self.spinBox_max_size_input.setPrefix("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Starting Image No:", None))
        self.toolButton_prev.setText(QCoreApplication.translate("MainWindow", u"<--", None))
        self.toolButton_next.setText(QCoreApplication.translate("MainWindow", u"-->", None))
        self.label_background_src.setText(QCoreApplication.translate("MainWindow", u"Background Src:", None))
        self.lineEdit_background_src.setText("")
        self.lineEdit_background_src.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No background selected", None))
        self.comboBox_profile.setItemText(0, QCoreApplication.translate("MainWindow", u"1024 x 1024   Default", None))
        self.comboBox_profile.setItemText(1, QCoreApplication.translate("MainWindow", u"3840 x 2160   SAM", None))
        self.comboBox_profile.setItemText(2, QCoreApplication.translate("MainWindow", u"1920 x 1920   Yolo v11", None))
        self.comboBox_profile.setItemText(3, QCoreApplication.translate("MainWindow", u"1280 x 1280   Yolo v8 Seg", None))
        self.comboBox_profile.setItemText(4, QCoreApplication.translate("MainWindow", u"640 x 640       Yolo v8", None))
        self.comboBox_profile.setItemText(5, QCoreApplication.translate("MainWindow", u"512 x 512       Yolo v5", None))
        self.comboBox_profile.setItemText(6, QCoreApplication.translate("MainWindow", u"256 x 256       ResNet", None))
        self.comboBox_profile.setItemText(7, QCoreApplication.translate("MainWindow", u"224 x 224       ResNet", None))

        self.label_background_src_2.setText(QCoreApplication.translate("MainWindow", u"Profile:", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Generator", None))
        self.pushButton_show_in_browser.setText(QCoreApplication.translate("MainWindow", u"Open in Browser", None))
#if QT_CONFIG(shortcut)
        self.pushButton_show_in_browser.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+G", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cutouts Maker", None))
        self.pushButton_btn_select_label.setText(QCoreApplication.translate("MainWindow", u"Select Box Annotate File", None))
        self.pushButton_btn_select_image.setText(QCoreApplication.translate("MainWindow", u"Select Image", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Box View", None))
        self.pushButton_btn_image2.setText(QCoreApplication.translate("MainWindow", u"Select Image", None))
        self.pushButton_btn_txt2.setText(QCoreApplication.translate("MainWindow", u"Select Segment Txt File", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Masked Segment View", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuForm.setTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi



from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

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
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton_show_in_browser.setFont(font1)
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
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
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


# -*- coding: utf-8 -*-

################################################################################
# # Form generated from reading UI file 'gui_window.ui'
##
# # Created by: Qt User Interface Compiler version 6.5.2
##
# # WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QAction, QFont, QIcon)
from PySide6.QtWidgets import (QAbstractItemView, QCheckBox, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMenu,
                               QMenuBar, QPushButton, QSizePolicy, QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
                               QTableWidgetItem, QTextEdit, QToolButton, QVBoxLayout, QWidget)
import src.gui.res_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1206, 685)
        MainWindow.setMinimumSize(QSize(1206, 685))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QStatusBar: {\n"
                                 "background-color : rgb(255, 237, 254);\n"
                                 "}\n"
                                 "/*\n"
                                 "QMenu:hover {\n"
                                 "background-color: rgba(255, 255, 255, 80);\n"
                                 "border: 1px solid rgba(255, 255, 255, 80);\n"
                                 "border-radius: 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu:pressed {\n"
                                 "background-color: rgba(255, 255, 255, 160);\n"
                                 "border: 1px solid rgba(255, 255, 255, 160);\n"
                                 "border-radius: 1px;\n"
                                 "}\n"
                                 "*/")
        MainWindow.setDocumentMode(False)
        self.CreateAction = QAction(MainWindow)
        self.CreateAction.setObjectName(u"CreateAction")
        icon = QIcon()
        icon.addFile(u":/icon/icons/create.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CreateAction.setIcon(icon)
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)
        self.CreateAction.setFont(font1)
        self.OpenAction = QAction(MainWindow)
        self.OpenAction.setObjectName(u"OpenAction")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenAction.setIcon(icon1)
        self.OpenAction.setFont(font1)
        self.SaveAction = QAction(MainWindow)
        self.SaveAction.setObjectName(u"SaveAction")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/print.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SaveAction.setIcon(icon2)
        self.SaveAction.setFont(font1)
        self.SaveAsAction = QAction(MainWindow)
        self.SaveAsAction.setObjectName(u"SaveAsAction")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/save_as.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SaveAsAction.setIcon(icon3)
        self.SaveAsAction.setFont(font1)
        self.PrintAction = QAction(MainWindow)
        self.PrintAction.setObjectName(u"PrintAction")
        self.PrintAction.setIcon(icon2)
        self.PrintAction.setFont(font1)
        self.ExitAction = QAction(MainWindow)
        self.ExitAction.setObjectName(u"ExitAction")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/exit_to_app.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ExitAction.setIcon(icon4)
        self.ExitAction.setFont(font1)
        self.UndoAction = QAction(MainWindow)
        self.UndoAction.setObjectName(u"UndoAction")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/undo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.UndoAction.setIcon(icon5)
        self.UndoAction.setFont(font1)
        self.RedoAction = QAction(MainWindow)
        self.RedoAction.setObjectName(u"RedoAction")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/redo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RedoAction.setIcon(icon6)
        self.RedoAction.setFont(font1)
        self.CutAction = QAction(MainWindow)
        self.CutAction.setObjectName(u"CutAction")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/cut.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CutAction.setIcon(icon7)
        self.CutAction.setFont(font1)
        self.CopyAction = QAction(MainWindow)
        self.CopyAction.setObjectName(u"CopyAction")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/file_copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CopyAction.setIcon(icon8)
        self.CopyAction.setFont(font1)
        self.PasteAction = QAction(MainWindow)
        self.PasteAction.setObjectName(u"PasteAction")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons/content_paste.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PasteAction.setIcon(icon9)
        self.PasteAction.setFont(font1)
        self.DeleteAction = QAction(MainWindow)
        self.DeleteAction.setObjectName(u"DeleteAction")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.DeleteAction.setIcon(icon10)
        self.DeleteAction.setFont(font1)
        self.AboutAction = QAction(MainWindow)
        self.AboutAction.setObjectName(u"AboutAction")
        icon11 = QIcon()
        icon11.addFile(u":/icon/icons/help_about.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AboutAction.setIcon(icon11)
        self.AboutAction.setFont(font1)
        self.AboutPreprocessorAction = QAction(MainWindow)
        self.AboutPreprocessorAction.setObjectName(u"AboutPreprocessorAction")
        self.AboutPreprocessorAction.setFont(font1)
        self.AboutProcessorAction = QAction(MainWindow)
        self.AboutProcessorAction.setObjectName(u"AboutProcessorAction")
        self.AboutProcessorAction.setFont(font1)
        self.AboutPostprocessorAction = QAction(MainWindow)
        self.AboutPostprocessorAction.setObjectName(u"AboutPostprocessorAction")
        self.AboutPostprocessorAction.setFont(font1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setFont(font1)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout = QVBoxLayout()
        self.MainLayout.setSpacing(0)
        self.MainLayout.setObjectName(u"MainLayout")
        # self.TitleFrame = QFrame(self.centralwidget)
        # self.TitleFrame.setObjectName(u"TitleFrame")
        # self.TitleFrame.setMinimumSize(QSize(800, 24))
        # self.TitleFrame.setMaximumSize(QSize(16777215, 24))
        # self.TitleFrame.setStyleSheet(u"")
        # self.TitleFrame.setFrameShape(QFrame.StyledPanel)
        # self.TitleFrame.setFrameShadow(QFrame.Raised)
        # self.TitleFrame.setLineWidth(0)

        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1206, 22))

        self.gridLayout_3 = QGridLayout(self.menuBar)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.NameLabel = QLabel(self.menuBar)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setMinimumSize(QSize(0, 20))
        self.NameLabel.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamilies([u"Montserrat Medium"])
        font2.setPointSize(11)
        self.NameLabel.setFont(font2)
        self.NameLabel.setAlignment(Qt.AlignCenter)
        self.NameLabel.setWordWrap(False)

        self.horizontalLayout_6.addWidget(self.NameLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.BtnRoll = QPushButton(self.menuBar)
        self.BtnRoll.setObjectName(u"BtnRoll")
        self.BtnRoll.setMinimumSize(QSize(43, 22))
        self.BtnRoll.setMaximumSize(QSize(50, 22))
        self.BtnRoll.setStyleSheet(u"QPushButton {\n"
                                   "background-color: rgba(255, 255, 255, 80);\n"
                                   "border: 1px solid rgba(0, 0, 0, 80);\n"
                                   "border-radius: 2px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "background-color: rgba(255, 255, 255, 180);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "background-color: rgba(255, 255, 255, 245);\n"
                                   "}\n"
                                   "")
        icon12 = QIcon()
        icon12.addFile(u":/icon/icons/remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnRoll.setIcon(icon12)
        self.BtnRoll.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.BtnRoll)

        self.BtnExpand = QPushButton(self.menuBar)
        self.BtnExpand.setObjectName(u"BtnExpand")
        self.BtnExpand.setMinimumSize(QSize(43, 22))
        self.BtnExpand.setMaximumSize(QSize(45, 22))
        self.BtnExpand.setStyleSheet(u"QPushButton {\n"
                                     "background-color: rgba(255, 255, 255, 80);\n"
                                     "border: 1px solid rgba(0, 0, 0, 80);\n"
                                     "border-radius: 2px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "background-color: rgba(255, 255, 255, 180);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "background-color: rgba(255, 255, 255, 245);\n"
                                     "}\n"
                                     "")
        icon13 = QIcon()
        icon13.addFile(u":/icon/icons/fullscreen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnExpand.setIcon(icon13)
        self.BtnExpand.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.BtnExpand)

        self.BtnClose = QPushButton(self.menuBar)
        self.BtnClose.setObjectName(u"BtnClose")
        self.BtnClose.setMinimumSize(QSize(43, 22))
        self.BtnClose.setMaximumSize(QSize(50, 22))
        self.BtnClose.setStyleSheet(u"QPushButton {\n"
                                    "border: 1px solid rgba(0, 0, 0, 80);\n"
                                    "border-radius: 2px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "background-color: rgba(229, 0, 0, 180);\n"
                                    "border: 1px solid rgba(0, 0, 0, 180);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "background-color: rgba(229, 0, 0, 245);\n"
                                    "border: 1px solid rgba(0, 0, 0, 255);\n"
                                    "}\n"
                                    "")
        icon14 = QIcon()
        icon14.addFile(u":/icon/icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnClose.setIcon(icon14)
        self.BtnClose.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.BtnClose)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6.setStretch(0, 90)
        self.horizontalLayout_6.setStretch(1, 10)

        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.MainLayout.addWidget(self.menuBar)

        self.TabWidget = QTabWidget(self.centralwidget)
        self.TabWidget.setObjectName(u"TabWidget")
        self.TabWidget.setEnabled(True)
        self.TabWidget.setFont(font1)
        self.TabWidget.setStyleSheet(u"background-color : rgb(255, 237, 254);\n"
                                     "QTabWidget{\n"
                                     "border: 1px solid rgba(0, 0, 0, 80);\n"
                                     "}\n"
                                     "QWidget:hover{\n"
                                     "background-color : rgba(255, 237, 254, 160);\n"
                                     "}\n"
                                     "")
        self.TabWidget.setTabShape(QTabWidget.Triangular)
        self.TabWidget.setDocumentMode(True)
        self.PreprocessorTab = QWidget()
        self.PreprocessorTab.setObjectName(u"PreprocessorTab")
        self.PreprocessorTab.setFont(font1)
        self.PreprocessorTab.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.PreprocessorTab)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.WorkPreprocLayout = QVBoxLayout()
        self.WorkPreprocLayout.setSpacing(0)
        self.WorkPreprocLayout.setObjectName(u"WorkPreprocLayout")
        self.WorkLayout = QHBoxLayout()
        self.WorkLayout.setSpacing(0)
        self.WorkLayout.setObjectName(u"WorkLayout")
        self.DataWorkFrame = QFrame(self.PreprocessorTab)
        self.DataWorkFrame.setObjectName(u"DataWorkFrame")
        self.DataWorkFrame.setMaximumSize(QSize(400, 16777215))
        self.DataWorkFrame.setFont(font1)
        self.DataWorkFrame.setStyleSheet(u"background-color : #FFE0FB;")
        self.DataWorkFrame.setFrameShape(QFrame.StyledPanel)
        self.DataWorkFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.DataWorkFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.DataWorkVerticalLayout = QVBoxLayout()
        self.DataWorkVerticalLayout.setSpacing(0)
        self.DataWorkVerticalLayout.setObjectName(u"DataWorkVerticalLayout")
        self.PathToFileFrame = QFrame(self.DataWorkFrame)
        self.PathToFileFrame.setObjectName(u"PathToFileFrame")
        self.PathToFileFrame.setMaximumSize(QSize(16777215, 60))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(11)
        self.PathToFileFrame.setFont(font3)
        self.PathToFileFrame.setStyleSheet(u"background-color : rgb(255, 237, 254);")
        self.PathToFileFrame.setFrameShape(QFrame.StyledPanel)
        self.PathToFileFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.PathToFileFrame)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.PathToFileVerticalLayout = QVBoxLayout()
        self.PathToFileVerticalLayout.setSpacing(0)
        self.PathToFileVerticalLayout.setObjectName(u"PathToFileVerticalLayout")
        self.PathToFileLabel = QLabel(self.PathToFileFrame)
        self.PathToFileLabel.setObjectName(u"PathToFileLabel")
        self.PathToFileLabel.setFont(font3)
        self.PathToFileLabel.setAlignment(Qt.AlignCenter)

        self.PathToFileVerticalLayout.addWidget(self.PathToFileLabel)

        self.PathLineHorizontalLayout = QHBoxLayout()
        self.PathLineHorizontalLayout.setSpacing(0)
        self.PathLineHorizontalLayout.setObjectName(u"PathLineHorizontalLayout")
        self.LineEditPath = QLineEdit(self.PathToFileFrame)
        self.LineEditPath.setObjectName(u"LineEditPath")
        self.LineEditPath.setMinimumSize(QSize(0, 24))
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(9)
        self.LineEditPath.setFont(font4)
        self.LineEditPath.setStyleSheet(u"background-color: #FAEDFF;")
        self.LineEditPath.setReadOnly(True)

        self.PathLineHorizontalLayout.addWidget(self.LineEditPath)

        self.BtnPath = QToolButton(self.PathToFileFrame)
        self.BtnPath.setObjectName(u"BtnPath")
        self.BtnPath.setMinimumSize(QSize(24, 24))
        self.BtnPath.setFont(font3)
        self.BtnPath.setStyleSheet(u"QToolButton {\n"
                                   "background-color: rgba(255, 255, 255, 80);\n"
                                   "border: 1px solid rgba(0, 0, 0, 80);\n"
                                   "border-radius: 2px;\n"
                                   "}\n"
                                   "\n"
                                   "QToolButton:hover {\n"
                                   "background-color: rgba(255, 255, 255, 180);\n"
                                   "}\n"
                                   "\n"
                                   "QToolButton:pressed {\n"
                                   "background-color: rgba(255, 255, 255, 245);\n"
                                   "}\n"
                                   "")
        icon15 = QIcon()
        icon15.addFile(u":/icon/icons/folder_open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnPath.setIcon(icon15)

        self.PathLineHorizontalLayout.addWidget(self.BtnPath)

        self.PathToFileVerticalLayout.addLayout(self.PathLineHorizontalLayout)

        self.gridLayout_7.addLayout(self.PathToFileVerticalLayout, 0, 0, 1, 1)

        self.DataWorkVerticalLayout.addWidget(self.PathToFileFrame)

        self.line = QFrame(self.DataWorkFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.DataWorkVerticalLayout.addWidget(self.line)

        self.DescriptionRodsFrame = QFrame(self.DataWorkFrame)
        self.DescriptionRodsFrame.setObjectName(u"DescriptionRodsFrame")
        self.DescriptionRodsFrame.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Montserrat"])
        font5.setPointSize(99)
        self.DescriptionRodsFrame.setFont(font5)
        self.DescriptionRodsFrame.setStyleSheet(u"background-color : rgb(255, 237, 254);")
        self.DescriptionRodsFrame.setFrameShape(QFrame.StyledPanel)
        self.DescriptionRodsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.DescriptionRodsFrame)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.DescriptionRodsVerticalLayout = QVBoxLayout()
        self.DescriptionRodsVerticalLayout.setSpacing(0)
        self.DescriptionRodsVerticalLayout.setObjectName(u"DescriptionRodsVerticalLayout")
        self.DescriptionRodsTableverticalLayout = QVBoxLayout()
        self.DescriptionRodsTableverticalLayout.setSpacing(0)
        self.DescriptionRodsTableverticalLayout.setObjectName(u"DescriptionRodsTableverticalLayout")
        self.DescriptionRodsLabel = QLabel(self.DescriptionRodsFrame)
        self.DescriptionRodsLabel.setObjectName(u"DescriptionRodsLabel")
        self.DescriptionRodsLabel.setMaximumSize(QSize(16777215, 16777215))
        self.DescriptionRodsLabel.setFont(font3)
        self.DescriptionRodsLabel.setAlignment(Qt.AlignCenter)

        self.DescriptionRodsTableverticalLayout.addWidget(self.DescriptionRodsLabel)

        self.TableRodsDescription = QTableWidget(self.DescriptionRodsFrame)
        if self.TableRodsDescription.columnCount() < 4:
            self.TableRodsDescription.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.TableRodsDescription.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.TableRodsDescription.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.TableRodsDescription.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.TableRodsDescription.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if self.TableRodsDescription.rowCount() < 1:
            self.TableRodsDescription.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.TableRodsDescription.setVerticalHeaderItem(0, __qtablewidgetitem4)
        font6 = QFont()
        font6.setPointSize(10)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font6);
        self.TableRodsDescription.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font6);
        self.TableRodsDescription.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font6);
        self.TableRodsDescription.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font6);
        self.TableRodsDescription.setItem(0, 3, __qtablewidgetitem8)
        self.TableRodsDescription.setObjectName(u"TableRodsDescription")
        self.TableRodsDescription.setMaximumSize(QSize(16777215, 16777215))
        self.TableRodsDescription.setFont(font1)
        self.TableRodsDescription.setStyleSheet(u"background-color: #FAEDFF;")
        self.TableRodsDescription.setFrameShadow(QFrame.Raised)
        self.TableRodsDescription.setShowGrid(True)
        self.TableRodsDescription.setGridStyle(Qt.DashDotLine)
        self.TableRodsDescription.setCornerButtonEnabled(False)
        self.TableRodsDescription.horizontalHeader().setMinimumSectionSize(60)
        self.TableRodsDescription.horizontalHeader().setDefaultSectionSize(63)
        self.TableRodsDescription.horizontalHeader().setStretchLastSection(True)

        self.DescriptionRodsTableverticalLayout.addWidget(self.TableRodsDescription)

        self.DescriptionRodsVerticalLayout.addLayout(self.DescriptionRodsTableverticalLayout)

        self.DescriptionRodsButtonHorizontalLayout = QHBoxLayout()
        self.DescriptionRodsButtonHorizontalLayout.setSpacing(4)
        self.DescriptionRodsButtonHorizontalLayout.setObjectName(u"DescriptionRodsButtonHorizontalLayout")
        self.BtnDeleteRodsDescription = QPushButton(self.DescriptionRodsFrame)
        self.BtnDeleteRodsDescription.setObjectName(u"BtnDeleteRodsDescription")
        self.BtnDeleteRodsDescription.setMinimumSize(QSize(0, 35))
        self.BtnDeleteRodsDescription.setFont(font3)
        self.BtnDeleteRodsDescription.setStyleSheet(u"QPushButton {\n"
                                                    "background-color: rgba(255, 255, 255, 80);\n"
                                                    "border: 1px solid rgba(0, 0, 0, 80);\n"
                                                    "border-radius: 2px;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:hover {\n"
                                                    "background-color: rgba(255, 255, 255, 180);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "background-color: rgba(255, 255, 255, 245);\n"
                                                    "}\n"
                                                    "")
        self.BtnDeleteRodsDescription.setIcon(icon12)

        self.DescriptionRodsButtonHorizontalLayout.addWidget(self.BtnDeleteRodsDescription)

        self.BtnAddRodsDescription = QPushButton(self.DescriptionRodsFrame)
        self.BtnAddRodsDescription.setObjectName(u"BtnAddRodsDescription")
        self.BtnAddRodsDescription.setMinimumSize(QSize(0, 35))
        self.BtnAddRodsDescription.setFont(font3)
        self.BtnAddRodsDescription.setStyleSheet(u"QPushButton {\n"
                                                 "background-color: rgba(255, 255, 255, 80);\n"
                                                 "border: 1px solid rgba(0, 0, 0, 80);\n"
                                                 "border-radius: 2px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "background-color: rgba(255, 255, 255, 180);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed {\n"
                                                 "background-color: rgba(255, 255, 255, 245);\n"
                                                 "}\n"
                                                 "")
        icon16 = QIcon()
        icon16.addFile(u":/icon/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnAddRodsDescription.setIcon(icon16)

        self.DescriptionRodsButtonHorizontalLayout.addWidget(self.BtnAddRodsDescription)

        self.DescriptionRodsVerticalLayout.addLayout(self.DescriptionRodsButtonHorizontalLayout)

        self.gridLayout_6.addLayout(self.DescriptionRodsVerticalLayout, 0, 0, 1, 1)

        self.DataWorkVerticalLayout.addWidget(self.DescriptionRodsFrame)

        self.line_2 = QFrame(self.DataWorkFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.DataWorkVerticalLayout.addWidget(self.line_2)

        self.DescriptionPowerFrame = QFrame(self.DataWorkFrame)
        self.DescriptionPowerFrame.setObjectName(u"DescriptionPowerFrame")
        self.DescriptionPowerFrame.setFont(font3)
        self.DescriptionPowerFrame.setStyleSheet(u"background-color : rgb(255, 237, 254);")
        self.DescriptionPowerFrame.setFrameShape(QFrame.StyledPanel)
        self.DescriptionPowerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.DescriptionPowerFrame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.DescriptionPowerRodsVerticalLayout = QVBoxLayout()
        self.DescriptionPowerRodsVerticalLayout.setSpacing(0)
        self.DescriptionPowerRodsVerticalLayout.setObjectName(u"DescriptionPowerRodsVerticalLayout")
        self.DescriptionPowerRodsVerticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.DescriptionPowerRodsLabel = QLabel(self.DescriptionPowerFrame)
        self.DescriptionPowerRodsLabel.setObjectName(u"DescriptionPowerRodsLabel")
        self.DescriptionPowerRodsLabel.setFont(font3)
        self.DescriptionPowerRodsLabel.setAlignment(Qt.AlignCenter)

        self.DescriptionPowerRodsVerticalLayout.addWidget(self.DescriptionPowerRodsLabel)

        self.TableRodsPowerDescription = QTableWidget(self.DescriptionPowerFrame)
        if self.TableRodsPowerDescription.columnCount() < 1:
            self.TableRodsPowerDescription.setColumnCount(1)
        font7 = QFont()
        font7.setFamilies([u"Montserrat"])
        font7.setPointSize(10)
        font7.setHintingPreference(QFont.PreferFullHinting)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font7);
        self.TableRodsPowerDescription.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        if self.TableRodsPowerDescription.rowCount() < 1:
            self.TableRodsPowerDescription.setRowCount(1)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font7);
        self.TableRodsPowerDescription.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.TableRodsPowerDescription.setItem(0, 0, __qtablewidgetitem11)
        self.TableRodsPowerDescription.setObjectName(u"TableRodsPowerDescription")
        self.TableRodsPowerDescription.setMinimumSize(QSize(197, 130))
        self.TableRodsPowerDescription.setFont(font1)
        self.TableRodsPowerDescription.setStyleSheet(u"background-color: #FAEDFF;")
        self.TableRodsPowerDescription.setFrameShadow(QFrame.Raised)
        self.TableRodsPowerDescription.setGridStyle(Qt.DashDotLine)
        self.TableRodsPowerDescription.setCornerButtonEnabled(False)
        self.TableRodsPowerDescription.horizontalHeader().setStretchLastSection(True)

        self.DescriptionPowerRodsVerticalLayout.addWidget(self.TableRodsPowerDescription)

        self.line_7 = QFrame(self.DescriptionPowerFrame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.DescriptionPowerRodsVerticalLayout.addWidget(self.line_7)

        self.ChoiceSealingVerticalLayout = QVBoxLayout()
        self.ChoiceSealingVerticalLayout.setSpacing(0)
        self.ChoiceSealingVerticalLayout.setObjectName(u"ChoiceSealingVerticalLayout")
        self.ChoiceSealingVerticalLayout.setContentsMargins(4, -1, 0, -1)
        self.CheckBoxLeftSealing = QCheckBox(self.DescriptionPowerFrame)
        self.CheckBoxLeftSealing.setObjectName(u"CheckBoxLeftSealing")
        self.CheckBoxLeftSealing.setFont(font3)
        self.CheckBoxLeftSealing.setStyleSheet(u"QCheckBox:hover {\n"
                                               "background-color: rgba(255, 255, 255, 80);\n"
                                               "border: 1px solid rgba(255, 255, 255, 80);\n"
                                               "border-radius: 1px;\n"
                                               "}\n"
                                               "\n"
                                               "QCheckBox:pressed {\n"
                                               "background-color: rgba(255, 255, 255, 160);\n"
                                               "border: 1px solid rgba(255, 255, 255, 160);\n"
                                               "border-radius: 1px;\n"
                                               "}\n"
                                               "")
        icon17 = QIcon()
        icon17.addFile(u":/icon/icons/left_sealing.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CheckBoxLeftSealing.setIcon(icon17)
        self.CheckBoxLeftSealing.setChecked(True)

        self.ChoiceSealingVerticalLayout.addWidget(self.CheckBoxLeftSealing)

        self.CheckBoxRightSealing = QCheckBox(self.DescriptionPowerFrame)
        self.CheckBoxRightSealing.setObjectName(u"CheckBoxRightSealing")
        self.CheckBoxRightSealing.setFont(font3)
        self.CheckBoxRightSealing.setStyleSheet(u"QCheckBox:hover {\n"
                                                "background-color: rgba(255, 255, 255, 80);\n"
                                                "border: 1px solid rgba(255, 255, 255, 80);\n"
                                                "border-radius: 1px;\n"
                                                "}\n"
                                                "\n"
                                                "QCheckBox:pressed {\n"
                                                "background-color: rgba(255, 255, 255, 160);\n"
                                                "border: 1px solid rgba(255, 255, 255, 160);\n"
                                                "border-radius: 1px;\n"
                                                "}\n"
                                                "")
        icon18 = QIcon()
        icon18.addFile(u":/icon/icons/right_sealing.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CheckBoxRightSealing.setIcon(icon18)

        self.ChoiceSealingVerticalLayout.addWidget(self.CheckBoxRightSealing)

        self.DescriptionPowerRodsVerticalLayout.addLayout(self.ChoiceSealingVerticalLayout)

        self.horizontalLayout_3.addLayout(self.DescriptionPowerRodsVerticalLayout)

        self.line_5 = QFrame(self.DescriptionPowerFrame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.DescriptionPowerKontsVerticalLayout = QVBoxLayout()
        self.DescriptionPowerKontsVerticalLayout.setSpacing(0)
        self.DescriptionPowerKontsVerticalLayout.setObjectName(u"DescriptionPowerKontsVerticalLayout")
        self.DescriptionPowerKontsVerticalLayout.setContentsMargins(0, -1, -1, -1)
        self.DescriptionPowerKontsLabel = QLabel(self.DescriptionPowerFrame)
        self.DescriptionPowerKontsLabel.setObjectName(u"DescriptionPowerKontsLabel")
        self.DescriptionPowerKontsLabel.setMinimumSize(QSize(0, 38))
        self.DescriptionPowerKontsLabel.setFont(font3)
        self.DescriptionPowerKontsLabel.setAlignment(Qt.AlignCenter)

        self.DescriptionPowerKontsVerticalLayout.addWidget(self.DescriptionPowerKontsLabel)

        self.TableKontsPowerDescription = QTableWidget(self.DescriptionPowerFrame)
        if self.TableKontsPowerDescription.columnCount() < 1:
            self.TableKontsPowerDescription.setColumnCount(1)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font6);
        self.TableKontsPowerDescription.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        if self.TableKontsPowerDescription.rowCount() < 2:
            self.TableKontsPowerDescription.setRowCount(2)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.TableKontsPowerDescription.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.TableKontsPowerDescription.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font6);
        self.TableKontsPowerDescription.setItem(0, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font6);
        self.TableKontsPowerDescription.setItem(1, 0, __qtablewidgetitem16)
        self.TableKontsPowerDescription.setObjectName(u"TableKontsPowerDescription")
        self.TableKontsPowerDescription.setMinimumSize(QSize(150, 140))
        self.TableKontsPowerDescription.setFont(font)
        self.TableKontsPowerDescription.setStyleSheet(u"background-color: #FAEDFF;")
        self.TableKontsPowerDescription.setFrameShadow(QFrame.Raised)
        self.TableKontsPowerDescription.setGridStyle(Qt.DashDotLine)
        self.TableKontsPowerDescription.setCornerButtonEnabled(False)
        self.TableKontsPowerDescription.horizontalHeader().setMinimumSectionSize(72)
        self.TableKontsPowerDescription.horizontalHeader().setDefaultSectionSize(72)
        self.TableKontsPowerDescription.horizontalHeader().setStretchLastSection(True)

        self.DescriptionPowerKontsVerticalLayout.addWidget(self.TableKontsPowerDescription)

        self.horizontalLayout_3.addLayout(self.DescriptionPowerKontsVerticalLayout)

        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.DataWorkVerticalLayout.addWidget(self.DescriptionPowerFrame)

        self.line_3 = QFrame(self.DataWorkFrame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.DataWorkVerticalLayout.addWidget(self.line_3)

        self.ManipulationButtonsFrame = QFrame(self.DataWorkFrame)
        self.ManipulationButtonsFrame.setObjectName(u"ManipulationButtonsFrame")
        self.ManipulationButtonsFrame.setMinimumSize(QSize(0, 40))
        self.ManipulationButtonsFrame.setFont(font3)
        self.ManipulationButtonsFrame.setStyleSheet(u"background-color : rgb(255, 237, 254);")
        self.ManipulationButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.ManipulationButtonsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.ManipulationButtonsFrame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ManipulationButtonsHorizontalLayout = QHBoxLayout()
        self.ManipulationButtonsHorizontalLayout.setSpacing(4)
        self.ManipulationButtonsHorizontalLayout.setObjectName(u"ManipulationButtonsHorizontalLayout")
        self.BtnUploadData = QPushButton(self.ManipulationButtonsFrame)
        self.BtnUploadData.setObjectName(u"BtnUploadData")
        self.BtnUploadData.setMinimumSize(QSize(0, 35))
        self.BtnUploadData.setFont(font3)
        self.BtnUploadData.setStyleSheet(u"QPushButton {\n"
                                         "background-color: rgba(255, 255, 255, 80);\n"
                                         "border: 1px solid rgba(0, 0, 0, 80);\n"
                                         "border-radius: 2px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background-color: rgba(255, 255, 255, 180);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "background-color: rgba(255, 255, 255, 245);\n"
                                         "}\n"
                                         "")
        icon19 = QIcon()
        icon19.addFile(u":/icon/icons/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnUploadData.setIcon(icon19)

        self.ManipulationButtonsHorizontalLayout.addWidget(self.BtnUploadData)

        self.BtnCalc = QPushButton(self.ManipulationButtonsFrame)
        self.BtnCalc.setObjectName(u"BtnCalc")
        self.BtnCalc.setMinimumSize(QSize(0, 35))
        self.BtnCalc.setFont(font3)
        self.BtnCalc.setStyleSheet(u"QPushButton {\n"
                                   "background-color: rgba(255, 255, 255, 80);\n"
                                   "border: 1px solid rgba(0, 0, 0, 80);\n"
                                   "border-radius: 2px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "background-color: rgba(255, 255, 255, 180);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "background-color: rgba(255, 255, 255, 245);\n"
                                   "}\n"
                                   "")
        icon20 = QIcon()
        icon20.addFile(u":/icon/icons/calculate.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnCalc.setIcon(icon20)

        self.ManipulationButtonsHorizontalLayout.addWidget(self.BtnCalc)

        self.gridLayout_4.addLayout(self.ManipulationButtonsHorizontalLayout, 1, 0, 1, 1)

        self.DataWorkVerticalLayout.addWidget(self.ManipulationButtonsFrame)

        self.verticalLayout_2.addLayout(self.DataWorkVerticalLayout)

        self.WorkLayout.addWidget(self.DataWorkFrame)

        self.GraphWorkFrame = QFrame(self.PreprocessorTab)
        self.GraphWorkFrame.setObjectName(u"GraphWorkFrame")
        self.GraphWorkFrame.setStyleSheet(u"background-color: rgb(255, 240, 238)\n"
                                          "/*#FFE4E1*/\n"
                                          "")
        self.GraphWorkFrame.setFrameShape(QFrame.StyledPanel)
        self.GraphWorkFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.GraphWorkFrame)
        self.gridLayout_8.setSpacing(1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(1, 1, 1, 1)
        self.GraphWidget = QWidget(self.GraphWorkFrame)
        self.GraphWidget.setObjectName(u"GraphWidget")
        self.GraphWidget.setStyleSheet(u"")
        self.gridLayout_10 = QGridLayout(self.GraphWidget)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BtnVisibleLabels = QPushButton(self.GraphWidget)
        self.BtnVisibleLabels.setObjectName(u"BtnVisibleLabels")
        self.BtnVisibleLabels.setMinimumSize(QSize(24, 24))
        self.BtnVisibleLabels.setFont(font)
        self.BtnVisibleLabels.setStyleSheet(u".QPushButton {\n"
                                            "background-color: rgba(255, 255, 255, 80);\n"
                                            "image: None;\n"
                                            "border: 1px solid rgba(0, 0, 0, 80);\n"
                                            "border-radius: 2px;\n"
                                            "}\n"
                                            "\n"
                                            ".QPushButton:hover {\n"
                                            "background-color: rgba(245, 245, 245, 180);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "background-color: rgba(255, 255, 255, 245);\n"
                                            "}\n"
                                            "")
        icon21 = QIcon()
        icon21.addFile(u":/icon/icons/visibility_off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnVisibleLabels.setIcon(icon21)

        self.horizontalLayout.addWidget(self.BtnVisibleLabels)

        self.BtnFullscreenImage = QPushButton(self.GraphWidget)
        self.BtnFullscreenImage.setObjectName(u"BtnFullscreenImage")
        self.BtnFullscreenImage.setMinimumSize(QSize(24, 24))
        self.BtnFullscreenImage.setStyleSheet(u"QPushButton {\n"
                                              "background-color: rgba(255, 255, 255, 80);\n"
                                              "image: None;\n"
                                              "border: 1px solid rgba(0, 0, 0, 80);\n"
                                              "border-radius: 2px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "background-color: rgba(245, 245, 245, 180);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "background-color: rgba(255, 255, 255, 245);\n"
                                              "}\n"
                                              "")
        self.BtnFullscreenImage.setIcon(icon13)

        self.horizontalLayout.addWidget(self.BtnFullscreenImage)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout_10.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout_8.addWidget(self.GraphWidget, 0, 0, 1, 1)

        self.WorkLayout.addWidget(self.GraphWorkFrame)

        self.WorkLayout.setStretch(0, 30)

        self.WorkPreprocLayout.addLayout(self.WorkLayout)

        self.gridLayout_2.addLayout(self.WorkPreprocLayout, 0, 0, 1, 1)

        self.TabWidget.addTab(self.PreprocessorTab, "")
        self.PostprocessorTab = QWidget()
        self.PostprocessorTab.setObjectName(u"PostprocessorTab")
        self.gridLayout_14 = QGridLayout(self.PostprocessorTab)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.WorkPreprocLayout_2 = QVBoxLayout()
        self.WorkPreprocLayout_2.setSpacing(0)
        self.WorkPreprocLayout_2.setObjectName(u"WorkPreprocLayout_2")
        self.WorkLayout_2 = QHBoxLayout()
        self.WorkLayout_2.setSpacing(0)
        self.WorkLayout_2.setObjectName(u"WorkLayout_2")
        self.DataWorkFrame_2 = QFrame(self.PostprocessorTab)
        self.DataWorkFrame_2.setObjectName(u"DataWorkFrame_2")
        self.DataWorkFrame_2.setMaximumSize(QSize(400, 16777215))
        self.DataWorkFrame_2.setFont(font)
        self.DataWorkFrame_2.setStyleSheet(u"background-color : #FFE0FB;")
        self.DataWorkFrame_2.setFrameShape(QFrame.StyledPanel)
        self.DataWorkFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.DataWorkFrame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.DataWorkVerticalLayout_2 = QVBoxLayout()
        self.DataWorkVerticalLayout_2.setSpacing(1)
        self.DataWorkVerticalLayout_2.setObjectName(u"DataWorkVerticalLayout_2")
        self.PathToFileFrame_2 = QFrame(self.DataWorkFrame_2)
        self.PathToFileFrame_2.setObjectName(u"PathToFileFrame_2")
        self.PathToFileFrame_2.setMaximumSize(QSize(16777215, 60))
        self.PathToFileFrame_2.setFont(font)
        self.PathToFileFrame_2.setStyleSheet(u"background-color : rgb(255, 237, 254);")
        self.PathToFileFrame_2.setFrameShape(QFrame.StyledPanel)
        self.PathToFileFrame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.PathToFileFrame_2)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.PathToFileVerticalLayout_2 = QVBoxLayout()
        self.PathToFileVerticalLayout_2.setSpacing(0)
        self.PathToFileVerticalLayout_2.setObjectName(u"PathToFileVerticalLayout_2")
        self.PathToFileLabel_2 = QLabel(self.PathToFileFrame_2)
        self.PathToFileLabel_2.setObjectName(u"PathToFileLabel_2")
        self.PathToFileLabel_2.setMaximumSize(QSize(16777215, 19))
        self.PathToFileLabel_2.setFont(font3)
        self.PathToFileLabel_2.setAlignment(Qt.AlignCenter)

        self.PathToFileVerticalLayout_2.addWidget(self.PathToFileLabel_2)

        self.PathLineHorizontalLayout_2 = QHBoxLayout()
        self.PathLineHorizontalLayout_2.setSpacing(0)
        self.PathLineHorizontalLayout_2.setObjectName(u"PathLineHorizontalLayout_2")
        self.LineEditPath_2 = QLineEdit(self.PathToFileFrame_2)
        self.LineEditPath_2.setObjectName(u"LineEditPath_2")
        self.LineEditPath_2.setMinimumSize(QSize(0, 24))
        self.LineEditPath_2.setFont(font)
        self.LineEditPath_2.setStyleSheet(u"background-color: #FAEDFF;")
        self.LineEditPath_2.setDragEnabled(False)
        self.LineEditPath_2.setReadOnly(True)

        self.PathLineHorizontalLayout_2.addWidget(self.LineEditPath_2)

        self.BtnPath_2 = QToolButton(self.PathToFileFrame_2)
        self.BtnPath_2.setObjectName(u"BtnPath_2")
        self.BtnPath_2.setMinimumSize(QSize(24, 24))
        self.BtnPath_2.setFont(font)
        self.BtnPath_2.setStyleSheet(u"QToolButton {\n"
                                     "background-color: rgba(255, 255, 255, 80);\n"
                                     "border: 1px solid rgba(0, 0, 0, 80);\n"
                                     "border-radius: 2px;\n"
                                     "}\n"
                                     "\n"
                                     "QToolButton:hover {\n"
                                     "background-color: rgba(255, 255, 255, 180);\n"
                                     "}\n"
                                     "\n"
                                     "QToolButton:pressed {\n"
                                     "background-color: rgba(255, 255, 255, 245);\n"
                                     "}\n"
                                     "")
        self.BtnPath_2.setIcon(icon15)

        self.PathLineHorizontalLayout_2.addWidget(self.BtnPath_2)

        self.PathToFileVerticalLayout_2.addLayout(self.PathLineHorizontalLayout_2)

        self.gridLayout_9.addLayout(self.PathToFileVerticalLayout_2, 0, 0, 1, 1)

        self.DataWorkVerticalLayout_2.addWidget(self.PathToFileFrame_2)

        self.line_4 = QFrame(self.DataWorkFrame_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.DataWorkVerticalLayout_2.addWidget(self.line_4)

        self.frame = QFrame(self.DataWorkFrame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color : rgb(255, 237, 254);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.textEditInfo = QTextEdit(self.frame)
        self.textEditInfo.setObjectName(u"textEditInfo")
        self.textEditInfo.setFont(font1)
        self.textEditInfo.setStyleSheet(u"background-color: #FAEDFF;")
        self.textEditInfo.setTextInteractionFlags(Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse)

        self.gridLayout_12.addWidget(self.textEditInfo, 0, 0, 1, 1)

        self.DataWorkVerticalLayout_2.addWidget(self.frame)

        self.DescriptionPowerFrame_2 = QFrame(self.DataWorkFrame_2)
        self.DescriptionPowerFrame_2.setObjectName(u"DescriptionPowerFrame_2")
        self.DescriptionPowerFrame_2.setFont(font)
        self.DescriptionPowerFrame_2.setStyleSheet(u"background-color : rgb(255, 237, 254);")
        self.DescriptionPowerFrame_2.setFrameShape(QFrame.StyledPanel)
        self.DescriptionPowerFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.DescriptionPowerFrame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(30, -1, 30, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.BtnTableResult = QPushButton(self.DescriptionPowerFrame_2)
        self.BtnTableResult.setObjectName(u"BtnTableResult")
        self.BtnTableResult.setMinimumSize(QSize(0, 60))
        self.BtnTableResult.setFont(font3)
        self.BtnTableResult.setStyleSheet(u"QPushButton {\n"
                                          "background-color: rgba(255, 255, 255, 80);\n"
                                          "border: 1px solid rgba(0, 0, 0, 80);\n"
                                          "border-radius: 2px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgba(255, 255, 255, 180);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "background-color: rgba(255, 255, 255, 245);\n"
                                          "}\n"
                                          "")
        self.BtnTableResult.setFlat(False)

        self.verticalLayout_4.addWidget(self.BtnTableResult)

        self.BtnPointResult = QPushButton(self.DescriptionPowerFrame_2)
        self.BtnPointResult.setObjectName(u"BtnPointResult")
        self.BtnPointResult.setMinimumSize(QSize(0, 60))
        self.BtnPointResult.setFont(font3)
        self.BtnPointResult.setStyleSheet(u"QPushButton {\n"
                                          "background-color: rgba(255, 255, 255, 80);\n"
                                          "border: 1px solid rgba(0, 0, 0, 80);\n"
                                          "border-radius: 2px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgba(255, 255, 255, 180);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "background-color: rgba(255, 255, 255, 245);\n"
                                          "}\n"
                                          "")

        self.verticalLayout_4.addWidget(self.BtnPointResult)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LineEditNumRod = QLineEdit(self.DescriptionPowerFrame_2)
        self.LineEditNumRod.setObjectName(u"LineEditNumRod")
        self.LineEditNumRod.setMinimumSize(QSize(0, 30))
        self.LineEditNumRod.setFont(font3)
        self.LineEditNumRod.setStyleSheet(u"")
        self.LineEditNumRod.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.LineEditNumRod)

        self.LineEditPoint = QLineEdit(self.DescriptionPowerFrame_2)
        self.LineEditPoint.setObjectName(u"LineEditPoint")
        self.LineEditPoint.setEnabled(True)
        self.LineEditPoint.setMinimumSize(QSize(0, 30))
        self.LineEditPoint.setFont(font3)
        self.LineEditPoint.setStyleSheet(u"QLineEdit:{\n"
                                         "	background-color: #FAEDFF;\n"
                                         "	border: 1px solid rgba(0, 0, 0, 80);\n"
                                         "	border-radius: 2px;\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit: hover:!pressed{\n"
                                         "background-color: rgba(255.255.255. 80);\n"
                                         "}\n"
                                         "QLineEdit: pressed{\n"
                                         "	background-color: #FAEDFF;\n"
                                         "	border: 1px solid rgba(0, 0, 0, 80);\n"
                                         "	border-radius: 2px;\n"
                                         "}")
        self.LineEditPoint.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.LineEditPoint)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.BtnShowEpure = QPushButton(self.DescriptionPowerFrame_2)
        self.BtnShowEpure.setObjectName(u"BtnShowEpure")
        self.BtnShowEpure.setMinimumSize(QSize(0, 60))
        self.BtnShowEpure.setFont(font3)
        self.BtnShowEpure.setStyleSheet(u"QPushButton {\n"
                                        "background-color: rgba(255, 255, 255, 80);\n"
                                        "border: 1px solid rgba(0, 0, 0, 80);\n"
                                        "border-radius: 2px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgba(255, 255, 255, 180);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "background-color: rgba(255, 255, 255, 245);\n"
                                        "}\n"
                                        "")

        self.verticalLayout_4.addWidget(self.BtnShowEpure)

        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.DataWorkVerticalLayout_2.addWidget(self.DescriptionPowerFrame_2)

        self.DataWorkVerticalLayout_2.setStretch(0, 10)
        self.DataWorkVerticalLayout_2.setStretch(1, 1)
        self.DataWorkVerticalLayout_2.setStretch(2, 60)
        self.DataWorkVerticalLayout_2.setStretch(3, 30)

        self.verticalLayout_3.addLayout(self.DataWorkVerticalLayout_2)

        self.WorkLayout_2.addWidget(self.DataWorkFrame_2)

        self.GraphWorkFrame_2 = QFrame(self.PostprocessorTab)
        self.GraphWorkFrame_2.setObjectName(u"GraphWorkFrame_2")
        self.GraphWorkFrame_2.setStyleSheet(u"background-color: rgb(255, 240, 238)\n"
                                            "/*#FFE4E1*/\n"
                                            "")
        self.GraphWorkFrame_2.setFrameShape(QFrame.StyledPanel)
        self.GraphWorkFrame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.GraphWorkFrame_2)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.WorkWidget_2 = QWidget(self.GraphWorkFrame_2)
        self.WorkWidget_2.setObjectName(u"WorkWidget_2")
        self.WorkWidget_2.setStyleSheet(u"")
        self.gridLayout_15 = QGridLayout(self.WorkWidget_2)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.TableAnswer = QTableWidget(self.WorkWidget_2)
        if self.TableAnswer.columnCount() < 3:
            self.TableAnswer.setColumnCount(3)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font1);
        self.TableAnswer.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font1);
        self.TableAnswer.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font1);
        self.TableAnswer.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        if self.TableAnswer.rowCount() < 1:
            self.TableAnswer.setRowCount(1)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font1);
        self.TableAnswer.setVerticalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font6);
        self.TableAnswer.setItem(0, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font6);
        self.TableAnswer.setItem(0, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font6);
        self.TableAnswer.setItem(0, 2, __qtablewidgetitem23)
        self.TableAnswer.setObjectName(u"TableAnswer")
        self.TableAnswer.setMaximumSize(QSize(16777215, 16777215))
        self.TableAnswer.setFont(font1)
        self.TableAnswer.setStyleSheet(u"background-color: #FAEDFF;")
        self.TableAnswer.setFrameShadow(QFrame.Raised)
        self.TableAnswer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TableAnswer.setAlternatingRowColors(False)
        self.TableAnswer.setShowGrid(True)
        self.TableAnswer.setGridStyle(Qt.DashDotLine)
        self.TableAnswer.setCornerButtonEnabled(False)
        self.TableAnswer.horizontalHeader().setMinimumSectionSize(60)
        self.TableAnswer.horizontalHeader().setDefaultSectionSize(63)
        self.TableAnswer.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_11.addWidget(self.TableAnswer, 0, 0, 1, 1)

        self.WelcomeLabel = QLabel(self.WorkWidget_2)
        self.WelcomeLabel.setObjectName(u"WelcomeLabel")
        self.WelcomeLabel.setMaximumSize(QSize(16777215, 19))
        self.WelcomeLabel.setFont(font3)
        self.WelcomeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.WelcomeLabel, 0, 1, 1, 1)

        self.GraphWidget_2 = QFrame(self.WorkWidget_2)
        self.GraphWidget_2.setObjectName(u"GraphWidget_2")
        self.GraphWidget_2.setFrameShape(QFrame.StyledPanel)
        self.GraphWidget_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.GraphWidget_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.BtnVisibleLabels_2 = QPushButton(self.GraphWidget_2)
        self.BtnVisibleLabels_2.setObjectName(u"BtnVisibleLabels_2")
        self.BtnVisibleLabels_2.setMinimumSize(QSize(24, 24))
        self.BtnVisibleLabels_2.setStyleSheet(u"QPushButton {\n"
                                              "background-color: rgba(255, 255, 255, 80);\n"
                                              "image: None;\n"
                                              "border: 1px solid rgba(0, 0, 0, 80);\n"
                                              "border-radius: 2px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "background-color: rgba(245, 245, 245, 180);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "background-color: rgba(255, 255, 255, 245);\n"
                                              "}\n"
                                              "")
        self.BtnVisibleLabels_2.setIcon(icon21)

        self.horizontalLayout_7.addWidget(self.BtnVisibleLabels_2)

        self.BtnFullscreenImage_2 = QPushButton(self.GraphWidget_2)
        self.BtnFullscreenImage_2.setObjectName(u"BtnFullscreenImage_2")
        self.BtnFullscreenImage_2.setMinimumSize(QSize(24, 24))
        self.BtnFullscreenImage_2.setStyleSheet(u"QPushButton {\n"
                                                "background-color: rgba(255, 255, 255, 80);\n"
                                                "image: None;\n"
                                                "border: 1px solid rgba(0, 0, 0, 80);\n"
                                                "border-radius: 2px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "background-color: rgba(245, 245, 245, 180);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "background-color: rgba(255, 255, 255, 245);\n"
                                                "}\n"
                                                "")
        self.BtnFullscreenImage_2.setIcon(icon13)

        self.horizontalLayout_7.addWidget(self.BtnFullscreenImage_2)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.gridLayout_13.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.gridLayout_11.addWidget(self.GraphWidget_2, 0, 2, 1, 1)

        self.gridLayout_15.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.gridLayout_16.addWidget(self.WorkWidget_2, 0, 0, 1, 1)

        self.WorkLayout_2.addWidget(self.GraphWorkFrame_2)

        self.WorkLayout_2.setStretch(0, 30)

        self.WorkPreprocLayout_2.addLayout(self.WorkLayout_2)

        self.WorkPreprocLayout_2.setStretch(0, 95)

        self.gridLayout_14.addLayout(self.WorkPreprocLayout_2, 0, 0, 1, 1)

        self.TabWidget.addTab(self.PostprocessorTab, "")

        self.MainLayout.addWidget(self.TabWidget)

        self.gridLayout.addLayout(self.MainLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.FileMenu = QMenu(self.menuBar)
        self.FileMenu.setObjectName(u"FileMenu")
        self.FileMenu.setTearOffEnabled(False)
        icon22 = QIcon()
        icon22.addFile(u":/icon/icons/File.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.FileMenu.setIcon(icon22)
        self.FileMenu.setSeparatorsCollapsible(False)
        self.FileMenu.setToolTipsVisible(False)
        self.EditMenu = QMenu(self.menuBar)
        self.EditMenu.setObjectName(u"EditMenu")
        icon23 = QIcon()
        icon23.addFile(u":/icon/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.EditMenu.setIcon(icon23)
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        icon24 = QIcon()
        icon24.addFile(u":/icon/icons/help.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuHelp.setIcon(icon24)
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMaximumSize(QSize(16777215, 15))
        font8 = QFont()
        font8.setFamilies([u"Montserrat"])
        font8.setBold(False)
        self.statusBar.setFont(font8)
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.FileMenu.menuAction())
        self.menuBar.addAction(self.EditMenu.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.FileMenu.addAction(self.CreateAction)
        self.FileMenu.addAction(self.OpenAction)
        self.FileMenu.addAction(self.SaveAction)
        self.FileMenu.addAction(self.SaveAsAction)
        self.FileMenu.addSeparator()
        self.FileMenu.addAction(self.PrintAction)
        self.FileMenu.addSeparator()
        self.FileMenu.addAction(self.ExitAction)
        self.EditMenu.addAction(self.UndoAction)
        self.EditMenu.addAction(self.RedoAction)
        self.EditMenu.addSeparator()
        self.EditMenu.addAction(self.CutAction)
        self.EditMenu.addAction(self.CopyAction)
        self.EditMenu.addAction(self.PasteAction)
        self.EditMenu.addAction(self.DeleteAction)
        self.menuHelp.addAction(self.AboutAction)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.AboutPreprocessorAction)
        self.menuHelp.addAction(self.AboutProcessorAction)
        self.menuHelp.addAction(self.AboutPostprocessorAction)

        self.retranslateUi(MainWindow)

        self.TabWidget.setCurrentIndex(0)
        self.BtnTableResult.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.CreateAction.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        # if QT_CONFIG(tooltip)
        self.CreateAction.setToolTip(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.CreateAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                  u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u0430\u0439\u043b",
                                                                  None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.CreateAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
        # endif // QT_CONFIG(shortcut)
        self.OpenAction.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        # if QT_CONFIG(statustip)
        self.OpenAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b",
                                                                None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.OpenAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
        # endif // QT_CONFIG(shortcut)
        self.SaveAction.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        # if QT_CONFIG(statustip)
        self.SaveAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b",
                                                                None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.SaveAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
        # endif // QT_CONFIG(shortcut)
        self.SaveAsAction.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...",
                                                             None))
        # if QT_CONFIG(statustip)
        self.SaveAsAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                  u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b \u043a\u0430\u043a...",
                                                                  None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.SaveAsAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
        # endif // QT_CONFIG(shortcut)
        self.PrintAction.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
        # if QT_CONFIG(statustip)
        self.PrintAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                 u"\u041f\u0435\u0447\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u0430",
                                                                 None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.PrintAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
        # endif // QT_CONFIG(shortcut)
        self.ExitAction.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        # if QT_CONFIG(statustip)
        self.ExitAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                u"\u0412\u044b\u0445\u043e\u0434 \u0438\u0437 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b",
                                                                None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.ExitAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
        # endif // QT_CONFIG(shortcut)
        self.UndoAction.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        # if QT_CONFIG(statustip)
        self.UndoAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435",
                                                                None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.UndoAction.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(shortcut)
        self.UndoAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
        # endif // QT_CONFIG(shortcut)
        self.RedoAction.setText(
            QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c", None))
        # if QT_CONFIG(statustip)
        self.RedoAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435",
                                                                None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.RedoAction.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(shortcut)
        self.RedoAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Z", None))
        # endif // QT_CONFIG(shortcut)
        self.CutAction.setText(
            QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0440\u0435\u0437\u0430\u0442\u044c", None))
        # if QT_CONFIG(statustip)
        self.CutAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                               u"\u0412\u044b\u0440\u0435\u0437\u0430\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442",
                                                               None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.CutAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
        # endif // QT_CONFIG(shortcut)
        self.CopyAction.setText(
            QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                                       None))
        # if QT_CONFIG(statustip)
        self.CopyAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 \u0431\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430",
                                                                None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.CopyAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
        # endif // QT_CONFIG(shortcut)
        self.PasteAction.setText(
            QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c", None))
        # if QT_CONFIG(statustip)
        self.PasteAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                 u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0438\u0437 \u0431\u0443\u0444\u0435\u0440\u0430 \u043e\u0431\u043c\u0435\u043d\u0430",
                                                                 None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.PasteAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
        # endif // QT_CONFIG(shortcut)
        self.DeleteAction.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        # if QT_CONFIG(statustip)
        self.DeleteAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                  u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442",
                                                                  None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.DeleteAction.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
        # endif // QT_CONFIG(shortcut)
        self.AboutAction.setText(QCoreApplication.translate("MainWindow",
                                                            u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435...",
                                                            None))
        # if QT_CONFIG(statustip)
        self.AboutAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                 u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e  \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435...",
                                                                 None))
        # endif // QT_CONFIG(statustip)
        self.AboutPreprocessorAction.setText(QCoreApplication.translate("MainWindow",
                                                                        u"\u041e \u043f\u0440\u0435\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0435...",
                                                                        None))
        # if QT_CONFIG(statustip)
        self.AboutPreprocessorAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                             u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u0435\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0435...",
                                                                             None))
        # endif // QT_CONFIG(statustip)
        self.AboutProcessorAction.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u041e \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0435...",
                                                                     None))
        # if QT_CONFIG(statustip)
        self.AboutProcessorAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                          u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0435...",
                                                                          None))
        # endif // QT_CONFIG(statustip)
        self.AboutPostprocessorAction.setText(QCoreApplication.translate("MainWindow",
                                                                         u"\u041e \u043f\u043e\u0441\u0442\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0435...",
                                                                         None))
        # if QT_CONFIG(statustip)
        self.AboutPostprocessorAction.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                              u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u0441\u0442\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0435...",
                                                                              None))
        # endif // QT_CONFIG(statustip)
        self.NameLabel.setText(QCoreApplication.translate("MainWindow", u"Name File", None))
        # if QT_CONFIG(statustip)
        self.BtnRoll.setStatusTip(QCoreApplication.translate("MainWindow",
                                                             u"\u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443",
                                                             None))
        # endif // QT_CONFIG(statustip)
        self.BtnRoll.setText("")
        # if QT_CONFIG(statustip)
        self.BtnExpand.setStatusTip(QCoreApplication.translate("MainWindow",
                                                               u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c/\u0437\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u043e\u043b\u043d\u043e\u044d\u043a\u0440\u0430\u043d\u043d\u044b\u0439 \u0440\u0435\u0436\u0438\u043c",
                                                               None))
        # endif // QT_CONFIG(statustip)
        self.BtnExpand.setText("")
        # if QT_CONFIG(statustip)
        self.BtnClose.setStatusTip(QCoreApplication.translate("MainWindow",
                                                              u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443",
                                                              None))
        # endif // QT_CONFIG(statustip)
        self.BtnClose.setText("")
        self.PathToFileLabel.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u041f\u0443\u0442\u044c \u0434\u043e \u0444\u0430\u0439\u043b\u0430",
                                                                None))
        self.LineEditPath.setText("")
        self.LineEditPath.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                        u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0451\u043d \u043f\u0443\u0442\u044c \u0434\u043e \u0444\u0430\u0439\u043b\u0430...",
                                                                        None))
        # if QT_CONFIG(statustip)
        self.BtnPath.setStatusTip(QCoreApplication.translate("MainWindow",
                                                             u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b",
                                                             None))
        # endif // QT_CONFIG(statustip)
        self.BtnPath.setText("")
        self.DescriptionRodsLabel.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441\u0442\u0435\u0440\u0436\u043d\u0435\u0439",
                                                                     None))
        ___qtablewidgetitem = self.TableRodsDescription.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"L, \u043c", None));
        ___qtablewidgetitem1 = self.TableRodsDescription.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"A, \u043c\u00b2", None));
        ___qtablewidgetitem2 = self.TableRodsDescription.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"E, \u041F\u0430", None));
        ___qtablewidgetitem3 = self.TableRodsDescription.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"[\u03c3], \u041F\u0430", None));
        ___qtablewidgetitem4 = self.TableRodsDescription.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u0440\u0436\u0435\u043d\u044c 1", None));

        __sortingEnabled = self.TableRodsDescription.isSortingEnabled()
        self.TableRodsDescription.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.TableRodsDescription.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem6 = self.TableRodsDescription.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem7 = self.TableRodsDescription.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem8 = self.TableRodsDescription.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.TableRodsDescription.setSortingEnabled(__sortingEnabled)

        # if QT_CONFIG(statustip)
        self.BtnDeleteRodsDescription.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                              u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0441\u0442\u0435\u0440\u0436\u0435\u043d\u044c",
                                                                              None))
        # endif // QT_CONFIG(statustip)
        self.BtnDeleteRodsDescription.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        # if QT_CONFIG(statustip)
        self.BtnAddRodsDescription.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                           u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0435\u0440\u0436\u0435\u043d\u044c",
                                                                           None))
        # endif // QT_CONFIG(statustip)
        self.BtnAddRodsDescription.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.DescriptionPowerRodsLabel.setText(QCoreApplication.translate("MainWindow",
                                                                          u"\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0435\n"
                                                                          "\u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0438",
                                                                          None))
        ___qtablewidgetitem9 = self.TableRodsPowerDescription.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"q", None));
        ___qtablewidgetitem10 = self.TableRodsPowerDescription.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("MainWindow", u"C\u0442\u0435\u0440\u0436\u0435\u043d\u044c 1", None));

        __sortingEnabled1 = self.TableRodsPowerDescription.isSortingEnabled()
        self.TableRodsPowerDescription.setSortingEnabled(False)
        ___qtablewidgetitem11 = self.TableRodsPowerDescription.item(0, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.TableRodsPowerDescription.setSortingEnabled(__sortingEnabled1)

        self.CheckBoxLeftSealing.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0417\u0430\u0434\u0435\u043b\u043a\u0430 \u0441\u043b\u0435\u0432\u0430",
                                                                    None))
        self.CheckBoxRightSealing.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u0417\u0430\u0434\u0435\u043b\u043a\u0430 \u0441\u043f\u0440\u0430\u0432\u0430",
                                                                     None))
        self.DescriptionPowerKontsLabel.setText(QCoreApplication.translate("MainWindow",
                                                                           u"\u0421\u043e\u0441\u0440\u0435\u0434\u043e\u0442\u043e\u0447\u0435\u043d\u043d\u044b\u0435\n"
                                                                           "\u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0438",
                                                                           None))
        ___qtablewidgetitem12 = self.TableKontsPowerDescription.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"F, qL", None));
        ___qtablewidgetitem13 = self.TableKontsPowerDescription.verticalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u0435\u043b 1", None));
        ___qtablewidgetitem14 = self.TableKontsPowerDescription.verticalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u0435\u043b 2", None));

        __sortingEnabled2 = self.TableKontsPowerDescription.isSortingEnabled()
        self.TableKontsPowerDescription.setSortingEnabled(False)
        ___qtablewidgetitem15 = self.TableKontsPowerDescription.item(0, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem16 = self.TableKontsPowerDescription.item(1, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.TableKontsPowerDescription.setSortingEnabled(__sortingEnabled2)

        # if QT_CONFIG(statustip)
        self.BtnUploadData.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                   u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b",
                                                                   None))
        # endif // QT_CONFIG(statustip)
        self.BtnUploadData.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 \u0444\u0430\u0439\u043b\u0430",
                                                              None))
        # if QT_CONFIG(statustip)
        self.BtnCalc.setStatusTip(QCoreApplication.translate("MainWindow",
                                                             u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440",
                                                             None))
        # endif // QT_CONFIG(statustip)
        self.BtnCalc.setText(
            QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c",
                                       None))
        # if QT_CONFIG(statustip)
        self.BtnVisibleLabels.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                      u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u043d\u0430 \u0440\u0438\u0441\u0443\u043d\u043a\u0435",
                                                                      None))
        # endif // QT_CONFIG(statustip)
        self.BtnVisibleLabels.setText("")
        # if QT_CONFIG(statustip)
        self.BtnFullscreenImage.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                        u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0440\u0438\u0441\u0443\u043d\u043e\u043a \u043d\u0430 \u043f\u043e\u043b\u043d\u044b\u0439 \u044d\u043a\u0440\u0430\u043d",
                                                                        None))
        # endif // QT_CONFIG(statustip)
        self.BtnFullscreenImage.setText("")
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.PreprocessorTab), QCoreApplication.translate("MainWindow",
                                                                                                           u"\u041f\u0440\u0435\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440",
                                                                                                           None))
        self.PathToFileLabel_2.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u041f\u0443\u0442\u044c \u0434\u043e \u0444\u0430\u0439\u043b\u0430",
                                                                  None))
        self.LineEditPath_2.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0451\u043d \u043f\u0443\u0442\u044c \u0434\u043e \u0444\u0430\u0439\u043b\u0430...",
                                                                          None))
        # if QT_CONFIG(statustip)
        self.BtnPath_2.setStatusTip(QCoreApplication.translate("MainWindow",
                                                               u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b",
                                                               None))
        # endif // QT_CONFIG(statustip)
        self.BtnPath_2.setText("")
        self.textEditInfo.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                        u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044b \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0441\u0442\u0435\u0440\u0436\u043d\u0435\u0439, \u0443\u0437\u043b\u043e\u0432 \u0438 \u043d\u0430\u0433\u0440\u0443\u0437\u043e\u043a.  \u0414\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u0434\u043e \u0444\u0430\u0439\u043b\u0430...",
                                                                        None))
        self.BtnTableResult.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0412\u044b\u0432\u043e\u0434 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u0440\u0430\u0441\u0447\u0451\u0442\u043e\u0432\n"
                                                               "\u0432 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u043e\u043c \u0432\u0438\u0434\u0435",
                                                               None))
        self.BtnPointResult.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0412\u044b\u0432\u043e\u0434 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0432 \u0442\u043e\u0447\u043a\u0435",
                                                               None))
        self.LineEditNumRod.setText("")
        self.LineEditNumRod.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u041d\u043e\u043c\u0435\u0440 \u0441\u0442\u0435\u0440\u0436\u043d\u044f:",
                                                                          None))
        self.LineEditPoint.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430 X:", None))
        self.BtnShowEpure.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u044d\u043f\u044e\u0440\u044b",
                                                             None))
        ___qtablewidgetitem17 = self.TableAnswer.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Nx", None));
        ___qtablewidgetitem18 = self.TableAnswer.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Ux", None));
        ___qtablewidgetitem19 = self.TableAnswer.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"[\u03c3]x", None));
        ___qtablewidgetitem20 = self.TableAnswer.verticalHeaderItem(0)
        ___qtablewidgetitem20.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u0440\u0436\u0435\u043d\u044c 1", None));

        __sortingEnabled3 = self.TableAnswer.isSortingEnabled()
        self.TableAnswer.setSortingEnabled(False)
        ___qtablewidgetitem21 = self.TableAnswer.item(0, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem22 = self.TableAnswer.item(0, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem23 = self.TableAnswer.item(0, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.TableAnswer.setSortingEnabled(__sortingEnabled3)

        self.WelcomeLabel.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0436\u0435\u043b\u0430\u0435\u043c\u0443\u044e \u0444\u0443\u043d\u043a\u0446\u0438\u044e",
                                                             None))
        # if QT_CONFIG(statustip)
        self.BtnVisibleLabels_2.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                        u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u043d\u0430 \u0440\u0438\u0441\u0443\u043d\u043a\u0435",
                                                                        None))
        # endif // QT_CONFIG(statustip)
        self.BtnVisibleLabels_2.setText("")
        # if QT_CONFIG(statustip)
        self.BtnFullscreenImage_2.setStatusTip(QCoreApplication.translate("MainWindow",
                                                                          u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0440\u0438\u0441\u0443\u043d\u043e\u043a \u043d\u0430 \u043f\u043e\u043b\u043d\u044b\u0439 \u044d\u043a\u0440\u0430\u043d",
                                                                          None))
        # endif // QT_CONFIG(statustip)
        self.BtnFullscreenImage_2.setText("")
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.PostprocessorTab),
                                  QCoreApplication.translate("MainWindow",
                                                             u"\u041f\u043e\u0441\u0442\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440",
                                                             None))
        # if QT_CONFIG(tooltip)
        self.FileMenu.setToolTip(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.FileMenu.setStatusTip(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.FileMenu.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.FileMenu.setAccessibleName(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.FileMenu.setAccessibleDescription(
            QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        # endif // QT_CONFIG(accessibility)
        self.FileMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.EditMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043a\u0430", None))
        self.menuHelp.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

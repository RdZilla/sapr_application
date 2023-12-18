# -*- coding: UTF-8 -*
import warnings
import sys
import json
import re
import os

from PySide6.QtCore import Signal, QSize, Qt
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QFont

from src.gui.gui_window import Ui_MainWindow
from src.draw_pic_preprocessor import draw_picture
from src.draw_epure_postprocessor import draw_epure
from src.processor import nx_equation, ux_equation, sgx_equation


class MainWindow(QMainWindow):
    resized = Signal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.num_rod = None
        self.value_x = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setWindowIcon(QIcon(u":/icon/icons/cad_icon.ico"))
        self.ui.NameLabel.setText(f"САПР - Untitled")
        self.setWindowTitle(u"\u0421\u0410\u041F\u0420 - Untitled")
        self.file_name = None

        # app manipulation buttons
        self.ui.BtnRoll.clicked.connect(self.change_view_window)
        self.ui.BtnExpand.clicked.connect(self.change_size_window)
        self.ui.BtnClose.clicked.connect(self.exit_frame)

        self.ui.CreateAction.triggered.connect(self.create_new_file_action)
        self.ui.OpenAction.triggered.connect(self.file_path_choose)
        self.ui.SaveAction.triggered.connect(self.save_file)
        self.ui.SaveAsAction.triggered.connect(self.save_as_file)
        self.ui.PrintAction.triggered.connect(self.print_file)
        self.ui.ExitAction.triggered.connect(self.exit_frame)
        self.ui.AboutAction.triggered.connect(self.show_information_about_program)
        self.ui.AboutPreprocessorAction.triggered.connect(self.show_information_about_preproc)
        self.ui.AboutProcessorAction.triggered.connect(self.show_information_about_proc)
        self.ui.AboutPostprocessorAction.triggered.connect(self.show_information_about_postprocessor)

        self.widget_width = self.ui.GraphWidget.width()
        self.widget_height = self.ui.GraphWidget.height()
        # ========================================================================
        # TAB_1
        self.list_of_length = [1]
        self.list_of_width = [1]
        self.list_of_young_modulus = [1]
        self.list_of_sigma = [1]

        self.list_of_loads = [0]

        self.powers = {'1': 0, '2': 0}

        self.left_sealing = True
        self.right_sealing = False

        self.ui.BtnPath.clicked.connect(self.file_path_choose)

        self.ui.TableRodsDescription.cellChanged.connect(self.edit_lists_description)
        self.ui.TableRodsPowerDescription.cellChanged.connect(self.edit_list_power_rods)
        self.ui.TableKontsPowerDescription.cellChanged.connect(self.edit_dict_power_knots)

        self.ui.BtnAddRodsDescription.clicked.connect(self.add_rows)
        self.ui.BtnDeleteRodsDescription.clicked.connect(self.delete_rows)

        self.ui.CheckBoxLeftSealing.clicked.connect(self.left_right_sealing)
        self.ui.CheckBoxRightSealing.clicked.connect(self.left_right_sealing)

        self.ui.BtnUploadData.clicked.connect(self.file_path_choose)
        self.ui.BtnCalc.clicked.connect(self.calc_btn_clicked)

        self.visible = True
        self.ui.BtnVisibleLabels.clicked.connect(self.visible_graph_labels)

        self.ui.BtnFullscreenImage.clicked.connect(self.fullscreen_image)

        self.resized.connect(self.resize_window)
        # =============================================================================
        # TAB_2
        self.widget_width_2 = None
        self.widget_height_2 = None
        self.list_of_length_preproc = [1]
        self.list_of_width_preproc = [1]
        self.list_of_young_modulus_preproc = [1]
        self.list_of_sigma_preproc = [1]

        self.list_of_loads_preproc = [0]

        self.powers_preproc = {'1': 0, '2': 0}

        self.left_sealing_2 = True
        self.right_sealing_2 = True

        self.ui.TableAnswer.hide()
        self.ui.GraphWidget_2.hide()

        self.ui.BtnPath_2.clicked.connect(self.file_path_choose_2)

        self.ui.BtnTableResult.clicked.connect(self.print_table_result)

        self.ui.LineEditPoint.hide()
        self.ui.LineEditNumRod.hide()

        self.ui.BtnPointResult.clicked.connect(self.show_line_edit)
        self.ui.LineEditPoint.textChanged.connect(self.calc_result_in_point)
        self.ui.LineEditNumRod.textChanged.connect(self.calc_result_in_point)

        self.ui.BtnShowEpure.clicked.connect(self.show_epure)

        self.visible_2 = True
        self.ui.BtnVisibleLabels_2.clicked.connect(self.visible_graph_labels_2)
        self.ui.BtnFullscreenImage_2.clicked.connect(self.fullscreen_image_2)

    # =======================================================================================
    def change_size_window(self):
        if not self.isFullScreen():
            icon_fullscreen_exit = QIcon()
            icon_fullscreen_exit.addFile(u":/icon/icons/fullscreen_exit.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.BtnExpand.setIcon(icon_fullscreen_exit)
            self.ui.BtnExpand.setIconSize(QSize(20, 20))
            self.showFullScreen()
        else:
            icon_fullscreen = QIcon()
            icon_fullscreen.addFile(u":/icon/icons/fullscreen.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.BtnExpand.setIcon(icon_fullscreen)
            self.ui.BtnExpand.setIconSize(QSize(20, 20))
            self.showNormal()
        self.paint_picture()

    def change_view_window(self):
        if not self.isMaximized():
            self.showMinimized()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainWindow, self).resizeEvent(event)

    def resize_window(self):
        self.widget_width = self.ui.GraphWidget.width()
        self.widget_height = self.ui.GraphWidget.height()
        self.widget_width = self.ui.GraphWidget_2.width()
        self.widget_height = self.ui.GraphWidget_2.height()
        self.paint_picture()

        self.widget_width_2 = self.ui.GraphWidget.width()
        self.widget_height_2 = self.ui.GraphWidget.height()
        self.widget_width_2 = self.ui.GraphWidget_2.width()
        self.widget_height_2 = self.ui.GraphWidget_2.height()

        width_table_answer = self.ui.TableAnswer.width()
        size_column = width_table_answer / 4
        self.ui.TableAnswer.horizontalHeader().resizeSection(0, size_column)
        self.ui.TableAnswer.horizontalHeader().resizeSection(1, size_column)
        self.ui.TableAnswer.horizontalHeader().resizeSection(2, size_column)

    def save_file(self):
        try:
            discharge = self.calculation()
            if self.file_name:
                if self.file_name[0] != '':
                    with open(self.file_name[0], 'w') as file:
                        json.dump(discharge, file, indent=4)
                    file.close()
                else:
                    self.save_as_file()
            else:
                self.save_as_file()
        except Exception as e:
            print(e)

    def save_as_file(self):
        try:
            discharge = self.calculation()
            text_dir_data = 'src/resources/data'
            if self.file_name is None:
                file_name_new = QFileDialog.getSaveFileName(self, 'Сохранение файла', text_dir_data,
                                                            "Json Files (*.json);;Все файлы (*)")
            else:
                if self.file_name[0] != "":
                    text_dir = re.sub(r'\w*\.\S*', '', self.file_name[0])
                    file_name_new = QFileDialog.getSaveFileName(self, 'Сохранение файла', text_dir,
                                                                "Json Files (*.json);;Все файлы (*)")
                else:
                    file_name_new = QFileDialog.getSaveFileName(self, 'Сохранение файла', text_dir_data,
                                                                "Json Files (*.json);;Все файлы (*)")
            if file_name_new[0]:
                self.file_name = file_name_new
                self.ui.LineEditPath.setText(self.file_name[0])

                text_label_file = re.sub(r'\S*/', '', self.file_name[0])
                text_label = 'САПР — ' + text_label_file
                self.ui.NameLabel.setText(text_label)
                self.setWindowTitle(f"{text_label}")
                with open(self.file_name[0], 'w') as file:
                    json.dump(discharge, file, indent=4)
                file.close()
        except Exception as e:
            print(e)

    def create_new_file_action(self):

        self.list_of_length = [1]
        self.list_of_width = [1]
        self.list_of_young_modulus = [1]
        self.list_of_sigma = [1]

        self.list_of_loads = [0]

        self.powers = {'1': 0, '2': 0}

        self.save_as_file()
        self.change_in_line_path()

    def print_file(self):
        self.warning_development()

    def show_information_about_program(self):
        self.warning_development()

    def show_information_about_preproc(self):
        self.warning_development()

    def show_information_about_proc(self):
        self.warning_development()

    def show_information_about_postprocessor(self):
        self.warning_development()

    def warning_development(self):
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)

        msg = QMessageBox(self)
        msg.setFont(font1)
        msg.setWindowFlags(QtCore.Qt.ToolTip)

        msg.setText("Упс...\n"
                    "Раздел находится в разработке...\n"
                    "Ждите в следующих обновлениях")
        msg.setStyleSheet('background-color : rgb(235, 215, 234);')
        btn_accept = msg.addButton(QMessageBox.StandardButton.Apply)
        btn_accept.setStyleSheet(u"QPushButton {\n"
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
        btn_accept.setMinimumSize(75, 28)
        btn_accept.setText('Ок')
        btn_accept.setFont(font1)
        msg.setDefaultButton(btn_accept)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()

    def warning_file_error(self, e):
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)

        msg = QMessageBox(self)
        msg.setFont(font1)
        msg.setWindowFlags(QtCore.Qt.ToolTip)

        msg.setText("Файл повреждён или не соответствует шаблону\n" +
                    "Проверьте структуру файла вручную согласно справке или создайте новый\n" +
                    f"Код ошибки: {e}")
        msg.setStyleSheet('background-color : rgb(235, 215, 234);')
        btn_accept = msg.addButton(QMessageBox.StandardButton.Apply)
        btn_accept.setStyleSheet(u"QPushButton {\n"
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
        btn_accept.setMinimumSize(75, 28)
        btn_accept.setText('Ок')
        btn_accept.setFont(font1)
        msg.setDefaultButton(btn_accept)
        msg.setIcon(QMessageBox.Critical)
        msg.exec()

    def value_error(self, e, num_table):
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)

        msg = QMessageBox(self)
        msg.setFont(font1)
        msg.setWindowFlags(QtCore.Qt.ToolTip)
        name_table = ''
        if num_table == 1:
            name_table = 'характеристик стержня'
        if num_table == 2:
            name_table = 'распределённых нагрузок'
        if num_table == 3:
            name_table = 'сосредоточенных нагрузок'
        msg.setText("Введён символ вместо численного значения\n" +
                    f"Проверьте все заданные значения в таблице {name_table}\n"
                    "Символьные значения будут перезаписаны на 0\n\n" +
                    f"Код ошибки: {e}")
        msg.setStyleSheet('background-color : rgb(235, 215, 234);')
        btn_accept = msg.addButton(QMessageBox.StandardButton.Apply)
        btn_accept.setStyleSheet(u"QPushButton {\n"
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
        btn_accept.setMinimumSize(75, 28)
        btn_accept.setText('Ок')
        btn_accept.setFont(font1)
        msg.setDefaultButton(btn_accept)
        msg.setIcon(QMessageBox.Critical)
        msg.exec()

    def incorrect_value(self, error_type):
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)

        msg = QMessageBox(self)
        msg.setFont(font1)
        msg.setWindowFlags(QtCore.Qt.ToolTip)

        if error_type == 0:
            msg.setText('Введено некорректное значение (значение не может быть нулевым)\n'
                        'Значение будет изменено на 1')
        if error_type == 1:
            msg.setText('Введено некорректное значение (значение не может быть отрицательным)\n'
                        'Значение будет изменено на соответствующее по модулю')

        if error_type == 2:
            msg.setText('Введено некорректное значение\n'
                        '(значение не может быть нулевым или отрицательным)\n'
                        'Значение будет изменено на 1')
        if error_type == 3:
            msg.setText('Введено некорректное значение\n'
                        '(Стержня с таким номером не существует)\n'
                        'Значение будет изменено на 1')

        msg.setStyleSheet('background-color : rgb(235, 215, 234);')
        btn_accept = msg.addButton(QMessageBox.StandardButton.Apply)
        btn_accept.setStyleSheet(u"QPushButton {\n"
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
        btn_accept.setMinimumSize(75, 28)
        btn_accept.setText('Ок')
        btn_accept.setFont(font1)
        msg.setDefaultButton(btn_accept)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()

    def sealing_error(self):
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)

        msg = QMessageBox(self)
        msg.setFont(font1)
        msg.setWindowFlags(QtCore.Qt.ToolTip)

        msg.setText('Должна присутствовать хотя бы одна заделка')

        msg.setStyleSheet('background-color : rgb(235, 215, 234);')
        btn_accept = msg.addButton(QMessageBox.StandardButton.Apply)
        btn_accept.setStyleSheet(u"QPushButton {\n"
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
        btn_accept.setMinimumSize(75, 28)
        btn_accept.setText('Ок')
        btn_accept.setFont(font1)
        msg.setDefaultButton(btn_accept)
        msg.setIcon(QMessageBox.Critical)
        msg.exec()

    def value_x_error(self):
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)

        msg = QMessageBox(self)
        msg.setFont(font1)
        msg.setWindowFlags(QtCore.Qt.ToolTip)

        msg.setText('Введено некорректное значение\n'
                    '(значение не может быть отрицательным или больше длины стержням)\n'
                    'Значение будет изменено на 0')

        msg.setStyleSheet('background-color : rgb(235, 215, 234);')
        btn_accept = msg.addButton(QMessageBox.StandardButton.Apply)
        btn_accept.setStyleSheet(u"QPushButton {\n"
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
        btn_accept.setMinimumSize(75, 28)
        btn_accept.setText('Ок')
        btn_accept.setFont(font1)
        msg.setDefaultButton(btn_accept)
        msg.setIcon(QMessageBox.Critical)
        msg.exec()

    # =========================================================
    def exit_frame(self):
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)

        msg = QMessageBox(self)
        msg.setFont(font1)
        msg.setWindowFlags(QtCore.Qt.ToolTip)

        msg.setText("Вы точно хотите выйти?")
        msg.setStyleSheet('background-color : rgb(235, 215, 234);')

        btn_accept = msg.addButton(QMessageBox.StandardButton.Close)
        btn_accept.setStyleSheet(u"QPushButton {\n"
                                 "background-color: rgba(255, 255, 255, 80);\n"
                                 "border: 1px solid rgba(0, 0, 0, 80);\n"
                                 "border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "background-color: rgba(229, 0, 0, 160);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "background-color: rgba(229, 0, 0, 240);\n"
                                 "}\n"
                                 "")
        btn_accept.setMinimumSize(75, 28)
        btn_accept.setText('Выйти')
        btn_accept.setFont(font1)
        btn_cancel = msg.addButton(QMessageBox.StandardButton.Cancel)
        btn_cancel.setStyleSheet(u"QPushButton {\n"
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
        btn_cancel.setMinimumSize(75, 28)
        btn_cancel.setText('Отмена')
        btn_cancel.setFont(font1)
        msg.setDefaultButton(btn_cancel)
        msg.setIcon(QMessageBox.Icon.Question)
        button = msg.exec()

        if button == QMessageBox.Close:
            sys.exit()
    # =======================================================================================
    # TAB_1

    def create_new_file_from_path(self):
        self.list_of_length = [1]
        self.list_of_width = [1]
        self.list_of_young_modulus = [1]
        self.list_of_sigma = [1]

        self.list_of_loads = [0]

        self.powers = {'1': 0, '2': 0}

    def file_path_choose(self):
        text_dir_data = 'src/resources/data'
        if self.file_name is None:
            self.file_name = QFileDialog.getOpenFileName(self, 'Открытие файла', text_dir_data,
                                                         "Json Files (*.json);;Все файлы (*)")
        else:
            if self.file_name[0] != "":
                text_dir = re.sub(r'\w*\.\S*', '', self.file_name[0])
                self.file_name = QFileDialog.getOpenFileName(self, 'Открытие файла', text_dir,
                                                             "Json Files (*.json);;Все файлы (*)")

            else:
                self.file_name = QFileDialog.getOpenFileName(self, 'Открытие файла', text_dir_data,
                                                             "Json Files (*.json);;Все файлы (*)")
        if self.file_name[0] != "":
            self.ui.LineEditPath.setText(self.file_name[0])
            try:
                self.change_in_line_path()
            except Exception as e:
                self.warning_file_error(e)
        else:
            self.file_name = None

    def change_in_line_path(self):
        text_path_file = self.ui.LineEditPath.text()
        text_name_label = 'САПР — ' + re.sub(r'\S*/', '', text_path_file)
        self.ui.NameLabel.setText(text_name_label)
        self.setWindowTitle(f"{text_name_label}")
        if os.stat(text_path_file).st_size == 0:
            self.create_new_file_from_path()
            self.save_file()
        with open(text_path_file, 'r') as openfile:
            json_obj = json.load(openfile)
        openfile.close()
        rods = json_obj['Rods']
        knots = json_obj['Knots']
        closures = json_obj['Sealing']

        self.ui.TableRodsDescription.clear()
        self.ui.TableRodsDescription.setRowCount(1)

        self.ui.TableRodsPowerDescription.clear()
        self.ui.TableRodsPowerDescription.setRowCount(1)

        self.ui.TableKontsPowerDescription.clear()
        self.ui.TableKontsPowerDescription.setRowCount(2)

        self.list_of_length = []
        self.list_of_width = []
        self.list_of_young_modulus = []
        self.list_of_sigma = []

        self.list_of_loads = []

        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)

        for num_rod in range(len(rods)):
            if num_rod == 0:
                pass
            else:
                self.ui.TableRodsDescription.insertRow(num_rod)
                self.ui.TableRodsPowerDescription.insertRow(num_rod)

            new_item_name_rod = QTableWidgetItem()
            new_item_name_rod.setText(f'Стержень {num_rod + 1}')
            new_item_name_rod.setFont(font1)
            self.ui.TableRodsDescription.setVerticalHeaderItem(num_rod, new_item_name_rod)

            new_item_length = QTableWidgetItem()
            new_item_length.setText('L, м')
            new_item_length.setFont(font1)
            self.ui.TableRodsDescription.setHorizontalHeaderItem(0, new_item_length)

            new_item_square = QTableWidgetItem()
            new_item_square.setText('A, м²')
            new_item_square.setFont(font1)
            self.ui.TableRodsDescription.setHorizontalHeaderItem(1, new_item_square)

            new_item_young_modulus = QTableWidgetItem()
            new_item_young_modulus.setText('E, Па')
            new_item_young_modulus.setFont(font1)
            self.ui.TableRodsDescription.setHorizontalHeaderItem(2, new_item_young_modulus)

            new_item_sigma = QTableWidgetItem()
            new_item_sigma.setText(u"[\u03c3], Па")
            new_item_sigma.setFont(font1)
            self.ui.TableRodsDescription.setHorizontalHeaderItem(3, new_item_sigma)

            length = rods[str(num_rod + 1)]['Length']
            length = float(length)
            new_item_rod_value_length = QTableWidgetItem()
            new_item_rod_value_length.setText(str(length))
            new_item_rod_value_length.setFont(font1)
            self.ui.TableRodsDescription.setItem(num_rod, 0, new_item_rod_value_length)

            width = rods[str(num_rod + 1)]['Width']
            width = float(width)
            new_item_rod_value_width = QTableWidgetItem()
            new_item_rod_value_width.setText(str(width))
            new_item_rod_value_width.setFont(font1)
            self.ui.TableRodsDescription.setItem(num_rod, 1, new_item_rod_value_width)

            young_modulus = rods[str(num_rod + 1)]['Young modulus']
            young_modulus = float(young_modulus)
            new_item_rod_value_young_modulus = QTableWidgetItem()
            new_item_rod_value_young_modulus.setText(str(young_modulus))
            new_item_rod_value_young_modulus.setFont(font1)
            self.ui.TableRodsDescription.setItem(num_rod, 2, new_item_rod_value_young_modulus)

            sigma = rods[str(num_rod + 1)]['Sigma']
            sigma = float(sigma)
            new_item_rod_value_sigma = QTableWidgetItem()
            new_item_rod_value_sigma.setText(str(sigma))
            new_item_rod_value_sigma.setFont(font1)
            self.ui.TableRodsDescription.setItem(num_rod, 3, new_item_rod_value_sigma)

            new_item_name_loads_rod = QTableWidgetItem()
            # Добавление нового заголовка "название стержня"
            new_item_name_loads_rod.setText(f'Стержень {num_rod + 1}')
            new_item_name_loads_rod.setFont(font1)
            self.ui.TableRodsPowerDescription.setVerticalHeaderItem(num_rod, new_item_name_loads_rod)

            new_item_load = QTableWidgetItem()
            new_item_load.setText('q')
            new_item_load.setFont(font1)
            self.ui.TableRodsPowerDescription.setHorizontalHeaderItem(0, new_item_load)

            load = rods[str(num_rod + 1)]['Load']
            load = float(load)
            new_item_load_value = QTableWidgetItem()
            new_item_load_value.setText(str(load))
            new_item_load_value.setFont(font1)
            self.ui.TableRodsPowerDescription.setItem(num_rod, 0, new_item_load_value)

            self.list_of_length.append(length)
            self.list_of_width.append(width)
            self.list_of_young_modulus.append(young_modulus)
            self.list_of_sigma.append(sigma)

            self.list_of_loads.append(load)

        self.powers.clear()

        new_item_power = QTableWidgetItem()
        new_item_power.setText('F, qL')
        new_item_power.setFont(font1)
        self.ui.TableKontsPowerDescription.setHorizontalHeaderItem(0, new_item_power)

        for num_knot in range(len(knots)):
            if num_knot == 0 or num_knot == 1:
                pass
            else:
                self.ui.TableKontsPowerDescription.insertRow(num_knot)

            power = knots[str(num_knot + 1)]
            power = float(power)

            new_item_name_knot = QTableWidgetItem()
            new_item_name_knot.setText(f'Узел {num_knot + 1}')
            new_item_name_knot.setFont(font1)
            self.ui.TableKontsPowerDescription.setVerticalHeaderItem(num_knot, new_item_name_knot)

            # добавление значения в таблицу сосредоточенных нагрузок (0 по умолчанию)
            new_item_knot_value = QTableWidgetItem()
            new_item_knot_value.setText(str(power))
            new_item_knot_value.setFont(font1)
            self.ui.TableKontsPowerDescription.setItem(num_knot, 0, new_item_knot_value)

            self.powers[str(num_knot + 1)] = 0

            self.powers[str(num_knot + 1)] = power

        self.left_sealing = closures['Left']

        self.ui.CheckBoxLeftSealing.setChecked(self.left_sealing)

        self.right_sealing = closures['Right']
        self.ui.CheckBoxRightSealing.setChecked(self.right_sealing)

        self.paint_picture()

    def edit_lists_description(self, row, column):
        try:
            if column == 0:
                input_length = float(self.ui.TableRodsDescription.item(row, 0).text())

                if input_length == 0:
                    error_type = 0
                    self.incorrect_value(error_type)
                    input_length = 1
                    self.ui.TableRodsDescription.item(row, 0).setText(str(input_length))

                if input_length < 0:
                    error_type = 1
                    self.incorrect_value(error_type)
                    input_length = abs(input_length)
                    self.ui.TableRodsDescription.item(row, 0).setText(str(input_length))

                self.list_of_length[row] = input_length

            if column == 1:
                input_width = float(self.ui.TableRodsDescription.item(row, 1).text())

                if input_width == 0:
                    error_type = 0
                    self.incorrect_value(error_type)
                    input_width = 1
                    self.ui.TableRodsDescription.item(row, 1).setText(str(input_width))

                if input_width < 0:
                    error_type = 1
                    self.incorrect_value(error_type)
                    input_width = abs(input_width)
                    self.ui.TableRodsDescription.item(row, 1).setText(str(input_width))

                self.list_of_width[row] = input_width

            if column == 2:
                input_young_modulus = float(self.ui.TableRodsDescription.item(row, 2).text())

                if input_young_modulus == 0:
                    error_type = 0
                    self.incorrect_value(error_type)
                    input_young_modulus = 1
                    self.ui.TableRodsDescription.item(row, 2).setText(str(input_young_modulus))

                if input_young_modulus < 0:
                    error_type = 1
                    self.incorrect_value(error_type)
                    input_young_modulus = abs(input_young_modulus)
                    self.ui.TableRodsDescription.item(row, 2).setText(str(input_young_modulus))

                self.list_of_young_modulus[row] = input_young_modulus

            if column == 3:
                input_sigma = float(self.ui.TableRodsDescription.item(row, 3).text())

                if input_sigma == 0:
                    error_type = 0
                    self.incorrect_value(error_type)
                    input_sigma = 1
                    self.ui.TableRodsDescription.item(row, 3).setText(str(input_sigma))

                if input_sigma < 0:
                    error_type = 1
                    self.incorrect_value(error_type)
                    input_sigma = abs(input_sigma)
                    self.ui.TableRodsDescription.item(row, 3).setText(str(input_sigma))

                self.list_of_sigma[row] = input_sigma

        except IndexError:
            pass
        except ValueError as e:
            if column == 0:
                input_length = 1
                self.ui.TableRodsDescription.item(row, 0).setText(str(input_length))
                self.list_of_length[row] = input_length

            if column == 1:
                input_width = 1
                self.ui.TableRodsDescription.item(row, 1).setText(str(input_width))
                self.list_of_width[row] = input_width

            if column == 2:
                input_young_modulus = 1
                self.ui.TableRodsDescription.item(row, 2).setText(str(input_young_modulus))
                self.list_of_young_modulus[row] = input_young_modulus

            if column == 3:
                input_sigma = 1
                self.ui.TableRodsDescription.item(row, 3).setText(str(input_sigma))
                self.list_of_sigma[row] = input_sigma

            self.value_error(e, 1)
        self.paint_picture()

    def edit_list_power_rods(self, row):
        try:
            self.list_of_loads[row] = float(self.ui.TableRodsPowerDescription.item(row, 0).text())
        except IndexError:
            pass
        except ValueError as e:
            input_load = 0
            self.ui.TableRodsPowerDescription.item(row, 0).setText(str(input_load))
            self.list_of_loads[row] = input_load
            self.value_error(e, 2)
        self.paint_picture()

    def edit_dict_power_knots(self, row):
        try:
            name_row = str(row + 1)
            input_power = float(self.ui.TableKontsPowerDescription.item(row, 0).text())
            self.powers[name_row] = input_power
        except (IndexError, KeyError):
            pass
        except ValueError as e:
            input_power = 0
            self.ui.TableKontsPowerDescription.item(row, 0).setText(str(input_power))
            self.powers[str(row + 1)] = input_power
            self.value_error(e, 3)
        self.paint_picture()

    def add_rows(self):
        # # # #  Таблица характеристик стержня  # # # #
        # Добавление новой строки
        count_rows = self.ui.TableRodsDescription.rowCount()
        self.ui.TableRodsDescription.insertRow(count_rows)
        # Добавление нового заголовка "название стержня"
        new_item_name_rod = QTableWidgetItem()
        new_item_name_rod.setText(f'Стержень {count_rows + 1}')
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)
        new_item_name_rod.setFont(font1)
        self.ui.TableRodsDescription.setVerticalHeaderItem(count_rows, new_item_name_rod)

        # Добавление нового значения длины в таблицу (1 по умолчанию)
        new_item_rod_value_length = QTableWidgetItem()
        new_item_rod_value_length.setText('1')
        new_item_rod_value_length.setFont(font1)
        self.ui.TableRodsDescription.setItem(count_rows, 0, new_item_rod_value_length)
        # добавление значения (по умолчанию 1) в массив длин для отрисовки и расчётов
        self.list_of_length.append(1)

        # Добавление нового значения ширины в таблицу (1 по умолчанию)
        new_item_rod_value_width = QTableWidgetItem()
        new_item_rod_value_width.setText('1')
        new_item_rod_value_width.setFont(font1)
        self.ui.TableRodsDescription.setItem(count_rows, 1, new_item_rod_value_width)
        # добавление значения (по умолчанию 1) в массив ширин для отрисовки и расчётов
        self.list_of_width.append(1)

        # Добавление нового значения E в таблицу (1 по умолчанию)
        new_item_rod_value_young_modulus = QTableWidgetItem()
        new_item_rod_value_young_modulus.setText('1')
        new_item_rod_value_young_modulus.setFont(font1)
        self.ui.TableRodsDescription.setItem(count_rows, 2, new_item_rod_value_young_modulus)
        # добавление значения (по умолчанию 1) в массив E для отрисовки и расчётов
        self.list_of_young_modulus.append(1)

        # Добавление нового значения сигма в таблицу (1 по умолчанию)
        new_item_rod_value_sigma = QTableWidgetItem()
        new_item_rod_value_sigma.setText('1')
        new_item_rod_value_sigma.setFont(font1)
        self.ui.TableRodsDescription.setItem(count_rows, 3, new_item_rod_value_sigma)
        # добавление значения (по умолчанию 0) в массив Sigma для отрисовки и расчётов
        self.list_of_sigma.append(1)

        # # # #  Таблица распределённых нагрузок стержня  # # # #
        # добавление новой строки
        self.ui.TableRodsPowerDescription.insertRow(count_rows)
        new_item_name_rod_2 = QTableWidgetItem()
        # Добавление нового заголовка "название стержня"
        new_item_name_rod_2.setText(f'Стержень {count_rows + 1}')
        new_item_name_rod_2.setFont(font1)
        self.ui.TableRodsPowerDescription.setVerticalHeaderItem(count_rows, new_item_name_rod_2)

        # добавление значения нагрузки в таблицу (0 по умолчанию)
        new_item_power_value = QTableWidgetItem()
        new_item_power_value.setText('0')
        new_item_power_value.setFont(font1)
        self.ui.TableRodsPowerDescription.setItem(count_rows, 0, new_item_power_value)
        # добавление значения (по умолчанию 0) в массив нагрузок для отрисовки и расчётов
        self.list_of_loads.append(0)

        # # # #  Таблица сосредоточенных нагрузок стержня  # # # #
        # добавление строки в таблицу сосредоточенных нагрузок
        count_rows_knots = self.ui.TableKontsPowerDescription.rowCount()
        self.ui.TableKontsPowerDescription.insertRow(count_rows_knots)
        # Добавление нового заголовка "название узла"
        new_item_knot_0 = QTableWidgetItem()
        new_item_knot_0.setText(f'Узел {count_rows_knots + 1}')
        new_item_knot_0.setFont(font1)
        self.ui.TableKontsPowerDescription.setVerticalHeaderItem(count_rows_knots, new_item_knot_0)

        # добавление значения в таблицу сосредоточенных нагрузок (0 по умолчанию)
        new_item_knot_value_0 = QTableWidgetItem()
        new_item_knot_value_0.setText('0')
        new_item_knot_value_0.setFont(font1)
        self.ui.TableKontsPowerDescription.setItem(count_rows_knots, 0, new_item_knot_value_0)
        # Добавление новых значений в словарь сил (по умолчанию 0)
        number_knot = str(count_rows_knots + 1)
        self.powers[number_knot] = 0

        self.paint_picture()

    def delete_rows(self):
        description_row_for_del = self.ui.TableRodsDescription.currentRow()
        if description_row_for_del > -1 and description_row_for_del != 0:
            self.ui.TableRodsDescription.removeRow(description_row_for_del)
            self.ui.TableRodsDescription.selectionModel().clearCurrentIndex()

            self.ui.TableRodsPowerDescription.removeRow(description_row_for_del)
            self.ui.TableRodsPowerDescription.selectionModel().clearCurrentIndex()

            self.ui.TableKontsPowerDescription.removeRow(description_row_for_del + 1)
            self.ui.TableKontsPowerDescription.selectionModel().clearCurrentIndex()

            font1 = QFont()
            font1.setFamilies([u"Montserrat"])
            font1.setPointSize(10)

            self.list_of_length = []
            self.list_of_width = []
            self.list_of_young_modulus = []
            self.list_of_sigma = []

            self.list_of_loads = []

            count_rows = self.ui.TableRodsDescription.rowCount()
            for row_description in range(count_rows):
                new_item_name_description_rod = QTableWidgetItem()
                new_item_name_description_rod.setText(f'Стержень {row_description + 1}')
                new_item_name_description_rod.setFont(font1)
                self.ui.TableRodsDescription.setVerticalHeaderItem(row_description, new_item_name_description_rod)

                length = float(self.ui.TableRodsDescription.item(row_description, 0).text())
                width = float(self.ui.TableRodsDescription.item(row_description, 1).text())
                young_modulus = float(self.ui.TableRodsDescription.item(row_description, 2).text())
                sigma = float(self.ui.TableRodsDescription.item(row_description, 3).text())

                loads = float(self.ui.TableRodsPowerDescription.item(row_description, 0).text())

                self.list_of_length.append(length)
                self.list_of_width.append(width)
                self.list_of_young_modulus.append(young_modulus)
                self.list_of_sigma.append(sigma)

                self.list_of_loads.append(loads)

                new_item_name_rod_power = QTableWidgetItem()
                new_item_name_rod_power.setText(f'Стержень {row_description + 1}')
                new_item_name_rod_power.setFont(font1)
                self.ui.TableRodsPowerDescription.setVerticalHeaderItem(row_description, new_item_name_rod_power)

            count_knots = self.ui.TableKontsPowerDescription.rowCount()

            self.powers.clear()

            for row_knot in range(count_knots):
                new_item_nane_knot = QTableWidgetItem()
                new_item_nane_knot.setText(f'Узел {row_knot + 1}')
                new_item_nane_knot.setFont(font1)
                self.ui.TableKontsPowerDescription.setVerticalHeaderItem(row_knot, new_item_nane_knot)

                number_knot = str(row_knot + 1)
                self.powers[number_knot] = 0

                knot_power = float(self.ui.TableKontsPowerDescription.item(row_knot, 0).text())
                self.powers[number_knot] = knot_power

            print(self.list_of_length)
            print(self.list_of_width)
            print(self.list_of_young_modulus)
            print(self.list_of_loads)
            print(self.powers)

            self.paint_picture()

    def left_right_sealing(self):

        if self.ui.CheckBoxLeftSealing.isChecked():
            self.left_sealing = True
        else:
            self.left_sealing = False

        if self.ui.CheckBoxRightSealing.isChecked():
            self.right_sealing = True
        else:
            self.right_sealing = False
        self.paint_picture()

    def calculation(self):
        discharge = {}
        discharge_rods = {}
        discharge_sealing = {}

        for number in range(len(self.list_of_length)):
            length = abs(float(self.list_of_length[number]))
            width = abs(float(self.list_of_width[number]))
            young_modulus = abs(float(self.list_of_young_modulus[number]))
            sigma = abs(float(self.list_of_sigma[number]))

            load = float(self.list_of_loads[number])

            discharge_rods[f'{number + 1}'] = {'Length': length, 'Width': width, 'Young modulus': young_modulus,
                                               'Sigma': sigma, 'Load': load}

            discharge_sealing = {'Left': self.left_sealing, 'Right': self.right_sealing}

        discharge['Rods'] = discharge_rods
        discharge['Knots'] = self.powers
        discharge['Sealing'] = discharge_sealing

        return discharge

    def paint_picture(self):

        self.widget_width = self.ui.GraphWidget.width()
        self.widget_height = self.ui.GraphWidget.height()

        list_of_length = self.list_of_length.copy()
        list_of_width = self.list_of_width.copy()
        list_of_loads = self.list_of_loads.copy()
        list_of_young_modulus = self.list_of_young_modulus.copy()
        powers = self.powers.copy()
        img = draw_picture(list_of_length, list_of_width, list_of_loads, list_of_young_modulus, powers,
                           self.left_sealing, self.right_sealing,
                           '#fff0ee', self.widget_width, self.widget_height, self.visible)
        img.save('src/resources/pictures/image.png')
        self.ui.GraphWidget.setStyleSheet(u"image:url(src/resources/pictures/image.png) 0 0 0 0 stretch")
        return img

    def calc_btn_clicked(self):
        if self.left_sealing is False and self.right_sealing is False:
            self.sealing_error()
        else:
            try:
                self.save_file()
                if self.file_name[0]:
                    self.ui.TabWidget.setCurrentIndex(1)
                    self.ui.LineEditPath_2.setText(self.file_name[0])
                    self.change_in_line_path_2()
            except Exception as e:
                print(e)

    def visible_graph_labels(self):
        if self.visible:
            icon_visible_labels = QIcon()
            icon_visible_labels.addFile(u":/icon/icons/visibility.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.BtnVisibleLabels.setIcon(icon_visible_labels)
            self.visible = False
        else:
            icon_visible_labels = QIcon()
            icon_visible_labels.addFile(u":/icon/icons/visibility_off.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.BtnVisibleLabels.setIcon(icon_visible_labels)
            self.visible = True
        self.paint_picture()

    def fullscreen_image(self):
        image = self.paint_picture()
        image.show()

    # =======================================================================================
    # TAB_2
    def file_path_choose_2(self):
        text_dir_data = 'src/resources/data'
        if self.file_name is None:
            self.file_name = QFileDialog.getOpenFileName(self, 'Открытие файла', text_dir_data,
                                                         "Json Files (*.json);;Все файлы (*)")
        else:
            if self.file_name[0] != "":
                text_dir = re.sub(r'\w*\.\S*', '', self.file_name[0])
                self.file_name = QFileDialog.getOpenFileName(self, 'Открытие файла', text_dir,
                                                             "Json Files (*.json);;Все файлы (*)")

            else:
                self.file_name = QFileDialog.getOpenFileName(self, 'Открытие файла', text_dir_data,
                                                             "Json Files (*.json);;Все файлы (*)")
        if self.file_name[0] != "":
            self.ui.LineEditPath_2.setText(self.file_name[0])
            try:
                self.change_in_line_path_2()
            except Exception as e:
                self.warning_file_error(e)
        else:
            self.file_name = None

    def change_in_line_path_2(self):
        text_path_file = self.ui.LineEditPath_2.text()
        text_name_label = 'САПР — ' + re.sub(r'\S*/', '', text_path_file)
        self.ui.NameLabel.setText(text_name_label)
        self.setWindowTitle(f"{text_name_label}")
        if os.stat(text_path_file).st_size == 0:
            print('empty')
        with open(text_path_file, 'r') as openfile:
            json_obj = json.load(openfile)
        openfile.close()
        rods = json_obj['Rods']
        knots = json_obj['Knots']
        closures = json_obj['Sealing']
        rods_text = ''
        knots_text = '\n'

        self.list_of_length_preproc = []
        self.list_of_width_preproc = []
        self.list_of_young_modulus_preproc = []
        self.list_of_sigma_preproc = []
        self.list_of_loads_preproc = []

        for num_rod in range(len(rods)):
            length = rods[str(num_rod + 1)]['Length']
            self.list_of_length_preproc.append(length)
            width = rods[str(num_rod + 1)]['Width']
            self.list_of_width_preproc.append(width)
            young_modulus = rods[str(num_rod + 1)]['Young modulus']
            self.list_of_young_modulus_preproc.append(young_modulus)
            sigma = rods[str(num_rod + 1)]['Sigma']
            self.list_of_sigma_preproc.append(sigma)
            load = rods[str(num_rod + 1)]['Load']
            self.list_of_loads_preproc.append(load)
            rods_text = rods_text + f'Стержень {num_rod + 1}:\n' \
                                    f'    L = {length},\n' \
                                    f'    A = {width},\n' \
                                    f'    E = {young_modulus},\n' \
                                    f'    [σ] = {sigma},\n' \
                                    f'    q = {load}\n'

        self.powers_preproc.clear()
        for num_knot in range(len(knots)):
            power = knots[str(num_knot + 1)]

            self.powers_preproc[str(num_knot + 1)] = 0

            self.powers_preproc[str(num_knot + 1)] = power

            knots_text = knots_text + f'Узел {num_knot + 1}: F = {power}\n'
        closures_text = ''
        if closures['Left'] and closures['Right']:
            closures_text = '\nЗаделка: слева и справа'
            self.left_sealing_2 = True
            self.right_sealing_2 = True

        if closures['Left'] and not closures['Right']:
            closures_text = '\nЗаделка: слева'
            self.left_sealing_2 = True
            self.right_sealing_2 = False

        if not closures['Left'] and closures['Right']:
            closures_text = '\nЗаделка: справа'
            self.left_sealing_2 = False
            self.right_sealing_2 = True

        info_text = rods_text + knots_text + closures_text
        self.ui.textEditInfo.setText(info_text)

        self.ui.LineEditPath.setText(text_path_file)
        self.change_in_line_path()

    def print_table_result(self):
        self.ui.LineEditPoint.hide()
        self.ui.LineEditNumRod.hide()

        self.ui.GraphWidget_2.hide()
        self.ui.WelcomeLabel.hide()

        self.ui.TableAnswer.show()

        self.ui.TableAnswer.setRowCount(0)

        width_table_answer = self.ui.TableAnswer.width()
        size_column = width_table_answer / 4
        self.ui.TableAnswer.horizontalHeader().resizeSection(0, size_column)
        self.ui.TableAnswer.horizontalHeader().resizeSection(1, size_column)
        self.ui.TableAnswer.horizontalHeader().resizeSection(2, size_column)

        nx_values = nx_equation(self.list_of_length_preproc, self.list_of_width_preproc, self.list_of_loads_preproc,
                                self.list_of_young_modulus_preproc, self.powers_preproc, self.left_sealing_2,
                                self.right_sealing_2, None, -1)
        ux_values = ux_equation(self.list_of_length_preproc, self.list_of_width_preproc, self.list_of_loads_preproc,
                                self.list_of_young_modulus_preproc, self.powers_preproc, self.left_sealing_2,
                                self.right_sealing_2, None, -1)
        sgx_values = sgx_equation(self.list_of_length_preproc, self.list_of_width_preproc, self.list_of_loads_preproc,
                                  self.list_of_young_modulus_preproc, self.powers_preproc, self.left_sealing_2,
                                  self.right_sealing_2, None, -1)

        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(10)

        for num_rod in range(len(nx_values)):
            self.ui.TableAnswer.insertRow(num_rod)
            new_item_name_rod = QTableWidgetItem()
            new_item_name_rod.setText(f'Стержень {num_rod + 1}')
            new_item_name_rod.setFont(font1)
            self.ui.TableAnswer.setVerticalHeaderItem(num_rod, new_item_name_rod)

            nx_value = nx_values[num_rod]
            nx_text = f'Nₓ[0] = {nx_value[0]};     Nₓ[{self.list_of_length_preproc[num_rod]}] = {nx_value[1]}'
            new_item_nx_value = QTableWidgetItem()
            new_item_nx_value.setTextAlignment(Qt.AlignCenter)
            new_item_nx_value.setText(str(nx_text))
            new_item_nx_value.setFont(font1)
            self.ui.TableAnswer.setItem(num_rod, 0, new_item_nx_value)

            ux_value = ux_values[num_rod]
            ux_text = f'Uₓ[0] = {ux_value[0]};     Uₓ[{self.list_of_length_preproc[num_rod]}] = {ux_value[1]}'
            new_item_ux_value = QTableWidgetItem()
            new_item_ux_value.setTextAlignment(Qt.AlignCenter)
            new_item_ux_value.setText(str(ux_text))
            new_item_ux_value.setFont(font1)
            self.ui.TableAnswer.setItem(num_rod, 1, new_item_ux_value)

            sgx_value = sgx_values[num_rod]
            sgx_text = f'[\u03c3]ₓ[0] = {sgx_value[0]};     [\u03c3]ₓ[{self.list_of_length_preproc[num_rod]}] = {sgx_value[1]}'
            new_item_sgx_value = QTableWidgetItem()
            new_item_sgx_value.setTextAlignment(Qt.AlignCenter)
            new_item_sgx_value.setText(str(sgx_text))
            new_item_sgx_value.setFont(font1)
            self.ui.TableAnswer.setItem(num_rod, 2, new_item_sgx_value)

    def show_line_edit(self):
        self.print_table_result()
        self.ui.LineEditPoint.show()
        self.ui.LineEditNumRod.show()
        self.ui.GraphWidget_2.hide()
        self.ui.WelcomeLabel.hide()

        self.ui.TableAnswer.show()

        if self.num_rod != '' and self.value_x != '':
            self.calc_result_in_point()

    def calc_result_in_point(self):
        self.num_rod = self.ui.LineEditNumRod.text()
        self.value_x = self.ui.LineEditPoint.text()
        try:
            if self.num_rod != '' and self.value_x != '':
                num_rod = int(self.num_rod)
                value_x = float(self.value_x)
                if num_rod <= 0:
                    error_type = 2
                    self.incorrect_value(error_type)
                    num_rod = 1
                    self.ui.LineEditNumRod.setText(str(num_rod))
                if value_x < 0 or value_x > self.list_of_length_preproc[num_rod - 1]:
                    self.value_x_error()
                    value_x = 0
                    self.ui.LineEditPoint.setText(str(value_x))
                    return 0
                nx_value = nx_equation(self.list_of_length_preproc, self.list_of_width_preproc,
                                       self.list_of_loads_preproc,
                                       self.list_of_young_modulus_preproc, self.powers_preproc,
                                       self.left_sealing_2,
                                       self.right_sealing_2, num_rod, value_x)
                ux_value = ux_equation(self.list_of_length_preproc, self.list_of_width_preproc,
                                       self.list_of_loads_preproc,
                                       self.list_of_young_modulus_preproc, self.powers_preproc,
                                       self.left_sealing_2,
                                       self.right_sealing_2, num_rod, value_x)
                sgx_value = sgx_equation(self.list_of_length_preproc, self.list_of_width_preproc,
                                         self.list_of_loads_preproc,
                                         self.list_of_young_modulus_preproc, self.powers_preproc,
                                         self.left_sealing_2,
                                         self.right_sealing_2, num_rod, value_x)
                self.ui.TableAnswer.setRowCount(1)
                font1 = QFont()
                font1.setFamilies([u"Montserrat"])
                font1.setPointSize(10)

                new_item_name_rod = QTableWidgetItem()
                new_item_name_rod.setText(f'Стержень {num_rod}')
                new_item_name_rod.setFont(font1)
                self.ui.TableAnswer.setVerticalHeaderItem(0, new_item_name_rod)

                new_item_nx_value = QTableWidgetItem()
                new_item_nx_value.setTextAlignment(Qt.AlignCenter)
                new_item_nx_value.setText(str(nx_value))
                new_item_nx_value.setFont(font1)
                self.ui.TableAnswer.setItem(0, 0, new_item_nx_value)

                new_item_ux_value = QTableWidgetItem()
                new_item_ux_value.setTextAlignment(Qt.AlignCenter)
                new_item_ux_value.setText(str(ux_value))
                new_item_ux_value.setFont(font1)
                self.ui.TableAnswer.setItem(0, 1, new_item_ux_value)

                new_item_sgx_value = QTableWidgetItem()
                new_item_sgx_value.setTextAlignment(Qt.AlignCenter)
                new_item_sgx_value.setText(str(sgx_value))
                new_item_sgx_value.setFont(font1)
                self.ui.TableAnswer.setItem(0, 2, new_item_sgx_value)
        except ValueError:
            pass
        except IndexError:
            error_type = 3
            self.incorrect_value(error_type)
            num_rod = 1
            self.ui.LineEditNumRod.setText(str(num_rod))

    def show_epure(self):
        self.ui.WelcomeLabel.show()
        self.ui.WelcomeLabel.setText('Загрузка...')
        self.ui.TableAnswer.hide()
        self.ui.LineEditPoint.hide()
        self.ui.LineEditNumRod.hide()

        self.paint_picture_2()

        self.ui.GraphWidget_2.show()
        self.ui.WelcomeLabel.hide()

        self.ui.GraphWidget_2.setStyleSheet(u"image:url(src/resources/pictures/image_epure.png) 0 0 0 0 stretch")

    def paint_picture_2(self):
        self.widget_width_2 = self.ui.GraphWidget_2.width()
        self.widget_height_2 = self.ui.GraphWidget_2.height()
        list_of_length = self.list_of_length_preproc.copy()
        list_of_width = self.list_of_width_preproc.copy()
        list_of_loads = self.list_of_loads_preproc.copy()
        list_of_young_modulus = self.list_of_young_modulus_preproc.copy()
        powers = self.powers_preproc.copy()
        img_epure = draw_epure(list_of_length, list_of_width, list_of_young_modulus, list_of_loads, powers,
                               self.left_sealing_2, self.right_sealing_2,
                               '#fff0ee', self.widget_width_2, self.widget_height_2, self.visible_2)
        img_epure.save('src/resources/pictures/image_epure.png')
        return img_epure

    def visible_graph_labels_2(self):
        if self.visible_2:
            icon_visible_labels_2 = QIcon()
            icon_visible_labels_2.addFile(u":/icon/icons/visibility.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.BtnVisibleLabels_2.setIcon(icon_visible_labels_2)
            self.visible_2 = False
        else:
            icon_visible_labels_2 = QIcon()
            icon_visible_labels_2.addFile(u":/icon/icons/visibility_off.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.BtnVisibleLabels_2.setIcon(icon_visible_labels_2)
            self.visible_2 = True
        self.paint_picture()

    def fullscreen_image_2(self):
        image = self.paint_picture_2()
        image.show()


def set_move_window(widget):
    """
    Allows you to move the window by grabbing not only the title, but also an arbitrary widget.
    :param widget: The widget, grabbing for which the movement will be performed
    :return: widget – The widget, grabbing for which the movement will be performed
    """
    win = widget.window()
    cursor_shape = widget.cursor().shape()
    move_source = getattr(widget, "mouseMoveEvent")
    press_source = getattr(widget, "mousePressEvent")
    release_source = getattr(widget, "mouseReleaseEvent")

    def move(event):
        if move.b_move:
            x = event.globalX() + move.x_korr - move.lastPoint.x()
            y = event.globalY() + move.y_korr - move.lastPoint.y()
            win.move(x, y)
            widget.setCursor(QtCore.Qt.SizeAllCursor)
        return move_source(event)

    def press(event):
        if event.button() == QtCore.Qt.LeftButton:
            # Коррекция геометрии окна: учитываем размеры рамки и заголовка
            x_korr = win.frameGeometry().x() - win.geometry().x()
            y_korr = win.frameGeometry().y() - win.geometry().y()
            # Коррекция геометрии виджета: учитываем смещение относительно окна
            parent = widget
            while not parent == win:
                x_korr -= parent.x()
                y_korr -= parent.y()
                parent = parent.parent()
            move.__dict__.update({"lastPoint": event.pos(), "b_move": True, "x_korr": x_korr, "y_korr": y_korr})
        else:
            move.__dict__.update({"b_move": False})
            widget.setCursor(cursor_shape)
        return press_source(event)

    def release(event):
        move.__dict__.update({"b_move": False})
        widget.setCursor(cursor_shape)
        return release_source(event)

    setattr(widget, "mouseMoveEvent", move)
    setattr(widget, "mousePressEvent", press)
    setattr(widget, "mouseReleaseEvent", release)
    move.__dict__.update({"b_move": False})
    return widget


def create_required_folders():
    """
    Function for create necessary folders
    """
    if os.path.exists('src'):
        pass
    else:
        os.mkdir('src')

    if os.path.exists('src/resources'):
        pass
    else:
        os.mkdir('src/resources')

    if os.path.exists('src/resources/data'):
        pass
    else:
        os.mkdir('src/resources/data')

    if os.path.exists('src/resources/pictures'):
        pass
    else:
        os.mkdir('src/resources/pictures')


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    create_required_folders()

    app = QApplication(sys.argv)
    window = MainWindow()
    set_move_window(window.ui.NameLabel)
    window.show()
    sys.exit(app.exec())

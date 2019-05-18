from registerUI import Ui_Dialog
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from Cregister import register
from CsendQQ import SendQQ
import traceback
import base64


class My_registerWindow(Ui_Dialog, QDialog):
    def __init__(self, o_register):
        super(My_registerWindow, self).__init__()
        self.setupUi(self)
        self.o_register = o_register
        self.init()

    def init(self):
        try:
            self.lineEdit_register.setEnabled(False)  # 注册码输入框
            self.label_serial.setEnabled(False)  # 序列号文本
            self.pushButtoncopy.setEnabled(False)  # 复制到剪贴板按钮
            self.pushButton_registe.setEnabled(False)  # 注册按钮

            str_tips = '欢迎来到德莱联盟\r\n'
            if self.o_register.final_serial_list.__len__() != 6:
                self.label.setText('error')
            else:
                self.had_registed = self.o_register.final_serial_list[0]  # 1已注册；0未注册 字符串
                self.serial_number = self.o_register.final_serial_list[1]  # 主板序列号 字符串
                self.try_date = self.o_register.final_serial_list[2]  # 试用日期%Y-%m-%d 字符串
                self.try_dates = self.o_register.final_serial_list[3]  # 试用有效期 天数 字符串
                self.registe_date = self.o_register.final_serial_list[4]  # 注册日期%Y-%m-%d 字符串
                self.registe_dates = self.o_register.final_serial_list[5]  # 注册有效期 天数 字符串
                # -2 - 4 - 5 - 6
                # 过期
                # 序列号不匹配
                # 已注册，未生效，试用期已到
                # 试用日期 | 试用有效期有个为0
                register_re = self.o_register.re
                if self.had_registed == '0':
                    if register_re == 0:
                        str_tips += '您还未注册,正在试用,试用开始日期：' + self.try_date + '，\r\n'
                        str_tips += '可试用总天数：' + self.try_dates + '，\r\n'
                        str_tips += '可将您的序列号发送给作者获取注册码，\r\n' \
                                    '填写在下方注册码输入框中，点击注册即可。\r\n'
                    elif register_re == -2:
                        str_tips += '试用期已过，您还未注册，\r\n' \
                                    '请点击下方的\'复制到剪贴板\'按钮，\r\n' \
                                    '将您的序列号发送给作者获取注册码，\r\n' \
                                    '填写在下方注册码输入框中，点击注册即可。\r\n'
                    elif register_re == -4:
                        str_tips += '您还未注册，系统检测到序列号与之前不一致，\r\n' \
                                    '请联系作者。\r\n'
                    else:
                        str_tips += '发生未知错误[' + str(register_re) + '],请联系作者。\r\n'

                    if register_re == 0 or register_re == -2:
                        self.label_serial.setText(self.serial_number)
                        self.lineEdit_register.setEnabled(True)  # 注册码输入框
                        self.label_serial.setEnabled(True)  # 序列号文本
                        self.pushButtoncopy.setEnabled(True)  # 复制到剪贴板按钮
                        self.pushButton_registe.setEnabled(True)  # 注册按钮
                else:
                    if register_re == 0:
                        str_tips += '您已注册,正常使用,注册日期：' + self.registe_date + '\r\n'
                        str_tips += '可使用总天数：' + self.registe_dates + '，感谢您的支持。\r\n'
                    elif register_re == -2:
                        str_tips += '有效期已过，您还未注册，\r\n' \
                                    '请点击下方的\'复制到剪贴板\'按钮，\r\n' \
                                    '将您的序列号发送给作者获取注册码，\r\n' \
                                    '填写在下方注册码输入框中，点击注册即可。\r\n'
                    elif register_re == -4:
                        str_tips += '您已注册，系统检测到序列号与之前不一致，\r\n' \
                                    '暂无法使用，请联系作者。\r\n'
                    elif register_re == -5:
                        str_tips += '您已注册，未到生效日期，试用期已到，暂无法使用。\r\n'
                    else:
                        str_tips += '发生未知错误[' + str(register_re) + '],请联系作者。\r\n'
                    if register_re == -2:
                        self.label_serial.setText(self.serial_number)
                        self.lineEdit_register.setEnabled(True)  # 注册码输入框
                        self.label_serial.setEnabled(True)  # 序列号文本
                        self.pushButtoncopy.setEnabled(True)  # 复制到剪贴板按钮
                        self.pushButton_registe.setEnabled(True)  # 注册按钮
                self.label.setText(str_tips)
        except Exception as e:
            str_log = "Exception:" + traceback.format_exc() + "\r\n"
            print(str_log)
            QMessageBox.information(self, "异常", '注册程序，请截图联系作者' + str_log, QMessageBox.Yes)

    def registe(self):
        try:
            register_number = self.lineEdit_register.text()
            try:
                base64.b64decode(register_number)
            except Exception as e:
                QMessageBox.information(self, "警告", '注册码格式不正确，请检查！', QMessageBox.Yes)
                return 0
            re = self.o_register.register_button(register_number)
            print('registe' + register_number)
            # 0成功；-1不存在文件;-4序列号不匹配;
            text = ''
            if re == 0:
                text = '恭喜！注册成功！\r\n'
            elif re == -1:
                text = '注册失败，不存在注册文件，请联系作者'
            else:
                text = '注册失败，序列号不匹配，请联系作者'
            QMessageBox.information(self, "提示", text, QMessageBox.Yes)
            if re == 0:
                QDialog.accept(self)

        except Exception as e:
            str_log = "Exception:" + traceback.format_exc() + "\r\n"
            print(str_log)
            QMessageBox.information(self, "异常", '注册程序，请截图联系作者' + str_log, QMessageBox.Yes)
        return 0

    def cptoClipboard(self):
        SendQQ.set_text(self.serial_number)
        text = '已复制' + self.serial_number + '到剪贴板，在qq粘贴即可。'
        QMessageBox.information(self, "提示", text, QMessageBox.Yes)
        return 0


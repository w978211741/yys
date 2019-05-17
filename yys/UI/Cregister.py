from des import MyDESCrypt
import time
import sys
import wmi
import datetime
import os


class register():
    def __init__(self):
        self.key = '*$h@D$f8'
        self.final_serial_list = []
        self.re = 0

    def encode_str(self, str_str):
        des = MyDESCrypt(self.key)
        enboard_id = des.encrypt(str_str)

        if isinstance(enboard_id, bytes):
            enboard_id = enboard_id.decode()
        return enboard_id

    def decode_str(self, str_str):
        des = MyDESCrypt(self.key)
        dec_board_id = des.decrypt(str_str)

        if isinstance(dec_board_id, bytes):
            dec_board_id = dec_board_id.decode()
        return dec_board_id

    def get_serial_number(self):
        c = wmi.WMI()
        board_id = c.Win32_PhysicalMedia()[0].SerialNumber.lstrip().rstrip()
        return board_id

    # 是否已注册（1已注册）|主板序列号|试用日期|试用有效期|注册日期|注册有效期 初始值：0|0|0|0
    # 1|hhhhh|2019-05-11|1|2019-05-11|1
    # 0|0|0|1|0|0
    # 如果未注册，且主板序列号为0，设置试用日期为当天

    # return int :0成功；-1不存在文件；-2过期；-3未注册;-4序列号不匹配;-5已注册，未生效；
    # 如果-3未注册，-5已注册，未生效；进入试用判断
    def jian_cha(self):
        file_name = 'serial'
        re = os.path.isfile(file_name)
        iret = 0
        if re is True:
            fp = open(file_name, 'rb')
            str_read = fp.read().decode()
            fp.close()
            # print(str_read)
            # des解码
            str_read = self.decode_str(str_read)
            serial_list = str_read.split('|')
            # print(serial_list)
            if serial_list.__len__() != 6:
                iret = -1
            elif serial_list[0] == '1':
                serial_no = serial_list[1]
                number = self.get_serial_number()
                if serial_no != number:
                    iret = -4
                else:
                    # 注册日期|注册有效期
                    serial_time = serial_list[4]
                    can_use_time = int(serial_list[5])
                    now = datetime.datetime.now()
                    time_now = now.strftime('%Y-%m-%d')

                    d1 = datetime.datetime.strptime(time_now, '%Y-%m-%d')
                    d2 = datetime.datetime.strptime(serial_time, '%Y-%m-%d')
                    delta = d1 - d2
                    days = delta.days
                    # print(days)
                    # print(can_use_time)
                    if days < 0:
                        iret = -5
                    elif days >= can_use_time:
                        iret = -2
            else:
                iret = -3
        else:
            iret = -1
        return iret

    # return int :0成功；-1不存在文件；-2过期；-3未注册;-4序列号不匹配;-5已注册，未生效；-6试用日期|试用有效期有个为0
    # 试用判断 传入参数 int ifrom 和序列列表serial_list，如果是-3未注册，试用期已过提示试用期已过。返回值-2
    # 如果是-5已注册，未生效，试用期已过提示试用期已过，有效期未到，未生效。返回值-5
    def probater(self, ifrom):
        iret = 0
        file_name = 'serial'
        re = os.path.isfile(file_name)
        iret = 0
        if re is True:
            fp = open(file_name, 'rb')
            str_read = fp.read().decode()
            fp.close()
            # des解码
            str_read = self.decode_str(str_read)
            serial_list = str_read.split('|')
            # print(serial_list)
            if serial_list.__len__() != 6:
                iret = -1
            if serial_list[1] == '0':
                # 设置序列号
                serial_number = self.get_serial_number()
                serial_list[1] = serial_number
                # 设置试用日期
                now = datetime.datetime.now()
                time_now = now.strftime('%Y-%m-%d')
                serial_list[2] = time_now
                # 写注册文件 结束
                self.write_file(serial_list)
                iret = 0
            else:
                serial_no = serial_list[1]
                number = self.get_serial_number()
                # print(number)
                if serial_no != number:
                    iret = -4
                else:
                    # 试用日期|试用有效期
                    serial_time = serial_list[2]
                    can_use_time = int(serial_list[3])
                    if serial_time == '0' or can_use_time == '0':
                        iret = -6
                    else:
                        now = datetime.datetime.now()
                        time_now = now.strftime('%Y-%m-%d')

                        d1 = datetime.datetime.strptime(time_now, '%Y-%m-%d')
                        d2 = datetime.datetime.strptime(serial_time, '%Y-%m-%d')
                        delta = d1 - d2
                        days = delta.days
                        # print(days)
                        # print(can_use_time)
                        if days >= can_use_time:
                            if ifrom == -3:
                                iret = -2
                            elif ifrom == -5:
                                iret = -5
                        else:
                            iret = 0
            self.final_serial_list = serial_list
        else:
            iret = -1
        return iret

    # return int :0成功；-1不存在文件;-4序列号不匹配;
    # register
    def register_button(self, register_number):
        # print('register_number' + register_number)
        file_name = 'serial'
        re = os.path.isfile(file_name)
        iret = 0
        if re is True:
            fp = open(file_name, 'rb')
            str_read = fp.read().decode()
            # print("str_read:" + str_read)
            fp.close()
            # des 解密
            str_read = self.decode_str(str_read)
            serial_list = str_read.split('|')
            # des 解密
            str_register = self.decode_str(register_number)
            register_list = str_register.split('|')

            if serial_list.__len__() != 6 or register_list.__len__() != 6:
                iret = -1
            else:
                # 校验序列号
                serial_number = self.get_serial_number()
                if serial_number != register_list[1] or serial_number != serial_list[1]:
                    iret = -4
                else:
                    # 设置注册时间和注册有效期
                    serial_list[4] = register_list[4]
                    serial_list[5] = register_list[5]

                    # 设置是否注册
                    serial_list[0] = register_list[0]
                    # 写注册文件 结束
                    self.write_file(serial_list)
                    iret = 0
        else:
            iret = -1
        return iret

    def write_file(self, serial_list):
        file_name = 'serial'
        fp = open(file_name, 'w')
        str_jian = '|'
        str_write = str_jian.join(serial_list)
        print(str_write)
        # des加密
        str_write = self.encode_str(str_write)
        fp.writelines(str_write)
        fp.close()

    def set_register_number(self, serial_number, date='', dates='30'):
        register_list = ['1', serial_number, '0', '0', '0', '0']
        if date == '':
            now = datetime.datetime.now()
            time_now = now.strftime('%Y-%m-%d')
            register_list[4] = time_now
            register_list[5] = dates
        else:
            register_list[4] = date
            register_list[5] = dates
        str_jian = '|'
        register_number = str_jian.join(register_list)
        # des加密
        register_number = self.encode_str(register_number)
        return register_number

    def check(self):
        re = self.jian_cha()
        if re == -3 or re == -5:
            re = self.probater(re)
        self.re = re
        return re
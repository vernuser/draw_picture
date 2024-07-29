# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import nice
import allyest
import pymysql
from main_2 import *
import global_phone
db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='1024',
            database='体育馆管理',
            charset='utf8mb4',
            # cursorclass=pymysql.cursors.DictCursor
        )




class pages_window(nice.Ui_yuyueMainWindow, QMainWindow):
    def __init__(self):
        super(pages_window, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # 设置信号与槽
        # 点击左侧按钮页面切换到第一个页面
        self.pushButton_6.clicked.connect(self.display_page1)
        self.pushButton_7.clicked.connect(self.display_page2)
        self.pushButton_8.clicked.connect(self.display_page3)
        self.pushButton_9.clicked.connect(self.display_page4)
        self.pushButton_18.clicked.connect(self.display_page5)
        self.pushButton_19.clicked.connect(self.display_page6)
        self.pushButton_20.clicked.connect(self.display_page1)
        # 九键跳转
        self.pushButton_10.clicked.connect(self.display_page4)
        self.pushButton_11.clicked.connect(self.display_page4)
        self.pushButton_12.clicked.connect(self.display_page4)
        self.pushButton_13.clicked.connect(self.display_page4)
        self.pushButton_14.clicked.connect(self.display_page4)
        self.pushButton_15.clicked.connect(self.display_page4)
        self.pushButton_16.clicked.connect(self.display_page4)
        self.pushButton_17.clicked.connect(self.display_page4)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        # 地址
        self.pushButton_9.clicked.connect(lambda: self.openPageWithText())
        self.pushButton_10.clicked.connect(lambda: self.openPageWithText1())
        self.pushButton_11.clicked.connect(lambda: self.openPageWithText2())
        self.pushButton_12.clicked.connect(lambda: self.openPageWithText3())
        self.pushButton_13.clicked.connect(lambda: self.openPageWithText4())
        self.pushButton_14.clicked.connect(lambda: self.openPageWithText5())
        self.pushButton_15.clicked.connect(lambda: self.openPageWithText6())
        self.pushButton_16.clicked.connect(lambda: self.openPageWithText7())
        self.pushButton_17.clicked.connect(lambda: self.openPageWithText8())
        #
        self.pushButton_21.clicked.connect(lambda: self.openwindow1())
        self.pushButton_22.clicked.connect(self.subscribe)

        self.textEdit.setReadOnly(True)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_3.setReadOnly(True)


        self.pushButton_18.clicked.connect(lambda: self.Find())
        self.pushButton_19.clicked.connect(lambda: self.Insert())

    def subscribe(self):
        self.tool_window = Tool_Window()
        self.tool_window.show()
        self.close()


    def showDate1(self):
        self.dateEdit.clear()
        current_date = QDate.currentDate()
        self.dateEdit.setDate(current_date)

    def display_page1(self):
        self.stackedWidget.setCurrentIndex(0)

    def display_page2(self):
        self.stackedWidget.setCurrentIndex(1)

    def display_page3(self):
        self.stackedWidget.setCurrentIndex(2)

    def display_page4(self):
        self.stackedWidget.setCurrentIndex(3)

    def display_page5(self):
        self.stackedWidget_2.setCurrentIndex(0)

    def display_page6(self):
        self.stackedWidget_2.setCurrentIndex(1)

    def openPageWithText(self):
        self.textEdit.clear()
        button = self.pushButton_9.text()
        self.textEdit.append(f'{button}预定:1')

    def openPageWithText1(self):
        self.textEdit.clear()
        button = self.pushButton_10.text()
        self.textEdit.append(f'{button}预定:2')

    def openPageWithText2(self):
        self.textEdit.clear()
        button = self.pushButton_11.text()
        self.textEdit.append(f'{button}预定:3')

    def openPageWithText3(self):
        self.textEdit.clear()
        button = self.pushButton_12.text()
        self.textEdit.append(f'{button}预定:4')

    def openPageWithText4(self):
        self.textEdit.clear()
        button = self.pushButton_13.text()
        self.textEdit.append(f'{button}预定:5')

    def openPageWithText5(self):
        self.textEdit.clear()
        button = self.pushButton_14.text()
        self.textEdit.append(f'{button}预定:6')

    def openPageWithText6(self):
        self.textEdit.clear()
        button = self.pushButton_15.text()
        self.textEdit.append(f'{button}预定:7')

    def openPageWithText7(self):
        self.textEdit.clear()
        button = self.pushButton_16.text()
        self.textEdit.append(f'{button}预定:8')

    def openPageWithText8(self):
        self.textEdit.clear()
        button = self.pushButton_17.text()
        self.textEdit.append(f'{button}预定:9')

    def openwindow1(self):
        self.allwindow = allDialog()
        self.allwindow.exec_()

    def Find(self):
        selected_value1 = int(self.comboBox.currentText())
        selected_value2 = int(self.comboBox_2.currentText())  # 获取当前选中的 ComboBox 中的值，并转换为整数
        selected_value3 = int(self.lineEdit.text())
        text = self.textEdit.toPlainText()  # 获取 textEdit 的所有文本
        lines = text.split('\n')  # 按行分割文本
        for line in lines:
            # 提取冒号后面的数字部分并转换为整数
            number_str = line.split(':')[1].strip()
            n = int(number_str)
        try:
            cursor = db.cursor()
            # 查询数据库获取已有的年月日
            cursor.execute('SELECT start_time, end_time FROM time_table WHERE place_id=%s AND use_time=%s',(n,selected_value3))
            existing_time_ranges = cursor.fetchall()

            overlaps = False
            for start_time, end_time in existing_time_ranges:
                if not (selected_value2 <= start_time or selected_value1 >= end_time):
                    overlaps = True
                    break

            if overlaps:
                self.textEdit_2.clear()
                self.textEdit_2.append('该时间段有冲突')
                if selected_value2 <= selected_value1:
                    self.textEdit_2.clear()
                    self.textEdit_2.append('结束时间必须大于起始时间')
            else:
                # 如果没有重叠，则可以添加新的时间段到数据库
                #cursor.execute('INSERT INTO time_table (start_time, end_time) VALUES (%s, %s)',
                #               (selected_value1, selected_value2))
                #db.commit()
                self.textEdit_2.clear()
                self.textEdit_2.append('该时间段可以预约')
                if selected_value2 <= selected_value1:
                    self.textEdit_2.clear()
                    self.textEdit_2.append('结束时间必须大于起始时间')
        except Exception as e:
            print('数据库异常:', e)


    def Insert(self):
        selected_value1 = int(self.comboBox.currentText())
        selected_value2 = int(self.comboBox_2.currentText())  # 获取当前选中的 ComboBox 中的值，并转换为整数
        selected_value3 = int(self.lineEdit.text())
        text = self.textEdit.toPlainText()  # 获取 textEdit 的所有文本
        lines = text.split('\n')  # 按行分割文本
        for line in lines:
            # 提取冒号后面的数字部分并转换为整数
            number_str = line.split(':')[1].strip()
            n = int(number_str)
        try:
            cursor = db.cursor()
            # 查询数据库获取已有的年月日
            cursor.execute('SELECT start_time, end_time FROM time_table WHERE place_id=%s AND use_time=%s',(n,selected_value3))
            existing_time_ranges = cursor.fetchall()

            overlaps = False
            for start_time, end_time in existing_time_ranges:
                if not (selected_value2 <= start_time or selected_value1 >= end_time):
                    overlaps = True
                    break

            if overlaps:
                self.textEdit_3.clear()
                self.textEdit_3.append('预约失败')
                if selected_value2 <= selected_value1:
                    self.textEdit_3.clear()
                    self.textEdit_3.append('结束时间必须大于起始时间')
            else:
                # 如果没有重叠，则可以添加新的时间段到数据库

                if selected_value2 <= selected_value1:
                    self.textEdit_3.clear()
                    self.textEdit_3.append('结束时间必须大于起始时间')
                else:
                    cursor.execute(
                        'INSERT INTO time_table (place_id,start_time, end_time, use_time, user_phone) VALUES (%s, %s,%s,%s,%s)',
                        (n, selected_value1, selected_value2, selected_value3, global_phone.phone_num))
                    cursor.execute('UPDATE usr_table SET white = white+1 WHERE phone_number=%s',(global_phone.phone_num,))
                    cursor.execute('SELECT white FROM usr_table WHERE phone_number=%s',(global_phone.phone_num,))
                    vip_ranges = cursor.fetchall()
                    for white in vip_ranges:
                        if white[0] >= 50:
                            cursor.execute(
                                'UPDATE usr_table SET vip = 1 WHERE phone_number=%s',(global_phone.phone_num,))
                    db.commit()
                    self.textEdit_3.clear()
                    self.textEdit_3.append('预约成功')
        except Exception as e:
            print('数据库异常:', e)









class allDialog(allyest.Ui_allDialog, QDialog):
    def __init__(self):
        super(allDialog, self).__init__()
        self.setupUi(self)
        ##
        self.textEdit_2.setReadOnly(True)
        self.textEdit.setReadOnly(True)
        self.showDate()
        ##
        self.pushButton_2.clicked.connect(lambda: self.Insert1())
        self.pushButton_3.clicked.connect(lambda: self.Insert2())
        self.pushButton_4.clicked.connect(lambda: self.Insert3())
        self.pushButton_5.clicked.connect(self.subscribe)

    def subscribe(self):
        self.tool_window = Tool_Window()
        self.tool_window.show()
        self.close()  # 关闭当前窗口

    def showDate(self):
        self.textEdit_2.clear()
        current_date = QDate.currentDate()
        date_str = current_date.toString('yyyy-MM-dd')
        self.textEdit_2.insertPlainText(date_str)

    def Insert1(self):
        selected_value = int(self.lineEdit.text())
        try:
            cursor = db.cursor()
            cursor.execute('SELECT use_time FROM time_table WHERE (place_id=1 OR place_id=2 OR place_id=3) AND use_time=%s', (selected_value,))
            existing_time_ranges = cursor.fetchall()
            if not existing_time_ranges:
                cursor.execute('INSERT INTO time_table (place_id,start_time, end_time,use_time, user_phone) VALUES (1, 8,18,%s,%s)', (selected_value,global_phone.phone_num,))
                cursor.execute('INSERT INTO time_table (place_id,start_time, end_time,use_time, user_phone) VALUES (2, 8,18,%s,%s)', (selected_value,global_phone.phone_num,))
                cursor.execute('INSERT INTO time_table (place_id,start_time, end_time,use_time, user_phone) VALUES (3, 8,18,%s,%s)', (selected_value,global_phone.phone_num,))
                self.textEdit.append('预约成功！')
                cursor.execute('UPDATE usr_table SET white = white+30 WHERE phone_number=%s', (global_phone.phone_num,))
                cursor.execute('SELECT white FROM usr_table WHERE phone_number=%s', (global_phone.phone_num,))
                vip_ranges = cursor.fetchall()
                for white in vip_ranges:
                    if white[0] >= 50:
                        cursor.execute(
                            'UPDATE usr_table SET vip = 1 WHERE phone_number=%s', (global_phone.phone_num,))
            else:
                self.textEdit.clear()
                self.textEdit.append('当天的场地已有时间段被预定！若事态紧急请联系管理员！')
            db.commit()
        except Exception as e:
            print('数据库异常:', e)

    def Insert2(self):
        selected_value = int(self.lineEdit.text())
        try:
            cursor = db.cursor()
            cursor.execute('SELECT use_time FROM time_table WHERE (place_id=4 OR place_id=5 OR place_id=6) AND use_time=%s', (selected_value,))
            existing_time_ranges = cursor.fetchall()
            if not existing_time_ranges:
                cursor.execute(
                    'INSERT INTO time_table (place_id,start_time, end_time,use_time, user_phone) VALUES (4, 8,18,%s,%s)',
                    (selected_value, global_phone.phone_num,))
                cursor.execute(
                    'INSERT INTO time_table (place_id,start_time, end_time,use_time, user_phone) VALUES (5, 8,18,%s,%s)',
                    (selected_value, global_phone.phone_num,))
                cursor.execute(
                    'INSERT INTO time_table (place_id,start_time, end_time,use_time, user_phone) VALUES (6, 8,18,%s,%s)',
                    (selected_value, global_phone.phone_num,))
                self.textEdit.append('预约成功！')
                cursor.execute('UPDATE usr_table SET white = white+30 WHERE phone_number=%s', (global_phone.phone_num,))
                cursor.execute('SELECT white FROM usr_table WHERE phone_number=%s', (global_phone.phone_num,))
                vip_ranges = cursor.fetchall()
                for white in vip_ranges:
                    if white[0] >= 50:
                        cursor.execute(
                            'UPDATE usr_table SET vip = 1 WHERE phone_number=%s', (global_phone.phone_num,))
            else:
                self.textEdit.clear()
                self.textEdit.append('当天的场地已有时间段被预定！若事态紧急请联系管理员！')
            db.commit()
        except Exception as e:
            print('数据库异常:', e)

    def Insert3(self):
        selected_value = int(self.lineEdit.text())
        try:
            cursor = db.cursor()
            cursor.execute('SELECT use_time FROM time_table WHERE (place_id=7 OR place_id=8 OR place_id=9) AND use_time=%s', (selected_value,))
            existing_time_ranges = cursor.fetchall()
            if not existing_time_ranges:
                cursor.execute(
                    'INSERT INTO time_table (place_id,start_time, end_time,use_time, user_phone) VALUES (7, 8,18,%s,%s)',
                    (selected_value, global_phone.phone_num,))
                cursor.execute(
                    'INSERT INTO time_table (place_id,start_time, end_time,use_time, user_phone) VALUES (8, 8,18,%s,%s)',
                    (selected_value, global_phone.phone_num,))
                cursor.execute(
                    'INSERT INTO time_table (place_id,start_time, end_time,use_time, user_phone) VALUES (9, 8,18,%s,%s)',
                    (selected_value, global_phone.phone_num,))
                self.textEdit.append('预约成功！')
                cursor.execute('UPDATE usr_table SET white = white+30 WHERE phone_number=%s', (global_phone.phone_num,))
                cursor.execute('SELECT white FROM usr_table WHERE phone_number=%s', (global_phone.phone_num,))
                vip_ranges = cursor.fetchall()
                for white in vip_ranges:
                    if white[0] >= 50:
                        cursor.execute(
                            'UPDATE usr_table SET vip = 1 WHERE phone_number=%s', (global_phone.phone_num,))
            else:
                self.textEdit.clear()
                self.textEdit.append('当天的场地已有时间段被预定！若事态紧急请联系管理员！')
            db.commit()
        except Exception as e:
            print('数据库异常:', e)

    # def Insert3(self):
    #     selected_value = int(self.lineEdit.text())
    #     try:
    #         cursor = db.cursor()
    #         cursor.execute('SELECT use_time FROM time_table WHERE (place_id=7 OR place_id=8 OR place_id=9) AND use_time=%s',(selected_value,))
    #         existing_time_ranges = cursor.fetchall()
    #         if not existing_time_ranges:
    #             cursor.execute('INSERT INTO time_table (place_id,start_time, end_time,use_time) VALUES (7, 8,18,%s)',(selected_value,))
    #             cursor.execute('INSERT INTO time_table (place_id,start_time, end_time,use_time) VALUES (8, 8,18,%s)',(selected_value,))
    #             cursor.execute('INSERT INTO time_table (place_id,start_time, end_time,use_time) VALUES (9, 8,18,%s)',(selected_value,))
    #             self.textEdit.append('预约成功！')
    #         else:
    #             self.textEdit.clear()
    #             self.textEdit.append('当天的场地已有时间段被预定！若事态紧急请联系管理员！')
    #         db.commit()
    #     except Exception as e:
    #         print('数据库异常:', e)




if __name__ == "__main__":
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        # 为main_window类和login_window类创建对象
        main_window = pages_window()
        # 显示登录窗口
        main_window.show()
        # 关闭程序，释放资源
        sys.exit(app.exec_())

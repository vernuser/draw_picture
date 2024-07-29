from tools import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import sys
import pymysql
import global_phone
# 数据库连接
db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='1024',
    database='体育馆管理',
    charset='utf8mb4',
)

class Tool_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Tool_Window()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.pushButton_Find.clicked.connect(self.Find)
        self.ui.pushButton_next.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(1))
        self.ui.pushButton_Update_2.clicked.connect(self.Update)
        self.ui.stackedWidget_4.setCurrentIndex(0)
        self.ui.stackedWidget_3.setCurrentIndex(0)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_back.clicked.connect(self.goBackToQueryPage)
        self.show()

    def goBackToQueryPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.stackedWidget_4.setCurrentIndex(0)
        self.ui.stackedWidget_3.setCurrentIndex(0)

    def Find(self):
        cursor = db.cursor()
        sql = 'SELECT * FROM tools_table WHERE tool_name LIKE %s'
        value = '%' + self.ui.lineEdit_Findtool.text() + '%'
        try:
            cursor.execute(sql, (value,))
            res = cursor.fetchall()
            self.ui.plainTextEdit.clear()
            if res:
                headers = ['工具编号', '设备名称', '库存数量', '价格/小时']
                self.ui.plainTextEdit.appendPlainText('\t'.join(headers))
                self.ui.plainTextEdit.appendPlainText('-' * 50)
                for row in res:
                    row_data = '\t'.join([str(item) for item in row])
                    self.ui.plainTextEdit.appendPlainText(row_data)
            else:
                self.ui.plainTextEdit.appendPlainText('没有找到匹配的记录')
        except Exception as e:
            print('数据库异常:', e)

    def Update(self):
        if not self.ui.lineEdit_number.text() or not self.ui.lineEdit_Update.text():
            self.ui.stackedWidget_4.setCurrentIndex(1)
            self.ui.stackedWidget_3.setCurrentIndex(0)
            return

        try:
            number = int(self.ui.lineEdit_number.text())
            tool_id = int(self.ui.lineEdit_Update.text())
        except ValueError:
            print('输入值无效')
            self.ui.stackedWidget_4.setCurrentIndex(1)
            self.ui.stackedWidget_3.setCurrentIndex(0)
            return

        if tool_id <= 0:
            self.ui.stackedWidget_4.setCurrentIndex(1)
            self.ui.stackedWidget_3.setCurrentIndex(0)
            return

        cursor = db.cursor()
        sql = 'SELECT yes_number, price FROM tools_table WHERE tool_id=%s'
        try:
            cursor.execute(sql, (tool_id,))
            result = cursor.fetchone()
            if not result:
                self.ui.stackedWidget_4.setCurrentIndex(1)
                self.ui.stackedWidget_3.setCurrentIndex(0)
                return

            yes_number, price = result
            if number > yes_number:
                self.ui.stackedWidget_4.setCurrentIndex(2)
                self.ui.stackedWidget_3.setCurrentIndex(0)
                return

            new_yes_number = yes_number - number
            update_sql = 'UPDATE tools_table SET yes_number=%s WHERE tool_id=%s'
            insert_sql='insert into borrow_table(phone_number,tool_id) values (%s,%s)'
            update_sql2='update usr_table set is_equipment_reserved = %s where phone_number = %s'
            value=(0,global_phone.phone_num)
            value2=(global_phone.phone_num,tool_id)
            cursor.execute(update_sql, (new_yes_number, tool_id))
            cursor.execute(insert_sql,value2)
            cursor.execute(update_sql2,value)
            db.commit()
            print('更新成功')
            self.ui.stackedWidget.setCurrentIndex(0)
            total_price = number * price
            message = f"预订成功！总价格为：{total_price} 元，请到现场领取使用！"
            self.ui.textEdit.setPlainText(message)
        except Exception as e:
            print('数据库更新出问题:', e)
            db.rollback()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Tool_Window()
    sys.exit(app.exec_())
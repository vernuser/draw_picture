# main.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from LoginUI import *
from admin_window import *
import sys
import pymysql
import base64
from cryptography.fernet import Fernet
from runnice import pages_window  # 导入 pages_window 类

import global_phone


class LoginUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.pushButton_login.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.pushButton_register.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_3.clicked.connect(self.login_clicked)
        self.ui.pushButton_4.clicked.connect(self.regedit_clicked)
        self.ui.pushButton_admin.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_admin_2.clicked.connect(self.admin_clicked)

        self.show()
        #
        # 密钥
        self.key_pass = Fernet.generate_key()
        plaintext1 = base64.b64decode("cm9vdA==").decode('utf-8')
        plaintext2 = base64.b64decode("MTAyNA==").decode('utf-8')
        encrypted_text1 = self.encrypt_text(plaintext1, self.key_pass)
        encrypted_text2 = self.encrypt_text(plaintext2, self.key_pass)

        # 解密后的文本
        self.decrypted_text1 = self.decrypt_text(encrypted_text1, self.key_pass)
        self.decrypted_text2 = self.decrypt_text(encrypted_text2, self.key_pass)

    def encrypt_text(self, text, key):
        f = Fernet(key)
        encrypted_text = f.encrypt(text.encode())
        return encrypted_text

    def decrypt_text(self, encrypted_text, key):
        f = Fernet(key)
        decrypted_text = f.decrypt(encrypted_text)
        return decrypted_text.decode()

    def login_clicked(self):
        username = self.ui.lineEdit_login_phone.text()
        password = self.ui.lineEdit_login_passwd.text()
        password11 = base64.b64encode(password.encode('utf-8')).decode('utf-8')
        global phone_num
        try:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user=self.decrypted_text1,
                passwd=self.decrypted_text2,
                db="体育馆管理"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT phone_number, usr_pass, black FROM usr_table")
            rows = cursor.fetchall()

            # 遍历查询结果进行登录验证
            login_successful = False
            account_blacklisted = False
            for row in rows:
                db_username, db_password, db_black = row
                print(rows)

                if username == str(db_username) and password11 == str(db_password):
                    if db_black < 5:
                        login_successful = True
                        global_phone.phone_num = username
                        break
                    else:
                        account_blacklisted = True
                        break

            if login_successful:
                print("登录成功")
                self.ui.stackedWidget_2.setCurrentIndex(0)  # 登录成功后跳转到相应页面
                self.close()

                # 创建并显示 pages_window 窗口
                self.runnice_window = pages_window()
                self.runnice_window.show()

            elif account_blacklisted:
                print("账号已被拉黑，联系管理员")
                self.ui.stackedWidget.setCurrentIndex(2)  # 账号被拉黑，跳转到管理员联系页面
                cursor.execute("SELECT admin_name, admin_usr FROM admine_table")
                admin_info = cursor.fetchall()
                admin_details = "账号已被拉黑，联系管理员！！！\n"+"\n".join([f"管理员姓名: {name}, 电话号码: {user}" for name, user in admin_info])
                self.ui.plainTextEdit.setPlainText(admin_details)  # 在页面的QPlainTextEdit上显示管理员信息

            else:
                if len(username) == 0 or len(password) == 0:
                    print("用户名或密码不能为空")
                else:
                    print("用户名或密码错误或该账号已被拉黑！")
                self.ui.stackedWidget_2.setCurrentIndex(3)  # 设置为错误页面

        except Exception as e:
            print("数据库连接失败:", str(e))
            # 在数据库连接失败时设置为错误页面
            self.ui.stackedWidget_2.setCurrentIndex(3)

        finally:
            if conn:
                conn.close()

    def admin_clicked(self):
        username1 = self.ui.lineEdit_login_phone_2.text()
        password1 = self.ui.lineEdit_login_passwd_2.text()

        try:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user=self.decrypted_text1,
                passwd=self.decrypted_text2,
                db="体育馆管理"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT admin_usr,admin_pass FROM admine_table")
            rows = cursor.fetchall()

            password11=base64.b64encode(password1.encode('utf-8')).decode('utf-8')
            print(password11)
            # 遍历查询结果进行登录验证
            login_successful = False
            for row in rows:
                db_username1, db_password1 = row
                if username1 == str(db_username1) and password1 == str(db_password1):
                    login_successful = True
                    break

            if login_successful:
                print("登录成功")
                self.ui.stackedWidget_2.setCurrentIndex(0)  # 登录成功后跳转到相应页面
                self.admin_window = Admin_Window()
                self.admin_window.show()
                self.close()
            else:
                if len(username1) == 0 or len(password1) == 0:
                    print("用户名或密码不能为空")
                else:
                    print("用户名或密码错误")
                self.ui.stackedWidget_2.setCurrentIndex(3)  # 设置为错误页面

        except Exception as e:
            print("数据库连接失败:", str(e))

        finally:
            if conn:
                conn.close()
            # 在数据库连接失败时设置为错误页面

    def regedit_clicked(self):
        re_username1 = self.ui.lineEdit_register_phone.text().strip()
        re_password1 = self.ui.lineEdit_register_passwd.text().strip()
        re_password12 = self.ui.lineEdit_register_passwd2.text().strip()
        # global phone_num
        try:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user=self.decrypted_text1,
                passwd=self.decrypted_text2,
                db="体育馆管理"
            )
            cursor = conn.cursor()

            # 检查用户名是否已经存在
            cursor.execute("SELECT phone_number FROM usr_table WHERE phone_number = %s", (re_username1,))
            existing_user = cursor.fetchone()

            if existing_user:
                print("账号已存在！")
                self.ui.stackedWidget_2.setCurrentIndex(4)
                return

            if len(re_username1) == 11:
                if re_password1 == re_password12 and len(re_password1) != 0 and len(
                        re_password12) != 0:  # 检查密码匹配
                    insert_query = "INSERT INTO usr_table (phone_number, white, black, vip, usr_pass,is_equipment_reserved) VALUES (%s, 0, 0, 0, %s,1)"
                    encoded_data = base64.b64encode(re_password1.encode('utf-8')).decode('utf-8');
                    cursor.execute(insert_query, (re_username1, encoded_data))
                    conn.commit()
                    print("注册成功")
                    self.ui.stackedWidget_2.setCurrentIndex(2)
                elif len(re_password1) == 0 or len(re_password12) == 0:
                    print("密码不能为空")
                    self.ui.stackedWidget_2.setCurrentIndex(1)


                else:
                    print("密码不匹配")
                    self.ui.stackedWidget_2.setCurrentIndex(1)
            else:
                print("账号必须11位")
                self.ui.stackedWidget_2.setCurrentIndex(4)
        except Exception as e:
            print("数据库连接失败:", str(e))
        finally:
            if conn:
                conn.close()


class Admin_Window(QMainWindow):  # 更正类名
    def __init__(self):
        super().__init__()
        self.ui = Ui_Admin_Window()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_111.clicked.connect(self.back)
        self.ui.pushButton_222.clicked.connect(self.unback)
        self.ui.pushButton_search.clicked.connect(self.search)
        self.ui.pushButton_black.clicked.connect(self.black)
        self.ui.pushButton_white.clicked.connect(self.white)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.show()

        # 密钥
        self.key_pass = Fernet.generate_key()
        plaintext1 = base64.b64decode("cm9vdA==").decode('utf-8')
        plaintext2 = base64.b64decode("MTAyNA==").decode('utf-8')
        encrypted_text1 = self.encrypt_text(plaintext1, self.key_pass)
        encrypted_text2 = self.encrypt_text(plaintext2, self.key_pass)

        # 解密后的文本
        self.decrypted_text1 = self.decrypt_text(encrypted_text1, self.key_pass)
        self.decrypted_text2 = self.decrypt_text(encrypted_text2, self.key_pass)

    def encrypt_text(self, text, key):
        f = Fernet(key)
        encrypted_text = f.encrypt(text.encode())
        return encrypted_text

    def decrypt_text(self, encrypted_text, key):
        f = Fernet(key)
        decrypted_text = f.decrypt(encrypted_text)
        return decrypted_text.decode()

    def search(self):
        try:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user=self.decrypted_text1,
                passwd=self.decrypted_text2,
                db="体育馆管理"
            )
            cursor = conn.cursor()
            inputtext = self.ui.lineEdit_search.text()

            if inputtext == '用户' or inputtext == 'user' or inputtext == 'u':
                table_name = 'usr_table'
                headers = ['电话号码', '预约数', '失约次数', '是否vip', '用户密码', '是否归还']
            elif inputtext == "值班" or inputtext == 'work':
                table_name = "worker_table"
                headers = ['工作号', '管理员/员工编号', '工作日期']
            elif inputtext == "安全设施" or inputtext == '安全' or inputtext == 'safe' or inputtext == 's':
                table_name = "place_table"
                headers = ['场地编号', '开放情况', '场地名称', '安全设施到期时间']
            else:
                self.ui.plainTextEdit.appendPlainText('无效的表名')
                return

            try:
                cursor.execute(f"SELECT * FROM {table_name}")
                res = cursor.fetchall()

                if res:
                    # 清空plainTextEdit
                    self.ui.plainTextEdit.clear()

                    # 添加表头
                    self.ui.plainTextEdit.appendPlainText('\t'.join(headers))
                    self.ui.plainTextEdit.appendPlainText('-' * 50)

                    # 添加查询结果
                    for row in res:
                        row_data = '\t'.join([str(item) for item in row])
                        self.ui.plainTextEdit.appendPlainText(row_data)
                else:
                    self.ui.plainTextEdit.appendPlainText('没有找到匹配的记录')

            except Exception as e:
                self.ui.plainTextEdit.appendPlainText(f'查询出错: {str(e)}')

        except Exception as e:
            print("数据库连接失败:", str(e))

        finally:
            if conn:
                conn.close()

    def black(self):
        try:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user=self.decrypted_text1,
                passwd=self.decrypted_text2,
                db="体育馆管理"
            )
            cursor = conn.cursor()
            try:
                sql = 'update usr_table set black = 5 where phone_number = %s'
                value = self.ui.lineEdit_object.text()

                cursor.execute(sql, (value))
                conn.commit()
                print('成功拉黑！')

            except:
                print('拉黑出问题')
        except Exception as e:
            print(f'数据库链接出错: {str(e)}')
        finally:
            if conn:
                conn.close()

    def white(self):
        try:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user=self.decrypted_text1,
                passwd=self.decrypted_text2,
                db="体育馆管理"
            )
            cursor = conn.cursor()
            sql = 'update usr_table set black = 0 where phone_number = %s'
            value = self.ui.lineEdit_object.text()

            try:
                cursor.execute(sql, (value))
                conn.commit()
                print('成功移除黑名单！')
            except:
                print('移除黑名单出问题')

        except Exception as e:
            print("数据库连接失败:", str(e))
        finally:
            if conn:
                conn.close()

    def back(self):
        try:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user=self.decrypted_text1,
                passwd=self.decrypted_text2,
                db="体育馆管理"
            )
            cursor = conn.cursor()
            phone_number = self.ui.lineEdit_object.text().strip()

            if not phone_number:
                print('请输入有效的电话号码')
                return

            try:
                sql = 'UPDATE usr_table SET is_equipment_reserved = 1 WHERE phone_number = %s'
                cursor.execute(sql, (phone_number))
                conn.commit()
                print('已设置为归还')
            except Exception as e:
                print(f'归还出问题: {e}')
        except Exception as e:
            print("数据库连接失败:", str(e))
        finally:
            if conn:
                conn.close()

    def unback(self):
        try:
            conn = pymysql.connect(
                host="localhost",
                port=3306,
                user=self.decrypted_text1,
                passwd=self.decrypted_text2,
                db="体育馆管理"
            )
            cursor = conn.cursor()
            phone_number = self.ui.lineEdit_object.text().strip()

            if not phone_number:
                print('请输入有效的电话号码')
                return

            try:
                sql = 'UPDATE usr_table SET is_equipment_reserved = 0 WHERE phone_number = %s'
                cursor.execute(sql, (phone_number))
                conn.commit()
                print('已设置为未归还')
            except Exception as e:
                print(f'未归还出问题: {e}')

        except Exception as e:
            print("数据库连接失败:", str(e))
        finally:
            if conn:
                conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_ui = LoginUI()
    sys.exit(app.exec_())
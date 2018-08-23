import pymysql.cursors
import datetime
class MYSQL:
    def __init__(self, port, user, passwd, db):
        self.port_ = port
        self.user_ = user
        self.passwd_ = passwd
        self.db_ = db
        self.login_sql()
    def __del__(self):
        self.cursor.close()
        self.connect.close()
    def login_sql(self):
        self.connect = pymysql.Connect(
            host = 'localhost',
            port= self.port_,
            user= self.user_,
            passwd= self.passwd_,
            db=self.db_,
            charset='utf8'
        )
        print('数据库连接')
        self.cursor = self.connect.cursor()
        self.date = datetime.datetime.now()
    # 获取游标
    def chekdate(self):
        d2 = datetime.datetime.now()
        hours = d2.hour - self.date.hour
        if hours > 3 or hours < 0:
            self.cursor.close()
            self.connect.close()
            self.login_sql()
    def 查询开始时间(self,form,tk):
        self.chekdate()
        try:
            sql = "SELECT date_k FROM " + form + " WHERE tk = '%s' "
            data = (tk)
            self.cursor.execute(sql % data)
            for row in self.cursor.fetchall():
                return row[0]
            return 0
        except:
            return 0
    def 查询到期时间(self,form,tk):
        self.chekdate()
        try:
            sql = "SELECT date_z FROM " + form + " WHERE tk = '%s' "
            data = (tk)
            self.cursor.execute(sql % data)
            for row in self.cursor.fetchall():
                return row[0]
            return 0
        except:
            return 0
    def 查询机器码(self, form, tk):
        self.chekdate()
        try:
            sql = "SELECT code FROM " + form + " WHERE tk = '%s' "
            data = (tk)
            self.cursor.execute(sql % data)
            for row in self.cursor.fetchall():
                print('查询结果 = ' + str(row[0]))
                return row[0]
            return 0
        except:
            return 0
    def 查(self, form, tk,code):
        self.chekdate()
        try:
            ret_code = self.查询机器码(form, tk)
            print('查询机器码返回 = ' + str(ret_code))
            if ret_code == 0:
                self.cursor.close()
                self.connect.close()
                self.login_sql()
                ret_code = self.查询机器码(form, tk)
            if ret_code == code:
                sql = "SELECT date_z FROM " + form + " WHERE tk = '%s' "
                data = (tk)
                self.cursor.execute(sql % data)
                for row in self.cursor.fetchall():
                    d1 = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
                    d2 = datetime.datetime.now()
                    # T到期F未到期
                    if d2.__gt__(d1):
                        print('ret = 102')
                        return 102
                    else:
                        print('ret = 1')
                        return 1
                print('retB = 0')
                return 0
            else:
                print('ret = 101')
                return 101
        except:
            print('retA = 0')
            return 0
    def 增(self, form, tk, name):
        self.chekdate()
        try:
            sql = "INSERT INTO " + form + " (tk, vip_name) VALUES ( '%s', '%s' )"
            data = (tk, name)
            self.cursor.execute(sql % data)
            self.connect.commit()
            return self.cursor.rowcount
        except:
            return 0
    def 删(self, form, tk):
        self.chekdate()
        try:
            sql = "DELETE FROM " + form + " WHERE tk = '%s' "
            data = (tk)
            self.cursor.execute(sql % data)
            self.connect.commit()
            return self.cursor.rowcount
        except:
            return 0
    def 检查版本(self):
        try:
            sql = "SELECT ver FROM imver WHERE tt = 101 "
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                return row[0]
            return 0
        except:
            return 0
    def login(self, form, tk, code,ip):
        try:
            self.chekdate()
            ret_code = self.查询机器码(form, tk)
            if ret_code == 0:
                self.cursor.close()
                self.connect.close()
                self.login_sql()
                ret_code = self.查询机器码(form, tk)
            if ret_code == None:
                date_K = datetime.datetime.now()
                date_temp = datetime.timedelta(days=30)
                date_Z = date_K + date_temp
                sql = "UPDATE " + form + " SET code = '%s', address = '%s', date_k = '%s', date_z = '%s' WHERE tk = '%s' "
                data = (code, ip, date_K.strftime('%Y-%m-%d %H:%M:%S'),date_Z.strftime('%Y-%m-%d %H:%M:%S'),tk)
                self.cursor.execute(sql % data)
                self.connect.commit()
                print('ret = 1')
                return 1
            else:
                ret_date = self.查询到期时间(form, tk)
                if ret_date != 0 and ret_date != '':
                    d1 = datetime.datetime.strptime(ret_date, '%Y-%m-%d %H:%M:%S')
                    d2 = datetime.datetime.now()
                    #T到期F未到期
                    if d2.__gt__(d1):
                        print('ret = 102')
                        return 102
                    else:
                        sql = "UPDATE " + form + " SET code = '%s', address = '%s', date = '%s' WHERE tk = '%s' "
                        data = (code, ip, d2.strftime('%Y-%m-%d %H:%M:%S'), tk)
                        self.cursor.execute(sql % data)
                        self.connect.commit()
                        print('ret = 1')
                        return 1
                else:
                    print('ret = 0')
                    return 0
        except:
            print('ret = 0')
            return 0
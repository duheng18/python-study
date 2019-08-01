#!/usr/bin/env python
#coding=utf-8

#现在已经没有MySQLdb
import  MySQLdb,time,traceback,logging

class DBOperateAction:
    def __init__(self,dbhost,dbaccount,dbpasswd,dbname,port=3306,charset="utf8"):
        self.dbhost=dbhost
        self.dbaccount=dbaccount
        self.dbpasswd=dbpasswd[::-1]
        self.dbname=dbname
        self.charset=charset
        self.port=port
        self.db_conn=""
        self.db_cursor=""

    def connect(self):
        try:
            self.db_conn=MySQLdb.connect(host=self.dbhost,user=self.dbaccount,passwd=self.dbpasswd,db=self.dbname,port=self.port,charset=self.charset,connect_timeout=5)
            self.db_cursor=self.db_conn.cursor()
            return True
        except MySQLdb.OperationError:
            logging.error("Connect to "+self.dbhost+"Faild")
            logging.exception("exception message:")
            return False

    def re_connect(self):
        logging.error("connect to mysql server failed,reconnect")
        try:
            self.db_conn=MySQLdb.connect(host=self.dbhost,user=self.dbaccount,passwd=self.dbpasswd,db=self.dbname,port=self.port,charset="utf8")
            self.db_cursor=self.db_conn.cursor()
            return True
        except MySQLdb.OperationError:
            logging.error("Reconnect MySQL faild")
            return False
    def get_all_result(self,sql):
        try:
            #logging.info("Execute sql:"+sql[:500])
            logging.info("Execute sql:"+sql)
            self.db_cursor.execute(sql)
            self.db_conn.commit()
            result=self.db_cursor.fetchall()
            return result
        except MySQLdb.OperationError:
            for i in range(0,3):
                time.sleep(5)
                if self.re_connect():
                    logging.info("reconnect to"+self.dbhost+"database successfully")
                    return False

    def close_connection(self):
        self.db_conn.close()

if __name__=="__main__":
    host="127.0.0.1"
    db_account="root"
    db_passwd="32imij"
    db_name="gakjod"

    db_operation=DBOperateAction(host,db_account,db_passwd,db_name,port=3306)
    db_operation.connect()
    select_sql="insert into countries(Name,CountryCode,shortCountryCode,region)values('testerhome','223','TH','Asia')"
    print(select_sql)

    result=db_operation.get_all_result(select_sql)
    db_operation.close_connection()
    print(result)

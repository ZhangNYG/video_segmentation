#!/usr/bin/python3

import pymysql

def connectSql():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "volley-nyg")
    return db
#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
#encoding:utf8
import sys
import codecs
import xlrd,xlwt
import mysql.connector
import cxMysql.cxMysql as mSqlControl

print 'Content-type: text/html\n'
print '======'

user = 'root'
pwd  = 'seat'
host = '127.0.0.1'
db   = 'test_tp'

mysqlObj = mSqlControl.class_mysql()
mysqlObj.connector(host,user,pwd,db,"utf8")

# select_sql = " SELECT x_no, name, id FROM sign_up_data "

_insertData = {}
_insertData['name'] = u"中文_python_user1"
_insertData['id'] = "0008"
_insertData['PaswdCode'] = "999991"


print mysqlObj.InsertSql( u"sign_up_data", _insertData)

mysqlObj.saveDB( u"sign_up_data", _insertData)
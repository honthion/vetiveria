# coding:utf-8
import MySQLdb
from openpyxl import Workbook
import time

# 打开日志文件
backup_date = time.strftime("%Y%m%d")
date_now = time.strftime('%Y-%m-%d %H:%M:%S')
sqlStr1 = 'SELECT DISTINCT `phone_no`FROM `record_interface` WHERE DATEDIFF(`ctime`,CURDATE())=-1'
try:
    db = MySQLdb.connect(host='172.16.50.150',
                         port=5541,
                         user='zhangrongxin',
                         passwd='ZDEwZjlhZmNlZDU0',
                         db='kemi'
                         )
    curSql1 = db.cursor()
    curSql1.execute(sqlStr1)
    all_count = curSql1.fetchall()
    # 写入excel
    workbook = Workbook()
    sheet = workbook.active
    for idx, val in enumerate(all_count):
        sheet.cell(row=idx+1, column=1).value = val[0]
    workbook.save(r'%s.xls' % (backup_date))
except MySQLdb.Error, err_msg:
    print "MySQL error msg:", err_msg

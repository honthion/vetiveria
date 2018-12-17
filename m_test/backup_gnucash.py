# -*- coding:utf-8 -*-
import MySQLdb
import time
import os
import zipfile
import sendgrid
import base64, urllib
from sendgrid.helpers.mail import *
import platform
import ConfigParser

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf = ConfigParser.ConfigParser()
sys = os.name
CONF_DIR = ''

if sys == 'nt':
    CONF_DIR = 'C://Users//user//Dropbox//properties//settings.ini'
elif sys == 'posix':
    CONF_DIR = '/data/config/properties/settings.ini'
conf.read(CONF_DIR)
os_name = platform.system()

dbUser = conf.get('guncash', 'mysql_username')
dbPasswd = conf.get('guncash', 'mysql_password')
dbHost = conf.get('guncash', 'mysql_host')
dbName = conf.get('guncash', 'mysql_dbname')
backupDir = conf.get('guncash', 'backup_dir')
api_key = conf.get('sendgrid', 'api_key')
from_email_str = conf.get('sendgrid', 'from_email')
to_email_str = conf.get('sendgrid', 'to_email')
dbCharset = 'utf8'
backupDate = time.strftime("%Y%m%d")
date_now = time.strftime('%Y-%m-%d %H:%M:%S')
# 查出MySQL中所有的数据库名称
sqlStr1 = "show databases like 'gnucash'"
file_name, file_path, zip_name = '', '', ''
try:
    connDB = MySQLdb.connect(dbHost, dbUser, dbPasswd, dbName)
    connDB.select_db(dbName)
    curSql1 = connDB.cursor()
    curSql1.execute(sqlStr1)
    allDatabase = curSql1.fetchall()
    print 'The database backup to start! %s' % date_now
    for db in allDatabase:
        dbName = db[0]
        fileName = '%s/%s_%s.sql' % (backupDir, backupDate, dbName)
        print fileName
        if os.path.exists(fileName):
            os.remove(fileName)
        file_name = "%s_%s.sql" % (backupDate, dbName)
        file_path = "%s/%s" % (backupDir, file_name)
        back_sql = "mysqldump -h%s -u%s -p%s %s --default_character-set=%s > %s " % (
            dbHost, dbUser, dbPasswd, dbName, dbCharset, file_path)
        print back_sql
        os.system(back_sql)
    print 'The database backup success! %s' % time.strftime('%Y-%m-%d %H:%M:%S')
    zip_name = file_name + '.zip'
    # 打包、压缩文件
    modes = {zipfile.ZIP_DEFLATED: 'deflated', zipfile.ZIP_STORED: 'stored'}
    if file_path:
        zf = zipfile.ZipFile('%s/%s' % (backupDir, zip_name), mode='w')
        try:
            print('adding %s with compression mode' % file_name + str(modes[compression]))
            zf.write(file_path, compress_type=compression)
        finally:
            zf.close()
    # 发送邮件
    sg = sendgrid.SendGridAPIClient(apikey=api_key)
    with open('%s/%s' % (backupDir, zip_name), 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    attachment = Attachment()
    attachment.content = encoded
    attachment.type = "application/zip"
    attachment.filename = "data.zip"
    attachment.disposition = "attachment"
    attachment.content_id = "zip Document file"

    from_email = Email(from_email_str)
    to_email = Email(to_email_str)
    subject = "数据备份【%s】-%s" % (os_name, dbName)
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    mail.add_attachment(attachment)
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
        print 'send email success'
    except urllib.HTTPError as e:
        print(e.read())
        exit()
# 异常
except MySQLdb.Error, err_msg:
    print "MySQL error msg:", err_msg

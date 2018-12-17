# coding:utf-8


f = open('phoneNo', 'r')  # 以读方式打开文件
result = list()
for line in f.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
        continue  # 是的话，跳过不处理
    c = line.split('\t')
    result.append(c[0])  # 保存
    if int(c[1]) < 10:
        break
open('cdays-4-result.txt', 'w').write('%s' % '\n'.join(result))  # 保存入结果文件

import pymysql
name = input('name>>:').strip()
password = input('password>>:').strip()

conn = pymysql.connect(
    host="192.168.0.102",
    user="programmer",password="123456",
    database="programmer",
    charset="utf8"
)

coursor = conn.cursor()
'''
#创建表
sql = """
create table user1 (
id int auto_increment PRIMARY KEY,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""

coursor.execute(sql)
'''

'''
#插入数据
sql = 'insert into user1(name,age,password) values(%s,%s,%s);'
data = [
    ('judy',19,'123'),
    ('marin',29,'345'),
    ('july',10,'890')
]

#拼接并执行sql语句
coursor.executemany(sql,data)
#涉及写操作要注意提交
conn.commit()
'''


#简单验证
#sql='select * from user1 where name = "%s" and password = "%s"' %(name,password)
#print(sql)
#res=coursor.execute(sql)
sql="select * from user1 where name=s% and password=%s"
print(sql)
res = coursor.execute(sql,[name,password])
print(res)


#关闭连接
coursor.close()
conn.close()

if res:
    print('login successful')
else:
    print('login failed')

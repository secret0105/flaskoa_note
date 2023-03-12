# 配置数据库的一些设置


host = '127.0.0.1'
port = 3306
user = 'root'
password = '123456'
database = 'flaskoa'
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8"

# 配置邮箱

MAIL_SERVER = 'smtp.163.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = 'xxxx'
MAIL_PASSWORD = 'xxxx'
MAIL_DEFAULT_SENDER = 'xxx.com'

# 配置session key

SECRET_KEY = 'hello-flask'
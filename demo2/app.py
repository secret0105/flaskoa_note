from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

# migrate 关系映射

from flask_migrate import Migrate

app = Flask(__name__)

# 连接mysql 数据库

host = "localhost"
port = 3306
user = "root"
password = "123456"
database = "flask"

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8"

db = SQLAlchemy(app)

migrate = Migrate(app,db)

# 创建对象

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100))

# user = User(username='zhangsan',password='123456')

# 多表联合查询，使用外键
class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    # String 只支持255个字符，长文本推荐text
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    # backref 反向引用
    author = db.relationship('User',backref='articles')






# 测试连接
with app.app_context():
    # with db.engine.connect() as conn:
    #     # 直接参考教程和会出现报错，需要使用以下写法
    #     rs = conn.execute(sqlalchemy.text("select 1"))
    #     print(rs.fetchone()) # (1,)

    # 创建表 需要上下文环境
    db.create_all()
    # pass



# 添加数据
@app.route("/article/add")
def add_article():
    # 由于之前的数据删除了，现在主键ID从2开始
    article_1 = Article(title='flask',content='flaskxx')
    article_1.author = User.query.get(2)
    
    article_2 = Article(title='django',content='djangoxx')
    article_2.author = User.query.get(2)

    # 批量添加，数据使用数组
    db.session.add_all([article_1,article_2])
    db.session.commit()
    return '添加文章成功'

# 查询
@app.route("/article/query")
def query_article():
    user = User.query.get(2)
    for article in user.articles:
        print(article.title)
    return "查找文章成功"


# 向数据库中插入对象
@app.route("/user/add")
def add_user():
    user = User(username='lisi',password='123456')
    db.session.add(user)
    db.session.commit()
    return "添加用户成功"


# 查询对象
@app.route("/user/query")
def query_user():
    # 根据主键查找
    # user = User.query.get(1)
    # 条件查询
    users = User.query.filter_by(username='lisi')
    for user in users:
        print('user:{}'.format(user.username))
    return "查询成功"
 
# 更新
@app.route("/user/update")
def update_user():
    user = User.query.filter_by(username='lisi').first()
    user.password = '232323'
    #session 没有update方法，直接commit就行
    db.session.commit()
    return '更新成功'


# 删除
@app.route("/user/del")
def del_user():
    user = User.query.get(1)
    db.session.delete(user)
    db.session.commit()
    return "删除成功"




# 增删改查




if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)
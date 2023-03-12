from exts import db

from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    # default 传入的是是函数，不是值
    join_time = db.Column(db.DateTime,default=datetime.now)


class EmailModel(db.Model):
    """邮箱对象，非必须"""
    __tablename__ = 'email_code'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(100),nullable=False)
    captcha = db.Column(db.String(100),nullable=False)



class QuestionModel(db.Model):
    """问题类"""
    __tablename__ = 'question'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)

    # 关联外键
    auth_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    auth = db.relationship(UserModel,backref='questions')


class AnswerModel(db.Model):
    """答案类"""
    __tablename__ = 'answer'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)

    # 两个外键，问题与用户
    question_id = db.Column(db.Integer,db.ForeignKey('question.id'))
    auth_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    # 关联外键，评论最新展示在最上面
    question = db.relationship(QuestionModel,backref=db.backref('answers',order_by=create_time.desc()))
    auth = db.relationship(UserModel,backref='answers')
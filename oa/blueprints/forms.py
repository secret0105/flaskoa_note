import wtforms
from wtforms import StringField,IntegerField
from wtforms.validators import Email,EqualTo,Length,InputRequired
from models import UserModel,EmailModel
from flask import session

class RegisterForm(wtforms.Form):
    email = StringField(validators=[Email(message='邮箱格式错误')])
    captcha = StringField(validators=[Length(min=4,max=4,message='验证码格式错误')])
    username = StringField(validators=[Length(min=3,max=20,message='用户名格式错误')])
    password = StringField(validators=[Length(min=6,max=20,message='密码格式错误')])
    # 要与前端name 一致
    password_confirm = StringField(validators=[EqualTo('password',message='输入的密码不一致')])



    #   自定义验证器会自动加载


    def validate_email(self,field):
        """验证邮箱是否被注册"""
        # email = field.data
        email = self.email.data
        # print(email)
        user = UserModel.query.filter_by(email=email).first()
        # print(user)
        if user:
            raise wtforms.ValidationError('邮箱已经被注册过了')


    def validate_captcha(self,field):
        """验证邮箱和验证码是否匹配"""
        captcha = field.data
        email = self.email.data
        print(captcha,email)
        # captcha_model = EmailModel.query.filter_by(email=email,captcha=captcha).first()
        # if not captcha_model:
        #     raise wtforms.ValidationError('邮箱或者验证码错误')
        # todo
        # 验证码是一次性的，在注册成功后，需要删除，但是每次删除会影响性能
        # 可以在emailmodel 中增加一个used字段，用于后期批量删除
        # 尝试session
        # session = field.data
        if session:
            print(session.get(email))
            if session.get(email) != captcha:
                raise wtforms.ValidationError('邮箱或者验证码错误')
            else:
                print('验证码正确')
                # session.clear()
        else:
            raise wtforms.ValidationError('邮箱或者验证码错误')
        


class QuestionForm(wtforms.Form):
    """问题数据校验"""
    title = StringField(validators=[Length(min=3,max=100,message="标题格式错误")])
    content = StringField(validators=[Length(min=3,message="内容格式错误")])

class AnswerForm(wtforms.Form):
    """答案数据校验"""
    content = StringField(validators=[Length(min=1,max=200,message="答案格式内容错误")])

    # 答案id感觉没有必要验证
    question_id = IntegerField(validators=[InputRequired(message='缺少问题id')])
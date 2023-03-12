from flask import Blueprint
from flask import render_template,request,jsonify,session,redirect,url_for
from flask_mail import Message
from exts import mail,db
from models import EmailModel,UserModel
import string 
import random
# 注意引用的格式 .文件名
from .forms import RegisterForm
from werkzeug.security import generate_password_hash,check_password_hash

# 测试邮箱

# 所有前缀都需要加上/auth,__name__ 是固定写法
bp = Blueprint('auth',__name__,url_prefix="/auth")

@bp.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        form = request.form.to_dict()
        print(form)
        # 出现了报错，提示找不到email，原因是没有创建loginForm验证类
        # 不用验证，直接将form转成字典
        email = form.get('email')
        password = form.get('password')
        user = UserModel.query.filter_by(email=email).first()
        print(user)
        if user:
            result = check_password_hash(user.password,password)
            if result:
                # 存入到session中
                session['user_id'] = user.id
                return redirect("/")
            else:
                print('用户邮箱和密码不匹配')
                return render_template("login.html")
        else:
            print("用户不存在") 
            return render_template("login.html")


@bp.route("/logout")
def logout():
    session.clear()
    # 问题 不能直接使用/
    # return redirect("/")
    return redirect("/")






@bp.route("/register",methods=["GET","POST"])
def register_user():
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            # 验证通过后删除session
            # 也可以通过删除key
            # session.pop(key)
            # session.clear()
            email = form.email.data
            username = form.username.data
            password = form.password.data
            
            # hash值过长，超过了100
            user = UserModel(username=username,password=generate_password_hash(password),email=email)
            db.session.add(user)
            db.session.commit()
            # 重定向时指向方法，需要加上蓝图前缀
            session.pop(email)
            return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            return redirect(url_for('auth.register_user'))



# 邮箱发送验证码

@bp.route("/mail/captcha")
def captcha():
    # 接收邮箱的两种方式:1.参数；2.写在url中
    # 本次使用第二种方法
    email = request.args.get("email")
    source = string.ascii_letters + string.digits
    cap_code = "".join(random.sample(source,4))

    # 正常验证码需要被记录，可以使用缓存 memcache  redis 等
    # 感觉也可以使用session  todo
    session[email] = cap_code

    # 使用数据库存储
    message = Message(subject="【flask-oa】验证码",recipients=[email],body="您好：验证码为{}".format(cap_code))
    mail.send(message)

    # email_code = EmailModel(email=email,captcha=cap_code)
    # db.session.add(email_code)
    # db.session.commit()

    data = {"code":"200","message":"success","data":None}
    return jsonify(data)




    

    # return '验证码为{}'.format(cap_code)





# 开始测试邮箱
@bp.route("/mail/test")
def test_mail():
    message = Message(subject='flask测试邮件发送',recipients=['1078274519@qq.com'],body='hello flask')
    mail.send(message)
    return '发送邮件成功'
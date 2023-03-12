from flask import Flask,session,g
from exts import db,mail
from flask_migrate import Migrate

import config


from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp

from models import UserModel

app = Flask(__name__)
app.config.from_object(config)

# session.permanent = True
db.init_app(app)
mail.init_app(app)

# 注册蓝图

app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)

migrate = Migrate(app,db)


# 持久化session中的user对象

@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g,'user',user)
    else:
        setattr(g,'user',None)

# 设置后全局都能使用了
@app.context_processor
def my_context_processor():
    return {'user': g.user}

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)
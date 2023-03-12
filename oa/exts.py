# flask-sqlalchme
# 避免出现循环引用
# model 依赖db  如果将db写到app 中,app又依赖model

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()
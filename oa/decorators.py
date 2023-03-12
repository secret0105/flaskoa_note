from functools import wraps

from flask import redirect,url_for,g

def login_request(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if g.user:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('auth.login'))
    return inner
from flask import Flask,request,render_template
from datetime import datetime

# 模板代码
app = Flask(__name__)

# 模板获取类或者字典的属性
class User:
    def __init__(self,name):
        self.name = name


data = {
    "age": 12
}


# 自定义过滤器
def date_format(value):
    return datetime.strftime(value,"%Y-%m-%d %H:%M")

app.add_template_filter(date_format,"dformat")
# 路由
# "/" 代表的是跟路由
@app.route("/")
def hello_world():
    # return "hello world"
    user = User("zhangsan")
    d_time = datetime.now()
    return render_template("index.html",user=user,data=data,d_time=d_time)


# 自定义一个路由
@app.route("/profile")
def profile():
    return("个人中心")

# 测试模板继承
@app.route("/temp")
def temp():
    return render_template("body.html")


# 测试加载静态文件
@app.route("/static")
def static_demo():
    return render_template("static.html")

# if 和 for 渲染
@app.route("/show")
def show():
    # 准备数据用于if判断和for循环
    age = 17
    datas = [
        {"name": "zhangsan","sex": "male"},
        {"name": "lisi","sex": "female"}
    ]

    return render_template("show.html",age=age,datas=datas)
# 路由传参
# 不支持限制参数为str
@app.route("/blog/<name>")
def blog(name):
    # return f"你访问的是{name}的博客"
    # render_template支持传递多个参数
    return render_template("blog_detail.html",username = name)

# 解析url中的参数
# 例如 blog/info?page=2 访问第二页数据，但是page2可选
@app.route("/blog/info")
def blog_info():
    # 还可以指定参数类型
    page = request.args.get("page",default=1)
    return "你访问的是第{}页的数据".format(page)


# 模板渲染 jinja2 render_template

if __name__ == "__main__":
    # 开启Debug 模式 
    # 默认不开启
    app.run(host="192.168.0.103",port=5001,debug=True)
    

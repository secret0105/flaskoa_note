#### flask 笔记

##### 版本

python 3.6以上

flask2.2

##### 项目基本目录结构

project

    static---静态资源目录

    templates---html 模板渲染文件

    app.py---主程序

##### 路由

##### 模板继承

##### 加载静态文件

使用 `url_for` 方法

```
{{ url_for('static',filename='images/a.webp') }}
```

##### 连接mysql

安装pymysql

`pip3 install pymysql`

安装flask-SQLAlchemy,不用写原生Sql语句

`pip3 install flask-sqlalchemy`

##### ORM 对象关系映射

通过对象来创建表

String 类型最多只支持255个字符

##### 增删改查

更新，删除，新增都要用到session.commit()

##### 外键

双向绑定，flask自动生成外键名

back_populates 和 backref 的区别

back_populates：需要双表中都创建对应属性

backref:自动绑定，适合类少的情景

##### 模型修改映射

flask-migrate 插件

前提：pip3 安装该插件

操作时需要使用命令行

```
flask db init
flask db migrate # 生成迁移脚本
flask db upgrade # 运行脚本，同步到数据库
```

在第二次使用时，修改类属性后，只用执行后面两条命令即可

##### 实战

模块化(对象，数据库，配置)

蓝图  渲染视图  blueprint


##### 邮箱配置

安装三方库 flask-mail  注意是mail 不是email


##### jquery ajax

完成点击发送邮件后，按钮置灰且倒计时的功能

向后端发送请求


##### 后端表单数据验证

安装三方库 flask-wtf email-validator


##### 钩子函数

before_request

全局对象g  存储session中的user 对象

context_processor 声明全局对象

用来处理登录后的渲染


##### migrate 操作报错

原因是后台修改了数据库格式，但是前端没有同步

解决办法

flask db stamp heads


##### 权限控制

登录后才能访问发布问答页面

装饰器


##### 搜索功能

条件查询

待改进

分页

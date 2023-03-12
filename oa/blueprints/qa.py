from flask import Blueprint,redirect,url_for,render_template,request,g
from .forms import QuestionForm,AnswerForm
from models import QuestionModel,AnswerModel
from exts import db

# 注意windows下的引用
from decorators import login_request

# 问答页面即是首页，直接访问url根路径
bp = Blueprint('qa',__name__,url_prefix="/")



@bp.route("/")
def index():
    """首页，显示所有内容"""
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template("index.html",questions=questions)




@bp.route("/qa/public",methods=["GET","POST"])
@login_request
def public_question():
    """发布问答"""
    if request.method == "GET":
        return render_template("question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            qs = QuestionModel(title=title,content=content,auth=g.user)
            db.session.add(qs)
            db.session.commit()
            return redirect(url_for('qa.index'))
        else:
            print(form.errors)
            return redirect(url_for('qa.public_question'))


@bp.route("/qa/detail/<qa_id>")
def detail(qa_id):
    """详情页，不需要登录就能访问"""
    question = QuestionModel.query.get(qa_id)
    return render_template("detail.html",question=question)


@bp.route("/answer/public",methods=["POST"])
@login_request
def answer():
    """评论"""
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content=content,question_id=question_id,auth_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        # 注意详情页接收的是qa_id
        return redirect(url_for('qa.detail',qa_id=question_id))
    else:
        print(form.errors)
        return redirect(url_for('qa.detail',qa_id=request.form.get('question_id')))


@bp.route("/search")
def search():
    keyword = request.args.get('keyword')
    print(keyword)
    questions = QuestionModel.query.filter(QuestionModel.title.contains(keyword)).all()
    print(questions)
    return render_template("index.html",questions=questions)
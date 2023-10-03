from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from app.forms import QuestionForm, Question_sec_Form
import app.cookpt as cpt
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/main')
def main():
    return render_template('main.html')

@bp.route('/first', methods=('GET', 'POST'))
def first():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        content=form.content.data
        action = request.form['action']  # action 필드의 값을 가져옴
        answer = ''
        if action == 'all':
            answer = cpt.calling_cookpt('당신은 요리사 입니다. 가지고 있는 재료만 알면 어떤 요리가 가능한지 알고 있습니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.','','재료는 %s가 있고, 이 재료를 가지고 만들 수 있는 요리를 알고 싶어요.' %content)
        elif action == 'kor':
            answer = cpt.calling_cookpt('당신은 요리사 입니다. 가지고 있는 재료만 알면 어떤 요리가 가능한지 알고 있습니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.','','재료는 %s가 있고, 이 재료를 가지고 만들 수 있는 한식 요리를 알고 싶어요.' %content)
        elif action == 'chn':
            answer = cpt.calling_cookpt('당신은 요리사 입니다. 가지고 있는 재료만 알면 어떤 요리가 가능한지 알고 있습니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.','','재료는 %s가 있고, 이 재료를 가지고 만들 수 있는 중식 요리를 알고 싶어요.' %content)
        elif action == 'jpn':
            answer = cpt.calling_cookpt('당신은 요리사 입니다. 가지고 있는 재료만 알면 어떤 요리가 가능한지 알고 있습니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.','','재료는 %s가 있고, 이 재료를 가지고 만들 수 있는 일식 요리를 알고 싶어요.' %content)
        elif action == 'sea':
            answer = cpt.calling_cookpt('당신은 요리사 입니다. 가지고 있는 재료만 알면 어떤 요리가 가능한지 알고 있습니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.','','재료는 %s가 있고, 이 재료를 가지고 만들 수 있는 동남아시아 요리를 알고 싶어요.' %content)
        elif action == 'fra':
            answer = cpt.calling_cookpt('당신은 요리사 입니다. 가지고 있는 재료만 알면 어떤 요리가 가능한지 알고 있습니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.','','재료는 %s가 있고, 이 재료를 가지고 만들 수 있는 프랑스 요리를 알고 싶어요.' %content)
        elif action == 'ita':
            answer = cpt.calling_cookpt('당신은 요리사 입니다. 가지고 있는 재료만 알면 어떤 요리가 가능한지 알고 있습니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.','','재료는 %s가 있고, 이 재료를 가지고 만들 수 있는 이탈리아 요리를 알고 싶어요.' %content)
        # return render_template("first.html", form=form, action=action, content=content, answer=answer)
        return render_template("chat.html", action=action, content=content, answer=answer)
    else:
        return render_template("first.html", form=form)




@bp.route('/second', methods=('GET', 'POST'))
def second():
    form = Question_sec_Form()
    if request.method == 'POST' and form.validate_on_submit():
        target=form.target.data
        content=form.content.data
        action = request.form['action']  # action 필드의 값을 가져옴
        answer = ''
        question = '만들고자 하는 요리는 ' + target + '입니다. 지금 가지고 있는 요리재료는 ' + content + '이며, 어떤 재료가 부족한지, 뭐가 더 있으면 좋은지 알려주세요.'
        answer = cpt.calling_cookpt('당신은 요리사 입니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.','', question)
        return render_template("chat.html", answer=answer)
    else:
        return render_template("second.html", form=form)



@bp.route('/third', methods=('GET', 'POST'))
def third():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        content=form.content.data
        answer = ''
        answer = cpt.calling_cookpt('당신은 요리사 입니다. 요청받은 요리의 필요한 재료와 함께 조리방법을 간단하게 알려줍니다.','','%s 를 만들고 싶은데, 어떤 재료가 필요하고 어떤 순서로 조리해야 하나요?' %content)
        return render_template("chat.html", content=content, answer=answer)
    else:
        return render_template('third.html', form=form)

@bp.route('/who')
def who():
    return render_template('who.html')
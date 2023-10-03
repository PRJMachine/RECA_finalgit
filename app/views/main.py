from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect


from app.forms import QuestionForm
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
        subject=form.subject.data
        content=form.content.data
        return render_template("first.html", form=form, subject=subject, content=content)
    else:
        return render_template("first.html", form=form)
     
@bp.route('/second')
def second():
    return render_template('second.html')

@bp.route('/third')
def third():
    return render_template('third.html')

@bp.route('/who')
def who():
    return render_template('who.html')
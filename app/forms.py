from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    # subject = StringField('제목', validators=[DataRequired()])
    #요리재료 입력하는 칸. main.py - first.html 에서 이용할 계획
    content = TextAreaField('내용', validators=[DataRequired('먼저 요리재료를 입력해 주세요.')])

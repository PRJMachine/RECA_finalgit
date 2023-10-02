from flask import Blueprint, render_template

#from app.models import reserve

bp = Blueprint('input', __name__, url_prefix='/input')


@bp.route('/')
#def order():
#   return 'customer!'

def index():
    #order_by는 함수
    #item_list = reserve.query.order_by(reserve.item_id.asc())
    #render_template함수 템플릿 화면을 렌더링 
    #item list를 render_template함수의 파라미터로 전달, order_list.html에 구성
    return render_template('./input.html')
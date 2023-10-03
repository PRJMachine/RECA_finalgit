from flask import Blueprint, render_template, request, jsonify
import app.cookpt as cpt

bp = Blueprint('chat', __name__, url_prefix='/chat')


@bp.route('/')
def main():
    return render_template('chat.html')

@bp.route('/messege', methods=['POST'])
def messege():
    data = request.get_json()  # 클라이언트에서 전송한 JSON 데이터 가져오기
    user_messages = data.get('userMessages', [])  # 사용자 메시지 추출
    assi_messages = data.get('assistantMessages', [])
    # assi_messages = data.get('assistantMessages', [])
    # 여기에서 사용자 메시지를 기반으로 작업을 수행하고 응답을 생성합니다.
    # response = {'assistant': 'Hello, Flask! Your messages: ' + ', '.join(user_messages)}
    response = {'assistant': cpt.calling_cookpt('당신은 최고의 요리사로써, 요리 분야 외의 질문은 단호하게 거절합니다. 대답은 간결하게, 필요한 내용만 대답합니다.',assi_messages[-1], user_messages[-1]) }

    return jsonify(response)  # JSON 형식의 응답 반환
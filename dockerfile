FROM python:3.8.16
WORKDIR /app 
COPY . /app
RUN pip3 install Flask
RUN cd /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP app
# 플라스크 애플리케이션을 환경변수로 지정합니다
ENTRYPOINT flask run --host 0.0.0.0

# RUN pip3 install gunicorn
# CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
# ENTRYPOINT gunicorn -b 0.0.0.0:5000 main:app
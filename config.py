import os

BASE_DIR = os.path.dirname(__file__)
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector:///prj4:VMware1!@10.0.0.199:3306/pybo' #뭔가 안됨. mysql사용 시
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:VMware1!@test.czh0sssi32uy.ap-northeast-2.rds.amazonaws.com:3306/pybo" #됨
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://prj4:VMware1!@175.196.82.14:60306/pybo" #됨(온프렘 마스터db에 직결)
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://mha:mha@175.196.82.14:40306/pybo" #됨(온프렘 vIP에 연결)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "devdev231016"

#인잇, 마이그레이션 하지말고 그냥 직접 만든 뒤 연결해서 쓰자
# CREATE DATABASE pybo;
# USE pybo;
# CREATE TABLE `user` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `username` varchar(150) NOT NULL,
#   `password` varchar(200) NOT NULL,
#   `email` varchar(120) NOT NULL,
#   PRIMARY KEY (`id`),
#   UNIQUE KEY `email` (`email`),
#   UNIQUE KEY `username` (`username`)
# ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4
import os

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector:///prj4:VMware1!@10.0.0.199:3306/pybo' #mysql사용 시
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://admin:VMware1!@test.czh0sssi32uy.ap-northeast-2.rds.amazonaws.com:3306/pybo' #mysql-aws rds사용 시
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:VMware1!@test.czh0sssi32uy.ap-northeast-2.rds.amazonaws.com:3306/pybo"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "devdevdev"

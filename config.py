
SECRET_KEY= "ADASDQWEWQEASDASDADW"


HOSTANAME="127.0.0.1"

PORT= '3306'

USERNAME="root"

PASSWORD="hong13516164136"

DATABASE="dmproject"



DB_URI='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTANAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI=DB_URI
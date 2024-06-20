import os

basedir = os.path.abspath(os.path.dirname(__file__))
base_de_datos = os.path.join(basedir,'datos.sqlite3')

SQLALCHEMY_DATABASE_URI = f'sqlite:///{base_de_datos}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "GDtfDCFYjD"
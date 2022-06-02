import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "dartsplus"
    ALCHEMICAL_DATABASE_URL = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    ALCHEMICAL_ENGINE_OPTIONS = {'echo': bool(os.environ.get('SQL_ECHO'))}
    DISABLE_AUTH = bool(os.environ.get('DISABLE_AUTH'))
    ACCESS_TOKEN_EXPIRATION = int(os.environ.get(
        'ACCESS_TOKEN_EXPIRATION', '60')) * 60  # 1 hour
    REFRESH_TOKEN_EXPIRATION = int(os.environ.get(
        'REFRESH_TOKEN_EXPIRATION', '1440')) * 60  # 24 hours
    RESET_TOKEN_EXPIRATION = int(os.environ.get(
        'RESET_TOKEN_EXPIRATION', '15')) * 60  # 15 minutes
    APIFAIRY_TITLE = 'DartsPlus API'
    APIFAIRY_VERSION = '0.1'
    APIFAIRY_UI = os.environ.get('DOCS_UI', 'elements')

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    Testing = False
    CSRF_ENABLED = True
    SECRET_KEY = 'THIS_KEY_SHOULD_BE_GENERATED_AND_UNIQUE'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    Testing = True


class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = 'any powerful key'
    DB_NAME = 'production.db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'admin'

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = 'development.db'

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True
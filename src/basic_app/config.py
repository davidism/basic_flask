
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # disable warning
    _POSTGRES = {
        'user': 'flask',
        'pw': '3CJuVaT7rRo75zGB3qmN6xzg3q9aM3G6SGWhPFXDWPRjskXcckD8HSQWG7v9wVfD',
        'db': 'flask',
        'host': 'postgres',
        'port': '5432',
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' %  _POSTGRES


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

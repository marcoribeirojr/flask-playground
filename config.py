# _*_ coding: utf-8 _*_

from os import getenv

class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    APP_PORT = getenv('APP_PORT')
    DEBUG = eval(getenv('DEBUG').title())

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

config = {
        'development' : DevelopmentConfig,
        'default' : DevelopmentConfig
}

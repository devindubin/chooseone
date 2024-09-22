import os
#Import .env file reader
from dotenv import load_dotenv

base_directory = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_directory,'.env'))

class Config:
    """Base configuration class to be inherited by more specific application case"""
    SECRET_KEY = os.environ.get("SECRET_KEY")
    #Using sessions instead of cookies
    #TODO: Research why on the above ^
    # SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME")
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class ProductionConfig(Config):
    """Defines configuration for production level application. Inherits from base config class."""
    FLASK_ENV = 'production'
    DEBUG = False 
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')

class DevelopmentConfig(Config):
    """Defines configuration for development level application. Inherits from base config class."""
    FLASK_ENV = 'development'
    DEBUG = True #Adds helpful debugging stuff 
    TESTING = True #Ensures exceptions are propagated rather than handled by the apps error handlers, which is useful when running automated tests
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
    TEMPLATES_AUTO_RELOAD = True


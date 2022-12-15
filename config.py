import os


class Config:
    SECRET_KEY: str = os.environ.get('SECRET_KEY', 'randomkey@12343434*^&$')
    TEMP = 'adithya'


class Production(Config):
    DEBUG: bool = False
    ENVIRONMENT: str = 'Production'


class Development(Config):
    DEBUG: bool = True
    ENVIRONMENT: str = 'Development'

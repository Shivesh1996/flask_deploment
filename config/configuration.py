class Config():
    ENV_NAME = "Default"
    
class DevConfig(Config):
    ENV_NAME = "Dev"
    DEBUG = True
    HOST = "127.0.0.1"
    PORT = 5000
    
class QAConfig(Config):
    ENV_NAME = "QA"
    DEBUG = False
    HOST = "0.0.0.0"
    PORT = 5001
    
class ProdConfig(Config):
    ENV_NAME = "Prod"
    DEBUG = False
    HOST = "0.0.0.0"
    PORT = 8000
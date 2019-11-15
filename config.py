import os

class Config:
  '''
  General class with general configurations
  '''
  NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
  '''
  Production configuration child class
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration chilf class
  '''
  DEBUG= True

config_option= {
  'development':DevConfig,
  'production':ProdConfig
}  
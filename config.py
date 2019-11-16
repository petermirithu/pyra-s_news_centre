import os

class Config:
  '''
  General class with general configurations
  '''
  BASE_HOME_URL='https://newsapi.org/v2/sources?apiKey={}'

  NEWS_ARTCLE_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'

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
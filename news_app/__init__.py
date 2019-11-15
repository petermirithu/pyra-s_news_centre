from flask import Flask
# from flask_bootstrap import Bootstrap
from config import config_option

# bootstrap=Bootstrap()

def create_app(config_name):
  '''
  function that can be launched from script takes in a configuration setting key an argument  
  '''
  newsApp=Flask(__name__):

  newsApp.configfrom_object(config_option[config_name])

  bootstrap.init_news(newsApp)

  from .lead import lead as lead_blueprint
  newsApp.register_blueprint(lead_blueprint)

  return newsApp



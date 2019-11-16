from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_option

bootstrap=Bootstrap()

def create_app(config_name):
  '''
  function that can be launched from script takes in a configuration setting key an argument  
  '''
  newsApp=Flask(__name__)

  newsApp.config.from_object(config_option[config_name])

  bootstrap.init_app(newsApp)

#register blueprint
  from .lead import crucial as lead_blueprint
  newsApp.register_blueprint(lead_blueprint)

#set config function from request
  from .request import configure_request
  configure_request(newsApp)

  return newsApp



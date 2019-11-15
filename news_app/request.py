import urllib.request,json
from models import source_class

Source=source_class.Source

api_key=None
base_url=None

def configure_request(newsApp):
  global api_key,base_url

  api_key=newsApp.config['NEWS_API_KEY']
  base_url=newsApp.config['BASE_HOME_URL']

def get_sources():
  '''
  function that gets a response from the url which sources
  '''





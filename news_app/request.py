import urllib.request,json
from news_app.models import source_class

Source=source_class.Source

api_key=None
base_url=None

def configure_request(newsApp):
  global api_key,base_url,news_article_url

  api_key=newsApp.config["NEWS_API_KEY"]
  base_url=newsApp.config["BASE_HOME_URL"]
  news_article_url=newsApp.config["NEWS_ARTCLE_URL"]

def get_sources():
  '''
  function that gets a response from the url which sources
  '''
  source_url=base_url.format(api_key)

  with urllib.request.urlopen(source_url) as url:
    source_data=url.read()
    source_response=json.loads(source_data)

    source_results=None

    if source_response['sources']:
      source_result_list=source_response['sources']
      source_results=process_results(source_result_list)

  return source_results   

def process_results(source_list):
  '''
  function that processes the source results to list of objects
  '''
  source_results=[]
  for source_x in source_list:
    id=source_x.get('id')
    name=source_x.get('name')
    language=source_x.get('language')
    country=source_x.get('country')

    source_object=Source(id,name,language,country)
    source_results.append(source_object)

  return source_results  

def get_news_article(id):
  get_news_article=news_article_url.format(id,api_key)

  with urllib.request.urlopen(get_news_article) as url:
    source_details=url.read()
    article_response=json.loads(source_details)

    source_object=None
    if








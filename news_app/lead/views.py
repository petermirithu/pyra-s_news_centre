from flask import render_template,request,redirect,url_for
from . import crucial
from ..request import get_sources,get_news_article


@crucial.route('/')
def index():
  '''
  view root page function that loads the home page
  '''
  title='News_Centre'

  sources_res=get_sources()

  return render_template("index.html",title=title,sources=sources_res)

@crucial.route('/articles/<id>')
def articles(id):
  '''
  view function that returns news articles for a specific source
  '''
  
  source_articles=get_news_article(id)
  title='Articles_Centre'

  return render_template('articles.html',title=title,source_articles=source_articles,id=id)

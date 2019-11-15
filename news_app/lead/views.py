from flask import render_template,request,redirect,url_for
from . import crucial
from ..request import get_sources


@crucial.route('/')
def index():
  '''
  view root page function that loads the home page
  '''
  title='News_Centre'

  sources=get_sources()

  return render_template("index.html",title=title,sources=sources)

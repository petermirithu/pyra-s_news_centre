from flask import render_template,request,redirect,url_for
from . import crucial

@crucial.route('/')
def index():
  '''
  view root page function that loads the home page
  '''
  title='News_Centre'

  return render_template("index.html",title=title)

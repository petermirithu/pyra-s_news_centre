class Article:
  '''
  class that defines how articles from a source.
  '''
  def __init__(self,id,name,title,description,url,urlToImage,publishedAt):
    self.id=id
    self.name=name
    self.title=title
    self.description=description
    self.url=url
    self.urlToImage=urlToImage
    self.publishedAt=publishedAt


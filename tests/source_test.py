import unittest
from models import source_class
from models import article_class

Article=article_class.Article

Source=source_class.Source



class sourceTest(unittest.TestCase):
  '''
  class to test behaviour pf the source objects and instances
  '''
  def setUp(self):
    '''
    function to set up a source object before every test
    '''
    self.new_source=Source(55,"BBC","en","us")
    self.new_article=Article(55,"BBC","Cars","BMW released their G-class car to pyra","https://www.BMW.com","https:www.BMW.com/wecc/3fcx/wsx.jpg","23-Jan-2019")

# test for source class--------------------------------------------------------
  def test_instance_for_source(self):
    '''
    test case to test if the object is instanciated correctly
    '''
    self.assertTrue(isinstance(self.new_source,Source))  

# test for article class-------------------------------------------------------
  def test_instance_for_article(self):
    '''
    test case to test if article objects take the respective format.instances fro class Article
    '''
    self.assertTrue(isinstance(self.new_article,Article))

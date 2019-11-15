import unittest
from models import source_class

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

  def test_instance(self):
    '''
    test case to test if the object is instanciated correctly
    '''
    self.assertTrue(isinstance(self.new_source,Source))  

if __name__== '__main__':
  unittest.main()
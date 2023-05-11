import unittest
from bee import Bee


class TestBee(unittest.TestCase):
   
   def setUp(self):
      self.bee = Bee
      
   def test_move(self, x,y):
      self.right = True
      maara = x
      self.assertEqual(maara, 2)
      
     
      
         


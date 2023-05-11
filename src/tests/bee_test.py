import pygame
import unittest
from bee import Bee
from events import Events


class TestBee(unittest.TestCase):

   def setUp(self):
      self.bee = Bee()

   def test_move_right(self):
      self.bee.right = True
      self.bee.liiku()
      maara = self.bee.x
      self.assertEqual(maara, 2)

   def test_move_left(self):
      self.bee.left = True
      self.bee.liiku()
      maara = self.bee.x
      self.assertEqual(maara, -2)

   def test_move_up(self):
      self.bee.up = True
      self.bee.liiku()
      maara = self.bee.y
      self.assertEqual(maara, 403)

   def test_move_down(self):
      self.bee.down = True
      self.bee.liiku()
      maara = self.bee.y
      self.assertEqual(maara, 407)


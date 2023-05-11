import pygame
import unittest
from events import Events


class TestEvents(unittest.TestCase):

    def setUp(self):
      self.event = Events()

    def gamePassed(self):
        self.event.go = True
        self.event.game_passed = True
        pisteet = self.event.points
        self.assertEqual(pisteet, 20)

import pygame
import unittest
from events import Events
from bee import Bee
from keys import Keys


class TestEvents(unittest.TestCase):

    def setUp(self):
        self.event = Events(Bee, Keys)

    def test_gamePassed(self):
        self.event.go = True
        self.event.points = 20
        value = self.event.game_passed()

        self.assertTrue(value)
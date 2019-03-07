"""
Created on 7 mars 2019
@author : Denis
"""

import unittest
from MVC.controller.go_to_goal import GoToGoalControlleur
from MVC.controlleur.move_forward import MoveForwardControlleur
from MVC.controller.stop import StopControlleur
from MVC.controlleur.turn_90 import Turn90Controlleur
from MVC.controlleur.strategie import Strategie
from MVC.model.superviseur import Superviseur
from MVC.model.robotsim import Robotsim

superviseur = Superviseur(Robotsim(100,100,"test","black"))
superviseur.goal = [0,0]

class TestGoToGoal(unittest.TestCase):

    def setUp(self):
        self.gotogoal = GoToGoalControlleur(superviseur)

    def test

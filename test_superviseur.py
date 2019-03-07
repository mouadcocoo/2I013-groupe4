import unittest
from MVC.model.superviseur import Superviseur
from MVC.model.abstract_robot import Robot
from MVC.controller.strategie import Strategie
from MVC.model.objectif import Objectif


class testSuperviseur(unittest.TestCase):

	def setUp(self):
		self.R = Robot(450,450)
		self.superviseur = Superviseur (R)
	
	def testInit(self):
		self.assertIs(self.superviseur.robot,self.R)
		self.assertIsNone(self.superviseur.goal)
		self.assertIsInstance(self.superviseur.strategie,Strategie)

	#def step

	def testTranslateCommand(self):
		self.superviseur.v = 2
		self.superviseur.omega = 10 
		self.assertEqual(self.superviseur.robot.vdroite,31.25)
		self.assertEqual(self.superviseur.robot.vgauche,18.75)

	def testCalculDps(self):
		self.assertTupleEqual(self.superviseur.calcul_dps(2,10),(31.25,18.75))
		
	def testDefineGoal(self):
		G1 = Objectif(600,600)
		self.assertIs(self.superviseur.define_goal(G1),self.superviseur.goal)


if __name__ =='__main__':
    unittest.main()

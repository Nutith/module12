import unittest
from t1 import RunnerTest
from t2 import TournamentTest


ts = unittest.TestSuite()
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(ts)

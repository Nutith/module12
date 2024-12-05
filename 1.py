from HumanMoveTest.runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner('slow run')

        for _ in range(10):
            walker.walk()

        self.assertEqual(walker.distance, 50)

    def test_run(self):
        walker = Runner('fast run')

        for _ in range(10):
            walker.run()

        self.assertEqual(walker.distance, 100)

    def test_challenge(self):
        slow_walker = Runner('turtle speed')
        fast_walker = Runner('light speed')

        for _ in range(10):
            # slow_walker.walk()
            slow_walker.run()  # портим тест
            fast_walker.run()

        self.assertNotEqual(slow_walker.distance, fast_walker.distance)


if __name__ == '__main__':
    unittest.main()

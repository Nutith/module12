from HumanMoveTest.runner import Runner
import unittest


def skip_frozen(func):
    def wrapper(*args):
        if args[0].is_frozen:
            return unittest.skip(reason='Тесты в этом кейсе заморожены')(func)(*args)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_frozen
    def test_walk(self):
        walker = Runner('slow run')

        for _ in range(10):
            walker.walk()

        self.assertEqual(walker.distance, 50)

    @skip_frozen
    def test_run(self):
        walker = Runner('fast run')

        for _ in range(10):
            walker.run()

        self.assertEqual(walker.distance, 100)

    @skip_frozen
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

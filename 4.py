from HumanMoveTest.rt_with_exceptions import Runner
import unittest
import logging


class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO,
                            filemode='w',
                            filename='runner_tests.log',
                            encoding='utf-8',
                            format='%(asctime)s %(levelname)s %(message)s')

    def test_walk(self):
        try:
            walker = Runner('slow run', -1)
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner. {e}')
        else:
            for _ in range(10):
                walker.walk()

            logging.info('"test_walk" выполнен успешно')

            self.assertEqual(walker.distance, 50)

    def test_run(self):
        try:
            walker = Runner(9876)
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner. {e}')
        else:
            for _ in range(10):
                walker.run()

            logging.info('"test_run" выполнен успешно')

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

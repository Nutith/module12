import unittest
from HumanMoveTest.runner_and_tournament import Runner, Tournament
from t1 import skip_frozen


class MyRunner(Runner):
    def __repr__(self):
        return self.name


class MyTournament(Tournament):
    def start(self):
        finishers = []
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers.append((self.full_distance / participant.distance + self.full_distance / participant.speed, participant))
                    self.participants.remove(participant)

        order_of_finish = sorted(finishers)
        result = {}

        for i in order_of_finish:
            result[place] = i[1]
            place += 1

        return result


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usain = MyRunner('Усэйн', 10)
        self.andrey = MyRunner('Андрей', 9)
        self.nick = MyRunner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

    @skip_frozen
    def test_tnmt1(self):
        tnmt = Tournament(90, self.usain, self.nick)
        result = tnmt.start()
        self.all_results.append(result)

        self.assertTrue(result[max([x for x in result.keys() if isinstance(x, int)])] is self.nick)

    @skip_frozen
    def test_tnmt2(self):
        tnmt = Tournament(90, self.andrey, self.nick)
        result = tnmt.start()
        self.all_results.append(result)

        self.assertTrue(result[max([x for x in result.keys() if isinstance(x, int)])] is self.nick)

    @skip_frozen
    def test_tnmt3(self):
        tnmt = Tournament(90, self.usain, self.andrey, self.nick)
        result = tnmt.start()
        result['comment'] = 'Как в условии'
        self.all_results.append(result)

        self.assertTrue(result[max([x for x in result.keys() if isinstance(x, int)])] is self.nick)

    @skip_frozen
    def test_tnmt4(self):
        tnmt = Tournament(90, self.andrey, self.usain, self.nick)
        result = tnmt.start()
        result['comment'] = 'Эксплуатируем баг в логике метода start, меняем бегунов местами, итог ложноположительный'
        self.all_results.append(result)

        self.assertTrue(result[max([x for x in result.keys() if isinstance(x, int)])] is self.nick)

    @skip_frozen
    def test_tnmt5(self):
        tnmt = Tournament(90, self.andrey, self.usain, self.nick)
        result = tnmt.start()
        result['comment'] = 'Эксплуатируем баг в логике метода start, меняем бегунов местами, меняем проверку, тест не пройден'
        self.all_results.append(result)

        self.assertTrue(result[min([x for x in result.keys() if isinstance(x, int)])] is self.usain)

    @skip_frozen
    def test_tnmt6(self):
        tnmt = MyTournament(90, self.andrey, self.usain, self.nick)
        result = tnmt.start()
        result['comment'] = 'перегружаем метод старт, итог не зависит от порядка бегунов'
        self.all_results.append(result)

        self.assertTrue(result[min([x for x in result.keys() if isinstance(x, int)])] is self.usain)


if __name__ == '__main__':
    unittest.main()

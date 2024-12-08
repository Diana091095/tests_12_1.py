from unittest import TestCase#import  unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5
       # return self.distance

    def __str__(self):
        return self.name

# ru = Runner('ncj')
# print(ru.walk())

class RunnerTest(TestCase):
    def test_walk(self):
        runner_1 = Runner('Walya')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = Runner('Rustam')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = Runner('Wikram')
        runner_4 = Runner('Zoya')
        for i in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)



runner_test = RunnerTest()
print(runner_test)





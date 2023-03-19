import unittest
from src.Repository.RepoTextFile import RepoTextFile


class RepoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo_test = RepoTextFile("C:/Users/stanbydrew/Desktop/University/1st year SEM.1/FPREPOS/MyHangman/testing.txt")

    def test_read_from_file(self):
        self.__repo_test.read_from_file()
        self.assertEqual(self.__repo_test.get_entity(0).strip(), "testing test")
        self.assertEqual(self.__repo_test.get_entity(1).strip(), "the tasty test")

if __name__ == '__main__':
    unittest.main()

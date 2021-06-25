from unittest.mock import patch
import unittest
from codeup.memorizeTest import memorizeTest

class memorizeTestTest(unittest.TestCase):

    def test_memorizeTest(self):
        userInput1 =[
            "3 4",
            "ddobot 3",
            "poketmon 5",
            "ddobot 7",
            "ddobot",
            "poketmon",
            "ddobot",
            "hellocarbot"
        ]
        procScores = [
            "10",
            "5",
            "10",
            "0"
        ]

        with patch("builtins.input",side_effect=userInput1):
            rslt = memorizeTest(userInput1)

        self.assertEqual(rslt,procScores)

if __name__ == '__main__':
    unittest.main()
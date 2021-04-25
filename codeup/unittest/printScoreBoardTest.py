from unittest.mock import patch
import unittest
from codeup.printScoreBoard import procInputs

class PrintScoreBoardTest(unittest.TestCase):

    def test_procInputs(self):
        userInput1 =[
            "Jeon 95",
            "Kim 59",
            "Lee 90",
            "Bae 100"
        ]
        procScores = [['Jeon', 95], ['Kim', 59], ['Lee', 90], ['Bae', 100]]

        with patch("builtins.input",side_effect=userInput1):
            rslt = procInputs("4 2")

        self.assertEqual(rslt.lineAmount,4)
        self.assertEqual(rslt.printAmount,2)
        self.assertEqual(rslt.scores,procScores)

if __name__ == '__main__':
    unittest.main()
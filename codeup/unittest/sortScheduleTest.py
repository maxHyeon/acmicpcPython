import unittest
from unittest.mock import patch
from codeup.sortSchedule import multiLineInputProc
from codeup.sortSchedule import procInputs
from codeup.sortSchedule import splitData
from codeup.sortSchedule import strToDate
import datetime

class PrintScoreBoardTest(unittest.TestCase):
    def test_multiLineInputProc(self):
        userInput1 = ["sleep 2014 05 23",
                      "golf 2014 06 02",
                      "travel 2015 11 22",
                      "baseball 2013 02 01",
                      "study 2014 05 23"]
        with patch("builtins.input", side_effect=userInput1):
            rslt = multiLineInputProc("5")
        self.assertEqual(rslt,userInput1)

    def test_procInputs(self):
        userInput1 = ["sleep 2014 05 23",
                      "golf 2014 06 02",
                      "travel 2015 11 22",
                      "baseball 2013 02 01",
                      "study 2014 05 23"]
        expect1 = [["sleep", "2014 05 23"],
                   ["golf", "2014 06 02"],
                   ["travel", "2015 11 22"],
                   ["baseball", "2013 02 01"],
                   ["study", "2014 05 23"]]
        with patch("builtins.input", side_effect=userInput1):
            rslt = procInputs(userInput1)
        self.assertEqual(rslt,expect1)
    def test_splitData(self):
        rawData1 = "sleep 2014 05 23"
        expect1 = ["sleep","2014 05 23"]
        index = 1
        with patch("builtins.input",side_effect=rawData1):
            rslt = splitData(rawData1,index)
        self.assertEqual(rslt,expect1)
    def test_strToDate(self):
        rawData1 = "2019 01 01"
        expect1 = datetime.datetime.strptime("2019-01-01","%Y-%m-%d")
        with patch("builtins.input",side_effect=rawData1):
            rslt = strToDate(rawData1)
        self.assertEqual(rslt,expect1)
if __name__ == '__main__':
    unittest.main()
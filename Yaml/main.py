import pytest
import os

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './allure-results',
                 os.os.path.dirname(os.path.abspath(__file__)) + "/Yaml/Test_001_01.py"])

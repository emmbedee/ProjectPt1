import pytest
from grade import *


class Test:
    def test_determine_grade(self):
        assert determine_grade(90) == 'A'
        assert determine_grade(80) == 'B'
        assert determine_grade(70) == 'C'
        assert determine_grade(60) == 'D'
        assert determine_grade(59) == 'F'

    def test_check_name(self):
        assert check_name('Amy') == 'Amy'
        assert check_name('amy') == 'amy'
        assert check_name('               Amy') == 'Amy'
        assert check_name('Amy!') is False
        assert check_name('[@_!#$%^&*()<>?/\|}{~:]') is False
        assert check_name('1') is False

        with pytest.raises(AttributeError):
            check_name(0)
            check_name(float(0))

    def test_check_score(self):
        assert check_score('1') == 1
        assert check_score('                          1          ') == 1
        assert check_score('-15') is False
        assert check_score('101') is False
        assert check_score('Test') is False

        with pytest.raises(AttributeError):
            check_score(0)
            check_score(float(0))

from unittest import mock
import pytest
from grade import *


class Test:
    def test_determine_grade(self):
        assert determine_grade(90) == 'A'
        assert determine_grade(80) == 'B'
        assert determine_grade(70) == 'C'
        assert determine_grade(60) == 'D'
        assert determine_grade(59) == 'F'
        with pytest.raises(TypeError):
            determine_grade('Hello')
            determine_grade('###$$##$')
            determine_grade(str(0))
        with pytest.raises(ValueError):
            determine_grade(-1)
            determine_grade(101)

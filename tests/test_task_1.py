import pytest

from passport_processor import PassportProcessor
from task_1 import number_valid_passports


def test_number_valid_passports():
    assert number_valid_passports() == 256

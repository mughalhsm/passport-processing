import pytest
import pandas as pd


from passport_processor import PassportProcessor

@pytest.fixture
def passport_processor():
    return PassportProcessor('input.txt')


def test_process_passports_returns_dataframe(passport_processor):
    df = passport_processor.process_passports()
    assert isinstance(df, pd.DataFrame)


def test_process_passports_returns_correct_number_of_rows(passport_processor):
    df = passport_processor.create_dataframe()
    assert len(df) == 285

def test_process_passports_returns_correct_columns(passport_processor):
    df = passport_processor.create_dataframe()
    expected_columns = ['eyr', 'iyr', 'byr', 'ecl', 'pid', 'hcl', 'hgt', 'cid']
    assert all(col in df.columns for col in expected_columns)



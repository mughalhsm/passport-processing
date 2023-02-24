import unittest.mock as mock

import pandas as pd
import pytest

from passport_processor import PassportProcessor


@pytest.fixture
def test_input_file(tmp_path):
    test_data = (
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n"
        "byr:1937 iyr:2017 cid:147 hgt:183cm\n\n"
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n"
        "hcl:#cfa07d byr:1929\n"
    )

    test_file = tmp_path / "test_input_file.txt"
    with test_file.open("w") as f:
        f.write(test_data)
    yield test_file
    test_file.unlink()


def test_passport_processor_init(test_input_file):
    pp = PassportProcessor(test_input_file)
    assert pp.passport_str == test_input_file.read_text()


def test_create_dataframe_using_mocking(monkeypatch):
    # Arrange
    test_data = (
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n"
        "byr:1937 iyr:2017 cid:147 hgt:183cm\n\n"
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n"
        "hcl:#cfa07d byr:1929\n"
    )

    # Act
    monkeypatch.setattr("builtins.open", mock.mock_open(read_data=test_data))
    pp = PassportProcessor("test_input_file.txt")
    df = pp.create_dataframe()
    expected_df = pd.DataFrame(
        [
            {
                "ecl": "gry",
                "pid": "860033327",
                "eyr": "2020",
                "hcl": "#fffffd",
                "byr": "1937",
                "iyr": "2017",
                "cid": "147",
                "hgt": "183cm",
            },
            {
                "ecl": "amb",
                "pid": "028048884",
                "eyr": "2023",
                "hcl": "#cfa07d",
                "byr": "1929",
                "iyr": "2013",
                "cid": "350",
                "hgt": None,
            },
        ]
    )

    # Assert
    assert isinstance(df, pd.DataFrame)
    pd.testing.assert_frame_equal(df, expected_df)


@pytest.fixture
def passport_processor():
    return PassportProcessor("input.txt")


def test_process_passports_returns_dataframe(passport_processor):
    df = passport_processor.process_passports()
    assert isinstance(df, pd.DataFrame)


def test_create_dataframe_returns_correct_number_of_rows(passport_processor):
    df = passport_processor.create_dataframe()
    assert len(df) == 285


def test_create_dataframe_returns_correct_columns(passport_processor):
    df = passport_processor.create_dataframe()
    expected_columns = ["eyr", "iyr", "byr", "ecl", "pid", "hcl", "hgt", "cid"]
    assert all(col in df.columns for col in expected_columns)


@pytest.fixture
def test_df():
    return pd.DataFrame(
        {
            "byr": [
                "1930",
                "1980",
                "2005",
                "1995",
                "1910",
                "1988",
                "1975",
                "1960",
            ],  # noqa: E501
            "iyr": [
                "2017",
                "2013",
                "2020",
                "2015",
                "2005",
                "2010",
                "2015",
                "2010",
            ],  # noqa: E501
            "eyr": [
                "2020",
                "2024",
                "2025",
                "2030",
                "2025",
                "2030",
                "2025",
                "2025",
            ],  # noqa: E501
            "hgt": [
                "183cm",
                "168cm",
                "175cm",
                "160cm",
                "170cm",
                "190cm",
                "155cm",
                "180cm",
            ],
            "hcl": [
                "#a97842",
                "#fffffd",
                "#123456",
                "#987654",
                "#abcdef",
                "#123abc",
                "#456def",
                "#789012",
            ],
            "ecl": ["amb", "brn", "blu", "gry", "grn", "hzl", "oth", "brn"],
            "pid": [
                "860033327",
                "760753108",
                "0123456789",
                "123456789",
                "000000001",
                "1234567890",
                "0987654321",
                "123456789",
            ],
            "cid": ["147", "", "123", "", "456", "", "", "789"],
        }
    )


def test_remove_cid(test_df, passport_processor):
    result_df = passport_processor.remove_cid(test_df)
    assert len(result_df.columns) == 7
    assert "cid" not in result_df.columns


def test_validate_birth_year(test_df, passport_processor):
    result_df = passport_processor.validate_birth_year(test_df)
    assert len(result_df) == 6
    assert (result_df["byr"].values >= 1920).all()
    assert (result_df["byr"].values <= 2002).all()

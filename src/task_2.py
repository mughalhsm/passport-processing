import pandas as pd

from passport_processor import PassportProcessor


def number_valid_passports_with_validation() -> int:
    pp = PassportProcessor("input.txt")
    df = pp.process_passports()
    return len(df)


if __name__ == "__main__":
    number_valid_passports_with_validation()

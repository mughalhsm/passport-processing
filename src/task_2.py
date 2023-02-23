from passport_processor import PassportProcessor
import pandas as pd


def number_valid_passports_with_validation():
    pp = PassportProcessor("input.txt")
    df = pp.process_passports()
    return len(df)


if __name__ == "__main__":
    number_valid_passports_with_validation()
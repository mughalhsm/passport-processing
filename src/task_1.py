import pandas as pd

from passport_processor import PassportProcessor


def number_valid_passports() -> int:
    pp = PassportProcessor("input.txt")
    df = pp.create_dataframe()
    df = pp.remove_cid(df)
    df = df.dropna()
    return len(df)


if __name__ == "__main__":
    number_valid_passports()

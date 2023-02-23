from passport_processor import PassportProcessor
import pandas as pd

def number_valid_passports():
    pp = PassportProcessor("input.txt")
    df = pp.create_dataframe()
    df = pp.remove_cid(df)
    df = df.dropna()
    return len(df)


if __name__ == "__main__":
    number_valid_passports()



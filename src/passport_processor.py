import pandas as pd


class PassportProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        with open(self.input_file, "r") as file:
            self.passport_str = file.read()

    def process_passports(self):
        passports = self.passport_str.split("\n\n")
        passport_dicts = []
        for passport in passports:
            fields = passport.split()
            passport_dict = {}
            for field in fields:
                key, value = field.split(":")
                passport_dict[key] = value
            passport_dicts.append(passport_dict)
        return pd.DataFrame(passport_dicts)


pp = PassportProcessor("input.txt")
df = pp.process_passports()
print(df)

# df = pd.DataFrame(passport_dicts)
# df = df.drop('cid', axis=1)
# df = df.dropna()

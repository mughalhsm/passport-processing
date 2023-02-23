import pandas as pd
import re


class PassportProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        with open(self.input_file, "r") as file:
            self.passport_str = file.read()

    def create_dataframe(self):
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
 
    def remove_cid(self, df):
        return df.drop('cid', axis=1)

    def validate_birth_year(self, df):
        df['byr'] = df['byr'].astype(int)
        return df.loc[(df['byr'] >= 1920) & (df['byr'] <= 2002)]
    
    def validate_issue_year(self, df):
        df['iyr'] = df['iyr'].astype(int)
        return df.loc[(df['iyr'] >= 2010) & (df['iyr'] <= 2020)]
    
    def validate_expiration_year(self, df):
        df['eyr'] = df['eyr'].astype(int)
        return df.loc[(df['eyr'] >= 2020) & (df['eyr'] <= 2030)]
    
    def validate_heights(self, df):
        df['hgt_units'] = df['hgt'].str.extract(r'([a-z]+)')
        df['hgt'] = pd.to_numeric(df['hgt'].apply(lambda x: re.sub('[^0-9]', '', x)))
        height_mask = ((df['hgt'].between(150, 193) & (df['hgt_units'] == 'cm')) | (df['hgt'].between(59, 76) & (df['hgt_units'] == 'in')))
        return df[height_mask]
    
    def validate_hair_color(self, df):
        pattern = r'^#[0-9a-fA-F]{6}$'
        hair_mask = df['hcl'].apply(lambda x: bool(re.match(pattern, x)))
        return df[hair_mask]
    
    def validate_eye_color(self, df):
        valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        eye_mask = df['ecl'].isin(valid_eye_colors)
        return df[eye_mask]
    
    def validate_passport_id(self, df):
        pattern = r'^\d{9}$'
        pid_mask = df['pid'].apply(lambda x: bool(re.match(pattern, x)))
        return df[pid_mask]
    
    def process_passports(self):
        df = self.create_dataframe()
        df = self.remove_cid(df)
        df = df.dropna()
        df = self.validate_birth_year(df)
        df = self.validate_issue_year(df)
        df = self.validate_expiration_year(df)
        df = self.validate_heights(df)
        df = self.validate_hair_color(df)
        df = self.validate_eye_color(df)
        df = self.validate_passport_id(df)
        return df





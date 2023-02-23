# Passport Processor

This project is part of the Advent of Code programming challenge.

The PassportProcessor is a Python class that can be used to validate passport data. The class reads in passport data from a text file and converts it into a Pandas DataFrame, which can then be processed and validated using various validation methods.

## Installation

To use the PassportProcessor class, first clone the repository:

```bash
git clone https://github.com/mughalhsm/passport_processor.git
```

Next, navigate to the project directory:


```bash
cd passport_processor
```

Install the project dependencies by running:

```
pip install -r requirements.txt
```

Finally, you can import the PassportProcessor class in your Python code:

```python
from passport_processor import PassportProcessor
```

## Usage

The PassportProcessor class has various methods for processing and validating passport data. Here's an example of how to use the class:

```python
pp = PassportProcessor("input.txt")
df = pp.process_passports()
```

In this example, input.txt is the name of the file containing the passport data. The process_passports() method reads in the data, converts it into a DataFrame, and then performs various validation steps on the data.

Once the validation steps are complete, you can access the validated data in the df variable.

## Validation Methods

The PassportProcessor class has several methods for validating different fields in the passport data:

* remove_cid(df: pd.DataFrame) -> pd.DataFrame: Remove the 'cid' column from the DataFrame.
* validate_birth_year(df: pd.DataFrame) -> pd.DataFrame: Validate the birth year field in the DataFrame.
* validate_issue_year(df: pd.DataFrame) -> pd.DataFrame: Validate the issue year field in the DataFrame.
* validate_expiration_year(df: pd.DataFrame) -> pd.DataFrame: Validate the expiration year field in the DataFrame.
* validate_heights(df: pd.DataFrame) -> pd.DataFrame: Validate the height field in the DataFrame.
* validate_hair_color(df: pd.DataFrame) -> pd.DataFrame: Validate the hair color field in the DataFrame.
* validate_eye_color(df: pd.DataFrame) -> pd.DataFrame: Validate the eye color field in the DataFrame.
* validate_passport_id(df: pd.DataFrame) -> pd.DataFrame: Validate the passport ID field in the DataFrame.

These methods modify the DataFrame by removing invalid rows or fields.

## Testing

The project includes a set of pytest tests to verify the functionality of the PassportProcessor class. To run the tests, simply run the following command in the project directory:

```
pytest
```

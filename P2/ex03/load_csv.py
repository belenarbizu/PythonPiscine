import pandas as pd
from pandas.errors import EmptyDataError, ParserError

def load(path: str)-> pd.DataFrame:
    try:
        dataset = pd.read_csv(path)
        return dataset
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Don't have permission to open the file")
    except EmptyDataError:
        print("Error: The file is empty")
    except ParserError:
        print("Error: The file doesn't have a valid format")
    return None
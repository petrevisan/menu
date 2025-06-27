import pandas as pd

def spreadsheet_reader(url: str):
  try:
    df = pd.read_csv(url)
    return df.to_dict(orient="records")
  except Exception as e:
    print(f"Error: {e}")
    return { "error": e}

# https://docs.google.com/spreadsheets/d/e/2PACX-1vS14nkgMyh61BCTN7yzOBdWb8X2Ygpp9iopcJUVjNKWfYP2gFtNklbyCXhdWhOR3sJIKauAjEqpfGYd/pub?output=csv
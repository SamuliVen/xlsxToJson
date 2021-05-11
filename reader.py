import pandas as pandas
from pandas import DataFrame
import json

# Reading the excel file and naming it as dataframe
df = pandas.read_excel('tuntiraportit_alkuperäinen.xlsx')

# Changing the date format to dd.mm.yyyy
df.update(df.select_dtypes('datetime').apply(lambda x: x.dt.strftime('%d.%m.%Y')))

# to_json must have orient="records" to make match the given model example
jsonData = df.to_json(orient="records")

parsed = json.loads(jsonData)

# Setting encoding to utf-8 so the Ö and Ä characters are not shown as �
tunnitJson = open("tuntiraportit.json", "w", encoding='utf-8')

# Formating parsed data with indent, sorted keys and ensure_ascii to false so the special characters are
# Ö and Ä instead of unicodes.
finaldata = json.dumps(parsed, default=str, indent=4, sort_keys=True, ensure_ascii=False)

# Printing finaldata to tuntiraportit.json file
print(finaldata, file=tunnitJson)

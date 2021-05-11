This is a simple excel to json converter for a spesific given task. 

reader.py reads the file 'tuntiraportit_alkuperäinen.xlsx' 
and writes it's content in json format to 'tuntiraportit.json'

There were some sanitations needed in the conversion i.e. date format 
and utf-8 encoding for Finnish special characters.

Making this small project I learned how to handle json format with Python
and how to use pandas Dataframe format and its tools.

Required installs:
$pip install pandas

Things to develop:
- Adding the main title to the json file "tuntikirjaus" before the data.
- Formatting the sum of hours in some convenient way.

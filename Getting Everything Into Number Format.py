import pandas

df = pandas.read_excel("No Dupes.xlsx")
pandas.to_numeric(df["CAPS"], errors='coerce')
df.to_excel("No Dupes All Numbers.xlsx")
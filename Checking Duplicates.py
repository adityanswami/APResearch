import pandas

df = pandas.read_excel("Combined Data.xlsx")
without_dupes = df.drop_duplicates()
without_dupes.to_excel("No Dupes.xlsx")
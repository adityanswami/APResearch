import pandas
df = pandas.read_excel("No Dupes.xlsx")
print(df[df["CAPS"]].apply(lambda x: isinstance(x, str))
)

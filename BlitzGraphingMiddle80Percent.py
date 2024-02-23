import matplotlib.pyplot as plt
import pandas


df = pandas.read_excel("Blitz Data Only.xlsx")
print(df)
for i in range(1, 25):
    inRange = df.loc[(df["Rating"] >= (i*100)) & (df["Rating"]< ((i*100)+99))]
    inRange.sort_values("CAPS", ascending=[True], inplace=True)
    numRowsToBeRemoved = int(0.1 * inRange.shape[0]+0.5)
    IDsToBeRemoved1 = inRange.iloc[0:numRowsToBeRemoved]["ID"].tolist()
    IDsToBeRemoved2 = inRange.iloc[inRange.shape[0]-numRowsToBeRemoved:inRange.shape[0]]["ID"].tolist()
    IDsToBeRemoved = IDsToBeRemoved1+IDsToBeRemoved2
    df = df.loc[~df["ID"].isin(IDsToBeRemoved)]
    print(df)
x = df["Rating"]
y = df["CAPS"]
df.to_excel("Blitz Data 10 Percent.xlsx")
plt.scatter(x=x, y=y, c="blue")
plt.show()
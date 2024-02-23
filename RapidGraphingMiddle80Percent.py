import matplotlib.pyplot as plt
import pandas


df = pandas.read_excel("Rapid Data Only.xlsx")
print(df)
for i in range(1, 22):
    inRange = df.loc[(df["Rating"] >= (i*100)) & (df["Rating"]< ((i*100)+99))]
    inRange.sort_values("CAPS", ascending=[True], inplace=True)
    numRowsToBeRemoved = int(0.2 * inRange.shape[0]+0.5)
    IDsToBeRemoved1 = inRange.iloc[0:numRowsToBeRemoved]["ID"].tolist()
    IDsToBeRemoved2 = inRange.iloc[inRange.shape[0]-numRowsToBeRemoved:inRange.shape[0]]["ID"].tolist()
    IDsToBeRemoved = IDsToBeRemoved1+IDsToBeRemoved2
    df = df.loc[~df["ID"].isin(IDsToBeRemoved)]
    print(df)
x = df["Rating"]
y = df["CAPS"]
df.to_excel("Rapid Data 20 Percent.xlsx")
plt.scatter(x=x, y=y, c="red")
plt.show()
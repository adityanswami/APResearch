from matplotlib import pyplot as plt
import pandas
df = pandas.read_excel("No Dupes Without Non-Number CAPS.xlsx")
x = df.loc[df["Time Category"] == "Bullet"]["Rating"]
y = df.loc[df["Time Category"] == "Bullet"]["CAPS"]
z = df.loc[df["Time Category"] == "Bullet"]["Time Category"]

def pltcolor(lst):
    cols = []
    for l in lst:
        if l == "Rapid":
            cols.append("red")
        elif l == "Blitz":
            cols.append("blue")
        elif l == "Bullet":
            cols.append("green")
    return cols

cols = pltcolor(z)
plt.scatter(x=x, y=y, c=cols)
plt.show()
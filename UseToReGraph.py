import matplotlib.pyplot as plt
import numpy
import numpy as np
import pandas
import statsmodels.api as sm
import seaborn as sns
import seaborn.objects as so


df = pandas.read_excel("Bullet Data 30 Percent Aggressive.xlsx")
x = df["Rating"]
y = df["CAPS"]

plt.scatter(x=x, y=y, c="green", label="Bullet")
plt.ylabel("CAPS Score (Calculated by Stockfish 16)")
plt.xlabel("Rating")
plt.title("CAPS Score vs Rating, 30% Top and Bottom Removed from Each 100-point Rating Range")

x = sm.add_constant(x)
model = sm.OLS(y, x, missing='drop')
model_Result = model.fit()

print(model_Result.pvalues.iloc[1])
x2 = numpy.linspace(0,2500, 3)
y2 = model_Result.params.iloc[1]*x2+model_Result.params.iloc[0]
plt.plot(x2, y2, label="CAPS Score = " +str(round(model_Result.params.iloc[1], 3))+"*Rating + "+str(round(model_Result.params.iloc[0], 3))+"; r = "+str(round(model_Result.rsquared**0.5, 3))+"; R^2 = "+str(round(model_Result.rsquared, 3))+"; P Value from T-Test = "+f"{model_Result.pvalues.iloc[1]:.3e}")
plt.legend(loc="lower right")
print(model_Result.summary())
plt.show()

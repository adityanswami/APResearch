# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating vectors X and Y
Ra = np.linspace(0, 3000, 3000)
Rb = 1500
E = 1/(1+10**(-(Ra-Rb)/400))
n = 10
Asymptote0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Asymptote1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
AsX = np.linspace(0, 3000, n)
fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(Ra, E)
plt.plot(AsX, Asymptote1, linestyle="--")
plt.plot(AsX, Asymptote0, linestyle="--")
plt.xlabel("Rating of Player A")
plt.ylabel("Expected score of game")
plt.title("Expected score vs Rating of Player A")
# Show the plot
plt.show()
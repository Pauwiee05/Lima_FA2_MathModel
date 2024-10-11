# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:45:44 2024

@author: dell
"""

import numpy as np
import matplotlib.pyplot as plt

# Given Values
a = 0.1  # percentage of pollutants removed each week
b = 2    # amount(tons) that seep in each week
T_0 = 70  # initial amount of pollutants in the lake
#duration = 8  # duration of 2 months (8 weeks when converted)
duration = 104  # duration of 2 years (104 weeks when converted)

# Initialize the pollutant levels array
T = np.zeros(duration + 1)
T[0] = T_0

# Variable to track the number of weeks until pollutant level reaches 2 tons
weeks_until_below_2 = None

# Iterate to compute the pollutant level each week
for n in range(duration):
    T[n + 1] = (1 - a) * T[n] + b
    
    # Check if pollutant level has dropped below 2 tons
    if T[n + 1] < 2 and weeks_until_below_2 is None:
        weeks_until_below_2 = n + 1  # Store the week count

# Plot the pollutant levels over time
plt.figure(figsize=(10, 6))
plt.plot(range(duration + 1), T, label="Pollutant Level", color="blue", linewidth=2)
plt.axhline(y=2, color='r', linestyle='--', label='2 Tons')
plt.axhline(y=20, color='g', linestyle='--', label='Steady State (20 Tons)')
plt.title('Pollutant Levels in the Lake Over Time')
plt.xlabel('Weeks')
plt.ylabel('Tons of Pollutant')
plt.legend()
plt.grid(True)
plt.show()

# Pollutant levels during 2 months
print(T)

# Pollutant level after 2 months
final_pollutant_level = T[8]
print("Final pollutant level after 2 months:", final_pollutant_level)

# Number of weeks until pollutant level drops below 2 tons
if weeks_until_below_2 is not None:
    print("Weeks until pollutant level drops below 2 tons:", weeks_until_below_2)
else:
    print("Pollutant level did not drop below 2 tons in the given duration.")

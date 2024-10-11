import numpy as np
import matplotlib.pyplot as plt

# Parameters
r_x = 1.5  # Growth rate of species x
r_y = 1.2  # Growth rate of species y
s_x = 0.1  # Effect of species y on the growth of species x
s_y = 0.1  # Effect of species x on the growth of species y
K_x = 10   # Carrying capacity of species x
K_y = 10   # Carrying capacity of species y


t = np.linspace(0, 20, 100)  # t time from 0 to 20

def simulate_populations(x_init, y_init):
    x_pop = np.zeros(len(t))
    y_pop = np.zeros(len(t))
    
    x_pop[0] = x_init
    y_pop[0] = y_init


    for i in range(1, len(t)):
        dx = r_x * x_pop[i-1] * (1 - x_pop[i-1] / K_x) - s_x * x_pop[i-1] * y_pop[i-1]
        dy = r_y * y_pop[i-1] * (1 - y_pop[i-1] / K_y) - s_y * x_pop[i-1] * y_pop[i-1]
        x_pop[i] = x_pop[i-1] + dx * (t[i] - t[i-1])
        y_pop[i] = y_pop[i-1] + dy * (t[i] - t[i-1])
    
    return x_pop, y_pop

initial_conditions = [
    (0, 0),                  
    (K_x / r_x, 0),         
    (0, K_y / r_y)            
]

# Titles for the plots
titles = [
    'Equilibrium Point (0, 0)',
    'Equilibrium Point (K_x/r_x, 0)',
    'Equilibrium Point (0, K_y/r_y)'
]


for i, (x_init, y_init) in enumerate(initial_conditions):
    x_pop, y_pop = simulate_populations(x_init, y_init)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, x_pop, label='Species X', color='blue', linewidth=2)
    plt.plot(t, y_pop, label='Species Y', color='red', linewidth=2)
    
 
    plt.title(titles[i])
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.xlim(0, 20)
    plt.ylim(-2, 12)
    plt.show()

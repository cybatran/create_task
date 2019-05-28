import random
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import numpy as np

total = 0
value = 100
value_2 = value

A_input = []

A_time = []
    
while total != 100:
    stock = random.choice(range(-3,3,1))
    print(stock)
    new_value = value * stock
    new_value = new_value / 100
    final = new_value + value_2
    A_time.append(final)
    A_input.append(value)
    value += 1
    total += 1

    

    

fig, ax = plt.subplots(1,1)
# plot(x_list, y_list, "color and style")
ax.plot(A_input, A_time, 'bo-', label='Stock Price') # red dots

# Label and show
ax.set_xlabel ("Inputed Stocks")
ax.set_ylabel("Total Stock Price")
ax.set_title("High Frequency Trading")
ax.legend(loc='center left') # Show and place the legend fig.set_facecolor('white')
fig.savefig('graph_data')




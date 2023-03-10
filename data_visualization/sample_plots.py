"""Chapter 15"""

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from random_walk import RandomWalk

# Initial playing around ######################################################
print('Fun with plots')
#print(plt.style.available)

input_values = range(1,101)
squares = []

# Calculate the squares of the input values
#for value in input_values:
    #squares.append(value**2)

# Alternatively, calculate the squares of the input values in a list comprehension
squares = [value**2 for value in input_values]

#plt.style.use('dark_background')
fig, ax = plt.subplots()

#ax.plot(input_values, squares, linewidth=3, color='red') 
# ax.plot(input_values, squares, linewidth=3, color=(0,0.8,0)) 

# Scatter plot with a color map. "c" specifies what values the colormap should 
# apply to, and "cmap" specifies the colormap to use.
ax.scatter(input_values, squares, s=50, c=squares, cmap=plt.cm.Blues)

# Set chart title and label axes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)


# Set the range for each axis
#ax.axis([0, 15, 0, 150])

#ax.ticklabel_format(style='plain') # Keep numbers not in scientific notation

#plt.show()
#plt.savefig('hey.png', bbox_inches='tight')


# Plot random walk ############################################################
print('Making a random walk')
my_walk = RandomWalk(100000)

fig2, ax2 = plt.subplots()
# fig2, ax2 = plt.subplots(figsize=(15,9)) # The tuple argument is inches (approximately!) on the scree

ax2.scatter(my_walk.walk_x, my_walk.walk_y, s=10, c=range(1,len(my_walk.walk_x)+1), cmap=plt.cm.Blues, edgecolors='none')

# Emphasize the first and last points
ax2.scatter(0, 0, s=30, color='green')
ax2.scatter(my_walk.walk_x[-1], my_walk.walk_y[-1], s=1, color='red')

ax2.set_title("A very random walk", fontsize=24)
ax2.set_xlabel("X (metres)", fontsize=14)
ax2.set_ylabel("Y (metres)", fontsize=14)
ax2.tick_params(labelsize=14)
# Set X and Y axes to be equal in terms of spacing
ax.set_aspect('equal')

# Remove the axes
#ax2.get_xaxis().set_visible(False)
#ax2.get_yaxis().set_visible(False)

plt.show()


# Now plot the random walk with plotly
title = "Random walk"
labels = {'x': "X (metres)", "y": "Y (metres)"}
fig3 = px.scatter(x=my_walk.walk_x, y=my_walk.walk_y, title=title, 
                  labels=labels, color=range(1, len(my_walk.walk_x)+1))
# emphasize first and last points
#hey = go.scatter.Marker(size=50) # Make an instance of a Scatter object
#fig3.add_trace(go.Scatter(x=[0], y=[0], marker=hey)) # Pass that instance into the add_trace function
fig3.add_trace(go.Scatter(x=[0], y=[0], marker=go.scatter.Marker(size=50, color='green')))
fig3.add_trace(go.Scatter(x=[my_walk.walk_x[-1]], y=[my_walk.walk_y[-1]], marker=go.scatter.Marker(size=50, color='red')))


# size=range(1, len(my_walk.walk_x)+1)
fig3.write_html("hey3.html")
print("End of program")
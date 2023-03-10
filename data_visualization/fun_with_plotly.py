"""TBD"""
from random import randint
import plotly.express as px
import matplotlib.pyplot as plt


class Die:
    """A class representing a single die"""
    
    def __init__(self, num_sides=6):
        """Assume a six-sided die"""
        self.num_sides = num_sides
    
    def roll(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.num_sides)
    

# Main routine
print("Fun with plotly")

# Create two D6 dice
die_1 = Die()
die_2 = Die(10)

# Make some rolls, store them in a list
sums = []
for roll_num in range(1000):
    value_1 = die_1.roll()
    value_2 = die_2.roll()

    sums.append(value_1 + value_2)

#
# Analyze the results
#
frequencies_of_sums = []
possible_sums = range(2, die_1.num_sides+die_2.num_sides+1)

# Loop over all possible values
for value in possible_sums:
    # Count instances in the list that have this value
    frequency = sums.count(value)

    # Build the list of frequencies of all values
    frequencies_of_sums.append(frequency)

print(frequencies_of_sums)

# Make a histogram and display it in the browser
title = "Sums of rolling 1 D6 and 1 D10 1,000 times"
labels = {'x': "Sum", "y": "Frequency of Sum"}
fig = px.bar(x=possible_sums, y=frequencies_of_sums, title=title, labels=labels)

# Further customize the bar chart - label all the bars
fig.update_layout(xaxis_dtick=1)
#fig.show()
#fig.write_html("hey.html")


# Make a bar chart with matplotlib
fig2, ax2 = plt.subplots()
ax2.bar(possible_sums, frequencies_of_sums, tick_label=possible_sums)
ax2.set_title(title, fontsize=14)
ax2.set_xlabel("Sum", fontsize=14)
ax2.set_ylabel("Frequency of sum", fontsize=14)
ax2.tick_params(labelsize=14)
plt.show()

print("End of program.")
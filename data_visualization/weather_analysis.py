"""Code for Chapter 16 - Data Visualization"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

print("Chapter 16")

def find_header(label, header_row):
    """Find index of label in the header row. Exits program if not found."""
    if header_row.__contains__(label):
        col = header_row.index(label)
    else:
        print(f"Cannot find {label} in data.")
        exit()

    return col


local_folder_path = 'data_visualization/weather_data/'

#file1_name = 'sitka_weather_07-2021_simple.csv'
#file1_name = 'sitka_weather_2021_simple.csv'
#file1_name = 'sitka_weather_2021_full.csv'
#file1_name = 'death_valley_2021_simple.csv'
file1_name = 'death_valley_2021_full.csv'
date_col = 2
high_label = "TMAX"
low_label = "TMIN"
precip_label = "PRCP"


path = Path(local_folder_path + file1_name)
lines = path.read_text().splitlines() # Get a list of all the lines in the file

reader = csv.reader(lines) # Create a "reader" object
header_row = next(reader) # Get the next line in the file

# Determine column numbers for highs, lows, and precipitation
high_col = find_header(high_label, header_row)
low_col = find_header(low_label, header_row)
precip_col = find_header(precip_label, header_row)

# Loop over all values in header. Note: 'Enumerate' returns the index and value
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Exract the dates, high temperatures, and low temperatures
dates, highs, lows, precips = [], [], [], []

# Loop over all remaining rows in the reader object. Note that we've already 
# read the header row, so it doesn't get included here. 
for row in reader:
    current_date = datetime.strptime(row[date_col], '%Y-%m-%d')
    try: 
        high = int(row[high_col])
        low = int(row[low_col])
        precip = float(row[precip_col])
    except ValueError:
        print(f'Missing data for {current_date}!')
    
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
    precips.append(precip)


# Plot the temps
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.3)

# Format plot
title_prefix = 'High and low temps: '
ax.set_title(title_prefix + file1_name, fontsize=14)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # Draw labels diagonally
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)
ax.set(ylim=(0,150)) # Set y-axis min and max values

plt.show()

# Plot the rainfall
fig2, ax2 = plt.subplots()
ax2.bar(dates, precips, color='blue')
title_prefix = 'Precipitation: '
ax2.set_title(title_prefix + file1_name, fontsize=14)
ax2.set_xlabel('', fontsize=16)
fig2.autofmt_xdate() # Draw labels diagonally
ax2.set_ylabel('Precipitation (mm)', fontsize=16)
ax2.tick_params(labelsize=16)

plt.show()
#Plot Other Data
#Jeffrey McCullough
#April 16, 2023
#Read data from CSV about Ohio unemployment rate and create a graph

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/OHUR.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rates = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%m/%d/%Y')
        try:
            rate = float(row[1])
        except ValueError:
            print(f"No data at {current_date}")
        else:
            dates.append(current_date)
            rates.append(rate)
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, rates, c='red')
ax.set_title('Ohio Unemployment Rates By Month (January 1976-May 2022)')
ax.set_xlabel('Date', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Unemployment Rate (in Percent)', fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)
plt.show()

                         



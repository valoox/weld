#!/usr/bin/python

# The usual preamble
import numpy as np
import pandas as pd
import time

# Get data (NYC 311 service request dataset) and start cleanup
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('data/311-service-requests.csv',
                       na_values=na_values, dtype={'Incident Zip': str})
print "Done reading input file..."

start = time.time()

# Fix requests with extra digits
requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)

# Fix requests with 00000 zipcodes
zero_zips = requests['Incident Zip'] == '00000'
requests['Incident Zip'][zero_zips] = np.nan

# Display unique incident zips again (this time cleaned)
print requests['Incident Zip'].unique()
end = time.time()

print "Total end-to-end time: %.2f" % (end - start)

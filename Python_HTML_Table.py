# Python script to generate an HTML file that displays table of data from a CSV file with 3 fields: MD5, Hostname and Time

from IPython.display import HTML
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pd.set_option('display.width', 1000)
pd.set_option('colheader_justify', 'center')
pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

data = "/Users/john/Desktop/file.csv"

data_plot = pd.read_csv(data) # av 

data_plot.columns = ["MD5", "Hostname", "Time"]

#print(data_plot)
#print(result)

host_ct = pd.value_counts(data_plot['Hostname'])

plt.axes(frameon=0)
host_ct.plot(kind='bar', rot=0, title="Summary by Host", figsize=(8,5)).grid(False)
# print(host_ct)

html_string = '''
<html>
  <head><title>HTML Pandas Dataframe with CSS</title></head>
  <link rel="stylesheet" type="text/css" href="df_style.css"/>
  <body>
    {table}
  </body>
</html>.
'''

with open('myhtml.html', 'w') as f:
    f.write(html_string.format(table=data_plot.to_html()))

# HTML(data_plot.head(30).to_html())

%matplotlib inline

import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.ylabel('some numbers')
plt.axis([0, 6, 0, 20])
plt.show()


import pandas as pd

df = pd.DataFrame.from_csv('/Users/catherine/performance_prediction/goog_20100101_20151031.csv', parse_dates=True)
ax = df.plot(secondary_y=['Open', 'Close'])

ax.set_ylabel('Open')
ax.right_ax.set_ylabel('Close')


# import pandas as pd
# import matplotlib.pyplot as plt

# # plt.rcParams["figure.figsize"] = [7.50, 3.50]
# # plt.rcParams["figure.autolayout"] = True

# headers = ['Keyword','Number of articles found']

# df = pd.read_csv('Searched_news.csv', names=headers)

# df.set_index('Number of articles found').plot()

# plt.show()

from matplotlib import pyplot as plt

# Median Developer Salaries by Age
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(dev_x, dev_y)
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.show()
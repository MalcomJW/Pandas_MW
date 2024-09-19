#.aggreagate(["function1", "function2])
# .agg({'column1': ['min', 'max', 'mean'],
#       'column2': ['min', 'max', 'mean']})

#grouped_df = df.groupby(by=['country', 'city'])
#total_pop=grouped_df["Population(2024)"].agg(["min", "max", "mean"])
#print(total_pop)

# aggregated_data = df.groupby("country").agg(
#     Average_Growth=('growth rate,', 'mean'),
#     total_cities=('population(2024)', 'count'),
#     Max_pop=('population(2024)', 'max'),
#     Min_pop=('population(2024)', 'min')
# )



import pandas as pd
import matplotlib.pyplot as plt

#load csv
data = pd.read_csv("WMT.csv")
# print(data.info())
# print(data.shape)
# print(data.head(10))


#agg
basic_agg = data["Open"].aggregate(['min', 'max', 'median', 'mean'])
#   print(basic_agg)

#agg 2
#dict mult col
multi_tier = data.agg({
    "Open" : ['min', 'max', 'median', 'mean'],
    "Close" : ['min', 'max', 'median', 'mean'],
    "Volume" : ['min', 'max', 'median', 'mean']
})
# print(multi_tier)

#cust func x any #
#range of values
def range_calc(x):
    return x.max() - x.min()


#agg date
#grab Date in data.  To_DateTime is a pandas. We now have col to wor
# new cols ->> modified cols
data["Date"] = pd.to_datetime(data["Date"])

advanced_data = data.groupby(data["Date"].dt.year).agg(
    Open_Min=("Open", "min"),
    Open_Max=("Open", "min"),
    Close_Mean=("Close", "mean"),
    Volume_Total=("Volume", "sum"),
    Open_Range = ("Open", range_calc)
)
# print(advanced_data)



#plotting
plt.figure(figsize=(10,6))
plt.plot(advanced_data.index, advanced_data["Open_Range"], color='green', marker="o")
plt.title("Range of Opening Prices")
plt.xlabel("Year")
plt.ylabel("Open Range")
plt.grid(True)
plt.show()
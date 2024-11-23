import pandas as pd
import matplotlib.pyplot as plt

fixed_df = pd.read_csv('2013.csv', 
                       sep=',', encoding='latin1', 
                       parse_dates=['Date'], dayfirst=True, 
                       index_col='Date')

print(fixed_df.head())
fixed_df.index = pd.to_datetime(fixed_df.index)

fixed_df.fillna(0, inplace=True)
fixed_df['Total'] = fixed_df.sum(axis=1)
monthly_totals = fixed_df.resample('M').sum()
most_popular_month = monthly_totals['Total'].idxmax()
print(f"Найпопулярніший місяць у 2013 році: {most_popular_month.strftime('%B')}")

fixed_df.plot(figsize=(15, 10))
plt.show()


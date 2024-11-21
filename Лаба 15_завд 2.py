import pandas as pd
import matplotlib.pyplot as plt

fixed_df = pd.read_csv('2013.csv', 
                       sep=',', encoding='latin1', 
                       parse_dates=['Date'], dayfirst=True, 
                       index_col='Date')

print(fixed_df.head())

monthly_totals = fixed_df.groupby('Date').sum()
monthly_totals['Total'] = monthly_totals.sum(axis=1)
most_popular_month = monthly_totals['Total'].idxmax()
print(f"Найпопулярніший місяць у 2013 році: {most_popular_month}")

fixed_df.plot(figsize=(15, 10))
plt.show()

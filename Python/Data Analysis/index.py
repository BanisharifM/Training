import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

surveys_df = pd.read_csv('./surveys.csv')
# print(surveys_df)
# surveys_df.head()
# print(type(surveys_df))
# print(surveys_df.columns)
# print(surveys_df.shape)
# print(surveys_df['weight'].describe())
# print(surveys_df['hindfoot_length'][2])

grouped_data = surveys_df.groupby('sex')
# print(grouped_data.describe())
# print(grouped_data.mean())

grouped_data2 = surveys_df.groupby(['site_id', 'sex'])
# print(grouped_data2.mean())

# Count the number of samples by species
species_counts = surveys_df.groupby('species_id')['record_id'].count()
# print(species_counts)

# Multiply all weight values by 2 but does not change the original weight data
surveys_df['weight']*2

# species_counts.plot(kind='bar')
# plt.show()

total_count = surveys_df.groupby('site_id')['record_id'].nunique()
total_count.plot(kind='bar')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
CSV_PATH = 'RunSensible_Acquisition_Table.csv'
df = pd.read_csv(CSV_PATH)

# Drop duplicate column if present
if 'Event count per user.1' in df.columns and (df['Event count per user'] == df['Event count per user.1']).all():
    df = df.drop(columns=['Event count per user.1'])

# Basic inspection
print('Data shape:', df.shape)
print('Columns:', df.columns.tolist())
print('\nHead:')
print(df.head())
print('\nSummary statistics:')
print(df.describe())

# Analysis: Top 10 sources by Views
sorted_df = df.sort_values('Views', ascending=False).head(10)

# Visualization
sns.set(style='whitegrid')
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(data=sorted_df, x='Views', y='First user source / medium', ax=ax, palette='viridis')
ax.set_title('Top 10 Sources by Views')
plt.tight_layout()
plt.savefig('top_sources_by_views.png')
plt.close()

# Scatter plot Bounce rate vs Average session duration
fig, ax = plt.subplots(figsize=(8,6))
scatter = ax.scatter(df['Average session duration'], df['Bounce rate'], c=df['Views'], cmap='viridis', alpha=0.7)
ax.set_xlabel('Average session duration')
ax.set_ylabel('Bounce rate')
ax.set_title('Bounce Rate vs. Average Session Duration')
plt.colorbar(scatter, label='Views')
plt.tight_layout()
plt.savefig('bounce_vs_duration.png')
plt.close()

print('\nPlots saved: top_sources_by_views.png, bounce_vs_duration.png')

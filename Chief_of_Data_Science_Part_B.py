# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# File path
reviews_path = '/Users/mohama56/BANA 5440 Python/Project 2/reviews.csv'

# Load dataset
reviews = pd.read_csv(reviews_path)

# Convert 'date' column to datetime format and handle errors
reviews['date'] = pd.to_datetime(reviews['date'], errors='coerce')

# Drop rows with invalid dates
reviews = reviews.dropna(subset=['date'])

# Extract the year from the 'date' column
reviews['year'] = reviews['date'].dt.year

# Filter data for the years 2018 to 2021
years_to_analyze = [2018, 2019, 2020, 2021]
filtered_reviews = reviews[reviews['year'].isin(years_to_analyze)]

# Debugging: Check filtered data
print("\nFiltered Reviews (First 5 Rows):")
print(filtered_reviews[['year', 'stars']].head())

# Group by year and rating to calculate the distribution
yearly_distributions = filtered_reviews.groupby(['year', 'stars']).size().unstack(fill_value=0)

# Debugging: Ensure yearly distribution table is correct
if yearly_distributions.empty:
    print("\nNo data available for the specified years (2018–2021).")
else:
    print("\nYearly Ratings Distribution (2018–2021):")
    print(yearly_distributions)

# Plot yearly distribution of ratings
yearly_distributions.plot(kind='bar', figsize=(12, 8), stacked=True, colormap='viridis', width=0.8)
plt.title('Yearly Ratings Distribution (2018–2021)')
plt.xlabel('Year')
plt.ylabel('Number of Reviews')
plt.legend(title='Ratings', loc='upper left', bbox_to_anchor=(1.0, 1.0))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

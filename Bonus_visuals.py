# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# File paths
reviews_path = '/Users/mohama56/BANA 5440 Python/Project 2/reviews.csv'
restaurants_path = '/Users/mohama56/BANA 5440 Python/Project 2/restaurants.csv'

# Load datasets
reviews = pd.read_csv(reviews_path)
restaurants = pd.read_csv(restaurants_path)

# Convert 'date' column to datetime format
reviews['date'] = pd.to_datetime(reviews['date'])

# Extract the year and month from the 'date' column
reviews['year'] = reviews['date'].dt.year
reviews['month'] = reviews['date'].dt.month

# --- Visual 1: Yearly Ratings Distribution ---
print("\nGenerating Visual 1: Yearly Ratings Distribution...")
yearly_distribution = reviews.groupby(['year', 'stars']).size().unstack(fill_value=0)
print("\nYearly Ratings Distribution (2018–2021):")
print(yearly_distribution.loc[2018:2021])  # Only print years 2018–2021

# Plot yearly distribution of ratings
yearly_distribution.plot(kind='bar', figsize=(12, 8), stacked=True, colormap='viridis', width=0.8)
plt.title('Yearly Ratings Distribution (2018–2021)')
plt.xlabel('Year')
plt.ylabel('Number of Reviews')
plt.legend(title='Ratings', loc='upper left', bbox_to_anchor=(1.0, 1.0))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# --- Visual 2: Bottom 10 Subway Locations by Average Rating ---
print("\nGenerating Visual 2: Bottom 10 Subway Locations by Average Rating...")
location_ratings = reviews.groupby('business_id')['stars'].mean().reset_index()
location_ratings = pd.merge(location_ratings, restaurants[['business_id', 'name', 'city', 'state']], on='business_id', how='left')
bottom_10_locations = location_ratings.sort_values(by='stars', ascending=True).head(10)
print("\nBottom 10 Subway Locations by Average Rating:")
print(bottom_10_locations[['name', 'city', 'state', 'stars']])

# Plot bottom 10 Subway locations by average rating
bottom_10_locations.plot(
    x='name', y='stars', kind='barh', figsize=(10, 6), color='orange'
)
plt.title('Bottom 10 Subway Locations by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('Subway Location')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# --- Visual 3: Monthly Trend of Average Ratings ---
print("\nGenerating Visual 3: Monthly Trend of Average Ratings...")
monthly_ratings = reviews.groupby('month')['stars'].mean().reset_index()
print("\nMonthly Average Ratings:")
print(monthly_ratings)

# Plot monthly trend of ratings
plt.figure(figsize=(10, 6))
plt.plot(
    monthly_ratings['month'], monthly_ratings['stars'],
    marker='o', linestyle='-', color='blue'
)
plt.title('Monthly Trend of Average Ratings')
plt.xlabel('Month')
plt.ylabel('Average Rating')
plt.xticks(range(1, 13))
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



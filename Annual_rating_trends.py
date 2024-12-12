# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# File paths
restaurants_path = '/Users/mohama56/BANA 5440 Python/Project 2/restaurants.csv'
reviews_path = '/Users/mohama56/BANA 5440 Python/Project 2/reviews.csv'

# Load datasets
restaurants = pd.read_csv(restaurants_path)
reviews = pd.read_csv(reviews_path)

# Get all Subway business IDs
subway = restaurants[restaurants['name'].str.contains('Subway', case=False, na=False)]
subway_ids = subway['business_id'].tolist()

# Filter reviews for Subway
subway_reviews = reviews[reviews['business_id'].isin(subway_ids)]

# Convert the 'date' column to datetime format
subway_reviews['date'] = pd.to_datetime(subway_reviews['date'])

# Extract the year from the date
subway_reviews['year'] = subway_reviews['date'].dt.year

# Group ratings by year and calculate the mean rating for each year
ratings_over_time = subway_reviews.groupby('year')['stars'].mean().reset_index()

# Print the yearly ratings
print("Yearly Average Ratings for Subway:")
print(ratings_over_time)

# Plot the trend of Subway's ratings over time
plt.figure(figsize=(10, 6))
plt.plot(ratings_over_time['year'], ratings_over_time['stars'], marker='o', linestyle='-')
plt.title("Subway's Ratings Over Time")
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.grid(True)
plt.ylim(0, 5)
plt.show()

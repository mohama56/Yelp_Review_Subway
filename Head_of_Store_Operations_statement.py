# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# File paths
restaurants_path = '/Users/mohama56/BANA 5440 Python/Project 2/restaurants.csv'
reviews_path = '/Users/mohama56/BANA 5440 Python/Project 2/reviews.csv'

# Load datasets
restaurants = pd.read_csv(restaurants_path)
reviews = pd.read_csv(reviews_path)

# Analyze ratings for sandwich restaurants
sandwich_restaurants = restaurants[restaurants['categories'].str.contains('Sandwiches', case=False, na=False)]
sandwich_ids = sandwich_restaurants['business_id'].tolist()
sandwich_reviews = reviews[reviews['business_id'].isin(sandwich_ids)]

# Calculate average and standard deviation of ratings for sandwich restaurants
sandwich_mean = sandwich_reviews['stars'].mean()
sandwich_std = sandwich_reviews['stars'].std()
print(f"Sandwich Restaurants - Mean Rating: {sandwich_mean:.2f}, Standard Deviation: {sandwich_std:.2f}")

# Analyze ratings for non-sandwich restaurants
non_sandwich_restaurants = restaurants[~restaurants['categories'].str.contains('Sandwiches', case=False, na=False)]
non_sandwich_ids = non_sandwich_restaurants['business_id'].tolist()
non_sandwich_reviews = reviews[reviews['business_id'].isin(non_sandwich_ids)]

# Calculate average and standard deviation of ratings for non-sandwich restaurants
non_sandwich_mean = non_sandwich_reviews['stars'].mean()
non_sandwich_std = non_sandwich_reviews['stars'].std()
print(f"Non-Sandwich Restaurants - Mean Rating: {non_sandwich_mean:.2f}, Standard Deviation: {non_sandwich_std:.2f}")

# Visualize comparison
categories = ['Sandwich Restaurants', 'Non-Sandwich Restaurants']
means = [sandwich_mean, non_sandwich_mean]
stds = [sandwich_std, non_sandwich_std]

plt.figure(figsize=(8, 6))
plt.bar(categories, means, yerr=stds, capsize=10, color=['orange', 'blue'])
plt.title('Comparison of Ratings: Sandwich vs Non-Sandwich Restaurants')
plt.ylabel('Mean Rating')
plt.ylim(0, 5)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# File paths
restaurants_path = '/Users/mohama56/BANA 5440 Python/Project 2/restaurants.csv'
reviews_path = '/Users/mohama56/BANA 5440 Python/Project 2/reviews.csv'

# Load datasets
restaurants = pd.read_csv(restaurants_path)
reviews = pd.read_csv(reviews_path)

# Count the number of unique cities for each business
city_counts = restaurants.groupby('business_id')['city'].nunique().reset_index()
city_counts.columns = ['business_id', 'city_count']

# Merge city counts back with the restaurants dataset
restaurants = pd.merge(restaurants, city_counts, on='business_id')

# Categorize restaurants as 'National' if present in >50 cities, 'Local' if present in 1 city
restaurants['chain_type'] = restaurants['city_count'].apply(
    lambda x: 'National' if x > 1 else 'Local'
)

# Filter reviews for national and local chains
national_ids = restaurants[restaurants['chain_type'] == 'National']['business_id']
local_ids = restaurants[restaurants['chain_type'] == 'Local']['business_id']

national_reviews = reviews[reviews['business_id'].isin(national_ids)]
local_reviews = reviews[reviews['business_id'].isin(local_ids)]

# Calculate mean and standard deviation for ratings
national_mean = national_reviews['stars'].mean()
national_std = national_reviews['stars'].std()
local_mean = local_reviews['stars'].mean()
local_std = local_reviews['stars'].std()

# Print results
print(f"National Chains - Average Rating: {national_mean:.2f}, Standard Deviation: {national_std:.2f}")
print(f"Local Chains - Average Rating: {local_mean:.2f}, Standard Deviation: {local_std:.2f}")

# Check city count distribution
city_count_distribution = restaurants['city_count'].value_counts()
print("City Count Distribution:")
print(city_count_distribution)

#  Count national and local chains
national_count = len(restaurants[restaurants['chain_type'] == 'National'])
local_count = len(restaurants[restaurants['chain_type'] == 'Local'])
print(f"\nNumber of National Chains: {national_count}")
print(f"Number of Local Chains: {local_count}")

# Check reviews for National Chains
print("\nSample Reviews for National Chains:")
print(national_reviews.head())

# Check if National Chains exist in the reviews dataset
print(f"\nNumber of reviews for National Chains: {len(national_reviews)}")
print(f"Number of reviews for Local Chains: {len(local_reviews)}")

# Visualize comparison
categories = ['National Chains', 'Local Chains']
means = [national_mean, local_mean]
stds = [national_std, local_std]

plt.figure(figsize=(8, 6))
plt.bar(categories, means, yerr=stds, capsize=10, color=['blue', 'orange'], alpha=0.7)
plt.title('Average Ratings: National vs Local Chains')
plt.ylabel('Average Rating')
plt.ylim(0, 5)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

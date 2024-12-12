# Import required libraries
import pandas as pd

# File Locations
restaurants_path = '/Users/mohama56/BANA 5440 Python/Project 2/restaurants.csv'

# Load the Restaurant Dataset
restaurants = pd.read_csv(restaurants_path)

# Display the first few rows of the dataset
print("First few rows of the Restaurant Dataset:")
print(restaurants.head())

# Summary of the dataset structure
print("\nDataset Info:")
print(restaurants.info())

# Check for missing values in the dataset
missing_values = restaurants.isnull().sum()
print("\nMissing values in the Restaurant Dataset:")
print(missing_values)

# Count distinct values for key columns
distinct_restaurants = restaurants['business_id'].nunique()
distinct_categories = restaurants['categories'].nunique()  # Corrected from 'category' to 'categories'
distinct_cities = restaurants['city'].nunique()
distinct_states = restaurants['state'].nunique()

print(f"\nNumber of distinct restaurants: {distinct_restaurants}")
print(f"Number of distinct categories: {distinct_categories}")
print(f"Number of distinct cities: {distinct_cities}")
print(f"Number of distinct states: {distinct_states}")

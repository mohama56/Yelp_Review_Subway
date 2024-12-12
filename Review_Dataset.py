# Required Libraries for Part One
import pandas as pd

# File Locations
reviews_path = '/Users/mohama56/BANA 5440 Python/Project 2/reviews.csv'

# Load Review datasets
reviews = pd.read_csv(reviews_path)


# Display the first few rows of the dataset
print("First few rows of the Review Dataset:")
print(reviews.head())

# Dataset structure summary
print("\nDataset Info:")
print(reviews.info())

# Total ratings and distinct restaurants
total_ratings = len(reviews)
distinct_restaurants = reviews['business_id'].nunique()

print(f"\nTotal number of ratings: {total_ratings}")
print(f"Number of distinct restaurants: {distinct_restaurants}")

# Check for missing values 
missing_values = reviews.isnull().sum()
print("\nMissing values in the dataset:")
print(missing_values)

# Review dates summary
print("\nSummary of the review dates:")
reviews['date'] = pd.to_datetime(reviews['date'])  # Execute in datetime format
print(reviews['date'].describe())
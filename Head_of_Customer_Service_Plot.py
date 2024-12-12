# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
subway_mean = subway_reviews['stars'].mean()
subway_std = subway_reviews['stars'].std()

# Print Subway stats
print(f"Total Subway Reviews: {len(subway_reviews)}")
print(f"Updated Subway Mean Rating: {subway_mean:.2f}")
print(f"Updated Subway Standard Deviation: {subway_std:.2f}")

# Find competitors based on categories containing "Sandwiches"
competitors = restaurants[restaurants['categories'].str.contains('Sandwiches', case=False, na=False)]
competitor_ids = competitors['business_id'].iloc[:2].tolist()

# Filter reviews for competitors
competitor_reviews = reviews[reviews['business_id'].isin(competitor_ids)]
competitor_stats = competitor_reviews.groupby('business_id')['stars'].agg(['mean', 'std']).reset_index()
competitor_stats = pd.merge(competitor_stats, restaurants[['business_id', 'name']], on='business_id')

# Print competitor stats
print("\nCompetitor Ratings:")
print(competitor_stats)

# Prepare data for visualization
x_labels = ['Subway'] + competitor_stats['name'].tolist()
mean_values = [subway_mean] + competitor_stats['mean'].tolist()
std_values = [subway_std] + competitor_stats['std'].tolist()

# Visualize comparison
plt.figure(figsize=(10, 6))
sns.barplot(x=x_labels, y=mean_values, capsize=0.1)

# Add error bars manually
for idx, (mean, std) in enumerate(zip(mean_values, std_values)):
    plt.errorbar(x=idx, y=mean, yerr=std, fmt='o', color='black', capsize=5)

plt.title('Mean Ratings: Subway vs Competitors')
plt.xlabel('Business')
plt.ylabel('Mean Rating')
plt.ylim(0, 5)
plt.xticks(rotation=15)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


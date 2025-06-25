

# An Exploratory data analysis on netflix dataset fromm 2008 to 2021



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading the data
df = pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\netflix_titles.xlsx")

# initial check in on the data
df.info()
df.head()

'''
   df['date_added'] = pd.to_datetime(df['date_added']):
   Converts the date_added column to a pandas datetime64 type, parsing various date formats (e.g., "January 1, 2020" or "2020-01-01").
'''

df['date_added'] = pd.to_datetime(df['date_added'])

'''
   df['year_added'] = df['date_added'].dt.year:
   Extracts the year from the date_added datetime column and stores it in a new column year_added as integers (e.g., 2020).
'''
df['year_added'] = df['date_added'].dt.year

'''
   movies_df = df[df['type'] == 'Movie'].copy():
   df['type'] == 'Movie': Filters rows in df where the type column equals "Movie".
   .copy(): Creates a deep copy of the filtered DataFrame to avoid SettingWithCopyWarning and ensure movies_df is independent of df.
   Result: movies_df contains only rows where type is "Movie".
'''
'''
   tv_shows_df = df[df['type'] == 'TV Show'].copy():
   Filters rows where type equals "TV Show" and creates a deep copy.
   Result: tv_shows_df contains only rows where type is "TV Show".
'''
movies_df = df[df['type'] == 'Movie'].copy()
tv_shows_df = df[df['type'] == 'TV Show'].copy()




# content type distribution on the basis of Movies vs TV Show
# here, ' palette='Set2'' applies a color scheme from Seaborn’s Set2 palette for visual distinction.
# sns.countplot() is used to create an count plot where it creates a bar plot where the x-axis represents unique values in the type column of DataFrame df, and the height of each bar represents the count of occurrences.


sns.countplot(data=df, x='type', palette='Set2')
plt.title('Distribution of Content Type')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()


# graph on titles added over years
# here , data=df.dropna(subset=['year_added']): Removes rows where year_added is missing (NaN) to ensure valid data for plotting.
# order=sorted(df['year_added'].dropna().unique()): Sorts the bars in ascending order based on unique, non-null values in year_added.
# plt.xticks(rotation=45): Rotates x-axis labels (years) by 45 degrees for better readability, especially if there are many years.

sns.countplot(data=df.dropna(subset=['year_added']), x='year_added', order=sorted(df['year_added'].dropna().unique()), palette='Set3')
plt.xticks(rotation=45)
plt.title('Titles Added to Netflix Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.show()


# graph indicating top 10 countries with most content on netflix
''' here , top_countries = df['country'].dropna().str.split(', ').explode().value_counts().head(10): 
    df['country'].dropna(): Removes rows where the country column is NaN.
    .str.split(', '): Splits comma-separated country names (e.g., "United States, Canada" into ['United States', 'Canada']).
    .explode(): Transforms each element of the split lists into a separate row (e.g., one row per country).
    .value_counts(): Counts the occurrences of each country.
    .head(10): Selects the top 10 countries with the highest counts.
The result, top_countries, is a pandas Series where the index is country names and values are the counts.'''


top_countries = df['country'].dropna().str.split(', ').explode().value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='coolwarm')
plt.title('Top 10 Countries with Most Netflix Content')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()


# this graph indicates top genres on netflix


top_genres = df['listed_in'].str.split(', ').explode().value_counts().head(10)
sns.barplot(x=top_genres.values, y=top_genres.index, palette='viridis')
plt.title('Top 10 Netflix Genres')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.show()


# graph indicating content rating distributions 
# here, border=df['rating'].value_counts().index: Orders the bars by the frequency of ratings (highest to lowest) based on the counts from value_counts().


sns.countplot(data=df, y='rating', order=df['rating'].value_counts().index, palette='magma')
plt.title('Content Rating Distribution')
plt.xlabel('Number of Titles')
plt.ylabel('Rating')
plt.show()

# graph indiacting distribution of movie duration
'''
   movies_df['duration_int'] = movies_df['duration'].str.extract('(\d+)').astype(float):
   str.extract('(\d+)'): Extracts the first sequence of digits from the duration column (e.g., "120 min" → "120").
   .astype(float): Converts the extracted strings to floating-point numbers.
'''
'''
   sns.histplot(movies_df['duration_int'].dropna(), bins=30, kde=True, color='skyblue'):
   movies_df['duration_int'].dropna(): Removes NaN values from duration_int to ensure valid data for plotting.
   bins=30: Divides the data into 30 bins for the histogram.
   kde=True: Adds a Kernel Density Estimate (KDE) curve to show the smoothed distribution.
   color='skyblue': Sets the histogram color to sky blue.
   Creates a histogram showing the frequency of movie durations.
'''


movies_df['duration_int'] = movies_df['duration'].str.extract('(\d+)').astype(float)
sns.histplot(movies_df['duration_int'].dropna(), bins=30, kde=True, color='skyblue')
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.show()


# this graph shows the seson counts of top 10 TV Shows


tv_show_seasons = tv_shows_df['duration'].value_counts().head(10)
sns.barplot(x=tv_show_seasons.values, y=tv_show_seasons.index, palette='autumn')
plt.title('TV Show Season Counts')
plt.xlabel('Number of Shows')
plt.ylabel('Seasons')
plt.show()




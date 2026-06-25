import pandas as pd
import openpyxl


# Specify the path to your Excel file
file_path = ""  

# QUESTON 1

# Read the Excel file
df_nflx_top_10 = pd.read_excel(file_path, sheet_name="NFLX Top 10", engine="openpyxl")

# filtered_df when category = Films(English)
films_english_df = df_nflx_top_10[df_nflx_top_10['category'] == "Films (English)"]
print(films_english_df.head())

# Find the most appeared title
most_appeared_title = films_english_df['show_title'].mode()[0]
print(most_appeared_title)

# Filter Dataframe having rows only with the most appeared title
most_appeared_title_df = films_english_df[films_english_df['show_title'] == most_appeared_title]
print(most_appeared_title_df)



# Calculate average weekly hours for most appeared title
avg_weekly_hours_viewed_most_appeared_title = most_appeared_title_df['weekly_hours_viewed'].mean()
print(f"The avg weekly hours for {most_appeared_title} is {avg_weekly_hours_viewed_most_appeared_title}")



df_imdb_rating = pd.read_excel(file_path, sheet_name="IMDB Rating", engine="openpyxl")
# print(df_imdb_rating.head())

# Perform a LEFT JOIN on 'show_title and title'
left_join_df = pd.merge(films_english_df, df_imdb_rating, left_on='show_title', right_on='title', how='left')

# Get the title where rating is the lowest
lowest_rated_title = left_join_df.loc[left_join_df['rating'].idxmin(), 'title']
print(lowest_rated_title)

# Filter Dataframe having rows only with the lowest rated IMDB title in 
lowest_rated_title_df = left_join_df[left_join_df['show_title'] == lowest_rated_title]
print(lowest_rated_title_df)

# Calculate average weekly hours for lowest rated english(Films) title
avg_weekly_hours_viewed_lowest_rated_title = lowest_rated_title_df['weekly_hours_viewed'].mean()
print(f"The avg weekly hours for {lowest_rated_title} is {avg_weekly_hours_viewed_lowest_rated_title}")



#filtered_df when category = Films(Non-English)
films_non_eng_df = df_nflx_top_10[df_nflx_top_10['category'] == "Films (Non-English)"]
print(films_non_eng_df.head())

# Film that has spent the most weeks in the top 10
most_weeks_top_10_non_eng_movie = films_non_eng_df.loc[films_non_eng_df['cumulative_weeks_in_top_10'].idxmax(), 'show_title']
print(most_weeks_top_10_non_eng_movie)




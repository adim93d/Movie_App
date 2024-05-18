"""import csv

# Open the CSV file in read mode
data_dict = {}
with open('movies.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file, delimiter=',')
    next(reader)
    print()
    # Iterate through each row in the CSV file
    for row in reader:
        # Get the movie name, rating, release date, and poster link
        movie_name = row[0]
        rating = row[1]
        release_date = row[2]
        poster_link = row[3]

        data_dict[movie_name] = {
            "rating": rating,
            "year": release_date,
            "poster": poster_link
        }

        # Display the information in the desired format
        print("Movie Name:", movie_name)
        print("Rating:", rating)
        print("Release Date:", release_date)
        print("Poster Link:", poster_link)
        print()

print(data_dict)
"""

data = self.read_file()
in_data = True
title_search = input("Enter title for new movie: ")
while in_data:
    if title_search in data:
        print('Movie already exist')
        title_search = input("Enter title for new movie: ")
    elif title_search not in data:
        in_data = False
try:
    res = requests.get(REQUEST_URL + API_KEY + SEARCH_BY_TITLE + title_search)
    res_content = json.loads(res.content)
    try:
        rating = res_content["Ratings"][0]["Value"]
        title = res_content["Title"]
        year = res_content["Year"]
        poster = res_content["Poster"]
        new_data = {title: {'rating': rating, 'year': year, 'poster': poster}}
        data.update(new_data)
        print("Movie added to the database")
    except KeyError:
        print("Key error, Movie not found")

except requests.exceptions.ConnectionError:
    print("Internet connection error, Please check your connection and try again")
try:
    with open('movies.json', 'w') as handle:
        json.dump(data, handle, indent=4)
except Exception:
    print('Error writing to file')



# Convert JSON data to a Python object
data = json.loads(json_data)

# Specify the existing CSV file path
csv_file_path = "existing_data.csv"

# Open the CSV file in append mode
with open(csv_file_path, mode='a', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the new data to the CSV file
    for row in data:
        writer.writerow([row["name"], row["age"]])

"""Take this method and implement it in the 'Delete_movie' method"""
import pandas as pd
data = pd.read_csv(self.file_path, index_col='id')
data = df.drop(title)
data.to_csv(self.file_path, index=True)

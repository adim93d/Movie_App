import csv
import json
import requests
from istorage import IStorage
import pandas as pd


REQUEST_URL = 'https://www.omdbapi.com/?'
API_KEY = 'apikey=3ac01df6'
SEARCH_BY_TITLE = '&t='


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    #
    def read_file(self):
        with open(self.file_path, 'r+') as handle:
            data = csv.reader(handle)
        return data

    def csv_to_dict(self):
        # Open the CSV file in read mode
        movies_dict = {}
        with open(self.file_path, 'r') as file:
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

                movies_dict[movie_name] = {
                    "rating": rating,
                    "year": release_date,
                    "poster": poster_link
                }
        return movies_dict

    def movies_data_dict(self):
        movies = self.csv_to_dict()
        return movies

    def list_movies(self):

        """
        Display the number of movies and their Title:Ratings
        """

        movies = self.csv_to_dict()
        print(f"\n{len(movies)} Movies in total")
        for key, value in movies.items():
            print(f"\nName: {key}\n"
                  f"Rating: {value['rating']}\n"
                  f"Year: {value['year']}\n"
                  f"Poster URL: {value['poster']}")

    def add_movie(self):

        """
        Adds a Movie:Rating to the Database
        """

        dict_data = self.csv_to_dict()
        in_data = True
        title_search = input("Enter title for new movie: ")
        while in_data:
            if title_search in dict_data:
                print('Movie already exist')
                title_search = input("Enter title for new movie: ")
            elif title_search not in dict_data:
                in_data = False
        try:
            res = requests.get(REQUEST_URL + API_KEY + SEARCH_BY_TITLE + title_search)
            res_content = json.loads(res.content)
            try:
                rating = res_content["Ratings"][0]["Value"]
                title = res_content["Title"]
                year = res_content["Year"]
                poster = res_content["Poster"]
                with open(self.file_path, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([title, rating, year, poster])
                print("Movie added to the database")
            except KeyError:
                print("Key error, Movie not found")
        except requests.exceptions.ConnectionError:
            print("Internet connection error, Please check your connection and try again")

    def delete_movie(self):
        """
        Delete a Movie:Rating from the Database
        """
        dict_data = self.csv_to_dict()
        found_in_database = False
        title = input("Enter name of movie to delete: ")
        while not found_in_database:
            if title in dict_data:
                data = pd.read_csv(self.file_path, index_col='title')
                data = data.drop(title)
                data.to_csv(self.file_path, index=True)
                found_in_database = True
                print("Movie Deleted")
            else:
                print("\nError, Movie not found. Please try again")
                title = input("Enter name of movie to delete: (You can quit to menu by writing: 'quit')")
                if title == "quit":
                    break

    def update_movie(self):
        # """
        # Update a Movie's Rating at the Database
        # """
        # title = input("Enter movie name to update rating: ")
        # with open(self.file_path, 'r') as file:
        #     reader = csv.reader(file)
        #     rows = list(reader)
        #     in_movies = False
        #     while not in_movies:
        #         for row in rows:
        #             if row[0] == title:
        #                 in_movies = True
        #                 new_rating = float(input("Enter updated rating: "))
        #                 row[1] = float(new_rating)
        #                 break
        #             else:
        #                 print("\nError, Movie not found. Please try again")
        #                 title = input("Enter movie name to update rating: (You can quit to menu by writing: 'quit')")
        #                 if title == "quit":
        #                     break
        # with open(self.file_path, 'w', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerows(rows)
        """
        Update a Movie's Rating at the Database
        """
        title = input("Enter movie name to update rating: ")
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            in_movies = False
            while not in_movies:
                for row in rows:
                    print('in rows')
                    if row[0] == title:
                        in_movies = True
                        new_rating = float(input("Enter updated rating: "))
                        rows[1] = float(new_rating)
                        break
                    else:
                        print('not in rows')
                        print("\nError, Movie not found. Please try again")
                        title = input("Enter movie name to update rating: (You can quit to menu by writing: 'quit')")
                    if title == "quit":
                        break
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

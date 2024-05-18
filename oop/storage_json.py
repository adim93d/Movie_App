import json
import requests
from istorage import IStorage

REQUEST_URL = 'https://www.omdbapi.com/?'
API_KEY = 'apikey=3ac01df6'
SEARCH_BY_TITLE = '&t='


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r+') as handle:
            data = json.load(handle)
        return data

    def json_to_dict(self):
        data = self.read_file()
    # Convert the data into a dictionary
        movies_dict = {}
        for movie in data:
            movie_data = data[movie]
            movie_dict = {
                "rating": movie_data["rating"],
                "year": movie_data["year"],
                "poster": movie_data["poster"]
            }
            movies_dict[movie] = movie_dict
        return movies_dict

    def movies_data_dict(self):
        movies = self.json_to_dict()
        return movies

    def list_movies(self):
        """
        Display the number of movies and their Title:Ratings
        """
        movies = self.json_to_dict()
        print(f"\n{len(movies)} Movies in total")
        for key, value in movies.items():
            print(f"\nName:{key}\n"
                  f"Rating: {value['rating']}\n"
                  f"Year: {value['year']}\n"
                  f"Poster URL: {value['poster']}")

    def add_movie(self):
        """
        Adds a Movie:Rating to the Database
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

    def delete_movie(self):
        """
        Delete a Movie:Rating from the Database
        """
        data = self.read_file()
        found_in_database = False
        title = input("Enter name of movie to delete: ")
        while not found_in_database:
            if title in data:
                del data[title]
                found_in_database = True
                print("Movie Deleted")
            else:
                print("\nError, Movie not found. Please try again")
                title = input("Enter name of movie to delete: (You can quit to menu by writing: 'quit')")
                if title == "quit":
                    break
        with open('movies.json', 'w') as handle:
            json.dump(data, handle)

    def update_movie(self):
        """
        Update a Movie's Rating at the Database
        """
        data = self.read_file()
        title = input("Enter movie name to update rating: ")
        in_movies = False
        while not in_movies:
            if title in data:
                in_movies = True
                rating_to_update = float(input("Enter updated rating: "))
                data[title]['rating'] = rating_to_update
                print("Rating updated")
            else:
                print("\nError, Movie not found. Please try again")
                title = input("Enter movie name to update rating: (You can quit to menu by writing: 'quit')")
                if title == "quit":
                    break

        with open('movies.json', 'w') as handle:
            json.dump(data, handle)


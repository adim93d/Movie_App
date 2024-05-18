from istorage import IStorage
import storage_json
import statistics


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        ...

    def _command_movie_best_rated(self):
        """
        Display the best rated movies from the database
        """
        movies = self._storage.read_file()
        highest_rated_movie_counter = 0
        movie_ratings = [float(value['rating'][0:3]) for key, value in movies.items()]
        highest_rated = max(movie_ratings)
        for key, value in movies.items():
            rating = value['rating'][0:3]
            if highest_rated == float(rating) \
                    and highest_rated_movie_counter == 0:
                print(f"The best rated movie is: {key} with a rating of {highest_rated}")
                highest_rated_movie_counter += 1
            elif highest_rated == float(rating) \
                    and highest_rated_movie_counter == 1:
                print(f"Movies with the same rating of: {rating}")
                print(key)
                highest_rated_movie_counter += 1
            elif highest_rated == float(rating) \
                    and highest_rated_movie_counter > 1:
                print(key)

    def _command_movie_worst_rated(self):
        """
        Display the worst rated movies from the database
        """
        movies = self._storage.read_file()
        lowest_rated_movie_counter = 0
        movie_ratings = [float(value['rating'][0:3]) for key, value in movies.items()]
        lowest_rated = min(movie_ratings)
        for key, value in movies.items():
            rating = value['rating'][0:3]
            if lowest_rated == float(rating) \
                    and lowest_rated_movie_counter == 0:
                print(f"The worst rated movie is: {key} with a rating of {lowest_rated}")
                lowest_rated_movie_counter += 1
            elif lowest_rated == float(rating) \
                    and lowest_rated_movie_counter == 1:
                print(f"Movies with the same rating of: {rating}")
                print(key)
                lowest_rated_movie_counter += 1
            elif lowest_rated == float(rating) \
                    and lowest_rated_movie_counter > 1:
                print(key)

    def _command_movie_stats(self):
        """
        Display the best and the worst rated movies from the database
        Display the median and the average ratings
        """
        movies = self._storage.read_file()
        number_of_items = int(len(movies))
        value_counter = 0.0
        median_list = []
        for key, value in movies.items():
            rating = value['rating'][0:3]
            value_counter = value_counter + float(rating)
            median_list.append(float(rating))

        average_value = value_counter / number_of_items
        print(f"\nThe average rating is {average_value}")
        print(f"The median rating is {statistics.median(median_list)}")
        self._command_movie_best_rated()
        self._command_movie_worst_rated()

    def _command_movie_random_movie(self):
        """
        Suggests a random movie and show their rating
        """
        movies = self._storage.read_file()
        import random
        list_items = list(movies.items())
        random_title = random.choice(list_items)
        print(f"\nThe movie for tonight is: {random_title[0]},"
              f" It is rated {random_title[1]['rating']}")

    def _command_movie_search_movie(self):
        """
        Search the Database with case-insensitive
        """
        movies = self._storage.read_file()
        movie_to_search = input("Enter name to search: ")
        for key, value in movies.items():
            if movie_to_search in key.casefold():
                print(f"\nName: {key}\n"
                      f"Rating: {value['rating']}\n"
                      f"Year: {value['year']}")

    def _command_movie_movie_sorted_by_rating(self):
        """
        Sort the database by the value at a descending order
        """
        movies = self._storage.read_file()
        sorted_movies = sorted(movies.items(),
                               key=lambda movie: movie[1]['rating'][0:3],
                               reverse=True)
        for key, value in sorted_movies:
            print(f"{key}: {value['rating']}")

    def _generate_website(self):
        output = self.serialize_movies()
        title_html = "Movie Database"
        with open("index_template.html", "r") as handle1:
            data2 = handle1.read()

        try:
            with open("index.html", "w") as handle2:
                handle2.write(data2.replace("__TEMPLATE_TITLE__", title_html)
                              .replace("__TEMPLATE_MOVIE_GRID__", output))
                print("Website generated successfully ")
        except Exception:
            print("Error Generating Website")

    def serialize_movies(self):
        movies = self._storage.read_file()
        output = ""
        for key, value in movies.items():
            output += "    <li>\n"
            output += "        <div class='movie'>\n"
            if "N/A" != value['poster']:
                output += f"            <img class='movie-poster'\n" \
                          f"            src='{value['poster']}'\n" \
                          f"            title= ''/>\n"
            output += f"            <div class='movie-title'>{key}</div>\n"
            output += f"            <div class='movie-rating'>{value['rating']}</div>\n"
            output += f"            <div class='movie-year'>{value['year']}</div>\n"
            output += '        </div>\n'
            output += '    </li>\n'
        return output

    def headline(self):
        """
        Display the headline
        """
        header = "********** My Movies Procrastination Database **********"
        print(header)

    def main_menu(self):
        """
        Display the menu
        """
        menu = ("""
    Menu:
    0. Exit the database
    1. List movies
    2. Add movie
    3. Delete movie
    4. Update movie
    5. Stats
    6. Random movie
    7. Search movie
    8. Movies sorted by rating
    9. Generate Website""")

        print(menu)
        menu_input = int(input("\nEnter choice (0-9): "))
        while menu_input < 10:
            if menu_input == 0:
                print("Good Bye!")
                quit()
            elif menu_input == 1:
                self._storage.list_movies()
            elif menu_input == 2:
                self._storage.add_movie()
            elif menu_input == 3:
                self._storage.delete_movie()
            elif menu_input == 4:
                self._storage.update_movie()
            elif menu_input == 5:
                self._command_movie_stats()
            elif menu_input == 6:
                self._command_movie_random_movie()
            elif menu_input == 7:
                self._command_movie_search_movie()
            elif menu_input == 8:
                self._command_movie_movie_sorted_by_rating()
            elif menu_input == 9:
                self._generate_website()
            input("\nPress Enter to continue")
            print(menu)
            menu_input = int(input("\nEnter choice (0-9): "))
        return menu_input

    def run(self):
        self.headline()
        self.main_menu()

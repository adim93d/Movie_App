import statistics
import main2


def best_rated():
    """
    Display the best rated movies from the database
    """
    movies = main.read_json_file()
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


def worst_rated():
    """
    Display the worst rated movies from the database
    """
    movies = main.read_json_file()
    lowest_rated_movie_counter = 0
    movie_ratings = [float(value['rating'][0:3]) for key, value in movies.items()]
    lowest_rated = min(movie_ratings)
    for key, value in movies.items():
        rating = value['rating'][0:3]
        if lowest_rated == float(rating)\
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


def stats():
    """
    Display the best and the worst rated movies from the database
    Display the median and the average ratings
    """
    from statistics import median
    movies = main.read_json_file()
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
    best_rated()
    worst_rated()


def random_movie():
    """
    Suggests a random movie and show their rating
    """
    movies = main.read_json_file()
    import random
    list_items = list(movies.items())
    random_title = random.choice(list_items)
    print(f"\nThe movie for tonight is: {random_title[0]},"
          f" It is rated {random_title[1]['rating']}")


def search_movie():
    """
    Search the Database with case-insensitive
    """
    movies = main.read_json_file()
    movie_to_search = input("Enter name to search: ")
    for key, value in movies.items():
        if movie_to_search in key.casefold():
            print(f"\nName: {key}\n"
                  f"Rating: {value['rating']}\n"
                  f"Year: {value['year']}")


def movie_sorted_by_rating():
    """
    Sort the database by the value at a descending order
    """
    movies = main.read_json_file()
    sorted_movies = sorted(movies.items(),
                           key=lambda movie: movie[1]['rating'][0:3],
                           reverse=True)
    for key, value in sorted_movies:
        print(f"{key}: {value['rating']}")


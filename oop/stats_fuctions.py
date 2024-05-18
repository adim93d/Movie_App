# import statistics
# import main
#
#
# def best_rated():
#     """
#     Display the best rated movies from the database
#     """
#     movies = main.read_json_file()
#     highest_rated_movie_counter = 0
#     movie_ratings = [float(value['rating'][0:3]) for key, value in movies.items()]
#     highest_rated = max(movie_ratings)
#     for key, value in movies.items():
#         rating = value['rating'][0:3]
#         if highest_rated == float(rating) \
#                 and highest_rated_movie_counter == 0:
#             print(f"The best rated movie is: {key} with a rating of {highest_rated}")
#             highest_rated_movie_counter += 1
#         elif highest_rated == float(rating) \
#                 and highest_rated_movie_counter == 1:
#             print(f"Movies with the same rating of: {rating}")
#             print(key)
#             highest_rated_movie_counter += 1
#         elif highest_rated == float(rating) \
#                 and highest_rated_movie_counter > 1:
#             print(key)
#
#
# def worst_rated():
#     """
#     Display the worst rated movies from the database
#     """
#     movies = main.read_json_file()
#     lowest_rated_movie_counter = 0
#     movie_ratings = [float(value['rating'][0:3]) for key, value in movies.items()]
#     lowest_rated = min(movie_ratings)
#     for key, value in movies.items():
#         rating = value['rating'][0:3]
#         if lowest_rated == float(rating)\
#                 and lowest_rated_movie_counter == 0:
#             print(f"The worst rated movie is: {key} with a rating of {lowest_rated}")
#             lowest_rated_movie_counter += 1
#         elif lowest_rated == float(rating) \
#                 and lowest_rated_movie_counter == 1:
#             print(f"Movies with the same rating of: {rating}")
#             print(key)
#             lowest_rated_movie_counter += 1
#         elif lowest_rated == float(rating) \
#                 and lowest_rated_movie_counter > 1:
#             print(key)
#
#
# def stats():
#     """
#     Display the best and the worst rated movies from the database
#     Display the median and the average ratings
#     """
#     from statistics import median
#     movies = main.read_json_file()
#     number_of_items = int(len(movies))
#     value_counter = 0.0
#     median_list = []
#     for key, value in movies.items():
#         rating = value['rating'][0:3]
#         value_counter = value_counter + float(rating)
#         median_list.append(float(rating))
#
#     average_value = value_counter / number_of_items
#     print(f"\nThe average rating is {average_value}")
#     print(f"The median rating is {statistics.median(median_list)}")
#     best_rated()
#     worst_rated()

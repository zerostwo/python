from collections import defaultdict

user_movie_rating = defaultdict(lambda :defaultdict(int))

# Initialize ratings for Alice
user_movie_rating["Alice"]["LOR1"] =  4
user_movie_rating["Alice"]["LOR2"] =  5
user_movie_rating["Alice"]["LOR3"] =  3
user_movie_rating["Alice"]["SW1"]  =  5
user_movie_rating["Alice"]["SW2"]  =  3

print user_movie_rating
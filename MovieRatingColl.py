from Collections import defaultdict

movie_ratings = defaultdict(lambda: defaultdict(int))

# initialise move ratings
movie_ratings["Prevs"]["Drishyam"] = 5
movie_ratings["Prevs"]["Spiderman"] = 3
movie_ratings["Prevs"]["Master"] = 4
movie_ratings["Prevs"]["96"] = 4
movie_ratings["Prevs"]["Dil"] = 1

print(movie_ratings)

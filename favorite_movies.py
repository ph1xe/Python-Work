favorite_movies = {
    "Ben": ["Ratatouille", "Wall-E", "Grown Ups"],
    "Jason": ["Kingsman", "Madagascar", "Pixels"],
    "Sam": ["Grownups 2", "Click", "Back to the Future"],
    "Alex": ["Napoleon Dynamite", "Billy Madison", "The Truman Show"]
}

for k,v in favorite_movies.items():
    print(k ,'likes the following movies:')
    for movie in v:
        print('- ' + movie)
    # print('- ' + str(favorite_movies[i[1]]))
    # print('- ' + str(favorite_movies[i[2]]))

'''
    Recommend movies watched by friends to users
'''

movies_watched=[[1,'A'],[1,'B'],[1,'C'],[2,'A'],[2,'D'],[3,'W'],[3,'E'],[7,'T']]
users=[[1,2],[1,8],[2,9],[5,2],[8,3],[9,10]]

def addtoDict(dict, values):
    if values[0] in dict:
        dict[values[0]].append(values[1])
    else:
        dict[values[0]] = []
        dict[values[0]].append(values[1])

def recommendation(movies_watched, relationship):
    # code below
    userFriends = {} # {1 : [2,8], 2: [1,9]}
    userMovies = {}
    moviesPerUser = {}

    for users in relationship:
        addtoDict(userFriends, [users[0], users[1]])
        addtoDict(userFriends, [users[1], users[0]])

    for movies in movies_watched:
        addtoDict(userMovies, movies)

    # debug prints
    print(userFriends)
    print(userMovies)

    for user, friends in userFriends.items():
        moviesPerUser[user] = set()
        for friend in friends:
            if friend in userMovies:
                for movie in userMovies[friend]:
                    moviesPerUser[user].add(movie)

    return moviesPerUser

print(recommendation(movies_watched, users))

import database

DRAMA_FACTOR = 0.98
ANIMATION_FACTOR = 0.98
ACTION_FACTOR = 0.98
DOCUMENTARY_FACTOR = 0.99
COMEDY_FACTOR = 0.99
SF_FACTOR = 0.99
ROMANCE_FACTOR = 1.0
CRIMINAL_FACTOR = 1.0
ADVENTURE_FACTOR = 1.0
FAMILY_FACTOR = 1.0
FANTASY_FACTOR = 1.01
WAR_FACTOR = 1.01
HORROR_FACTOR = 1.03
THRILLER_FACTOR = 1.03
MYSTERY_FACTOR = 1.03
MUSICAL_FACTOR = 1.0
NOIR_FACTOR = 1.04
NONE = 1.0

factors = [DRAMA_FACTOR, FANTASY_FACTOR, NONE, HORROR_FACTOR, ROMANCE_FACTOR, ADVENTURE_FACTOR, THRILLER_FACTOR, NOIR_FACTOR, NONE, DOCUMENTARY_FACTOR, COMEDY_FACTOR, FAMILY_FACTOR, MYSTERY_FACTOR, WAR_FACTOR, ANIMATION_FACTOR, CRIMINAL_FACTOR, MUSICAL_FACTOR, SF_FACTOR, ACTION_FACTOR]

'''
영화 재평가. 
가중치 factors를 곱함. 영화 페이지에 3, 9페이지 없어서 제외함
'''
def rerate(movie_list):
    for movie in movie_list:
        if movie[2] == 3 or movie[2] == 9:
            continue
        movie[1] = str(float(movie[1]) * factors[movie[2]-1])

        database.input_db('movie_list', 'rerated_movie_table', movie[0],movie[1],movie[2], movie[3])
        


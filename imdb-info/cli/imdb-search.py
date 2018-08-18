#Import necessary libraries
import imdb
import sys

#Create instance of imdb class to get access object
ia = imdb.IMDb()

argument = sys.argv[1:]
query = ' '.join(argument)

movies = ia.search_movie(query)
movie_name = movies[0]
ia.update(movie_name)
movie_id = movie_name.movieID
movie_rating = movie_name['rating']

print("Movie Name: ",movie_name['title'])
print("Movie ID: ",movie_id)
print("IMDb Rating: ",movie_rating)
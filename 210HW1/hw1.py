# Name: Aarti Rao
# Data Management for Data Science Assignment 1
# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    movie_ratings_dictionary = {}
    lines = f.readlines() #takes in rating file name and returns a dictionary
    for line in lines: #taking this through each line of the file
        words = line.strip().split('|') #splits the name of the movie and the rating 
        movie = words[0] #this is the movie part of the like
        rating = float(words[1]) #this is the rating part of the dictionary
        if movie in movie_ratings_dictionary:
            movie_ratings_dictionary[movie].append(rating)
        else:
            movie_ratings_dictionary[movie] = [rating]
    return movie_ratings_dictionary #returns dictionary with 1 to 1 mapping from movie to genre
    #pass
    

# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW
    movie_genre_dictionary ={}
    lines = f.readlines() #reads the lines of the file
    for line in lines: #goes through the entire file
        words  = line.strip().split('|') #splitting each line by genre and by movie 
        genre = words[0].strip()#this is the genre
        movie = words[2].strip()#keep in mind the third index is the movie, not the second according to the sample file
        movie_genre_dictionary[movie] = genre #map from movie to genre
    return movie_genre_dictionary #return the dictionary
        
    #pass

# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW
    genre_dictionary ={}
    lines = d.items()
    for movie, genre in lines: #iterates through the input file
        if genre in genre_dictionary: # maps all the movies to that specific genre
            genre_dictionary[genre].append(movie) 
        else:
            genre_dictionary[genre] = [movie]
    return genre_dictionary #returns the dictionary
    
    #pass
    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    avg_Arr = {}
    lines = d.items()
    for movie, rate in lines: #itirates through the input file
        if rate:
            avg = (sum(rate))/(len(rate)) #calculates the average rating for each movie
            avg_Arr[movie] = avg #maps the movie to the average rating
    return avg_Arr #returns dictionary
    #pass
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating, 
    #in ranked order from highest to lowest average rating
    # WRITE YOUR CODE BELOW
    lines = d.items()
    popular = sorted(lines, key = lambda x: x[1], reverse = True) #using lambda to sort the dictionary from highest rating to lowest rating
    sorted_dict=dict(popular[:n]) #sort the dictionary by the average
    if len(sorted_dict) < n: #if there are fewer than n movies
        return sorted_dict #return the sorted dictionary
    else: #if there are more than n movies
        return dict(popular[:n]) #return the top n items
    #pass
    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    lines = d.items()
    filt_mov={} 
    for movie, rate in lines: #for iteration through the file
        if rate>=thres_rating: #if the average rating is greater or equal than the threshold 
            filt_mov[movie]=rate #map the movie to the average rating 
    return filt_mov #return the filtered movie
    #pass
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    genre1 = genre_to_movies.get(genre) #get the genre name
    genre_rate = {} #dictionary that will do a movie to average rating of movies
    for movies in genre1: 
        if movies in movie_to_average_rating: #if there is a movie in movie:average rating
            genre_rate[movies] = movie_to_average_rating[movies] #map the movie to the average rating
        else:
            return None
    cnt = Counter(genre_rate) #set a counter which sorts through the ratings
    return dict(cnt.most_common(n)) #return the movies as per the value of n
    pass
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    if genre in genre_to_movies:
        genre1 = genre_to_movies.get(genre) #get the genre name
    
    sum_of_movies = float(0.0) #initialize sum of the movies
    len_of_movies = float(0.0) #initialize length of the movies
        
    for movies in genre1: #for loop for iteration
        if movies in movie_to_average_rating: #if movies are in movie_to_average_rating dictionary
            rating = float(movie_to_average_rating[movies])
            sum_of_movies = sum_of_movies + rating #increment the sum with the rating
            len_of_movies = len_of_movies + 1 #increment the length
    avg = float(sum_of_movies/len_of_movies) #calculate the average
    return avg #return the average
    pass
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    cnt = Counter() #initialize counter
    
    for genre in genre_to_movies: #using code from 3.4
        sum_of_movies = float(0.0) #initialize sum of the movies
        len_of_movies = float(0.0) #initialize length of the movies
        
        for movies in genre_to_movies.get(genre): #for loop for iteration
            if movies in movie_to_average_rating: #if movies are in movie_to_average_rating dictionary
                rating = float(movie_to_average_rating[movies])
                sum_of_movies = sum_of_movies + rating #increment the sum with the rating
                len_of_movies = len_of_movies + 1 #increment the length
        avg = float(sum_of_movies/len_of_movies)
        cnt[genre] = avg
    
    
     #set a counter which sorts through the ratings
    return dict(cnt.most_common(n)) #return the movies as per the value of n
    pass

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to list of (movie,rating)
    # WRITE YOUR CODE BELOW
    
    u_ratings_dictionary = {}
    #lines = f.readlines() #takes in rating file name and returns a dictionary
    for line in open(f): #taking this through each line of the file
        movies, rating, uid = line.strip().split('|') #splits the name of the movie and the rating and the uid
        
        if uid in u_ratings_dictionary:
            u_ratings_dictionary[uid].append((movies,rating)) #append the tuple if its there
        else:    
            u_ratings_dictionary[uid] = [(movies,rating)]
    return u_ratings_dictionary #returns dictionary with 1 to 1 mapping from movie to genre
    #pass
    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    dict_genre_ratings = {}
    average = {}
    collection = user_to_movies[user_id]
    for movies, collection in collection:
        if movies in movie_to_genre:
            genre1 = movie_to_genre[movies]
            if genre1 not in dict_genre_ratings:
                dict_genre_ratings[genre1] = []
            dict_genre_ratings[genre1].append(collection)
    for genre1, movieratings in dict_genre_ratings.items():
        average[genre1]= sum(float(movieratings))/float(len(movieratings))
    return max(average)
        
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW

# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    
    pass

# -------- main function for your testing -----
def main():
     # write all your test code here
    # this function will be ignored by us when grading
    filename = open("movieRatingSample.txt")
    movie_rate = read_ratings_data(filename)
    print(" ")
    print("Answer to 1.1: ")
    print(movie_rate)
    print(" ")
    filename2 = open("movies.txt", "r")
    rate_genre = read_movie_genre(filename2)
    print("Answer to 1.2: ")
    print(rate_genre)
    print(" ")
    print("Answer to 2.1:")
    question21 = create_genre_dict(rate_genre)
    print(question21)
    print(" ")
    print("Answer to 2.2:")
    question22 = calculate_average_rating(movie_rate)
    print(question22)
    print(" ")
    print("Answer to 3.1:")
    question31 = get_popular_movies(question22)
    print(question31)
    print("top 3 ratings: ")
    top3 = get_popular_movies(question22, n=3) #to do the top 3 i passed n as 3
    print(top3)
    print(" ")
    print("Answer to 3.2:")
    question32 = filter_movies(question22, 3)
    print("Threshold rating is 3")
    print(question32)
    print("Threshold rating is 4")
    question32b = filter_movies(question22, 4)
    print(question32b)
    print(" ")
    print("Answer to 3.3:")
    genre = 'Action'
    question33 = get_popular_in_genre(genre,question21,question22)
    print(question33)
    print(" ")
    print("Answer to 3.4:")
    genre1 = 'Action'
    question34 = get_genre_rating(genre1, question21,question22)
    print("The Average is")
    print(question34)
    print(" ")
    print("Answer to 3.5:")
    question35 = genre_popularity(question21, question22)
    print(question35)
    print(" ")
    print("Answer to 4.1:")
    question41 = read_user_ratings("movieRatingSample.txt")
    print(question41)
    print("Answer to 4.2:")
    user_id = '45'
    question42 = get_user_genre(user_id, question41, rate_genre)
    print(question42)
    #pass
main()
    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions
    
# program will start at the following main() function call
# when you execute hw1.py


    
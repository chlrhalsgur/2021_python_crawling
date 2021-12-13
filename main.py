import crawling as crw
import database
import Rerating_movie
import tkinter_gui


crw.crawling_movie()
movie_list = database.print_db('movie_table') 
Rerating_movie.rerate(movie_list)
movie_list_r = database.print_db('rerated_movie_table')

tkinter_gui.make_front(movie_list, movie_list_r)


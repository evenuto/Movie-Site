import movies
import fresh_tomatoes

# create movie instances

aladdin = movies.Movie("Aladdin",
                       "1992",
                       "http://orig02.deviantart.net/f311/f/2011/006/6/f/6f220f30cbdfc7347faaec00745941eb-d36l2gz.jpg",  # noqa
                       "https://www.youtube.com/watch?v=gWLa6y7Z2TE")  # noqa
anastasia = movies.Movie("Anastasia",
                         "1997",
                         "https://images-na.ssl-images-amazon.com/images/I/514ZF1BA5HL._SY450_.jpg",  # noqa
                         "https://www.youtube.com/watch?v=eNj53-mu7xw")  # noqa
beauty_and_beast = movies.Movie("Beauty and the Beast",
                                "1991",
                                "http://i.dailymail.co.uk/i/pix/2017/01/18/20/3C3FA2B500000578-4133768-image-a-44_1484772618253.jpg",  # noqa
                                "https://www.youtube.com/watch?v=tRlzmyveDHE")  # noqa
cinderella = movies.Movie("Cinderella",
                          "1950",
                          "http://img.moviepostershop.com/cinderella-movie-poster-1950-1010439898.jpg",  # noqa
                          "https://www.youtube.com/watch?v=oWrRk732srE")  # noqa
frozen = movies.Movie("Frozen",
                      "2013",
                      "http://www.impawards.com/2013/posters/frozen_ver8_xlg.jpg",  # noqa
                      "https://www.youtube.com/watch?v=TbQm5doF_Uc")  # noqa
little_mermaid = movies.Movie("The Little Mermaid",
                              "1989",
                              "http://img.moviepostershop.com/the-little-mermaid-movie-poster-1989-1020351925.jpg",  # noqa
                              "https://www.youtube.com/watch?v=ZGZX5-PAwR8")  # noqa
mulan = movies.Movie("Mulan",
                     "1998",
                     "https://s-media-cache-ak0.pinimg.com/originals/50/48/52/504852f4be1bc12c61ec76056a2310e5.jpg",  # noqa
                     "https://www.youtube.com/watch?v=MsAniqGowKE")  # noqa
pocahontas = movies.Movie("Pocahontas",
                          "1995",
                          "http://www.impawards.com/1995/posters/pocahontas_xlg.jpg",  # noqa
                          "https://www.youtube.com/watch?v=wdp1jRKECZ8")  # noqa
sleeping_beauty = movies.Movie("Sleeping Beauty",
                               "1959",
                               "http://vignette4.wikia.nocookie.net/disney/images/a/a9/Sleeping_Beauty_poster.jpg/revision/latest?cb=20130717204800",  # noqa
                               "https://www.youtube.com/watch?v=0sUZBUl1cg8")  # noqa
tangled = movies.Movie("Tangled",
                       "2010",
                       "https://s-media-cache-ak0.pinimg.com/736x/80/3a/d0/803ad097c3c569651bdea9170023821a--tangled-dvd-tangled-movie.jpg",  # noqa
                       "https://www.youtube.com/watch?v=2f516ZLyC6U")  # noqa

# list of movies instances
movie_list = [aladdin, anastasia, beauty_and_beast, cinderella, frozen,
              little_mermaid, mulan, pocahontas, sleeping_beauty, tangled]

# opens movie web page using the movies instances created
fresh_tomatoes.open_movies_page(movie_list)

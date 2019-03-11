import media
import fresh_tomatoes

Devadas = media.Movie("Devadas", "Devadas",
                  "https://www.youtube.com/watch?v=sdYO8Si6HKQ")
# print(Devadas.storyline)
Aravinda Sametha = media.Movie("Aravinda Sametha",
                       "https://www.youtube.com/watch?v=MIBAkM2IbhI")
Agnathavasi = media.Movie("Agnathavasi",
						"https://www.youtube.com/watch?v=knaCsR6dr58")
Bharath Ane Nenu = media.Movie("Bharath Ane Nenu",
                      "https://www.youtube.com/watch?v=orkPrGSAETs")
Sailaja Reddy Alludu = media.Movie("Sailaja Reddy Alludu", "Movie",
                          "https://www.youtube.com/watch?v=v8FEpl9QmFU")
Silly Fellows = media.Movie("Silly Fellows", 
                       "https://www.youtube.com/watch?v=UXX29E4hGSQ")


movies = [Devadas, Aravinda Sametha, Agnathavasi, Bharath Ane Nenu, Sailaja Reddy Alludu ,Silly Fellows]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.__doc__)

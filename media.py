import project
import fresh_tomatoes

three_idiots = project.movie("3 idiots","https://fanart.tv/fanart/movies/20453/moviethumb/3-idiots-56dbe7b229ce5.jpg","https://www.youtube.com/watch?v=xvszmNXdM4w","2009","8.4")
fandf7 = project.movie("Furious 7","https://2.bp.blogspot.com/-KCErRWJaS40/VYKwVVkoG1I/AAAAAAAAAD8/EV3SUyi4vIQ/s1600/Fast-and-Furious-7-Poster.jpg","https://www.youtube.com/watch?v=Skpu5HaVkOc","2015","7.2")
fandf8 = project.movie("Fast 8", "http://www.fotolip.com/wp-content/uploads/2016/05/Fast-And-Furious-8-1.jpg", "https://www.youtube.com/watch?v=uisBaTkQAEs","2017","9.0")
inters = project.movie("Interstellar","http://www.movienewz.com/img/gallery/interstellar/posters/interstellar_movie_poster_4.jpg","https://www.youtube.com/watch?v=0vxOhd4qlnA","2014","8.6")
darkknight = project.movie("The Dark Knight","https://akalol.files.wordpress.com/2008/08/new-joker-poster-for-the-dark-knight.jpg","https://www.youtube.com/watch?v=_PZpmTj1Q8Q","2008","9.0")
nysm = project.movie("Now You See Me","https://image.tmdb.org/t/p/original/hGsi9bPp4PEQANCUxswQDLymJag.jpg","https://www.youtube.com/watch?v=4OtM9j2lcUA","2013","7.3")
Dil Bechara = project.movie("Dil Bechara", "https://filmyzilla.monster/server/5136/Dil-bechara-2020-bollywood-full-movie-hdrip.mp4.html", "https://youtu.be/QTaRXv1f1HA","2020", "7.8")
MS Dhoni:the untold story = project.movie("MS Dhoni: the untold story", "https://freehqfullmoviesdownload.blogspot.com/2016/10/ms-dhoni.html", "https://youtu.be/CJEAKC1KOgs","2016","7.8")

movies = [three_idiots, fandf7, fandf8, inters, darkknight, nysm, Dil Bechara, MS Dhoni:the untold story, Khuda Hafiz]
movies=sorted(movies, key=lambda movie:movie.name)
fresh_tomatoes.open_movies_page(movies)

#code ends

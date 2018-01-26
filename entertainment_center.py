import movie
import fresh_tomatoes

"List of movie objects created"

schindlers_list = movie.Movie("Schindler's List",
                              "Based on true story, "
                              "Schindler's List is a story of "
                              "how Oskar schindler saved "
                              "thousands of polish jews.",
                              "https://fanart.tv/fanart/movies/424"
                              "/movieposter/schindlers-list-52e73e7ba8e35.jpg",
                              "https://www.youtube.com/watch?v=JdRGC-w9syA")
twelve_angry_men = movie.Movie("12 ANGRY MEN",
                               "A story of a jury consisting "
                               "of 12 men debating about "
                               "deliberating guilt or acquital "
                               "of a defendant.",
                               "https://501mustseemoviesproject.files."
                               "wordpress.com/"
                               "2014/08/twelveangrymenposter.jpg",
                               "https://www.youtube.com/watch?v=Dosg0p7LAB4")
dil_chahta_hain = movie.Movie("Dil Chahta "
                              "Hain",
                              "A coming of age drama of three friends "
                              "in urban India.",
                              "http://static.koimoi.com/wp-content/"
                              "new-galleries/"
                              "2014/05/dil-chahta-hai-koimoi-readers"
                              "-view-Dil_Chahta_Hai.jpg",
                              "https://www.youtube.com/watch?v=m13b25V0B10")
sunny = movie.Movie("Sunny",
                    "A korean movie about high school friends' "
                    "reunion and a run down their memory lane.",
                    "http://static.dramastyle.com/images/3/1/5907/"
                    "Sunny-2011-Korean-Movie_66.jpg",
                    "https://www.youtube.com/watch?v=0J1wz97q5t4")
roman_holiday = movie.Movie("Roman Holiday",
                            "A story of adventures of a princess and "
                            "a reporter in Rome.",
                            "https://images-na.ssl-images-amazon.com/"
                            "images/M/MV5BMTE2MDM4MTMtZmNkZC00Y2QyLWE0YjU"
                            "tMTAxZGJmODMxMDM0XkEyXkFqcGdeQXVyNjc1NTYyMjg@."
                            "_V1_UY1200_CR88,0,630,1200_AL_.jpg",
                            "https://www.youtube.com/watch?v=9GzCG6lpFUw")
spirited_away = movie.Movie("Spirited Away",
                            "The story of Chihiro Ogino, "
                            "a sullen ten-year-old girl who, while moving to "
                            "a new neighborhood, enters the spirit world."
                            "After her parents are transformed "
                            "into pigs by the "
                            "witch Yubaba, Chihiro takes "
                            "a job working in Yubaba's "
                            "bathhouse to find a way to free "
                            "herself and her parents "
                            "and return to the human world.",
                            "https://fontmeme.com/images/"
                            "USA_full-spirited-away-poster.jpg",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

"Putting movie objects into an array"
cinemas = [schindlers_list, twelve_angry_men, roman_holiday,
           spirited_away, dil_chahta_hain, sunny]

"Rendering web page with movie info"
fresh_tomatoes.open_movies_page(cinemas)

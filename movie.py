import webbrowser

"A information website for movies"

"""Class providing blueprint for object movie
like title, storyline, link to poster image
and youtube trailer url"""

class Movie():

    "Constructor for the class"
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Class Defination
# __x__ means that 'x' is a predefined variables.
# Function __init__ ; it initializes or creates space in memory for new instance.
# """ quotes represents class documentation, which can be description of class or other information about the class.
# Movie.__doc__
# Class Variables are in all caps for e.g. VALID_RATINGS


import webbrowser

class Movie():
  """ This class contains variables and Methods which are related to Media. """

  VALID_RATINGS = ["G","PG","PG-13","R"]                    # Class Variable

  def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image_url
    self.trailer_youtube_url = trailer_youtube_url

  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
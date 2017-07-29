import webbrowser

#constructor that allows for creation of movie instances and showing movie trailers
class Movie():
    """This class provides movie related data"""
    
    def __init__(self, title, year, poster_image, trailer_youtube):
        self.title = title
        self.year = year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

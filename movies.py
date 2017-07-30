import webbrowser


# Movie class allows for creation of movie instances and showing movie trailers
class Movie():
    """
    This class provides movie related data
    """
    def __init__(self, title, year, poster_image, trailer_youtube):
        """
        Assigns a title, year of release, poster image url,
        and youtube trailer url to the instance being created
        """
        self.title = title
        self.year = year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens the youtube link to the trailer of the specified instance
        """
        webbrowser.open(self.trailer_youtube_url)

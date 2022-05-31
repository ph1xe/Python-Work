from re import M


class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year
    def getTitle(self):
        return self.title
    def getReleaseDate(self):
        return self.year
    def changeTitle(self, newTitle):
        self.title = newTitle
    def setReleaseDate(self, newYear):
        self.year = newYear
    def __str__(self):
        return '{} was released in {}.'.format(self.title, self.year)

title = input('Enter the movie title: ')
year = int(input('Enter the release year: '))
movie = Movie(title, year)

print(movie)

title = input('Enter the movie title: ')
year = int(input('Enter the release year: '))
movie.changeTitle(title)
movie.setReleaseDate(year)

print(movie)
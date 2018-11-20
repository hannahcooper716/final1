import unittest
import proj1_w18 as proj1
import json

data = open('sample_json.txt', 'r')
info = json.load(data)
data.close()
# for x in info:
# 	x = json.loads(x)
# 	if x["wrapperType"] == 'track':
# 		if x["kind"] == 'feature-movie':
# 			Movie = Movie(json = x)
# 		if x["kind"] == 'song':
# 			Song = Song(json = x)
# 	if ['wrapperType'] == 'audiobook':
# 			Media = Media(json = x)

class TestMedia(unittest.TestCase):

    def testConstructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")
        m3 = proj1.Media("Star Wars", "Hannah", 1876)

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m3.year, 1876)

    def testMediastr(self):
        m2 = proj1.Media("1999", "Prince")

        self.assertEqual(m2.__str__(), "1999 by Prince (No Year)")

    def testMedialen(self):
        m2 = proj1.Media("1999", "Prince")

        self.assertEqual(m2.__len__(), 0)

    def testSong(self):
        m = proj1.Song()
        #title="No Title", author="No Author", releaseyear="No Year", album="No Album", genre="No Genre", tracklen="No Track Length"
        m1 = proj1.Song("Payphone", "Maroon 5", 2013, "Hannah", "pop", 5)


        self.assertEqual(m.title, "No Title")
        self.assertEqual(m.author, "No Author")
        self.assertEqual(m.year, "No Year")
        self.assertEqual(m.album, "No Album")
        self.assertEqual(m.genre, "No Genre")
        self.assertEqual(m.tracklen, "No Track Length")

        self.assertEqual(m1.title, "Payphone")
        self.assertEqual(m1.author, "Maroon 5")
        self.assertEqual(m1.year, 2013)
        self.assertEqual(m1.album, "Hannah")
        self.assertEqual(m1.genre, "pop")
        self.assertEqual(m1.tracklen, 5)

    def testSongstr(self):
        m1 = proj1.Song("Payphone", "Maroon 5", 2013, "Hannah", "pop", 5)

        self.assertEqual(m1.__str__(), "Payphone by Maroon 5 (2013)[pop]")

    def testSonglen(self):
        m1 = proj1.Song("Payphone", "Maroon 5", 2013, "Hannah", "pop", 5)

        self.assertEqual(m1.__len__(), 5)

    def testMovie(self):
        m = proj1.Movie()
        #self, title="No Title", author="No Author", releaseyear="No Year", rating="No Rating", movielen="No Movie Length"
        m1 = proj1.Movie("Stars", "Green", 2000, "R", 3)

        self.assertEqual(m.title, "No Title")
        self.assertEqual(m.author, "No Author")
        self.assertEqual(m.year, "No Year")
        self.assertEqual(m.rating, "No Rating")
        self.assertEqual(m.movielen, "No Movie Length")

        self.assertEqual(m1.title, "Stars")
        self.assertEqual(m1.author, "Green")
        self.assertEqual(m1.year, 2000)
        self.assertEqual(m1.rating, "R")
        self.assertEqual(m1.movielen, 3)

    def testMoviestr(self):
        m1 = proj1.Movie("Stars", "Green", 2000, "R", 3)

        self.assertEqual(m1.__str__(), "Stars by Green (2000)[R]")

    def testMovielen(self):
        m1 = proj1.Movie("Stars", "Green", 2000, "R", 3)

        self.assertEqual(m1.__len__(), 3)

    def test_jsonMediainit(self):
        m = proj1.Media(json = info[2])
        self.assertEqual(m.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(m.author, "Helen Fielding")
        self.assertEqual(m.year, 2012)

    def test_jsonMediastr(self):
        m = proj1.Media(json = info[2])
        self.assertEqual(m.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")

    def test_jsonMedialen(self):
        m = proj1.Media(json = info[2])
        self.assertEqual(m.__len__(), 0)

    def test_jsonMovieinit(self):
        m = proj1.Movie(json = info[0])
        self.assertEqual(m.title, "Jaws")
        self.assertEqual(m.author, "Steven Spielberg")
        self.assertEqual(m.year, 1975)
        self.assertEqual(m.rating, "PG")
        self.assertEqual(m.movielen, 124.19091666666667)

    def test_jsonMoviestr(self):
        m = proj1.Movie(json = info[0])
        self.assertEqual(m.__str__(), 'Jaws by Steven Spielberg (1975)[PG]')

    def test_jsonMovielen(self):
        m = proj1.Movie(json = info[0])
        self.assertEqual(m.__len__(), 124)

    def test_jsonSonginit(self):
        m = proj1.Song(json = info[1])
        self.assertEqual(m.title, "Hey Jude")
        self.assertEqual(m.author, "The Beatles")
        self.assertEqual(m.year, 1968)
        self.assertEqual(m.genre, "Rock")
        self.assertEqual(m.tracklen, 431.333)
        self.assertEqual(m.album, "TheBeatles 1967-1970 (The Blue Album)")

    def test_jsonSongstr(self):
        m = proj1.Song(json = info[1])
        self.assertEqual(m.__str__(), "Hey Jude by The Beatles (1968)[Rock]")

    def test_jsonSonglen(self):
        m = proj1.Song(json = info[1])
        self.assertEqual(m.__len__(), 431)

#part 3
    def test_itunesAPI(self):
        baby = proj1.ItunesAPI('baby')
        love = proj1.ItunesAPI('love')
        babylove = ('baby','love')
        together = proj1.ItunesAPI(babylove)
        self.assertEqual(len(baby), 10)
        self.assertEqual(len(love), 10)
        self.assertEqual(len(together), 10)

    def test_itunesAPI1(self):
        moana = proj1.ItunesAPI('moana')
        helterskelter = proj1.ItunesAPI('helter skelter')
        self.assertEqual(len(helterskelter), 10)
        self.assertEqual(len(moana), 10)

    def test_itunesAPI2(self):
        random = proj1.ItunesAPI('#$%^&^%$#$%^%$%^&*&*(*&*&^&*&^%)')
        self.assertEqual(len(random), 0)

unittest.main()

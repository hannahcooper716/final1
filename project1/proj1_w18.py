import json
import requests
import webbrowser

class Media:

	def __init__(self, title="No Title", author="No Author", releaseyear="No Year", json=None):
		if json is not None:
			try:
				self.title = json["trackName"]
				self.author = json["artistName"]
				self.year = int(json["releaseDate"][:4])
			except:
				self.title = json["collectionName"]
				self.author = json["artistName"]
				self.year = int(json["releaseDate"][:4])
		else:
			self.title = title
			self.author = author
			self.year = releaseyear
	def __str__(self):
		return "{} by {} ({})".format(self.title, self.author, self.year)
	def __len__(self):
		return 0

# Other classes, functions, etc. should go here

class Song(Media):
	def __init__(self, title="No Title", author="No Author", releaseyear="No Year", album="No Album", genre="No Genre", tracklen="No Track Length", json=None):
		super().__init__(title, author, releaseyear, json)
		if json is not None:
			self.genre = json["primaryGenreName"]
			self.tracklen = json["trackTimeMillis"] * 0.001
			self.album = json["collectionName"]
		else:
			self.genre = genre
			self.tracklen = tracklen
			self.album = album
	def __str__(self):
		return super().__str__() + "[" + self.genre + "]"
	def __len__(self):
		return int(self.tracklen)

class Movie(Media):
	def __init__(self, title="No Title", author="No Author", releaseyear="No Year", rating="No Rating", movielen="No Movie Length", json=None):
		super().__init__(title, author, releaseyear, json)
		if json is not None:
			self.rating = json["contentAdvisoryRating"]
			self.movielen = json["trackTimeMillis"] * .001/60
		else:
			self.rating = rating
			self.movielen = movielen
	def __str__(self):
		return super().__str__() + "[" + self.rating + "]"
	def __len__(self):
		return int(round(self.movielen, 0)) #need to check if this is how to round


# data = open('sample_json.txt', 'r')
# info = list(data.readlines())
# for x in info:
# 	x = json.loads(x)
def ItunesAPI(p):
	base_itunes_url = 'https://itunes.apple.com/search'
	req = requests.get(base_itunes_url, params = {'term': p, 'limit': 10})
	d = json.loads(req.text)
	l = d['results']
	return l

#print(ItunesAPI('baby'))


if __name__ == "__main__":
	resp = input('Enter a search term, or “exit” to quit: ')
	while resp != "exit":
		media = {}
		song = {}
		movie = {}
		number = 0
		user = ItunesAPI(resp)
		if len(resp)==0:
			resp = input('Enter a search term, or “exit” to quit: ')
			continue
		for x in user:
			if x["wrapperType"] == 'track':
				link = x["trackViewUrl"]
				if x["kind"] == 'feature-movie':
					mov = Movie(json = x)
					movie[link]= mov.__str__()
				elif x["kind"] == 'song':
					So = Song(json = x)
					song[link] = So.__str__()
				else:
				# 	#if x["kind"] != 'song' and 'feature-movie':
					Med = Media(json = x)
					media[link] = Med.__str__()
			else:
				link = x["collectionViewUrl"]
				Med = Media(json = x)
				media[link] = Med.__str__()


		print("OTHER MEDIA")
		number1 = {}
		for x in media:
			number = number +1
			number1[number] = x
			print(str(number)+" "+ media[x])
		print("MOVIE")
		for x in movie:
			number = number + 1
			number1[number] = x
			print(str(number)+" "+ movie[x])
		print("SONG")
		for x in song:
			number = number + 1
			number1[number] = x
			print(str(number)+" "+ song[x])


		r = input('Enter a number for more info, or another search term, or exit: ')
		try:
			if type(1)==type(int(r)):
				for x in number1.keys():
					if x == int(r):
						print("Launching " + number1[x] + ' in web browser')
						webbrowser.open(number1[x])

		except:
			resp = r
			if resp == 'exit':
				print("Bye!")

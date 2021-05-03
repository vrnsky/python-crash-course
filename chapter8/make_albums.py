def make_albums(artist, title, songs = None):
	album = {'artist': '', 'title': ''}
	album['artist'] = artist
	album['title'] = title
	if songs:
		album['songs'] = songs
	return album

fallout_boy_albums = make_albums('Fallout Boy', 'Centuries', 10)
for key, value in fallout_boy_albums.items():
	print(key.title(), "and their album", value)

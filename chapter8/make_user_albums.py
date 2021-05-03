def make_albums(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album


poll_active = True
while poll_active:
    print("Enter q in any step, to abort execution")
    artist = input("Enter an artist: ")
    if artist == 'q':
        break
    title = input("Enter a title: ")
    if title == 'q':
        break
    user_album = make_albums(artist, title)

    for key, value in user_album.items():
        print(key, "=", value)

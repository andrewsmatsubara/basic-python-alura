class Music:
  musics = []

  def __init__(self, name, artist, duration):
    self.name = name
    self.artist = artist
    self.duration = duration
    Music.musics.append(self)

  def list_musics():
    for music in Music.musics:
      print(f'{music.name} | {music.artist} | {music.duration}')

music_1 = Music('Music 1', 'Artist 1', '03:00')
music_2 = Music('Music 2', 'Artist 2', '04:00')
music_3 = Music('Music 3', 'Artist 3', '05:00')

Music.list_musics()
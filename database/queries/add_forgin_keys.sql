
""" Charts forgin keys"""
ALTER TABLE Charts
ADD FOREIGN KEY (track_id) REFERENCES Tracks(track_id);

ALTER TABLE Charts
ADD FOREIGN KEY (country_id) REFERENCES Countries(country_id);


""" Tracks forgin keys"""
ALTER TABLE Tracks
ADD FOREIGN KEY (artist_id) REFERENCES Artists(artist_id);

ALTER TABLE Tracks
ADD FOREIGN KEY (album_id) REFERENCES Albums(album_id);

ALTER TABLE Tracks
ADD FOREIGN KEY (genre_id) REFERENCES Genres(genre_id);


""" Lyrics forgin keys"""
ALTER TABLE Lyrics
ADD FOREIGN KEY (track_id) REFERENCES Tracks(track_id);


""" Artists forgin keys"""
ALTER TABLE Artists
ADD FOREIGN KEY (artist_country_id) REFERENCES Countries(country_id);


""" Albums forgin keys"""
ALTER TABLE Albums
ADD FOREIGN KEY (artist_id) REFERENCES Artists(artist_id);
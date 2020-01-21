-- For improving performance of the main track search feature
ALTER TABLE Tracks ADD INDEX track_name (track_name);
ALTER TABLE Artists ADD INDEX artist_name (artist_name);
ALTER TABLE Albums ADD INDEX album_name (album_name);
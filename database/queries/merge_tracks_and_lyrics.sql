CREATE TABLE IF NOT EXISTS TracksWithLyrics(
    track_id INT NOT NULL PRIMARY KEY,
    track_name VARCHAR(255),
    artist_id INT,
    album_id INT,
    genre_id INT,
    track_rating INT,
    track_release_date DATETIME,
    track_lyrics TEXT
   );


INSERT INTO TracksWithLyrics (TracksWithLyrics.track_id,TracksWithLyrics.track_name,TracksWithLyrics.artist_id,TracksWithLyrics.album_id,TracksWithLyrics.genre_id,TracksWithLyrics.track_rating,TracksWithLyrics.track_release_date,TracksWithLyrics.track_lyricsTracksWithLyrics)
SELECT  T.track_id,T.track_name ,T.artist_id,T.album_id , T.genre_id ,T.track_rating , T.track_release_date , L.track_lyrics
FROM Tracks T , Lyrics L
WHERE T.track_id = L.track_id


RENAME TABLE
Tracks TO TracksOld,
Lyrics TO LyricsOld



   RENAME TABLE
TracksWithLyrics TO Tracks
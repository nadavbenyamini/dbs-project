--====================================================================================================================--
-- 2) Creating the basic tables
--====================================================================================================================--
CREATE TABLE IF NOT EXISTS Countries(
    country_id VARCHAR(10) NOT NULL PRIMARY KEY,
    country_name VARCHAR(255),
    population INT
   );

CREATE TABLE IF NOT EXISTS Charts(
    country_id VARCHAR(10) NOT NULL,
    track_id INT NOT NULL,
    track_rank INT,
    PRIMARY KEY (country_id, track_id)
   );

CREATE TABLE IF NOT EXISTS Tracks(
    track_id INT NOT NULL PRIMARY KEY,
    track_name VARCHAR(255),
    artist_id INT,
    album_id INT,
    genre_id INT,
    track_rating INT,
    track_release_date DATETIME
   );

   CREATE TABLE IF NOT EXISTS Lyrics(
    track_id INT NOT NULL PRIMARY KEY,
    track_lyrics TEXT
   );

   CREATE TABLE IF NOT EXISTS Artists(
    artist_id INT NOT NULL PRIMARY KEY,
    artist_name VARCHAR(255),
    artist_rating INT,
    artist_country_id VARCHAR(10)
   );

   CREATE TABLE IF NOT EXISTS Albums(
    album_id INT PRIMARY KEY,
    artist_id INT NOT NULL ,
    album_name VARCHAR(255),
    album_release_date DATETIME,
    album_rating INT
   );

   CREATE TABLE IF NOT EXISTS Genres(
    genre_id INT NOT NULL PRIMARY KEY,
    genre_parent_id INT,
    genre_name VARCHAR(255)
   );

--====================================================================================================================--
-- 2) Merging Tracks and Lyrics to one table (after data insertion)
--====================================================================================================================--
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
INSERT INTO TracksWithLyrics (TracksWithLyrics.track_id,TracksWithLyrics.track_name,TracksWithLyrics.artist_id, TracksWithLyrics.album_id,TracksWithLyrics.genre_id,TracksWithLyrics.track_rating,TracksWithLyrics.track_release_date,TracksWithLyrics.track_lyricsTracksWithLyrics)
SELECT  T.track_id, T.track_name, T.artist_id, T.album_id, T.genre_id, T.track_rating, T.track_release_date, L.track_lyrics
  FROM Tracks T, Lyrics L
 WHERE T.track_id = L.track_id;

RENAME TABLE
Tracks TO TracksOld,
Lyrics TO LyricsOld;

RENAME TABLE
TracksWithLyrics TO Tracks;

--====================================================================================================================--
-- 3) Adding foreign keys
--====================================================================================================================--
ALTER TABLE Charts
ADD FOREIGN KEY (track_id) REFERENCES Tracks(track_id);

ALTER TABLE Charts
ADD FOREIGN KEY (country_id) REFERENCES Countries(country_id);

ALTER TABLE Tracks
ADD FOREIGN KEY (artist_id) REFERENCES Artists(artist_id);

ALTER TABLE Tracks
ADD FOREIGN KEY (album_id) REFERENCES Albums(album_id);

ALTER TABLE Tracks
ADD FOREIGN KEY (genre_id) REFERENCES Genres(genre_id);

ALTER TABLE Artists
ADD FOREIGN KEY (artist_country_id) REFERENCES Countries(country_id);

ALTER TABLE Albums
ADD FOREIGN KEY (artist_id) REFERENCES Artists(artist_id);

--====================================================================================================================--
-- 4) Adding indices to support the main track search query (the big table in the home page)
--====================================================================================================================--
ALTER TABLE Tracks ADD FULLTEXT(track_lyrics);
ALTER TABLE Tracks ADD INDEX track_name (track_name);
ALTER TABLE Artists ADD INDEX artist_name (artist_name);
ALTER TABLE Albums ADD INDEX album_name (album_name);

--====================================================================================================================--
-- 5) Adding views to reduce code duplication
--====================================================================================================================--

 -- This view flattens the tree structure of Genres to create on long list of genres
 -- Now filtering by genre_full_name like 'Rock%' e.g. results will include "Rock", "Rock/Hard Rock", etc.
 create or replace view GenresView as
 select g1.genre_id,
 		g2.genre_id as genre_parent_id,
 		case when g2.genre_id=34 or g2.genre_id is NULL
 			 then g1.genre_name
 			 else concat(g2.genre_name, '/', g1.genre_name) end as genre_full_name
  from Genres g1
  left join Genres g2 on g1.genre_parent_id = g2.genre_id
 where g2.genre_id is null
    or g1.genre_id != 34 -- 34="Music" so no point of displaying Music/Rock, Music/Pop etc. just Rock, Pop...
 order by genre_full_name

 -- One place for pulling and formatting all relevant details of a track
create or replace view TracksView as
 select t.track_id,
	    t.track_name,
	    t.album_id,
	    t.artist_id,
	    t.genre_id,
	    t.track_rating,
	    al.album_name,
	    ar.artist_name,
	    g.genre_parent_id,
	    g.genre_full_name as genre_name,
	    t.track_release_date,
	    DATE_FORMAT(t.track_release_date, '%M %d, %Y') as track_release_date_formatted,
	    t.track_lyrics
  from Tracks t
  left join GenresView g
    on g.genre_id = t.genre_id
  join Artists ar
    on ar.artist_id = t.artist_id
  join Albums al
    on al.album_id = t.album_id

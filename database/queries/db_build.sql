
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
    artist_id INT NOT NULL PRIMARY KEY,
    album_name VARCHAR(255),
    album_id INT,
    album_release_date DATETIME,
    album_rating INT
   );

   CREATE TABLE IF NOT EXISTS Genres(
    genre_id INT NOT NULL PRIMARY KEY,
    genre_parent_id INT,
    genre_name VARCHAR(255)
   );

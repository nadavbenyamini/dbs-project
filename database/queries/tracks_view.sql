create view TracksView as
 select t.track_id,
	    t.track_name,
	    t.album_id,
	    t.artist_id,
	    t.genre_id,
	    al.album_name,
	    ar.artist_name,
	    g.genre_name,
	    t.track_release_date,
	    t.track_lyrics
  from Tracks t
  join Genres g
    on g.genre_id = t.genre_id
  join Artists ar
    on ar.artist_id = t.artist_id
  join Albums al
    on al.album_id = t.album_id
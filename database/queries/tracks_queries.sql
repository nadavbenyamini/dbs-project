 # good example tracl_id =164504273

 SELECT DISTINCT t.track_id,  t.track_name , a.artist_name,al.album_name,genre_name AS track_genre, t.track_release_date
FROM Tracks t ,Artists a,Albums al ,Genres g, (SELECT MIN(c.track_rank) AS min_rank , MAX(c.track_rank) AS max_rank
						FROM 	 Charts c
						WHERE  c.track_id = "track_id"
						) AS  min_max_rank
WHERE a.artist_id = t.artist_id AND
		al.album_id =t.album_id AND
		g.genre_id =t.genre_id AND
		t.genre_id = (SELECT t2.genre_id
							FROM Tracks t2
							WHERE  t2.track_id = "track_id" ) AND
		t.track_id != "track_id"  AND
		min_max_rank.max_rank>=(SELECT AVG(c3.track_rank)
										FROM 	 Charts c3
										WHERE c3.track_id=t.track_id ) AND
		min_max_rank.min_rank<=(SELECT AVG(c4.track_rank)
										FROM 	 Charts c4
										WHERE c4.track_id=t.track_id );

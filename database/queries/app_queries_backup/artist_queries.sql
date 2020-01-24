	# good example artist_id = 29247465

# top countries for artist

SELECT cr.country_name ,
       SUM(101-c.track_rank) AS total_rank_in_country ,
       COUNT(t.track_id) AS  number_of_songs_on_country_chart,
       cr.population AS country_population
  FROM Tracks t , Charts c , Countries cr
 WHERE cr.country_id = c.country_id AND
			 c.track_id = t.track_id AND
			 t.artist_id = "artist id"
 GROUP BY cr.country_id
 ORDER BY total_rank_in_country DESC ;



# top songs for artist

SELECT t.track_name , al.album_name , SUM(101-c.track_rank) AS track_rating, t.track_release_date , g.genre_name AS track_genre
FROM Artists a , Tracks t , Charts c , Albums al, Genres g
WHERE a.artist_id = t.artist_id AND
		t.track_id = c.track_id AND
		al.album_id = t.album_id AND
		g.genre_id = t.genre_id AND
		a.artist_id = "artist id"
GROUP BY t.track_id
ORDER BY track_rating DESC ;

# relate artist list

SELECT DISTINCT a1.artist_name
FROM   	Artists a1, Tracks t1  ,Genres g1 ,
		(SELECT MAX(c.track_rank) AS max_rating , MIN(c.track_rank) AS min_rating
			FROM Artists a , Tracks t ,Charts c
			WHERE a.artist_id = t.artist_id AND
					c.track_id = t.track_id AND
					a.artist_id = "artist id") AS min_max_rating
WHERE a1.artist_id = t1.artist_id AND
		t1.genre_id =g1.genre_id AND
		g1.genre_id IN (SELECT DISTINCT  g0.genre_id
							 FROM Artists a0 , Tracks t0 , Genres g0
							 WHERE a0.artist_id = t0.artist_id AND
					  				t0.genre_id = g0.genre_id AND
					  			  	a0.artist_id = "artist id") AND
		t1.track_rating>=min_max_rating.min_rating AND
		t1.track_rating<=min_max_rating.max_rating;
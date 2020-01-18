# good example for country_id = "py"

# popular genres in country

SELECT g.genre_name , COUNT(DISTINCT g.genre_id) AS number_of_songs_in_chart
FROM Charts c , Tracks t , Genres g
WHERE c.country_id = %s AND
		c.track_id =t.track_id AND
		t.genre_id = g.genre_id
GROUP BY g.genre_id
ORDER BY number_of_songs_in_chart DESC;

# popular artist in country

SELECT a.artist_name , COUNT(DISTINCT a.artist_id) AS number_of_songs_in_chart
FROM Charts c , Tracks t ,Artists a
WHERE c.country_id = %s AND
		c.track_id =t.track_id AND
		t.artist_id = a.artist_id
GROUP BY a.artist_id
ORDER BY number_of_songs_in_chart DESC ;

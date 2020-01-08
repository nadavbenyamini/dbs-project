  select c.country_id,
	   ct.country_name,
	   c.track_rank,
	   t.track_id,
	   t.track_name,
	   al.album_name,
	   ar.artist_name,
	   g.genre_name,
	   t.track_release_date,
	   l.track_lyrics
  from Charts c
  left join Countries ct
    on ct.country_id = c.country_id
  left join Tracks t
    on c.track_id = t.track_id
  left join Genres g
    on g.genre_id = t.genre_id
  left join Artists ar
    on ar.artist_id = t.artist_id
  left join Albums al
    on al.album_id = t.album_id
  left join Lyrics l
    on l.track_id = t.track_id
 order by ct.population desc, c.track_rank
 limit 100






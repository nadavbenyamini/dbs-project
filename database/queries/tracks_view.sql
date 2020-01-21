-- Simplifying the process of pulling and formatting all relevant details of a track
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

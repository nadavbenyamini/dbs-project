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
  -- 34="Music" is the root genre so no point of displaying Music/Rock, Music/Pop etc. just Rock, Pop...
 where g2.genre_id is null or g1.genre_id != 34
 order by genre_full_name
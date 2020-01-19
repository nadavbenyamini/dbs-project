 create or replace view GenresView as
 select g1.genre_id,
 		g2.genre_id as genre_parent_id,
 		case when g2.genre_id=34 or g2.genre_id is NULL
 			 then g1.genre_name
 			 else concat(g2.genre_name, '/', g1.genre_name) end as genre_full_name
  from Genres g1
  left join Genres g2 on g1.genre_parent_id = g2.genre_id
 where g2.genre_id is null or g1.genre_id != 34 -- 34="Music" the root genre
   and g1.genre_name like '%/%'
 order by genre_full_name
select 'Countries' as table_name, count(*) as record_count from Countries union all  
select 'Charts' as table_name, count(*) as record_count from Charts union all  
select 'Tracks' as table_name, count(*) as record_count from Tracks union all   
select 'Genres' as table_name, count(*) as record_count from Genres union all   
select 'Albums' as table_name, count(*) as record_count from Albums union all    
select 'Lyrics' as table_name, count(*) as record_count from Lyrics union all 
select 'Artists' as table_name, count(*) as record_count from Artists
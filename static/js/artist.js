var table_songs = new Tabulator("#songs-table", {
    height:"311px",
    layout:"fitColumns",
    placeholder:"No Data Set",
    ajaxResponse:function(url, params, response){
        response.forEach(function(item){
			item["track_rating"] = item["track_rating"]/20
		})
        return response; //return the tableData property of a response json object
    },
        columns:[ //Define Table Columns
            {title:"Id", field:"al.artist_id", visible:false},
		    {title:"Id", field:"track_id", visible:false},
		    {title:"Id", field:"album_id", visible:false},
            {title:"Name", field:"track_name", width:150},
            {title:"Rating", field:"track_rating", align:"left", formatter:"star"},
            {title:"Album", field:"album_name"},
            {title:"Genere", field:"genre_name"},
            {title:"Release Date", field:"track_release_date"}
        ],
        rowClick:function(e, row){ 
            console.log(row.getData().track_id)
            url = `http://${server}:${port}/track/${row.getData().track_id}`
            console.log(url)
            location.replace(url)
        },
});

function temp(){
    artist_id = $("#artist_id").last().html();
    console.log(artist_id)
    table_songs.setData(`http://${server}:${port_api}/artist_tracks/${artist_id}`)
}
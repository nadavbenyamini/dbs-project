
function launch(){
    getChartsTable();
    getTracksTable();
}

function getTracksTable() {
    const artist_id = $("#artist_id").last().html();
    return new Tabulator("#songs-table", {
        height:"311px",
        layout:"fitColumns",
        placeholder:"No Data Set",
        ajaxURL: `http://${server}:${port_api}/artist_tracks/${artist_id}`,
        ajaxResponse:function(url, params, response){
            response.forEach(function(item){
                item["track_rating"] = item["track_rating"]/20
            });
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
        ]
    });
}

function getChartsTable() {
    const artist_id = $("#artist_id").last().html();
    return new Tabulator("#artist-chart", {
        height: "311px",
        layout: "fitColumns",
        placeholder: "No Data Set",
        ajaxURL: `http://${server}:${port_api}/artist_charts/${artist_id}`,
        ajaxResponse: function (url, params, response) {
            return response; //return the tableData property of a response json object
        },
        columns: [ //Define Table Columns
            {title: "album_name", field: "album_name"},
            {title: "country_id", field: "country_id"},
            {title: "country_name", field: "country_name"},
            {title: "track_id", field: "track_id", width: 150},
            {title: "track_name", field: "track_name", align: "left"},
            {title: "track_rank", field: "track_rank"},
        ]
    });
}

function launch(){
    getArtistInfoTable()
    getChartsTable();
    getTracksTable();
    getSimilarTable()
}


function getArtistInfoTable() {
    const artist_id = $("#artist_id").last().html();
    return new Tabulator("#artist-info-table", {
        height:"311px",
        layout:"fitColumns",
        placeholder:"No Data Set",
        ajaxURL: `http://${server}:${port_api}/artist/${artist_id}`,
        ajaxResponse:function(url, params, response){
            return response; //return the tableData property of a response json object
        },
        columns:[ //Define Table Columns
            {title:"Name", field:"artist_name", width:150},
            {title:"artist_country_id", field:"artist_country_id", visible:false},
            {title:"Country Name", field:"artist_country_name"},
            {title:"Id", field:"artist_id", visible:false},
            {title:"Rating", field:"artist_rating", align:"left"},
            {title:"Total tracks in charts", field:"total_tracks_in_charts"},
            {title:"Number of countries in charts", field:"unique_country_charts"}
        ]
    });
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
            {title:"Name", field:"track_name"},
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
            {title: "Album Name", field: "album_name"},
            {title: "country_id", field: "country_id", visible:false},
            {title: "Country Name", field: "country_name"},
            {title: "track_id", field: "track_id",visible:false},
            {title: "Track Name", field: "track_name", align: "left"},
            {title: "Track rank", field: "track_rank"},
        ]
    });
}
function getSimilarTable() {
    const artist_id = $("#artist_id").last().html();
    return new Tabulator("#similar-artist-chart", {
        height: "311px",
        layout: "fitColumns",
        placeholder: "No Data Set",
        ajaxURL: `http://${server}:${port_api}/similar_artists/${artist_id}`,
        ajaxResponse: function (url, params, response) {
            return response; //return the tableData property of a response json object
        },
        columns: [ //Define Table Columns
            {title: "artist_id", field: "artist_id",visible:false},
            {title: "artist_name", field: "artist_name"},
        ]
    });
}
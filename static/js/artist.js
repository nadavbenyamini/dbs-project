
function launch(){
    getArtistInfoTable()
    getChartsTable();
    getTracksTable();
    getSimilarTable()
}


function getArtistInfoTable() {
    const artist_id = $("#artist_id").last().html();
    const artistUrl = function(cell) { return `${cell['_cell']['value']}`;};
    const countryUrl = function(cell) { return `../country/${cell['_cell']['value']}`;};
    return new Tabulator("#artist-info-table", {
        height:"311px",
        layout:"fitColumns",
        placeholder:"No Data Set",
        ajaxURL: `http://${server}:${port_api}/artist/${artist_id}`,
        ajaxResponse:function(url, params, response){
            return response; //return the tableData property of a response json object
        },
        columns:[ //Define Table Columns
            {title:"Name", field:"artist_id", width:150, formatter: "link", formatterParams: {url: artistUrl, target: '_blank', labelField: 'artist_name'}},
            {title:"Country Name", field:"artist_country_id", formatter: "link", formatterParams: {url: countryUrl, target: '_blank', labelField: 'artist_country_name'}},
            {title:"Id", field:"artist_id", visible:false},
            {title:"Rating", field:"artist_rating", align:"left"},
            {title:"Total tracks in charts", field:"total_tracks_in_charts"},
            {title:"Number of countries in charts", field:"unique_country_charts"}
        ]
    });
}

function getTracksTable() {
    const artist_id = $("#artist_id").last().html();
    const trackUrl = function(cell) { return `../track/${cell['_cell']['value']}`;};
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
            {title:"Name", field:"track_id", formatter: "link", formatterParams: {url: trackUrl, target: '_blank', labelField: 'track_name'}},
            {title:"Id", field:"album_id", visible:false},
            {title:"Album", field:"album_name"},
            {title:"Genere", field:"genre_name"},
            {title:"Release Date", field:"track_release_date"}
        ]
    });
}

function getChartsTable() {
    const artist_id = $("#artist_id").last().html();
    const trackUrl = function(cell) { return `../track/${cell['_cell']['value']}`;};
    const countryUrl = function(cell) { return `../country/${cell['_cell']['value']}`;};
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
            {title: "country_Name", field: "country_id", formatter: "link", formatterParams: {url: countryUrl, target: '_blank', labelField: 'country_name'}},
            {title: "track_Name", field: "track_id", formatter: "link", formatterParams: {url: trackUrl, target: '_blank', labelField: 'track_name'}},
            {title: "Track rank", field: "track_rank"},
        ]
    });
}
function getSimilarTable() {
    const artist_id = $("#artist_id").last().html();
    const artistUrl = function(cell) { return `${cell['_cell']['value']}`;};
    return new Tabulator("#similar-artist-chart", {
        height: "311px",
        layout: "fitColumns",
        placeholder: "No Data Set",
        ajaxURL: `http://${server}:${port_api}/similar_artists/${artist_id}`,
        ajaxResponse: function (url, params, response) {
            return response; //return the tableData property of a response json object
        },
        columns: [ //Define Table Columns
            {title: "Artist Name", field: "artist_id", formatter: "link", formatterParams: {url: artistUrl, target: '_blank', labelField: 'artist_name'}},
            ]
    });
}

const artist_id = $("#artist_id").last().html();

function launch(){
    getArtistInfoTable();
    getChartsTable();
    getTracksTable();
    getSimilarTable();
}


function getArtistInfoTable() {
    const artist_id = $("#artist_id").last().html();
    const artistUrl = function(cell) { return `${cell['_cell']['value']}`;};
    const countryUrl = function(cell) { return `../country/${cell['_cell']['value']}`;};
    return new Tabulator("#artist-info-table", {
        layout:"fitColumns",
        placeholder: "No Data Set",
        ajaxURL: `http://${server}:${port_api}/artist/${artist_id}`,
        ajaxResponse:function(url, params, response){
            return response; //return the tableData property of a response json object
        },
        columns:[ //Define Table Columns
            {title:"Name", field:"artist_id", formatter: "link", formatterParams: {url: artistUrl, labelField: 'artist_name'}},
            {title:"Country", field:"artist_country_id", formatter: "link", formatterParams: {url: countryUrl, labelField: 'artist_country_name'}},
            {title:"Id", field:"artist_id", visible:false},
            {title:"Rating", field:"artist_rating", align:"left", formatter: "star", formatterParams: {stars: 5}},
            {title:"#Tracks in Charts", field:"total_tracks_in_charts"},
            {title:"#Charts with Tracks in", field:"unique_country_charts", width:300}
        ]
    });
}

function getTracksTable() {
    const artist_id = $("#artist_id").last().html();
    const trackUrl = function(cell) { return `../track/${cell['_cell']['value']}`;};
    return new Tabulator("#songs-table", {
        layout:"fitColumns",
        height: "311px",
        placeholder:"No Data Set",
        ajaxURL: `http://${server}:${port_api}/artist_tracks/${artist_id}`,
        ajaxResponse:function(url, params, response){
            return response; //return the tableData property of a response json object
        },
        columns:[ //Define Table Columns
            {title:"Id", field: "al.artist_id", visible:false},
            {title:"Name", field: "track_id", formatter: "link", formatterParams: {url: trackUrl, labelField: 'track_name'}},
            {title:"Id", field: "album_id", visible:false},
            {title:"Album", field: "album_name"},
            {title:"Genre", field: "genre_name"},
            {title:"Rating", field: "track_rating", align:"left", formatter: "star", formatterParams: {stars: 5}},
            {title:"Release Date", field: "track_release_date"}
        ]
    });
}

function getChartsTable() {
    const artist_id = $("#artist_id").last().html();
    const trackUrl = function(cell) { return `../track/${cell['_cell']['value']}`;};
    const countryUrl = function(cell) { return `../country/${cell['_cell']['value']}`;};
    return new Tabulator("#artist-chart", {
        layout:"fitColumns",
        height: "311px",
        placeholder: "No Data Set",
        ajaxURL: `http://${server}:${port_api}/artist_charts/${artist_id}`,
        ajaxResponse: function (url, params, response) {
            return response; //return the tableData property of a response json object
        },
        columns: [ //Define Table Columns
            {title: "Album Name", field: "album_name"},
            {title: "Track Name", field: "track_id", formatter: "link", formatterParams: {url: trackUrl, labelField: 'track_name'}},
            {title: "Country", field: "country_id", formatter: "link", formatterParams: {url: countryUrl, labelField: 'country_name'}},
            {title: "Track rank", field: "track_rank"},
        ]
    });
}
function getSimilarTable() {
    const artistUrl = function(cell) { return `${cell['_cell']['value']}`;};
    return new Tabulator("#similar-artist-chart", {
        layout: "fitColumns",
        height: "311px",
        placeholder: "No Data Set",
        ajaxURL: `http://${server}:${port_api}/similar_artists/${artist_id}`,
        ajaxResponse: function (url, params, response) {
            return response; //return the tableData property of a response json object
        },
        columns: [ //Define Table Columns
            {title: "Artist Name", field: "artist_id", formatter: "link", formatterParams: {url: artistUrl, labelField: 'artist_name'}},
            ]
    });
}
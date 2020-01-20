
const track_id = $("#track_id").last().html();

function launch() {
    const url = `http://${server}:${port_api}/track/${track_id}`;
    $.get({
    url:url,
    success:function(result){
        const artist_id = result[0]["artist_id"];
        const artist_name = result[0]["artist_name"];
        $("#card_track_name").html(result[0]["track_name"]);
        $("#card_artist").html(`<a href="http://${server}:${port}/artist/${artist_id}">${artist_name}</a>`);
        $("#card_genre").html(result[0]["genre_name"]);
        $("#track_date").html(result[0]["track_release_date"]);
        $("#card_lyrics").html(result[0]["track_lyrics"]);
        getTracksTable();
    }
});
}


function getTracksTable() {
    const trackUrl = function(cell) { return `../track/${cell['_cell']['value']}`;};
    return new Tabulator("#similar-tracks", {
        layout:"fitColumns",
        placeholder:"No Data Set",
        ajaxURL: `http://${server}:${port_api}/similar_tracks/${track_id}`,
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

//trigger button click
$("#card_google_link").click(function(){
    const artistName = $("#card_artist").html().split('>')[1].split('<')[0]; // Artist is a link tag now, need to clean it first
    const trackName = $("#card_track_name").html();
	const q = `${artistName} - ${trackName}`;
	window.open('http://google.com/search?q='+q, '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');
});

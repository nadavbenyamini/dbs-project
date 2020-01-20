google.charts.load('current', {'packages':['corechart']});

const trackUrl = function(cell) { return `../track/${cell['_cell']['value']}`;};
const artistUrl = function(cell) { return `../artist/${cell['_cell']['value']}`;};
var table_artists = new Tabulator("#artists-table", {
    layout:"fitColumns",
    height: "311px",
    placeholder:"No Data Set",
    ajaxResponse:function(url, params, response){
       //url - the URL of the request
       //params - the parameters passed with the request
       //response - the JSON object returned in the body of the response.
       return response; //return the tableData property of a response json object
    },
    columns:[ //Define Table Columns
        {title:"Name", field: "artist_id", formatter: "link", formatterParams: {url: trackUrl, target: '_blank', labelField: 'artist_name'}},
        {title:"Number of Song in Chart", field:"number_of_songs_in_chart"},
       
    ]
});

var table_songs = new Tabulator("#songs-table", {
    layout:"fitColumns",
    height: "311px",
    placeholder:"No Data Set",
    ajaxResponse:function(url, params, response){
       //url - the URL of the request
       //params - the parameters passed with the request
       //response - the JSON object returned in the body of the response.
       return response; //return the tableData property of a response json object
    },
    columns:[ //Define Table Columns
        {title:"Id", field:"track_id", visible: false},
        {title:"Track Name", field: "track_id", formatter: "link", formatterParams: {url: trackUrl, target: '_blank', labelField: 'track_name'}},
        {title:"Artist Name", field: "artist_id", formatter: "link", formatterParams: {url: artistUrl, target: '_blank', labelField: 'artist_name'}},
        {title:"Genre", field:"genre_name"},
        {title:"Rank", field:"track_rank"},
        {title:"Release Date", field:"track_release_date"},
    ]
});


function temp(){
    let country_id = $("#country_id").last().html();
    $("#country_flag_id").attr('src',`https://www.countryflags.io/${country_id}/flat/64.png`)

    let url = `http://${server}:${port_api}/country_artists/${country_id}`
    console.log(url)
    $.get({
        url:url,
        success:function(result){
            table_artists.setData(result)
        }
    });
  
    let url2 = `http://${server}:${port_api}/country_genres/${country_id}`

    $.get({
        url:url2,
        success:function(result){
            arr = [['Genre','Number of songs']]
            var options = {'title':'Genere distribution in the country', 'width':650, 'height':500};
            var chart = new google.visualization.PieChart(document.getElementById('country-chart'));
            result.forEach(element => {
                arr.push([element.genre_name, element.number_of_songs_in_chart])
            });
            console.log(arr)
            var data = google.visualization.arrayToDataTable(arr);
            chart.draw(data, options);
        }
    });  
    
    let url3 = `http://${server}:${port_api}/country_tracks/${country_id}`
    console.log(url3)
    $.get({
        url:url3,
        success:function(result){
            table_songs.setData(result)
        }
    });  
}

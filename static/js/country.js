google.charts.load('current', {'packages':['corechart']});

var table_artists = new Tabulator("#artists-table", {
    height:"311px",
    layout:"fitColumns",
    placeholder:"No Data Set",
    ajaxResponse:function(url, params, response){
       //url - the URL of the request
       //params - the parameters passed with the request
       //response - the JSON object returned in the body of the response.
       return response; //return the tableData property of a response json object
    },
    columns:[ //Define Table Columns
        {title:"Id", field:"artist_id", visible:false},
        {title:"Name", field:"artist_name"},
        {title:"Number of Song in Chart", field:"number_of_songs_in_chart"},
       
    ],
    rowClick:function(e, row){ //trigger an alert message when the row is clicked
        //alert("Row " + row.getData().artist_id + " Clicked!!!!");
       url = `http://${server}:${port}/artist/${row.getData().artist_id}`
       console.log(url)
       location.replace(url)
    },
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
}

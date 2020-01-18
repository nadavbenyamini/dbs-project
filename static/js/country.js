
const base_url = 'http://127.0.0.1:5001/api';

function get_data(country_id, query_name, element) {
    $.get({
        url: `${base_url}/${query_name}/${country_id}`,
        success: function (result) {
            element.setData(result);
        }
    });
}

function get_flag(country_id) {
    $("#country_flag_id").show();
    $("#country_flag_id").attr('src', `https://www.countryflags.io/${country_id}/flat/64.png`)
}

function launch(country_id) {
    get_flag(country_id);
    get_data(country_id, 'country_tracks', )
}


const chart_table = new Tabulator("#songs-table", {
   height: "311px",
   layout: "fitColumns",
   ajaxURL: `http://${server}:${port_api}/country_tracks/${country_id}`,
   placeholder: "No Data Set",
   ajaxResponse: function(url, params, response) {
       return response;
   },
   columns:[
        {title: "Id", field: "track_id", visible: false},
        {title: "Name", field: "track_name", width: 150},
        {title: "Artist", field: "artist_name"},
        {title: "Genre", field: "genre_name"},
        {title: "Release Date", field: "track_release_date"}
    ],
   rowClick:function(e, row){
       const url = `http://${server}:${port}/track/${row.getData()['track_id']}`;
       location.replace(url);
    },
});
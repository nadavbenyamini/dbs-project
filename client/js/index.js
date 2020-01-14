//define some sample data
 
 //create Tabulator on DOM element with id "example-table"
var table_artists = new Tabulator("#artists-table", {
 	height:"311px",
    layout:"fitColumns",
    placeholder:"No Data Set",
 	columns:[ //Define Table Columns
	 	{title:"Name", field:"name", width:150},
	 	{title:"Rating", field:"age", align:"left", formatter:"progress"},
	 	{title:"Country", field:"col"},
 	],
 	rowClick:function(e, row){ //trigger an alert message when the row is clicked
 		alert("Row " + row.getData().id + " Clicked!!!!");
 	},
});

var table_artist = new Tabulator("#artist-table", {
 	height:"311px",
    layout:"fitColumns",
	ajaxURL:"http://127.0.0.1:5001/artist_tracks/26",
	paginationSize:20,
    placeholder:"No Data Set",
 	columns:[ //Define Table Columns
	 	{title:"Track", field:"track_name", width:150},
		{title:"Album", field:"album_id"},
		{title:"Genere", field:"genre_id"},
	 	{title:"Rating", field:"track_rating", align:"left", formatter:"star"},
	 	{title:"Track release", field:"track_release_date", sorter:"date"},
 	],
 	rowClick:function(e, row){ //trigger an alert message when the row is clicked
 		alert("Row " + row.getData().id + " Clicked!!!!");
 	},
});


//trigger AJAX load on "Load Data via AJAX" button click
$("#ajax-trigger").click(function(){
    table.setData("/artists	data/ajax");
});
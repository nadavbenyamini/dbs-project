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
    placeholder:"No Data Set",
 	columns:[ //Define Table Columns
	 	{title:"Track", field:"name", width:150},
		{title:"Album", field:"col"},
		{title:"Genere", field:"col"},
	 	{title:"Rating", field:"name", align:"left", formatter:"progress"},
	 	{title:"Track release", field:"col"},
 	],
 	rowClick:function(e, row){ //trigger an alert message when the row is clicked
 		alert("Row " + row.getData().id + " Clicked!!!!");
 	},
});


//trigger AJAX load on "Load Data via AJAX" button click
$("#ajax-trigger").click(function(){
    table.setData("/exampledata/ajax");
});
//define some sample data
 
server = "127.0.0.1"
port = "5001/api"
var table_artist;
var countries;

function getAllCountries(){
    $.get({
        url:`http://${server}:${port}/countries`,
        success:function(result){
           countries = result;
           //console.log(result)
            countries.forEach(function(item){
                 $("#inlineFormCustomSelectPref").append(`<option value="${item.country_id}">${item.country_name}</option>`)
            });
        }
    });
}

$(function(){
    console.log("load");
    getAllCountries();
})

function spinner_visibilty(show){
	console.log(show)
	if(show){
		$(".spinner-border").show();
	}else{
		$(".spinner-border").hide();
	}
}

 //create Tabulator on DOM element with id "example-table"
var table_artists = new Tabulator("#artists-table", {
 	height:"311px",
    layout:"fitColumns",
	ajaxURL:`http://${server}:${port}/artists`,
    placeholder:"No Data Set",
	ajaxResponse:function(url, params, response){
        //url - the URL of the request
        //params - the parameters passed with the request
        //response - the JSON object returned in the body of the response.
        return response; //return the tableData property of a response json object
    },
 	columns:[ //Define Table Columns
		{title:"Id", field:"artist_id", visible:false},
	 	{title:"Name", field:"artist_name", width:150},
	 	{title:"Rating", field:"artist_rating", align:"left", formatter:"progress"},
	 	{title:"Country", field:"artist_country_id"},
 	],
 	rowClick:function(e, row){ //trigger an alert message when the row is clicked
 		//alert("Row " + row.getData().artist_id + " Clicked!!!!");
		//console.log(`http://${server}:${port}/artist_tracks/${row.getData().artist_id}`)
		table_artist.setData(`http://${server}:${port}/artist_tracks/${row.getData().artist_id}`)
		$("#artists-table").hide();
		$("#artist-table").show();
 	},
});

table_artist = new Tabulator("#artist-table", {
 	height:"400px",
    layout:"fitColumns",
	ajaxResponse:function(url, params, response){
        //url - the URL of the request
        //params - the parameters passed with the request
        //response - the JSON object returned in the body of the response.
		//console.log(response)
		response.forEach(function(item){
			item["track_rating"] = item["track_rating"]/20
		})
        return response; //return the tableData property of a response json object
    },
 	columns:[ //Define Table Columns
		{title:"Id", field:"al.artist_id", visible:false},
		{title:"Id", field:"track_id", visible:false},
		{title:"Id", field:"album_id", visible:false},
	 	{title:"Track", field:"track_name", width:150, headerFilter:"input"},
		{title:"Album", field:"album_name", headerFilter:"input"},
		{title:"Genere", field:"genre_name"},
	 	{title:"Rating", field:"track_rating", align:"left", formatter:"star"},
	 	{title:"Track release", field:"track_release_date", sorter:"date", headerFilter:"input"},
 	],
 	rowClick:function(e, row){ //trigger an alert message when the row is clicked
 		//alert("Row " + row.getData().id + " Clicked!!!!");
		spinner_visibilty(true)
		$.get({
			url:`http://${server}:${port}/tracks/${row.getData().track_id}`,
			success:function(result){
				console.log(result[0])
				spinner_visibilty(false)
				$("#card_track_name").html(result[0]["track_name"])
				$("#card_lyrics").html(result[0]["track_lyrics"])
				$("#card_artist").html(result[0]["artist_name"])
				$("#artist-table").hide();
				$("#sond_lyrics").show();
			}
		});
 	},
});

//trigger button click
$("#card_google_link").click(function(){
	q = $("#card_track_name").html()+" and "+$("#card_artist").html()
	window.open('http://google.com/search?q='+q, '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');
});

$("#music-form").submit(function(e){
    console.log("submit")
    e.preventDefault()
    let country_id = $("#inlineFormCustomSelectPref")[0].value
    $.get({
        url:`http://${server}:${port}/artists/${country_id}`,
        success:function(result){
            table_artists.setData(result)
        }
    });
    $("#country_flag_id").show();
    $("#country_flag_id").attr('src',`https://www.countryflags.io/${country_id}/flat/64.png`)

})

//custom max min header filter
var minMaxFilterEditor = function(cell, onRendered, success, cancel, editorParams){

    var end;

    var container = document.createElement("span");

    //create and style inputs
    var start = document.createElement("input");
    start.setAttribute("type", "number");
    start.setAttribute("placeholder", "Min");
    start.setAttribute("min", 0);
    start.setAttribute("max", 100);
    start.style.padding = "4px";
    start.style.width = "50%";
    start.style.boxSizing = "border-box";

    start.value = cell.getValue();

    function buildValues(){
        success({
            start:start.value,
            end:end.value,
        });
    }

    function keypress(e){
        if(e.keyCode == 13){
            buildValues();
        }

        if(e.keyCode == 27){
            cancel();
        }
    }

    end = start.cloneNode();
    end.setAttribute("placeholder", "Max");

    start.addEventListener("change", buildValues);
    start.addEventListener("blur", buildValues);
    start.addEventListener("keydown", keypress);

    end.addEventListener("change", buildValues);
    end.addEventListener("blur", buildValues);
    end.addEventListener("keydown", keypress);


    container.appendChild(start);
    container.appendChild(end);

    return container;
 }

//custom max min filter function
function minMaxFilterFunction(headerValue, rowValue, rowData, filterParams){
    //headerValue - the value of the header filter element
    //rowValue - the value of the column in this row
    //rowData - the data for the row being filtered
    //filterParams - params object passed to the headerFilterFuncParams property

        if(rowValue){
            if(headerValue.start != ""){
                if(headerValue.end != ""){
                    return rowValue >= headerValue.start && rowValue <= headerValue.end;
                }else{
                    return rowValue >= headerValue.start;
                }
            }else{
                if(headerValue.end != ""){
                    return rowValue <= headerValue.end;
                }
            }
        }

    return false; //must return a boolean, true if it passes the filter.
}

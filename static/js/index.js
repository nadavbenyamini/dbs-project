var countries;

function getAllCountries(){
    $.get({
        url:`http://${server}:${port_api}/countries`,
        success:function(result){
           countries = result;
           //console.log(result)
            countries.forEach(function(item){
                 $("#inlineFormCustomSelectPref").append(`<option value="${item.country_id}">${item.country_name}</option>`)
            });
        },
        error:function(e) {
            console.log(e)
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
	ajaxURL:`http://${server}:${port_api}/artists`,
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
        const url = `http://${server}:${port}/artist/${row.getData()['artist_id']}`;
        window.location.href = url;
		//table_artist.setData(`http://${server}:${port_api}/artist_tracks/${row.getData().artist_id}`)
 	},
});

function update_genre_list(){
    const genres = JSON.parse(this.responseText);
    for (const g of genres) {
        $('#tracks-search-genre').append(`<option value="${g['genre_id']}">${g['genre_full_name']}</option>`);
    }
}
function get_genres(){
    const xhr = new XMLHttpRequest();
    xhr.addEventListener("load", update_genre_list);
    xhr.open("GET", `http://${server}:${port_api}/genres`,);
    xhr.send();
}

function get_table_songs(search_text=null, search_by=null, date_from=null, date_to=null, genre_id=null, page_size=null, page_number=null) {
    const params = {};
    if (search_text) params['search_text'] = search_text;
    if (date_from) params['date_from'] = date_from;
    if (date_to) params['date_to'] = date_to;
    if (search_by) params['search_by'] = search_by;
    if (genre_id) params['genre_id'] = genre_id;
    if (page_size) params['page_size'] = page_size;
    if (page_number) params['page_number'] = page_number;

    const trackUrl = function(cell) { return `track/${cell['_cell']['value']}`;};
    const artistUrl = function(cell) { return `artist/${cell['_cell']['value']}`;};

    return new Tabulator("#songs-table", {
        layout:"fitColumns",
        ajaxURL: `http://${server}:${port_api}/search/track`,
        ajaxParams: params,
        placeholder:"No Data Set",
        ajaxResponse: function(url, params, response){
            document.getElementById('tracks-results-count').innerText = response?response.length:0;
            disable_next_page_button();
            return response;
        },
        columns: [
            {title:"Name", field: "track_id", formatter: "link",
                formatterParams: {url: trackUrl, target: '_blank', labelField: 'track_name'}},
            {title:"Name", field: "artist_id", formatter: "link",
                formatterParams: {url: artistUrl, target: '_blank', labelField: 'artist_name'}},
            {title:"Artist", field: "artist_name"},
            {title:"Album", field: "album_name"},
            {title:"Genre", field: "genre_name", width: 200},
            {title:"Release Date", field:"track_release_date", width: 300}
        ]
    });
}

$("#country-form").submit(function(e){
    let country_id = $("#inlineFormCustomSelectPref")[0].value;
    const url = `http://${server}:${port}/country/${country_id}`;
    window.open(url, '_blank');
});

$("#inlineFormCustomSelectPref").change(function(e) {
    toggleCountryButton();
});

function toggleCountryButton() {
    const chosen = $("#inlineFormCustomSelectPref")[0].value;
    if(!document.getElementById("country-submit-button")) addCountryButton();
    const button = $("#country-submit-button");
    if(chosen == '-1') button.hide();
    else button.show();
}

function addCountryButton() {
    $("#country-submit-div").append(`<button type="submit" id="country-submit-button" class="btn btn-primary">GO</button>`);
}

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

function delay(callback, ms) {
  let timer = 0;
  return function() {
    const context = this, args = arguments;
    clearTimeout(timer);
    timer = setTimeout(function () {
      callback.apply(context, args);
    }, ms || 0);
  };
}
// Launch function
$(document).ready(function() {
    getAllCountries();
    getGenres();

    // Setting listeners
    const wait = 500;
    $('#tracks-date-from').change(delay(function() { get_table();}, wait));
    $('#tracks-date-to').change(delay(function() { get_table();}, wait));
    $('#tracks-page-size').change(delay(function() { get_table();}, wait));
    $('#tracks-search-genre').change(delay(function() { get_table();}, wait));
    $('#tracks-search-box').keyup(delay(function() { get_table();}, wait));
    $('input[type=radio][name=tracks-search-type]').change(delay(function() {
        const searchType = getSearchType();
        document.getElementById('tracks-search-type-label').innerText = titleCase(searchType) + ':';
        if($('#tracks-search-box')[0].value.length > 0) get_table();
    }, wait*2));
    reset()
});


function reset() {
    const now = new Date();
    const nowString =
        now.getFullYear().toString() + '-' +
        ('0' + (now.getMonth()+1).toString()).substring(-1, 2) + '-' +
        now.getDate().toString();

    // Setting default values
    document.getElementById('tracks-search-type-label').innerText = 'Track Name:';
    $('#tracks-date-from').val('1900-01-01');
    $('#tracks-date-to').val(nowString);

    // First run
    get_table();
}

function getAllCountries(){
    $.get({
        url:`http://${server}:${port_api}/countries`,
        success:function(result){
            result.forEach(function(item){
                 $("#country-selector").append(`<option value="${item.country_id}">${item.country_name}</option>`)
            });
            $("#country-selector-default")[0].innerText = 'Choose...';
            $("#country-selector")[0].disabled = false;
        },
        error:function(e) {
            console.log(e)
        }
    });
}

function updateGenreList(){
    const genres = JSON.parse(this.responseText);
    for (const g of genres) {
        $('#tracks-search-genre').append(`<option value="${g['genre_id']}">${g['genre_full_name']}</option>`);
    }
}
function getGenres(){
    const xhr = new XMLHttpRequest();
    xhr.addEventListener("load", updateGenreList);
    xhr.open("GET", `http://${server}:${port_api}/genres`,);
    xhr.send();
}

function get_table(page_changed=false) {
    if (!page_changed) move_to_first_page();
    const text = $('#tracks-search-box')[0].value;
    const date_from = $('#tracks-date-from')[0].value;
    const date_to = $('#tracks-date-to')[0].value;
    const page_size = $('#tracks-page-size')[0].value;
    const page_number = parseInt($('#tracks-page-number')[0].innerText);
    let genre_id = $('#tracks-search-genre')[0].value;
    if (genre_id == '-1') genre_id = null;
    const search_by = getSearchType();
    getTracks(text, search_by, date_from, date_to, genre_id, page_size, page_number);
}

function getTracks(search_text=null, search_by=null, date_from=null, date_to=null, genre_id=null, page_size=null, page_number=null) {
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
    let country_id = $("#country-selector")[0].value;
    const url = `http://${server}:${port}/country/${country_id}`;
    window.open(url, '_blank');
});

$("#country-selector").change(function(e) {
    toggleCountryButton();
});

function toggleCountryButton() {
    const chosen = $("#country-selector")[0].value;
    if(!document.getElementById("country-submit-button")) addCountryButton();
    const button = $("#country-submit-button");
    if(chosen == '-1') button.hide();
    else button.show();
}

function addCountryButton() {
    $("#country-submit-div").append(`<button type="submit" id="country-submit-button" class="btn btn-primary">GO</button>`);
}


function getSearchType() {
    for (const radio of $('input[type=radio][name=tracks-search-type]')) {
        if (radio.checked) return radio.value;
    }
}

function move_to_first_page() {
    $('#tracks-page-number').val(1);
    $('#tracks-page-number').text(1);
    document.getElementById("tracks-page-prev").disabled = true;
}

function move_page(move=1) {
    const current = parseInt($('#tracks-page-number')[0].innerText);
    document.getElementById("tracks-page-prev").disabled = current + move <= 1;
    if (current + move < 1) return;
    $('#tracks-page-number').text(current + move);
    get_table(true);
}

function disable_next_page_button() {
    const pageSize = parseInt($('#tracks-page-size')[0].value);
    const resultsShown = parseInt($('#tracks-results-count')[0].innerText);
    document.getElementById("tracks-page-next").disabled = resultsShown < pageSize;
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

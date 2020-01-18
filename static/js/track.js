function temp(){
    let artist_id = $("#track_id").last().html();
    let url = `http://${server}:${port_api}/track/${artist_id}`
    console.log(url)
    $.get({
    url:url,
    success:function(result){
        console.log(result[0])
        $("#card_track_name").html(result[0]["track_name"])
        $("#card_lyrics").html(result[0]["track_lyrics"])
        // $("#card_artist").html(result[0]["artist_name"])
    }
});
}

//trigger button click
$("#card_google_link").click(function(){
	q = $("#card_track_name").html()+" and "+$("#card_artist").html()
	window.open('http://google.com/search?q='+q, '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');
});

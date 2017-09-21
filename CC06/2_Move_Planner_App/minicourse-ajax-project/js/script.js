
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview
    var streetStr = ('#street').val();
    var cityStr = ('#city').val();
    var address = streetStr +', '+ cityStr;
    console.log(address);
    $greeting.text('So you want to live at' + address + '?');

    var streetviewUrl = 'https://maps.googleapis.com/maps/api/streetview?size=600x400&location=' +address +'';
    // $body.append('<img class="bgimg" src="'+ streetviewUrl +'">')
    $body.append('<img class="bgimg" src="https://static.pexels.com/photos/126407/pexels-photo-126407.jpeg">')


    // return false;
};


$('#form-container').submit(loadData);});

// function loadData() {

//     var $body = $('body');
//     var $wikiElem = $('#wikipedia-links');
//     var $nytHeaderElem = $('#nytimes-header');
//     var $nytElem = $('#nytimes-articles');
//     var $greeting = $('#greeting');
//     var streetInput = $('#street').val();
//     var cityInput = $('#city').val();
//     var bgLocation = streetInput + ', ' + cityInput;
//     var streetViewURL = 'http://maps.googleapis.com/maps/api/streetview?size=600x400&location=' + bgLocation + '';

//     // clear out old data before new request
//     $wikiElem.text("");
//     $nytElem.text("");

//     $greeting.text("Is " + bgLocation + " where you want to live?")

//     // load streetview
//     $body.append('<img class="bgimg" src="' + streetViewURL + '">');

//     return false;
// };

// $('#form-container').submit(loadData);

// // loadData();
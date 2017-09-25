function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    // load streetview
    var $greeting = $('#greeting');
    var streetInput = $('#street').val();
    var cityInput = $('#city').val();
    var bglocation = streetInput + ', ' + cityInput;
    $greeting.text("So you want to live at:" + bglocation + "?");
    var streetViewURL = 'http://maps.googleapis.com/maps/api/streetview?size=600x400&location=' + bglocation + '';
    $body.append('<img class="bgimg" src="' + streetViewURL + '">');
    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // NYTimes AJAX request

    $.getJSON();




    return false;
};

$('#form-container').submit(loadData);

// loadData();
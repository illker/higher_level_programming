const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(URL, function(data) {
    const burger = data.results;
    for (const bu of burger) {
        $('UL#list_movies').append('<li>' + bu.title + '</li>');
    }
});
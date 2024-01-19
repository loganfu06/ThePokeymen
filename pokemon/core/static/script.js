var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.7.1.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

const SHOWPOKEMON = document.getElementById("showPokemon");
const POKELIST = document.getElementsByClassName(".pokelist");
const MYINPUT = document.getElementById("myInput");

if (!filter) {
    if (SHOWPOKEMON.classList.contains("hidden")) {
        SHOWPOKEMON.classList.remove("hidden");
    }
}
function filter() {
    var keyword = document.getElementById("myInput").value;

    var pokelist = document.getElementById("showPokemon");
    for (var i = 0; i < pokelist.length; i++) {
        var txt = pokelist.options[i].text;
        if (!txt.toUpperCase().match(keyword.toUpperCase())) {
            $(pokelist.options[i]).attr('disabled', 'disabled').hide();
        } else {
            $(pokelist.options[i]).removeAttr('disabled').show();
        }

    }
}
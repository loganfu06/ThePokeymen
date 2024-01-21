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
    let KEYWORD = document.getElementById("myInput").value;

    //let pokelist = document.getElementById("showPokemon");
    for (let i = 0; i < SHOWPOKEMON.length; i++) {
        let txt = SHOWPOKEMON.options[i].text;
        if (!txt.toUpperCase().slice(0, KEYWORD.length).match(KEYWORD.toUpperCase())) {
            $(SHOWPOKEMON.options[i]).attr('disabled', 'disabled').hide();
        } else {
            $(SHOWPOKEMON.options[i]).removeAttr('disabled').show();
        }
    }
}
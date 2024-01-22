var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.7.1.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

const SHOWPOKEMON = document.getElementById("showPokemon");
const POKELIST = document.getElementsByClassName("pokelist");
const MYINPUT = document.getElementById("myInput");
const ADDTOPOKEDEX = document.getElementById("addToPokedex");

ADDTOPOKEDEX.addEventListener('click', function () {
    let POKEMONCHOSEN = document.getElementById("showPokemon").value.toLowerCase();
    // let name = document.querySelector(POKEMONCHOSEN).id;
    // let POKEMONID = document.querySelector("." + POKEMONCHOSEN).id
    // POKEMONID = POKEMONID.match(/\d+/g);
    location.href=`http://127.0.0.1:8000/pokedex/create/${POKEMONCHOSEN}`
})


if (!filter) {
    if (SHOWPOKEMON.classList.contains("hidden")) {
        SHOWPOKEMON.classList.remove("hidden");
    }
}
function filter() {
    let reachedPokemon = false;
    let KEYWORD = document.getElementById("myInput").value;
    //let pokelist = document.getElementById("showPokemon");
    for (let i = 0; i < SHOWPOKEMON.length; i++) {
        let txt = SHOWPOKEMON.options[i].text;
        if (!txt.toUpperCase().slice(0, KEYWORD.length).match(KEYWORD.toUpperCase())) {
            $(SHOWPOKEMON.options[i]).attr('disabled', 'disabled').hide();
        } else {
            $(SHOWPOKEMON.options[i]).removeAttr('disabled').show();
        }
        // if (txt.toUpperCase() === KEYWORD.toUpperCase()) {
        //     reachedPokemon = true;
        //     if (ADDTOPOKEDEX.classList.contains("hidden")) {
        //         ADDTOPOKEDEX.classList.remove("hidden");
        //     }
        // } else if (!reachedPokemon) {
        //     if (!ADDTOPOKEDEX.classList.contains("hidden")) {
        //         ADDTOPOKEDEX.classList.add("hidden");
        //     }
        // }
    }
}


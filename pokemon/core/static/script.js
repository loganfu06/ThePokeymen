const SHOWPOKEMON = document.getElementById("showPokemon");
const POKELIST = document.getElementsByClassName(".pokelist");
const MYINPUT = document.getElementById("myInput");

SHOWPOKEMON.classList.add("hidden");
function filter() {
    console.log("OKOK");
    //const SEARCH = document.getElementById(".search");

    //document.getElementById("showPokemon").classList.toggle("hidden");

    // if (SHOWPOKEMON.classList.contains("hidden")) {
    //     SHOWPOKEMON.classList.remove("hidden");
    // }
    
    for (i = 0; i < POKELIST.length; i++) {
        for (let j = 0; j < MYINPUT.length; j++) {
            if (POKELIST.indexOf(i).slice(0,j) == MYINPUT.value.slice(0,j)) {
                POKELIST.indexOf(i).classList.remove("hidden");
            } else {
                POKELIST.indexOf(i).style.display = "none";
            }
        }
    }

    // for (i = 0; i < POKELIST.length; i++) {
    //     txtValue = a[i].textContent || a[i].innerText;
    //     if (txtValue.toUpperCase().indexOf(filter) > -1) {
    //         a[i].classList.remove("hidden");
    //     } else {
    //         a[i].style.display = "none";
    //     }
    // }

    //var pokelist = document.getElementById("pokelist").length;
    // for (var i = 0; i < pokelist; i++) {
    //     var txt = pokelist.options[i].text;
    //     if (!txt.match(keyword)) {
    //         $(pokelist.options[i]).attr('disabled', 'disabled').hide();
    //     } else {
    //         $(pokelist.options[i]).removeAttr('disabled').show();
    //     }

    // }
}
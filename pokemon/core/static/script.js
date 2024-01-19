//document.getElementById("myDropdown").classList.toggle("show");
const SEARCH = document.getElementById("search");
const SHOWPOKEMON = document.getElementById("showPokemon");
const POKELIST = document.getElementById("pokelist");

function filter() {

    SHOWPOKEMON.removeAttribute("hidden");
    
    for (i = 0; i < POKELIST.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }

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
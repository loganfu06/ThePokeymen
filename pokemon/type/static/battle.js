const BATTLEPOKEMON = document.getElementById("battlePokemon");

BATTLEPOKEMON.addEventListener('click', function() {
    console.log("bruhh")
    let pokemon1 = document.getElementById("pokemon1").value
    let pokemon2 = document.getElementById("pokemon2").value
    location.href=`http://127.0.0.1:8000/type/battle/${pokemon1}/${pokemon2}`

})
function recuperationSelect() {
    var x = document.getElementById("selectJeune");
    var i = x.selectedIndex;

    var y = document.getElementById("selectHebergeur");
    var j = y.selectedIndex;

    document.getElementById("jeune").innerHTML = x.options[i].text;
    document.getElementById("hebergeur").innerHTML = y.options[j].text;
};
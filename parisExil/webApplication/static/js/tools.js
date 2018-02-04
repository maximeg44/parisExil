//Méthode permettant de filtrer une liste pour n'en avoir que les lignes contenant l'entrée donnée
function searchByName() {
    //Déclaration des variables
    var input, filter, entryFound, table, tbody, tr, td, i, j;
    input = document.getElementById("searchBar");
    filter = input.value.toUpperCase();
    table = document.getElementById("acrylic");
    tr = table.getElementsByTagName("tr");

    //On boucle sur chaque ligne du tableau (sauf la première qui représente les intitulés du tableau et qu'il ne faut donc pas filtrer)
    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        //Pour chaque ligne, on inspecte le contenu de chaque case (sauf de la dernière case de chaque ligne sur laquelle nous n'avons pas à appliquer de filtre)
        for (j = 0; j < td.length-1; j++) {
            if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
                console.log(td[j].innerHTML.toUpperCase().indexOf(filter))
                entryFound = true;
            }
        }
        //Si l'entree est trouvée quelque part dans le tableau, on la laisse affichée, sinon, on la "cache"
        if (entryFound) {
            tr[i].style.display = "";
            entryFound = false;
        } else {
            tr[i].style.display = "none";
        }
    }
}
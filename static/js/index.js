// MDB Lightbox Init
$(function () {
    $("#mdb-lightbox-ui").load("mdb-addons/mdb-lightbox-ui.html");
    });

function copyimage(){
    document.getElementById("imagelink").select()
    document.execCommand("Copy");   
}
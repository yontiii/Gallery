
$(document).ready(function(){
    $(function () {
    $("#mdb-lightbox-ui").load("mdb-addons/mdb-lightbox-ui.html");
    });

 copyimage = () => {
    document.getElementById("imagelink").select()
    document.execCommand("copy");   
} 
})
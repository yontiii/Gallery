
$(document).ready(function(){
    $(function () {
    $("#mdb-lightbox-ui").load("mdb-addons/mdb-lightbox-ui.html");
    });

 copyimage = () => {
    var copyLink = document.getElementById("imagelink")
    copyLink.select()
    document.execCommand("copy")
    
} 
})
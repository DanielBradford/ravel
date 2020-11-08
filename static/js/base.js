$(document).ready(function () {
  $(".fixed-action-btn").floatingActionButton();
  $(".sidenav").sidenav();
  $(".modal").modal();
  $("#peek").click(function(){
    $(".carousel").show("slow");

  })

});
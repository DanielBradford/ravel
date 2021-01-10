$(document).ready(function () {
  $(".dropdown-trigger").dropdown();
  $(".fixed-action-btn").floatingActionButton();
  $(".sidenav").sidenav();
  $(".modal").modal();
  $('select').formSelect()
  $('.quantityInfo').hover(function(){
      


  });

  $('#sizeChoice, #colorChoice').on('input',function(e){
  $('#C').val(parseInt($('#sizeChoice').val()) + parseInt($('#colorChoice').val()));
    });


  

});
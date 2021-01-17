$(document).ready(function () {
  $(".dropdown-trigger").dropdown();
  $(".fixed-action-btn").floatingActionButton();
  $(".sidenav").sidenav();
  $(".modal").modal();
  $('select').formSelect()
  $('input#input_text, textarea#textarea2').characterCounter();
  $('#sizeChoice, #colorChoice').on('input',function(e){
  $('#C').val(parseInt($('#sizeChoice').val()) + parseInt($('#colorChoice').val()));
    });

  $(".remove-item").hover(function(){
    $(this).css("background-color", "pink");
  })
  $('.remove-item').click(function(e) {
        var csrfToken = "{{ csrf_token }}";
        var item_id = $(this).attr('id');
        var url = `/orders/remove/${item_id}`;
        var data = {'csrfmiddlewaretoken': csrfToken};
        $.post(url, data)
         .done(function() {
             location.reload();
         });
    })
});
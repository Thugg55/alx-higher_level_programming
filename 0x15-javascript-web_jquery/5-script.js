// JavaScript script that adds a <li> element to as list 
// when the user clicks on the tag DIV#add_item

$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});

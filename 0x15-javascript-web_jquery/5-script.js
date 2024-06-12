  // When the user clicks on the DIV with id "add_item"
$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });

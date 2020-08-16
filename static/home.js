getCategories()
getSubcategories()
doneTyping();
var send_data = {}
var typingTimer;                //timer identifier
var doneTypingInterval = 500;  //time in ms, 5 second for example
var $input = $('#input');
var categories = {}
var subcategories = {}



$('.sort').on('click', (e) => {
  var target = e.currentTarget
  var order = target.getAttribute('name')
  var icon = target.querySelector('.fa')
  icon.classList.toggle('fa-chevron-up')
  icon.classList.toggle('fa-chevron-down')
  var sign = icon.classList.contains('fa-chevron-up') ? '' : '-'
  send_data['order'] = order
  send_data['sign'] = sign
  doneTyping()

});

$input.on('keyup', function () {
  clearTimeout(typingTimer);
  send_data['search'] = this.value
  typingTimer = setTimeout(doneTyping, doneTypingInterval);
});


$input.on('keydown', function () {
  clearTimeout(typingTimer);
});



function doneTyping() {
  var url = $('#table').attr('url')
  $.ajax({
      method: "GET",
      url: url,
      data: send_data,
      success: function(result) {
          putTableData(result);
      },
  });
}
 
function putTableData(result) {
  let row;
  $("#table").show();
  $("#result").html("");
  result.map( (el) => {
      let cat_name = '---';
      let subcat_name = '---';
      
      categories.map((cat) => {

        if (el.cat_id == cat.id){
          cat_name = cat.name
        }
      });

      subcategories.map((subcat) => {
        if (el.subcat_id == subcat.id){
          subcat_name = subcat.name
        } 
      });


      row = `<tr> <th scope='row'>${el.sap}</th>"
        <td> ${el.name} </td>
        <td> ${cat_name} </td>
        <td> ${subcat_name}  </td>

        <td><a href='detail/${el  .id}'><button class='btn btn-sm btn-outline-light'>Detail</button></a></td></tr>`
      $("#result").append(row);
  });
}


function getCategories(){
  $.ajax({
    method: "GET",
    url: '/api/categories/',
    success: function(result) {
      categories = result
    },
  });
}

function getSubcategories(){
  $.ajax({
    method: "GET",
    url: '/api/subcategories/',
    success: (result) => {
      subcategories = result
    },
  });
}


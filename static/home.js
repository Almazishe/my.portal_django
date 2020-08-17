getCategories()
getSubcategories()
doneTyping();
var send_data = {}
var typingTimer;                //timer identifier
var doneTypingInterval = 500;  //time in ms, 5 second for example
var $input = $('#input');
var categories = {}
var subcategories = {}

var temp_page = 1;
var totalPages = 0;


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


$('.pag').on('click', (e) => {
  var target = e.currentTarget
  send_data['page'] = target.getAttribute('page')
  doneTyping()
});


function doneTyping() {
  var url = $('#table').attr('url')
  $.ajax({
      method: "GET",
      url: url,
      data: send_data,
      success: function(result) {
          putPagination(result.count)
          putTableData(result.results);
      },
  });
}

$('#page_count').on('change', (e) => {
  var x = e.currentTarget
  send_data['page_size'] = x.value
  doneTyping();
});

function putPagination(count){
  var x = document.getElementById('page_count')
  var page_count = count % x.value == 0 ? parseInt(count / x.value) : parseInt((count / x.value) + 1)
  totalPages = page_count
  $('.pagination').html("")
  $('.pagination').append('<li id="prev" class="page-item"><a class="page-link" href="javascript:void(0)">Prev</a>')
  
  for (var i = 1; i <= totalPages; i++) {
    if (temp_page == i){
      $(".pagination").append(
        "<li page=" + i +  " class='page-item current-page active'><a class='page-link'  href='javascript:void(0)'>" +
        i +
        "</a></li>"
        );
    } else {
      $(".pagination").append(
        "<li page=" + i +  " style='cursor:pointer;' class='page-item current-page'><a class='page-link'>" +
        i +
        "</a></li>"
      );
    }    
  }
  
  //appends the next button link as the final child element in the pagination
  
  $(".pagination").append(
    "<li class='page-item' id='next'><a class='page-link' href='javascript:void(0)'>Next</a></li>"
    );
  
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
      categories = result.results
    },
  });
}

function getSubcategories(){
  $.ajax({
    method: "GET",
    url: '/api/subcategories/',
    success: (result) => {
      subcategories = result.results
    },
  });
}

$(document).on("click",".pagination li", function () {
  if ($(this).attr('id') === 'next'){
    if (temp_page < totalPages) {
      temp_page += 1
    }
    send_data['page'] = temp_page
  } else if ($(this).attr('id') === 'prev'){
    if (temp_page > 1) {
      temp_page -= 1
    } 
    send_data['page'] = temp_page
  } else {
    send_data['page'] = $(this).attr('page')
    temp_page = $(this).attr('page')
  }
  doneTyping()
});

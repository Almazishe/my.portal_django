doneTyping();
var send_data = {}
var owner_data = {}
var typingTimer; 
var doneTypingInterval = 500;
var $input = $('#input');
var popup_time = 2000;



$(document).on("submit",".input", e => {
  e.preventDefault()
  var x = e.currentTarget, value = x.querySelector('.text').value, type = x.querySelector('.text').getAttribute('id')
  var url = $("#table").attr('url')
  putRequest(url, type, value)  


  show_popup()
  popup = document.getElementById("popup")
  popup.querySelector('.p').innerHTML = x.querySelector('.text').getAttribute('name') + " изменен удачно!"
  typingTimer = setTimeout(hide_popup, popup_time)
})

$(document).on("change", ".select", e => {
  e.preventDefault()
  var x = e.currentTarget, value = x.value, type = x.getAttribute('id')
  var url = $("#table").attr('url')
  if(type == 'cat_id'){
    putRequest(url, 'subcat_id', 0)
    set_subcats(value)
  } else if (type == 'owner_id'){
    var selected = x.options[x.selectedIndex].innerHTML
    putRequest(url, 'owner_name', selected)

  }
  putRequest(url, type, value)

  show_popup()
  popup = document.getElementById("popup")
  popup.querySelector('.p').innerHTML = x.getAttribute('name') + " изменен удачно!"
  typingTimer = setTimeout(hide_popup, popup_time)
  
})

function show_popup(){
  $('#popup').fadeIn('slow')
}

function hide_popup(){
  $('#popup').fadeOut('slow')
}


function set_subcats(cat_id){
  var url = $("#subcat_id").attr('url')
  var subcat = $('#subcat_id')
  subcat.html("")
  $.ajax({
    type: "GET",
    url: url,
    data: {
      cat_id: cat_id
    },
    success: function(res) {
      subcat.append(`<option  class="bg-dark1" value=0>Select....</option>`)
      res.map((row, _) => {
        subcat.append(`<option class="bg-dark1" value=${row.id}>${row.name}</option>`)
      })
    }
  })
}

function putRequest(url, type, value){ 
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  $.ajax({
    type: "PUT",
    url: url,
    headers: {
      'X-CSRFToken': csrftoken
    },
    data: {
      type: type,
      value: value
    }
  })
}


 
$input.on('keyup', function () {
  clearTimeout(typingTimer);
  send_data['search'] = this.value
  typingTimer = setTimeout(doneTyping, doneTypingInterval);
});

$input.on('keydown', function () {
  clearTimeout(typingTimer);
});



function doneTyping() {
  var url = $('#table').attr('url_list')
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

  if (result.length === 0){
    $("#detail_search_res").html("");
    $("#detail_search_res").append(`<li class="border-bottom text-light">There's nothing!</li>`);
  } else {
    let row;
    $("#detail_search_res").html("");
    $.each(result, function(a, b) {
        row = `<li class="border-bottom mb-2"><a class='text-light' href="/detail/${b.id}"><h6>${b.sap}</h6><p>${b.name}</p></a></li>`
        $("#detail_search_res").append(row);
    });
  }
};


$('#description').keydown(function(e) {
  if (e.which == 13) {
    e.preventDefault()
    var x = e.currentTarget, value = x.value, type = x.getAttribute('id')
    var url = $("#table").attr('url')
    putRequest(url, type, value)  
  
   
    show_popup()
    popup = document.getElementById("popup")
    popup.querySelector('.p').innerHTML = "Описание изменен удачно!"
    typingTimer = setTimeout(hide_popup, popup_time)
   } 
});


$('#owner_id').on('keyup', function () {
  clearTimeout(typingTimer);
  owner_data['search'] = this.value
  typingTimer = setTimeout(getUsers(), doneTypingInterval);
});

$('#owner_id').on('keydown', function () {
  clearTimeout(typingTimer);
});



function getUsers() {
  var url = $('#owner_id').attr('url')
  $.ajax({
      method: "GET",
      url: url,
      data: owner_data,
      success: function(result) {
          putUsers(result);
      },
  });
}

function putUsers(data){
  if (data.length === 0){
    $("#owner_names").html("");
    $("#owner_names").append(`<li class="border-bottom text-light">Нет владельца с таким именем или фамилией!</li>`);
  } else {
    let row;
    $("#owner_names").html("");
    console.log(data)
    data.map( (b) => {
        row = `<li  owner_id=${b.id} class="owner border-bottom mb-2">${b.firstname} ${b.secondname}</li>`
        $("#owner_names").append(row);
    });
  }
}


$(document).on('click', '.owner', (e) => {
  var owner = e.currentTarget
  var id = owner.getAttribute('owner_id')
  var val = owner.innerHTML
  var url = $('#table').attr('url')


  putRequest(url, 'owner_id', id)
  putRequest(url, 'owner_name', val)

  $('#owner_id').val(val)

  show_popup()
  popup = document.getElementById("popup")
  popup.querySelector('.p').innerHTML = "Владелец изменен удачно!"
  typingTimer = setTimeout(hide_popup, popup_time)
});
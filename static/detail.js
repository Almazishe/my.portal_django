var storage_url = $('#form').attr('url');
var state_url = $('#state_id').attr('url');
var cat_url = $('#cat_id').attr('url');
var resp_url = $('#resp_id').attr('url');
var subcat_url = $('#subcat_id').attr('url');

subcat_data = {}

$(document).on('change', "#form", (e) => {
  e.preventDefault();
  var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

  $.ajax({
    type: "PUT",
    url: storage_url,
    headers:{"X-CSRFToken": $crf_token},
    data: {
      id: $("#id").val(),
      name: $("#name").val(),
      sap: $("#sap").val(),
      sap_old: $("#sap_old").val(),
      cat_id: $("#cat_id").val(),
      subcat_id: $("#subcat_id").val(),
      state_id: $("#state_id").val(),
      owner_id: $("#owner_id").val(),
      owner_name: $("#owner_name").val(),
      resp_id: $("#resp_id").val(),
      date_open: $("#date_open").val(),
      date_assign: $("#date_assign").val(),
      model: $("#model").val(),
      serial_number: $("#serial_number").val(),
      manufacturer: $("#manufacturer").val(),
      modified_date: $("#modified_date").val(),
      address_id: $("#address_id").val(),
      floor: $("#floor").val(),
      description: $("#description").val(),

    }
  });
});

$("#cat_id").on('change', (e) => {
  subcat_data['cat_id'] = this.val();
  get_subcat_list();
});


$(document).ready(() => {
  get_cat_list();
  get_state_list();
  get_resp_list();
  $.get(storage_url, data => {
    $('#id').val(data['id']);  
    $('#name').val(data['name']);  
    $('#sap').val(data['sap']);  
    $('#sap_old').val(data['sap_old']);  
    $('#cat_id').val(data['cat_id'] == '' ? 0 : data['cat_id']); 
    subcat_data['cat_id'] = $("#cat_id").val(); 
    get_subcat_list();
    $('#subcat_id').val(data['subcat_id'] == '' ? 0 : data['subcat_id']);  
    $('#state_id').val(data['state_id'] == '' ? 0 : data['state_id']);  
    $('#owner_id').val(data['owner_id']);  
    $('#owner_name').val(data['owner_name']);  
    $('#resp_id').val(data['resp_id'] == '' ? 0 : data['resp_id']);  
    $('#date_open').val(data['date_open']);  
    $('#date_assign').val(data['date_assign']);  
    $('#model').val(data['model']);  
    $('#serial_number').val(data['serial_number']);  
    $('#manufacturer').val(data['manufacturer']);  
    $('#modified_date').val(data['modified_date']);  
    $('#address_id').val(data['address_id']);  
    $('#floor').val(data['floor']);  
    $('#description').val(data['description']);  
  });
});



function get_cat_list(){
  $.get(cat_url, data => {
    var cat = $("#cat_id");
    cat.append(
      `
      <option class='bg-dark text-light' value=0>Select...</option>
      `
    );
    data.map((v) => {
      cat.append(
      `
      <option class='bg-dark text-light' value=${v.id}>${v.name}</option>
      `);
    });
  });
}

function get_resp_list(){
  $.get(resp_url, data => {
    var resp = $("#resp_id");
    resp.append(
      `
      <option class='bg-dark text-light' value=0>Select...</option>
      `
    );
    data.map((v) => {
      resp.append(
      `
      <option class='bg-dark text-light' value=${v.id}>${v.firstname + " " + v.secondname}</option>
      `);
    });
  });
}

function get_state_list(){
  $.get(state_url, data => {
    var state = $("#state_id");
    state.append(
      `
      <option class='bg-dark text-light' value=0>Select...</option>
      `
    );
    data.map((v) => {
      state.append(
      `
      <option class='bg-dark text-light' value=${v.id}>${v.name}</option>
      `);
    });
  });
}

function get_subcat_list(){
  $.ajax({
    method: "GET",
    url: subcat_url,
    data: subcat_data,
    success: function(result) {
      var subcat = $("#subcat_id");
      subcat.append(
        `
        <option class='bg-dark text-light' value=0>Select...</option>
        `
      );
      result.map((v) => {
        subcat.append(
        `
        <option class='bg-dark text-light' value=${v.id}>${v.name}</option>
        `);
      });
    },
  });
}
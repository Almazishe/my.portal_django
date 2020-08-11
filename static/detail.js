var storage_url = $('#form').attr('url');
var subcat_url = $('#subcat_id').attr('url')





$(document).on('change', "#form", (e) => {
  console.log('FORM');
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
      model: $("#model").val(),
      serial_number: $("#serial_number").val(),
      manufacturer: $("#manufacturer").val(),
      address_id: $("#address_id").val(),
      floor: $("#floor").val(),
      description: $("#description").val()
    }
  });
});

$(document).on('change', '#cat_id', (e) => {
  console.log('CAT');

  e.preventDefault();
  var cat = $('#cat_id');
  var sub = $('#subcat_id');
  sub.html("");
  

  $.ajax({
    type: 'GET',
    url: subcat_url,
    data: {
      cat_id: cat.val()
    },
    success: function(res) {
      console.log('RES');
      sub.append(`<option  class="bg-dark" value=0>Select....</option>`);
      $.each(res['data'], (id, name) => {
        sub.append(`<option class="bg-dark" value="${id}">${name}</option>`);
      });
    }
  });

});
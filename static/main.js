doneTyping();
var send_data = {}
var typingTimer;                //timer identifier
var doneTypingInterval = 500;  //time in ms, 5 second for example
var $input = $('#input');

 
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
  $.each(result, function(a, b) {
      row = `<tr> <th scope='row'>${b.id}</th>"
        <td> ${b.name} </td>
        <td><a href='detail/${b.id}'><button class='btn btn-sm btn-outline-light'>Detail</button></a></td></tr>`
      $("#result").append(row);
  });
}

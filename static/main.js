doneTyping();
var send_data = {}
//setup before functions
var typingTimer;                //timer identifier
var doneTypingInterval = 500;  //time in ms, 5 second for example
var $input = $('#input');

//on keyup, start the countdown
$input.on('keyup', function () {
  clearTimeout(typingTimer);
  send_data['search'] = this.value
  typingTimer = setTimeout(doneTyping, doneTypingInterval);
});

//on keydown, clear the countdown 
$input.on('keydown', function () {
  clearTimeout(typingTimer);
});



//user is "finished typing," do something
function doneTyping() {
  var url = $('#table').attr('url')
  $.ajax({
      method: "GET",
      url: url,
      data: send_data,
      beforeSend: function() {
          $("#result").append("<tr><td><h1>Loading data...</h1></td><td></td></tr>");
      },
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

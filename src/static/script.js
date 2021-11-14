function calc(e) {
  var operacao = e.value;

  var n1 = parseFloat(document.getElementById("n1").value);
  var n2 = parseFloat(document.getElementById("n2").value);

  if (!n1 || !n2) {
    alert("Prencha os campos");
  } else {

    options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ args: n1 + operacao + n2 }),
    };
    fetch("http://192.168.100.6:9900/elementar", options)
      .then((res) => res.json())
      .then(
        (data) => (document.getElementById("result").value = data.resultado)
      );
  }
}

function transcendental() {
  var x = parseInt(document.getElementById("valX").value);

  if (!x) {
    alert("Preencha o campo!");
  } else {
    options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ x: x }),
    };
    fetch("http://192.168.100.6:9900/operacao", options)
      .then((res) => res.json())
      .then(
        (data) =>
          (document.getElementById("result-transcendental").value =
            data.resultado)
      );
  }
}

function limparT() {
  document.getElementById("result-transcendental").value = "";
  document.getElementById("valX").value = "";
}

function limpar() {
  document.getElementById("result").value = "";
  document.getElementById("n1").value = "";
  document.getElementById("n2").value = "";
}

$(document).ready(function () {
  $.ajax({
    url: "http://192.168.100.6:9900/listar",
    dataType: "json",
    type: "get",
    cache: false,
    success: function (data) {
      console.log(data)
      var event_data = "";
      $.each(data.logs, function (index, value) {
        event_data += "<tr>";
        event_data += "<td>" + value.date_op + "</td>";
        event_data += "<td>" + value.type_op + "</td>";
        event_data += "<td>" + value.spec_op + "</td>";
        event_data += "<td>" + value.args_op + "</td>";
        event_data += "<tr>";
      });
      $(".table").append(event_data);
    },
    error: function () {
      alert("erro ao obter os logs.");
    },
  });
});

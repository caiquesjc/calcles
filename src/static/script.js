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

function addData() {
  document.getElementById("value-table").innerHTML = "";
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function () {
    res = JSON.parse(this.responseText);
    res.logs.reverse().map(function (item) {
      document.getElementById(
        "value-table"
      ).innerHTML += `<tr><td>${item.date_op}</td><td>${item.name_op}</td><td>${item.spec_op}</td><td>${item.args_op}</td></tr>`;
    });
  };
  xhttp.open("GET", "http://192.168.100.6:9900/listar");
  xhttp.send();
}

function filterData() {
  let type_op = document.getElementById("type_op_sel").value;
  let date_op = document.getElementById("date_op_sel").value;

  const xhttp = new XMLHttpRequest();
  xhttp.onload = function () {
    res = JSON.parse(this.responseText);
    document.getElementById("value-table").innerHTML = "";
    res.logs.map(function (item) {
      if (
        item.type_op.toString() === type_op &&
        item.date_op.includes(date_op)
      ) {
        document.getElementById(
          "value-table"
        ).innerHTML += `<tr><td>${item.date_op}</td><td>${item.name_op}</td><td>${item.spec_op}</td><td>${item.args_op}</td></tr>`;
      }
    });
  };
  xhttp.open("GET", "http://192.168.100.6:9900/listar");
  xhttp.send();
}

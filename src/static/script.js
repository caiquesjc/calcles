function calc(e){
   
    var operacao = e.value
    
    var n1=parseFloat(document.getElementById("n1").value)
    var n2=parseFloat(document.getElementById("n2").value)
    
    var calculo = eval(n1+operacao+n2)
    
    if(!isNaN(calculo)){
      // alert(calculo);
      document.getElementById("result").value = calculo
    }
   
 }
 //sen(x^2) * (x+10) 
 function transcendental(){
    var x = parseFloat(document.getElementById("valX").value)

    var calculo = `sen(${x}^2) * (${x}+10)` 
    if(!isNaN(x))
      document.getElementById("result-transcendental").value = calculo//`sen(${x}^2) * (${x}+10)`
 }

 function limparT() {
   document.getElementById("result-transcendental").value = ""
   document.getElementById("valX").value = ""
 }

 function limpar(){
    //alert("1");s
    //var f=document.getElementById("frm");
    document.getElementById("result").value = ""
    document.getElementById("n1").value = ""
    document.getElementById("n2").value = ""
 }

 
 
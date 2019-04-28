/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


function calcword(){

    $("#result").html( "<h2>sending...</h2>");
    var formData = document.forms.input_from;
    var sendData = [];

    for (i = 1; i < 6; i++){
        data = {};
        if(formData["word" + i].value != ""){
            data["sw"] = formData["sw" + i].value
            data["text"] = formData["word" + i].value
            sendData.push(data)
        }
    }
    
    if(sendData.length == 0){
        $("#result").html( "<h2>文字を入力してください</h2>");
        return false;
    }

    console.log(sendData)
    
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "/api/calc_words",
        "method": "POST",
        "headers": {
          "Content-Type": "application/json",
          "cache-control": "no-cache",
        },
        "processData": false,
        "data": JSON.stringify(sendData)
      }
      
    $.ajax(settings)
    .done(
        function(data){
        $("#result").html( "<h2>result</h2>" + data);
    })
    .fail(function(jqXHR, textStatus, errorThrown){
        $("#result").html( "<h2>ERROR:Link failed. please retry.</h2>");
    });

}

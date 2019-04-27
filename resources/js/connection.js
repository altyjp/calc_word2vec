/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var graph = undefined;

function calcword(){
    var formData = document.forms.input_from;
    var sendData = [];

    for (i = 1; i < 6; i++){
        data = {};
        data["sw"] = formData["sw" + i].value
        data["text"] = formData["word" + i].value
        sendData.push(data)
    }
    
    console.log(sendData)

    $("#result").html( "<h2>sending...</h2>");
    
    $.post("/api/calc_words",sendData)
            .done(
                function(data){
                $("#result").html( "<h2>result</h2>" + data);
            })
            .fail(function(jqXHR, textStatus, errorThrown){
                $("#result").html( "<h2>ERROR:Link failed. please retry.</h2>");
            });
}

function alertme(msg){
    alert(msg)
}

function send(){
    var textInput = document.getElementById('username');
    var btn = document.getElementById('pass');
    var str = textInput.value;
    $.post("", { data: str });
    textInput.value="";

    alertme('data sent');
}
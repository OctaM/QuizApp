function toProfile()
{
    window.location.replace("http://localhost:8000/quiz/profile");

//    alert('In js : ' + buttonPressed)
//    $.post("", { but_pressed : buttonPressed});
}

function revealFields(){
    node = document.getElementById('hidden')
    var x = document.createElement("INPUT");
    x.setAttribute("type", "text");
    x.setAttribute("id", "inputText");
    node.appendChild(x);

    var y = document.createElement("INPUT");
    y.setAttribute("type", "submit");
    y.setAttribute("id", "join_but");
    y.setAttribute("value", "START NOW");
    node.appendChild(y);

    var text =
}
function send(){

   var user = document.getElementById('username');
   var pass = document.getElementById('pass');
//   var str = user.value
   $.post("", { username: user});
//  textInput.value="";
   alertme('data sent');
}
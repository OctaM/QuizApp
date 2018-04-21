function send(){

   var user = document.getElementById('username');
   var pass = document.getElementById('pass');
   var username_str = user.value;
   var password_str = pass.value;
//   var str = user.value
   $.post("", { username: username_str, password: password_str});
//  textInput.value="";
   alertme('data sent');
}
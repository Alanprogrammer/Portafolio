<?php
//Autor:Alanprogrammer
session_start();
if (isset($_SESSION['username'])){
header('location:admin.php');
}else{

}
?>

<html>
<head>
  <!-- Latest compiled and minified CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

  <!-- Optional theme -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

  <!-- Latest compiled and minified JavaScript -->
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>

<title>Keylogger Login</title>
<style>
/*body {background-color:black;}*/
.body {background:url("https://41.media.tumblr.com/tumblr_lx7agiexnM1r8a8t8o1_540.jpg");}

</style>
</head>


<body>

<div class="login_css">
<form method="post" action="login.php">

<table align="center">
    <div class="input-group">
<input type="text" name="usuario"/  class="form-control" placeholder="usuario"><br>


<input type="password" name="password" class="form-control" placeholder="password"/><br>
<input type="submit" value="login" class="form-control"/>

</div>
</table>



</form>


</div>


</body>
</html>

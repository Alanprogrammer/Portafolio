<?php
//Autor:Alanprogrammer
session_start();
@$user = $_POST['usuario'];
@$password = $_POST['password'];
if ($user == "admin" and $password =="admin"){
$_SESSION['username'] = $user;
header("location:admin.php");
}else{

header("location:https://41.media.tumblr.com/tumblr_lx7agiexnM1r8a8t8o1_540.jpg");

}


 ?>

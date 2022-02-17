<?php 
$usuario = "redaitbd"; 
$password = "redaitbd"; 
$endpoint = "redaitbd.c57rrkx9ku8z.us-east-1.rds.amazonaws.com";   
$basedatos = "redaitbd";

//Conectar a la base de datos 
$conexion = mysql_connect($endpoint, $usuario, $password) or die("Imposible conectar a MySQL"); 
echo "Conectado con exito a MySQL <br>"; 
$selected = mysql_select_db("$basedatos",$conexion) or die("Imposible conectar, revisar nombre de la base de datos."); 
?>

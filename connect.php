<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "test";
  
// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
$name= $_POST['name'];
$email= $_POST['email'];
$phone= $_POST['phone'];
$project= $_POST['project'];
$project= $message['message'];
  
$sql = "INSERT INTO test (name,email,phone,project,message) VALUES ('$name','$email','$phone','$project','$message')";
  
if (mysqli_query($conn, $sql)) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
  
mysqli_close($conn);
?>
<?php 
    $host = 'localhost';
    $user = 'daniel';
    $pass = '#Test123';
    $db = 'teste';

    $conn = mysqli_connect($host, $user, $pass, $db);

    $sql = 'SELECT * FROM users';
    $result = mysqli_query($conn, $sql);
    $users = mysqli_fetch_all($result, MYSQLI_ASSOC);

    mysqli_close($conn);

?>
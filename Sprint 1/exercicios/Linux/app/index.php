<?php 
    include_once "conn.php";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Usuários do sistema</h1>
    <ul>
        <?php foreach($users as $user): ?>
            <li>
                Nome:
                <?php echo $user['name'];?>,
                 idade:
                <?php echo $user['age'];?>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
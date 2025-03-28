<?php
header('Content-Type: text/plain; charset=utf-8');

$counterFile = 'counter.txt';

if (!file_exists($counterFile)) {
    file_put_contents($counterFile, '0');
}

if (!is_readable($counterFile) || !is_writable($counterFile)) {
    echo "Error: Counter file is not readable or writable";
    exit;
}

if(isset($_POST['increment']) && $_POST['increment'] == 1) {
    $count = (int)file_get_contents($counterFile);
    $count++;
    file_put_contents($counterFile, $count);
    echo $count;
    exit;
}

if(isset($_GET['get']) && $_GET['get'] == 1) {
    $count = (int)file_get_contents($counterFile);
    echo $count;
    exit;
}

echo (int)file_get_contents($counterFile);
?> 
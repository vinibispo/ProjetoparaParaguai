<?php
    $combination = explode(' ',$_POST['num']);
    $s = 0;
    foreach ($combination as $key => $value) {
        $s += (int)$value;
    }
    print($s);
?>
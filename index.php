<?php
    $combination = explode(' ',$_POST['num']);
    $s = 0;
    $list = [];
    foreach ($combination as $key => $el) {
        $element = (int)$el;
        foreach ($combination as $key => $value) {
                if($element != $value){
                    $s = $element + (int)$value;
                    array_push($list, $s);
                }
        }
    }
    print_r($list);
?>
<?php
$str=file_get_contents("items.json");

$search = array(" ","　","\n","\r","\t");
$replace = array("","","","","");
$str1=str_replace($search, $replace, $str);
$arr=json_decode($str1);
print_r($arr);
?>
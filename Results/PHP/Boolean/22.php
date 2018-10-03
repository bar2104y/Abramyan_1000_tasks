<?php
$a = readline("A: ");

$b = ($a % 100) / 10;
$b = (int)$b;
$c = $a % 10;
$a = $a / 100;
$a = (int)$a;

if ( ($a<$b && $b<$c) || ($a>$b && $b>$c)  ) echo "True";
else echo "Fasle";

echo "\n";
?>
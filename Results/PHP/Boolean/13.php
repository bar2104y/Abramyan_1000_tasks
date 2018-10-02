<?php
$a = readline("A: ");
$b = readline("B: ");
$c = readline("C: ");

$a = $a > 0;
$b = $b > 0;
$c = $c > 0;

if ( $a || $b || $c ) echo "True";
else echo "Fasle";

echo "\n";
?>
<?php
$a = readline("A: ");
$b = readline("B: ");
$c = readline("C: ");

$i = 0;

if ($a > 0) $i++;
if ($b > 0) $i++;
if ($c > 0) $i++;

if ( $i == 2 ) echo "True";
else echo "Fasle";

echo "\n";
?>
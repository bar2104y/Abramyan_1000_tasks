<?php
$a = readline("A: ");
$b = readline("B: ");
$c = readline("C: ");

$a = $a > 0;
$b = $b > 0;
$c = $c > 0;

if ( ($a xor $c) xor $b ) echo "True";
else echo "Fasle";


/*
$i = 0;

if ($a > 0) $i++;
if ($b > 0) $i++;
if ($c > 0) $i++;

if ( $i == 1 ) echo "True";
else echo "Fasle";
*/



echo "\n";
?>
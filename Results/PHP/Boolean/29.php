<?php

$x = readline("X: ");
$y = readline("Y: ");

$x1 = readline("X1: ");
$y1 = readline("Y1: ");

$x2 = readline("X2: ");
$y2 = readline("Y2: ");


if ( $x > $x1 && $x < $x2 && $y < $y1 && $y > $y2 ) echo "True";
else echo "Fasle";

echo "\n";

?>
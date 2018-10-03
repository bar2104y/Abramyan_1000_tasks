<?php

$x = readline("X 0<X1<9: ");
$y = readline("Y 0<Y1<9: ");
$x1 = readline("X 0<X2<9: ");
$y1 = readline("Y 0<Y2<9: ");

if ( abs($x-$x1) == abs($y-$y1) ) echo "True";
else echo "False";

echo "\n";
?>
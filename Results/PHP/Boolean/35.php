<?php

$x = readline("X 0<X1<9: ");
$y = readline("Y 0<Y1<9: ");
$x1 = readline("X 0<X2<9: ");
$y1 = readline("Y 0<Y2<9: ");

if ( ($x%2 == 0 xor $y%2 == 0) == ($x1%2 == 0 xor $y1%2 == 0) ) echo "True";
else echo "False";

echo "\n";

?>
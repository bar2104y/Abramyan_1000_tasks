<?php

$x = readline("X 0<X<9: ");
$y = readline("Y 0<Y<9: ");

if ( $x%2 == 0 xor $y%2 == 0 ) echo "White";
else echo "Black";

echo "\n";

?>
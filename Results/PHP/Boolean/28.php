<?php

$x = readline("X != 0: ");
$y = readline("Y != 0: ");

if ($x > 0 ) $x = 1;
else $x = -1;

if ($y > 0 ) $y = 1;
else $y = -1;

if ( $x * $y > 0 ) echo "True";
else echo "Fasle";

echo "\n";

?>
<?php

echo "A*x^2 + B*x + C = 0 \n";

$a = readline("A: ");
$b = readline("B: ");
$c = readline("C: ");

$d = $b*$b- (4*$c*$a);
if ( $d >= 0 ) echo "True";
else echo "Fasle";

echo "\n";

?>
<?php

$a = readline("A: ");
$b = readline("B: ");
$c = readline("C: ");

if ( $a+$b > $c && $a + $c > $b && $b+$c > $a ) echo "True";
else echo "Fasle";

echo "\n";

?>
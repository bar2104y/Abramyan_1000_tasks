<?php

$a = readline("A: ");
$b = readline("B: ");
$c = readline("C: ");

if ( ($a*$a == $b*$b + $c*$c) || ($b*$b == $a*$a + $c*$c) || ($c*$c == $a*$a + $b*$b)) echo "True";
else echo "Fasle";

echo "\n";

?>
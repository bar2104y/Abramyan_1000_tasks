<?php

$n = readline("N: ");

$a1 = 2;
$a2 = 1;
echo "1\n2\n";

for ($i = 0; $i<$n-2; $i++)
{
    $a = (2*$a1 + $a2)/3;
    $a2 = $a1
    $a1 = $a;
    echo $a . "\n";
}

?>
<?php

$n = readline("N: ");

$a1 = 3;
$a2 = 2;
$a3 = 1;
echo "1\n2\n3\n";

for ($i = 0; $i<$n-3; $i++)
{
    $a = $a1 + $a2- 2*$a3;
    $a3 = $a2;
    $a2 = $a1;
    $a1 = $a;
    echo $a . "\n";
}

?>
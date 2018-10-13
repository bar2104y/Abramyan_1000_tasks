<?php

$n = readline("N: ");

$f1 = 1;
$f2 = 1;
echo "1\n1\n";

for ($i = 0; $i<$n-2; $i++)
{
    $f = $f1 + $f2;
    $f2 = $f1;
    $f1 = $f;
    echo $f . "\n";
}


?>
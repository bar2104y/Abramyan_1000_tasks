<?php

$n = readline("N: ");
$k = readline("K: ");
$r = 0;

for ($i = 1; $i <= $n; $i++)
    $r += $i**$k;

echo "Sum = ".$r."\n";
?>
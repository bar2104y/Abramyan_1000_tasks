<?php
$n = readline("N: ");
$r = 0;

for ($i = 1; $i <= $n; $i++)
    $r += $i**$i;

echo "Sum = ".$r."\n";
?>
<?php
$n = readline("N: ");
$r = 0;

for ($i = 1; $i <= $n; $i++)
    $r += $i**($n-$i+1);
    
echo "Sum = ".$r."\n";
?>
<?php
echo "A<B\n";
$a = readline("A: ");
$b = readline("B: ");

for ($i = $a; $i <= $b; $i++)
    for ($j = 1; $j <= $i; $j++)
        echo $i."\n";
?>
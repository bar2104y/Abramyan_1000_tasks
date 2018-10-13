<?php
echo "A<B\n";
$a = readline("A: ");
$b = readline("B: ");
$k = 1;

for ($i = $a; $i <= $b; $i++)
{
	for ($j = 1; $j <= $k; $j++)
		echo $i."\n";
	$k++;
}
?>
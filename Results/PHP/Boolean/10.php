<?php
$a = readline("A: ");
$b = readline("B: ");

$a = $a % 2;
$b = $b % 2;

if ( $a xor $b )
{
	echo "True";
} else
{
	echo "Fasle";
}
echo "\n";
?>
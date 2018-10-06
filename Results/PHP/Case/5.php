<?php

$a = readline("Первое число: ");
$b = readline("Второе число: ");
$c = readline("Операция: ");

switch ($c) {
	case 1:
		$a = $a+$b;
		break;
	case 2:
		$a = $a-$b;
		break;
	case 3:
		$a = $a*$b;
		break;
	default:
		$a = $a/$b;
}

echo $a . "\n";

?>
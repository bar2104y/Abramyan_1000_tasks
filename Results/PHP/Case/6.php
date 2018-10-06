<?php

$a = readline("Единица измерения: ");
$b = readline("Длина: ");

switch ($b) {
	case 1:
		$a *= 0.1;
		break;
	case 2:
		$a *= 1000;
		break;
	case 3:
		break;
	case 4:
		$a /= 1000;
		break;
	case 5:
		$a /= 100;
}

echo $a . "\n";

?>
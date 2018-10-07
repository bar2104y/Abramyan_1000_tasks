<?php

$b = readline("Единица измерения: ");
$a = readline("Масса: ");

switch ($b) {
	case 1:
		break;
	case 2:
		$a /= 10000;
		break;
    case 3:
    $a /= 1000;
		break;
	case 4:
		$a *= 1000;
		break;
	case 5:
		$a *= 100;
}

echo $a . "\n";

?>
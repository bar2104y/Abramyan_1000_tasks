<?php

$a = readline("Оценка: ");

switch ($a) {
	case 1:
		$a = "Плохо";
		break;
	case 2:
		$a = "Неудовлетворительно";
		break;
	case 3:
		$a = "Удовлетворительно";
		break;
	case 4:
		$a = "Хорошо";
		break;
	case 5:
		$a = "Отлично";
		break;
}

echo $a . "\n";

?>
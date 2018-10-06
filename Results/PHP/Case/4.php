<?php

$a = readline("Номер месяца: ");

switch ($a) {
	case 1:
		$a = "Январь, 31 день";
		break;
	case 2:
		$a = "Февраль, 28 день";
		break;
	case 3:
		$a = "Март, 31 день";
		break;
	case 4:
		$a = "Апрель, 30 день";
		break;
	case 5:
		$a = "Май, 31 день";
		break;
	case 6:
		$a = "Июнь, 30 день";
		break;
	case 7:
		$a = "Июль, 31 день";
		break;
	case 8:
		$a = "Август, 31 день";
		break;
	case 9:
		$a = "Сентябрь, 30 день";
		break;
	case 10:
		$a = "Октябрь, 31 день";
		break;
	case 11:
		$a = "Ноябрь, 30 день";
		break;
	case 12:
		$a = "Декабрь, 31 день";
		break;
}

echo $a . "\n";

?>
package main

import (
	"fmt"
	"math"
)

func main(){
	var a,b float64

	fmt.Println("Результаты с модулями")

	fmt.Print("A: ")
	fmt.Scan(&a)

	fmt.Print("B: ")
	fmt.Scan(&b)

	a = math.Abs(a)
	b = math.Abs(b)

	fmt.Println("Сумма:    " , a+b)
	fmt.Println("Разность: " , a-b)
	fmt.Println("Частное:  " , a/b)
}
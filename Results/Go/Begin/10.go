package main

import "fmt"

func main(){
	var a,b float64

	fmt.Println("Среднее арифмитическое")

	fmt.Print("A: ")
	fmt.Scan(&a)

	fmt.Print("B: ")
	fmt.Scan(&b)

	a *= a
	b *= b

	fmt.Println("Сумма:    " , a+b)
	fmt.Println("Разность: " , a-b)
	fmt.Println("Частное:  " , a/b)
}
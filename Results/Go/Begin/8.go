package main

import "fmt"

func main() {
	var a,b float32

	fmt.Println("Среднее значение")

	fmt.Print("A: ")
	fmt.Scan(&a)

	fmt.Print("B: ")
	fmt.Scan(&b)

	var r float32
	r = (a+b)/2
	fmt.Println("Результат", r)
}

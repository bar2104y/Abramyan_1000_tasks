package main

import "fmt"
import "math"

func main(){
	var a,b,r float64

	fmt.Println("Среднее арифмитическое")

	fmt.Print("A: ")
	fmt.Scan(&a)

	fmt.Print("B: ")
	fmt.Scan(&b)

	r = math.Sqrt(a*b)
	fmt.Println("Результат" , r)
}
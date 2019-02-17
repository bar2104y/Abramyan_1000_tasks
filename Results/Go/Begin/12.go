package main

import (
	"fmt"
	"math"
)

func main(){
	var a,b float64

	fmt.Println("Теорема Пифагора")

	fmt.Print("A: ")
	fmt.Scan(&a)

	fmt.Print("B: ")
	fmt.Scan(&b)
	a *= a
	b *= b

	fmt.Println("Гипотенуза:" , math.Sqrt(a+b))
}
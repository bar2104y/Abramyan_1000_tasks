package main

import (
	"fmt"
)

func main(){
	var r1,r2 float64

	fmt.Println("Площади кругов R1>R2")

	fmt.Print("R1: ")
	fmt.Scan(&r1)

	fmt.Print("R2: ")
	fmt.Scan(&r2)

	fmt.Println("S1:" , S(r1))
	fmt.Println("S1:" , S(r2))
	fmt.Println("S1-S2:" , S(r1) - S(r2))
}

func S(r float64) float64{
	var Pi float64 = 3.14

	return Pi * r * r
}
package main

import "fmt"
import "math"

func main (){
	var d float32

	fmt.Print("d: ")
	fmt.Scan(&d)

	var l float32
	l = math.Pi * d

	fmt.Println("L = ", l)

}
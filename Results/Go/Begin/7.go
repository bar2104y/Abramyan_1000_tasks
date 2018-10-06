package main

import "fmt"
import "math"

func main (){
	var r float32

	fmt.Print("R: ")
	fmt.Scan(&r)

	var l = math.Pi * r*2
	var s = math.Pi * r*r

	fmt.Println("L = ", l)
	fmt.Println("S = ", s)
}
package main

import "fmt"

func main (){
	var a,b,c int

	fmt.Print("a: ")
	fmt.Scan(&a)
	fmt.Print("b: ")
	fmt.Scan(&b)
	fmt.Print("c: ")
	fmt.Scan(&c)

	var v = a*b*c
	var s = 2 * (a*b + b*c + a*c)

	fmt.Println("V = ", v)
	fmt.Println("S = ", s)
}
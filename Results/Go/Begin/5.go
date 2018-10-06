package main

import "fmt"

func main (){
	var a int

	fmt.Print("a: ")
	fmt.Scan(&a)

	var v = a*a*a
	var s = 6 * a

	fmt.Println("V = ", v)
	fmt.Println("S = ", s)

}
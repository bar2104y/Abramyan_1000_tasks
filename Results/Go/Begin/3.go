package main

import "fmt"

func main (){
	var a,b int

	fmt.Print("A:")
	fmt.Scan(&a)
	fmt.Print("B:")
	fmt.Scan(&b)

	fmt.Println("S = ", a*b)
	fmt.Println("P = ", 2*(a+b))

}
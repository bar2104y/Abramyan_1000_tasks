package main

import "fmt"

func main(){
	var a int
	fmt.Print("L: ")
	fmt.Scan(&a)

	a /= 100

	fmt.Println	(a)
}
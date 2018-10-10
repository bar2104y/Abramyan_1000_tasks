package main

import "fmt"

func main(){
	var a int
	fmt.Print("M: ")
	fmt.Scan(&a)

	a /= 1000

	fmt.Println	(a)
}
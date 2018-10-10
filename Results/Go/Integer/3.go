package main

import "fmt"

func main(){
	var a int
	fmt.Print("Size(bytes): ")
	fmt.Scan(&a)

	a /= 1024

	fmt.Println	(a, " KB")
}
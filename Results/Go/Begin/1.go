package main

import "fmt"

func main (){
	var a int

	fmt.Print("A:")
	fmt.Scan(&a)

	a = a * 4;

	fmt.Println(a)

}
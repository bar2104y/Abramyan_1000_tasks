package main

import "fmt"

func main (){
	var n int

	fmt.Print("N:")
	fmt.Scan(&n)

	a:= make([]int, n)

	for i := 0; i<n; i++{
		a[i] = i+1
	}

	fmt.Print(a)
	fmt.Println()

}
package main

import "fmt"

func main (){
	var n int
	var c int
	c = 2

	fmt.Print("N:")
	fmt.Scan(&n)

	a:= make([]int, n)

	for i := 0; i<n; i++{
		a[i] = c
		c *= 2
	}

	fmt.Print(a)
	fmt.Println()

}
// Project Euler - Problem 003
// Joao Antao

// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

package main
import ("fmt"; "runtime")

func Solution(n int) int {
  factor := 2

  for n > factor {
    if n % factor == 0 {
      n /= factor
      factor = 2
    } else {
      factor += 1
    }
  }
  return n
}

func main() {
    number := 600851475143
    os := runtime.GOOS

    defer fmt.Println(Solution(number))
    fmt.Println("Operating system: ", os)
}

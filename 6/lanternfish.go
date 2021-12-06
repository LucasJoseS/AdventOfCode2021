package main

import (
    "os"
    "fmt"
    "strings"
    "strconv"
    "log"
)

func main() {
     file, err := os.Open(os.Args[1])
     if err != nil { log.Fatal(err) }
     defer file.Close()

     stat, _ := file.Stat()

     bs := make([]byte, stat.Size())
     _, err = file.Read(bs)
     if err != nil { log.Fatal(err) }

     fishs := make(map[int]uint64, 0) // map[clock] count fishs

     content := string(bs)
     for _ , s := range strings.Split(content, ",") {
     	 clock, err := strconv.Atoi(s)
	 if err != nil { log.Fatal(err) }

	 fishs[clock] ++
     }

     for day := 0; day<=256; day++ {
     	 fmt.Print(day)

	 sum := uint64(0)
	 for i := 0; i <= 8; i++ {
	     sum += fishs[i]
	 }

	 fmt.Println(" ", sum)

	 for key := 0; key <= 8; key++ {
	     if value, ok := fishs[key]; ok {
	     	fishs[key-1] = value
		fishs[key] = 0
	     }
	 }

	 if value, ok := fishs[-1]; ok && value > 0 {
	    fishs[8] = value
	    fishs[6] += value
	    fishs[-1] = 0
	 }
     }
}
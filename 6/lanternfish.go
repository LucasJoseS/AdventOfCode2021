package main

import (
    "os"
    "fmt"
    "strings"
    "strconv"
)

func main() {
     file, err := os.Open(os.Args[1])
     if err != nil { fmt.Println("File no found"); return }
     defer file.Close()

     stat, _ := file.Stat()
     bs := make([]byte, stat.Size())
     
     _, err = file.Read(bs)
     if err != nil { return }

     content := string(bs)
     fish_ages_str := strings.Split(content, ",")
     fishs := make([]int, len(fish_ages_str))
     
     for i, s := range fish_ages_str {
     	 fishs[i], _ = strconv.Atoi(s)
     }

     max_day := 80
     for day := 0; day < max_day+1; day++ {
     	 fmt.Println(day, len(fishs))
	 
     	 for ifish, vfish := range fishs {
	     fishs[ifish] = fishs[ifish] - 1

	     if vfish == 0 { fishs[ifish] = 6; fishs = append(fishs, 8) }
	 }
     }
 }
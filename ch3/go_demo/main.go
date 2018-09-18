package main

import (
    "fmt"
    "log"
    "net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {

    str := "Hello go world !"
    fmt.Fprintf(w, str)
}

func main() {
    ht := http.HandlerFunc(helloHandler)
    if ht != nil {
        http.Handle("/hello", ht)
    }
    fmt.Println("go server start at port :9999!")
    err := http.ListenAndServe(":9999", nil)
    if err != nil {
        log.Fatal("ListenAndServe: ", err.Error())
    }
}
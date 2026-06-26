package main

import (
    "fmt"
    "net/http"
    "time"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        loc, _ := time.LoadLocation("Europe/Moscow")
        now := time.Now().In(loc)
        fmt.Fprintf(w, "Московское время: %s", now.Format("15:04:05"))
    })
    http.ListenAndServe(":8080", nil)
}

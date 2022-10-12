package main

import (
	"fmt"
	"net/http"

	"github.com/amitsaha/middleware-web-apps/go/server/middleware"
)

func indexHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello world")
}

func protectedHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "This is a protected resource")
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", indexHandler)
	mux.HandleFunc("/api/protected", middleware.AuthRequired(protectedHandler))
	http.ListenAndServe(":8080", mux)
}

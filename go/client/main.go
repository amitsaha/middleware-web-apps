package main

import (
	"log"

	"github.com/amitsaha/middleware-web-apps/go/client/middleware"
)

func main() {
	client := middleware.GetHTTPClient()

	resp, err := client.Head("https://github.com")
	if err != nil {
		log.Fatal(err)
	}
	log.Println(resp.Status)

	resp, err = client.Get("https://github.com")
	if err != nil {
		log.Fatal(err)
	}
	log.Println(resp.Status)
}

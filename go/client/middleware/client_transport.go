package middleware

import (
	"log"
	"net/http"
	"time"
)

type latencyLogger struct{}

func (l *latencyLogger) RoundTrip(req *http.Request) (*http.Response, error) {

	start := time.Now()
	resp, err := http.DefaultTransport.RoundTrip(req)
	log.Printf("url=%s method=%s error=\"%v\" latency=%v", req.URL.String(), req.Method, err, time.Since(start))
	return resp, err
}

func GetHTTPClient() *http.Client {
	return &http.Client{
		Transport: &latencyLogger{},
	}
}

package middleware

import "net/http"

func AuthRequired(handler http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if len(r.Header.Get("X-API-Key")) == 0 {
			http.Error(w, "Specify X-API-Key header", http.StatusUnauthorized)
			return
		}
		handler(w, r)
	}
}

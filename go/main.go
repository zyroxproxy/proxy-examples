// Zyrox Proxy with Go net/http: rotating, country and parallel sticky sessions.
//
//	go run .
package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
	"sync"
	"time"
)

// client builds an HTTP client whose proxy username carries the options.
// url.UserPassword escapes special characters in the password for you.
func client(options string) *http.Client {
	proxyURL := &url.URL{
		Scheme: "http",
		User:   url.UserPassword(os.Getenv("ZYROX_USER")+options, os.Getenv("ZYROX_PASS")),
		Host:   "host.zyroxproxy.com:7000",
	}
	return &http.Client{
		Transport: &http.Transport{Proxy: http.ProxyURL(proxyURL)},
		Timeout:   30 * time.Second,
	}
}

func getIP(c *http.Client) string {
	resp, err := c.Get("https://api.ipify.org")
	if err != nil {
		return "error: " + err.Error()
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	return string(body)
}

func main() {
	fmt.Println("Rotating:     ", getIP(client("")), getIP(client("")))
	fmt.Println("United States:", getIP(client("-country-us")))

	// Five sticky sessions in parallel: one IP per worker.
	var wg sync.WaitGroup
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			c := client(fmt.Sprintf("-country-us-session-worker%d", id))
			fmt.Printf("worker %d: %s\n", id, getIP(c))
		}(i)
	}
	wg.Wait()
}

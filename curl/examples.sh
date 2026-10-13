#!/usr/bin/env bash
# Zyrox Proxy with curl. Set ZYROX_USER and ZYROX_PASS first.
# Always quote the proxy URL — it can contain characters your shell treats specially.
set -euo pipefail
: "${ZYROX_USER:?set ZYROX_USER}" "${ZYROX_PASS:?set ZYROX_PASS}"
HOST="host.zyroxproxy.com"

echo "Rotating (new IP every request):"
curl -s -x "http://${ZYROX_USER}:${ZYROX_PASS}@${HOST}:7000" https://api.ipify.org; echo

echo "Country targeting (US):"
curl -s -x "http://${ZYROX_USER}-country-us:${ZYROX_PASS}@${HOST}:7000" https://api.ipify.org; echo

echo "Sticky session (same IP, 30 min by default):"
for i in 1 2; do
  curl -s -x "http://${ZYROX_USER}-country-us-session-demo1:${ZYROX_PASS}@${HOST}:7000" https://api.ipify.org; echo
done

echo "Sticky session held for 90 minutes (max 120):"
curl -s -x "http://${ZYROX_USER}-country-us-session-demo2-sessiontime-90:${ZYROX_PASS}@${HOST}:7000" https://api.ipify.org; echo

echo "SOCKS5 (port 7001, DNS resolved at the exit with socks5h):"
curl -s -x "socks5h://${ZYROX_USER}-country-de:${ZYROX_PASS}@${HOST}:7001" https://api.ipify.org; echo

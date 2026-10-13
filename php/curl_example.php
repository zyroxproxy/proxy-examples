<?php
// Zyrox Proxy with PHP cURL: country, sticky session and SOCKS5.
//   php curl_example.php

function fetchIp(string $options, bool $socks5 = false): string
{
    $ch = curl_init('https://api.ipify.org');

    if ($socks5) {
        curl_setopt($ch, CURLOPT_PROXY, 'host.zyroxproxy.com:7001');
        // _HOSTNAME = resolve DNS at the exit, not locally.
        curl_setopt($ch, CURLOPT_PROXYTYPE, CURLPROXY_SOCKS5_HOSTNAME);
    } else {
        curl_setopt($ch, CURLOPT_PROXY, 'host.zyroxproxy.com:7000');
    }

    curl_setopt($ch, CURLOPT_PROXYUSERPWD, getenv('ZYROX_USER') . $options . ':' . getenv('ZYROX_PASS'));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, 30);

    $body = curl_exec($ch);
    if ($body === false) {
        throw new RuntimeException('Proxy request failed: ' . curl_error($ch));
    }
    curl_close($ch);

    return $body;
}

echo 'United States: ', fetchIp('-country-us'), PHP_EOL;
echo 'Sticky (30m):  ', fetchIp('-country-us-session-php1-sessiontime-30'), ' ',
    fetchIp('-country-us-session-php1-sessiontime-30'), PHP_EOL;
echo 'SOCKS5 (DE):   ', fetchIp('-country-de', true), PHP_EOL;

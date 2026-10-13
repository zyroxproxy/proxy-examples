<?php
// Zyrox Proxy with Guzzle.
//   composer require guzzlehttp/guzzle
//   php guzzle_example.php

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;

function clientFor(string $options): Client
{
    $user = getenv('ZYROX_USER') . $options;
    // URL-encode the password in case it contains special characters.
    $pass = rawurlencode(getenv('ZYROX_PASS'));

    return new Client([
        'proxy' => "http://{$user}:{$pass}@host.zyroxproxy.com:7000",
        'timeout' => 30,
    ]);
}

echo 'United States: ', clientFor('-country-us')->get('https://api.ipify.org')->getBody(), PHP_EOL;

$sticky = clientFor('-country-gb-session-guzzle1');
echo 'Sticky (GB):   ', $sticky->get('https://api.ipify.org')->getBody(), ' ',
    $sticky->get('https://api.ipify.org')->getBody(), PHP_EOL;

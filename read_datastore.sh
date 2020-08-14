#!/usr/bin/env bash
php -r 'print(json_encode(unserialize(gzinflate(base64_decode(preg_replace("!.*/\* (.+) \*/.*!", "$1", file_get_contents("datastore.php")))))));' | jq .

#!/bin/bash
# cURL body size

curl -oI "$1" -w '%{size_download}\n'
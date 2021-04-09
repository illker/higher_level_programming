#!/bin/bash
# cURL body size

curl -soI "$1" -w '%{size_download}\n'

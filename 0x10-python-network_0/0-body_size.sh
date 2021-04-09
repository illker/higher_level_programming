#!/bin/bash
# cURL to the end
curl -oI "$1" -w '%{size_download}\n'

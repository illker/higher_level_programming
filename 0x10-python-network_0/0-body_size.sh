#!/bin/bash
# cURL to the end
curl -Is "$1" | grep Content-Length | cut -d " " -f2

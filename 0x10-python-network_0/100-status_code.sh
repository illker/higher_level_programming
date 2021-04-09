#!/bin/bash
# Only status code
curl -soI "$1" -w "%{http_code}"

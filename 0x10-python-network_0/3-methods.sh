#!/bin/bash
# cURL only methods
curl -sI "$1" | grep 'OPTIONS' | cut -d ' ' -f 2-

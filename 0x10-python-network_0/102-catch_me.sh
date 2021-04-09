#!/bin/bash
# Catch me if you can!
curl -soI /dev/null '0.0.0.0:5000/catch_me' -w 'You got me!'

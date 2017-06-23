#!/usr/bin/env bash

zip -r ./tmp ./
aws lambda update-function-code --function-name call_my_phone --zip-file fileb://tmp.zip
rm ./tmp.zip

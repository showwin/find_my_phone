# find_my_phone

This is an [AWS Lambda](https://aws.amazon.com/lambda/) function to make phone call with [Twilio](https://www.twilio.com/).

runtime: Python 3.6

## How to Use

1. Install `twilio` library to root directory of this repository.
```
$ cd /path/to/find_my_phone
$ pip install twilio -t ./
```
2. Just Deploy !!! (assume your Lambda function name is `call_my_phone`)
```
$ ./deploy.sh
```

## Prepare to call

1. Create Twilio account and get `ACCOUNT SID`, `AUTH TOKEN` and your Twilio phone number.
2. Make TwiML `sample.xml` like follows:
```xml
<Response>
    <Say voice="alice" language="ja-JP">こんにちは。(Hello)</Say>
</Response>
```
3. Upload `sample.xml` to somewhere like AWS S3.
4. Set environment variables at AWS lambda.
    * `TWILIO_ACCOUNT_SID`: Twilio `ACCOUNT SID`
    * `TWILIO_AUTH_TOKEN`: Twilio `AUTH TOKEN`
    * `PHONE_NUMBER_TO_CALL`: phone number which you want to call.
    * `TWILIO_PHONE_NUMBER`: your Twilio phone number.
    * `TWIML_PATH`: URL of `sample.xml`, need to response by HTTP request.

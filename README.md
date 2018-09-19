# Twilio Call Recorder

A simple AWS Lambda that allows you to call a Twilio incoming number, dial another number using your phone's keypad and record the subsequent call.

See [https://myles.eftos.id.au/blog/2018/09/19/call-recording-with-twilio-aws-lamba-rev/](https://myles.eftos.id.au/blog/2018/09/19/call-recording-with-twilio-aws-lamba-rev/) for details

## Packaging

```bash
git clone git https://github.com/madpilot/twilio-call-recorder
twilio-call-recorder
pip install twilio -t ./
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
zip -r lambda.zip *
```

## Licence

See LICENSE

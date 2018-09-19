# Twilio Call Recorder

A simple AWS Lambda that allows you to call a Twilio incoming number, dial another number using your phone's keypad and record the subsequent call.

## Packaging

```bash
git clone git https://github.com/madpilot/twilio-call-recorder
pip install -t twilio
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
zip -r lambda.zip *
```

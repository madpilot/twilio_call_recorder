from twilio.twiml.voice_response import VoiceResponse, Say, Gather, Dial
from urllib.parse import parse_qs

LANGUAGE="en-AU"
AUTHORISED_NUMBERS = ['ADD YOUR PHONE NUMBER HERE IN INTERNATIONAL FORMAT ie +61400000000']

def authorized_number(number):
    return number in AUTHORISED_NUMBERS

def say(words):
    return Say(words, voice="alice", language=LANGUAGE)

def get_outgoing_number(request):
    response = VoiceResponse()

    action = "/" + request['requestContext']['stage'] + "/ivr"
    words = say("Please dial the number you would like to call, followed by the hash key.")

    gather = Gather(action=action)
    gather.append(words)
    response.append(gather)

    return response

def add_country_code(number):
    if number[0] == "+":
        return number
    elif number[0] == "0":
        return "+61" + number[1:]
    elif number[0:2] == "13":
        return "+61" + number
    elif number[0:2] == "1800":
        return "+61" + number

def hangup():
    response = VoiceResponse()
    response.hangup()
    return response

def handle_ivr_input(params):
    to = params['Digits'][0]
    dial = Dial(add_country_code(to), record="record-from-answer-dual", caller_id=params['Caller'])

    response = VoiceResponse()
    response.append(say("Calling."))
    response.append(dial)
    return response

def handler(request, context):
    path = request['path']
    params = parse_qs(request['body'])

    response = ""
    if path == "/incoming":
        if authorized_number(params["Caller"][0]):
            response = get_outgoing_number(request)
        else:
            response = hangup()
    elif path == "/ivr":
        response = handle_ivr_input(params)
    else:
        return {
            'body': "Action not defined",
            'statusCode': 404,
            'isBase64Encoded': False,
            'headers': { 'context_type': 'text/plain' }
        }

    return {
        'body': str(response),
        'statusCode': 200,
        'isBase64Encoded': False,
        'headers': { 'content_type': 'text/xml' }
    }

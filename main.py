from flask import Flask, request, Response
from flask_cors import CORS
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

CORS(app)

def get_workers_on_shift():
    """
    Queries for workers on shift and their respective phone numbers.
    """
    return [('John', '')]

def forward_call(worker_obj):
    """
    Forwards the call to the selected shift worker

    worker_obj:tuple: Worker's name and number as two argument tuple.
    """

    print('Processing Call Forward')
    response = VoiceResponse()
    response.say(f"Forwarding your call to, {worker_obj[1]}")
    response.dial(worker_obj[1])

    return Response(str(response), 200, mimetype="application/xml")


@app.route('/callforward', methods=['POST'])
def index():
    print(request.values)

    workers = get_workers_on_shift()

    #answered = False
    #i = 0
    #while not answered:
    #    try:
    resp = forward_call(workers[0])
    #    except Exception as e:
    #        print(e)
    #    i += 1
    return resp


if __name__ == '__main__':
    app.run(debug=True)

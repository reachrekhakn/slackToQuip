import logging
import os
import quipclient
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from flask_restful import Resource



class HelloController(Resource):

    def get(self):
        ############################### slack section #######################################

        client = WebClient(token="xoxb-2412490052337-2386128563351-L4Eka0Vl96Z2x843bpvuw8a1")
        logger = logging.getLogger(__name__)
#         # ID of channel that the message exists in
        conversation_id = "C02BNRZHB2R"
        message = "yes"
        result = "hi"
        try:

            threadStrMessages = ""
            result = client.conversations_replies(
                channel=conversation_id,
                ts="1629396812.002000")

            print(result)
            threadMessages = []
            message = result["messages"]
            for msg in message:
                print(msg["text"])
                threadMessages.append(msg["text"])
                threadStrMessages = threadStrMessages + "\n "
                threadStrMessages = threadStrMessages + msg["text"]
        ############################### slack section ######################################


        ############################### quip section #######################################

            ACCESS_TOKEN = 'WkpEQU1BT0R4MnQ=|1661037573|7jTgRhINX59Ugjw2iiOHqQEgia8ZvcKm6nViNPJjh78='
            quipClient = quipclient.QuipClient(access_token=ACCESS_TOKEN)
            jso = quipClient.new_document(threadStrMessages, title="My Spreadsheet 345")

        ############################### quip section #######################################

        except SlackApiError as e:
            print(f"Error: {e}")
        return {"response": threadStrMessages}


def post(self):
    return {"response": "hello post"}


def put(self):
    return {"response": "hello put"}


def delete(self):
    return {"response": "hello delete"}

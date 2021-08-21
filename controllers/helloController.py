import logging
import os
import quipclient
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from flask_restful import Resource



class HelloController(Resource):

    def get(self):
        print("Fer")
        # WebClient insantiates a client that can call API methods
        # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
        # client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))



        # slack section
        client = WebClient(token="xoxb-2412490052337-2386128563351-IXvAQ3pmNuvEXYmInlv8D3dZ")
        client = WebClient(token="xoxb-2412490052337-2386128563351-5fRzhLjAQ2ukpZyseA7CVSPg")
        logger = logging.getLogger(__name__)
#         # ID of channel that the message exists in
        conversation_id = "C02BNRZHB2R"
        message = "yes"
        result = "hi"
        try:
            res = "hi"
#             # Call the conversations.history method using the WebClient
#             # The client passes the token you included in initialization
#             result = client.conversations_history(
#                 channel=conversation_id,
#                 inclusive=True,
#                 oldest="629396812.002000",
#                 limit=10
#             )
            #https://hackaton-sf.slack.com/archives/C02BNRZHB2R/p1629396812002000
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
            ACCESS_TOKEN = 'change'
            quipClient = quipclient.QuipClient(access_token=ACCESS_TOKEN)
            jso = quipClient.new_document(threadStrMessages, title="My Spreadsheet 345")
        except SlackApiError as e:
            print(f"Error: {e}")
        return {"response": threadStrMessages}


def post(self):
    return {"response": "hello post"}


def put(self):
    return {"response": "hello put"}


def delete(self):
    return {"response": "hello delete"}

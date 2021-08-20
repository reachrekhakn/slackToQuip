import logging
import os
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
        client = WebClient(token="xoxb-2412490052337-2386128563351-5fRzhLjAQ2ukpZyseA7CVSPg")
        logger = logging.getLogger(__name__)
        # ID of channel that the message exists in
        conversation_id = "C02BNRZHB2R"

        try:
            # Call the conversations.history method using the WebClient
            # The client passes the token you included in initialization    
            result = client.conversations_history(
                channel=conversation_id,
                inclusive=True,
                oldest="629396812.002000",
                limit=10
            )
            print(result)
            message = result["messages"][0]
            # Print message text
            print(message["text"])

        except SlackApiError as e:
            print(f"Error: {e}")
        return {"response": result}


def post(self):
    return {"response": "hello post"}


def put(self):
    return {"response": "hello put"}


def delete(self):
    return {"response": "hello delete"}

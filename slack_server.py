from concurrent import futures
import time

import grpc

import event_pb2
import event_pb2_grpc

import yaml
import requests
import json

import event_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
SLACK_MESSAGE_API = 'https://slack.com/api/chat.postMessage'

try:
    SLACK_TOKEN = yaml.load(open('settings.yml','r'))['slack_token']
except:
    SLACK_TOKEN = os.environ["SLACK_TOKEN"]

def post_message(msg):
    data = {
        'token': SLACK_TOKEN,
        'channel': "sandbox",
        'text': msg,
        'username': "Bot"
    }
    result = requests.post(url=SLACK_MESSAGE_API, data=data)
    return result

class Slack(event_pb2_grpc.SlackServicer):
    def SendEvent(self, request, context):
        msg = "Summary:" + request.summary + "\n" + "Description:" + request.description + "\n"
        res = post_message(msg)
        return event_pb2.Status(status_code = str(res))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    event_pb2_grpc.add_SlackServicer_to_server(Slack(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

from __future__ import print_function

import grpc

import event_pb2
import event_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = event_pb2_grpc.SlackStub(channel)
    response = stub.SendEvent(event_pb2.Event(summary='Test event',description="This is test"))
    print(response)


if __name__ == '__main__':
    run()

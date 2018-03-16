# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import event_pb2 as event__pb2


class SlackStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendEvent = channel.unary_unary(
        '/camome.calendar.Slack/SendEvent',
        request_serializer=event__pb2.Event.SerializeToString,
        response_deserializer=event__pb2.Status.FromString,
        )


class SlackServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SendEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SlackServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendEvent': grpc.unary_unary_rpc_method_handler(
          servicer.SendEvent,
          request_deserializer=event__pb2.Event.FromString,
          response_serializer=event__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'camome.calendar.Slack', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
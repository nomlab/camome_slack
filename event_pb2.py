# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event.proto',
  package='camome.calendar',
  syntax='proto3',
  serialized_pb=_b('\n\x0b\x65vent.proto\x12\x0f\x63\x61mome.calendar\x1a\x1fgoogle/protobuf/timestamp.proto\"0\n\x04\x44\x61te\x12(\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"J\n\x08\x44\x61teTime\x12,\n\x08\x64\x61teTime\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08timeZone\x18\x02 \x01(\t\"p\n\nDateOrTime\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x15.camome.calendar.DateH\x00\x12-\n\x08\x64\x61teTime\x18\x02 \x01(\x0b\x32\x19.camome.calendar.DateTimeH\x00\x42\x0c\n\nDateOrTime\"\x83\x01\n\x05\x45vent\x12*\n\x05start\x18\x01 \x01(\x0b\x32\x1b.camome.calendar.DateOrTime\x12(\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1b.camome.calendar.DateOrTime\x12\x0f\n\x07summary\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"\x1d\n\x06Status\x12\x13\n\x0bstatus_code\x18\x01 \x01(\t2G\n\x05Slack\x12>\n\tSendEvent\x12\x16.camome.calendar.Event\x1a\x17.camome.calendar.Status\"\x00\x42\x38\n\x11org.nomlab.camomeB\x0b\x45ventProtos\xaa\x02\x15\x43\x61mome.Calendar.Eventb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_DATE = _descriptor.Descriptor(
  name='Date',
  full_name='camome.calendar.Date',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='camome.calendar.Date.date', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=113,
)


_DATETIME = _descriptor.Descriptor(
  name='DateTime',
  full_name='camome.calendar.DateTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dateTime', full_name='camome.calendar.DateTime.dateTime', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeZone', full_name='camome.calendar.DateTime.timeZone', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=189,
)


_DATEORTIME = _descriptor.Descriptor(
  name='DateOrTime',
  full_name='camome.calendar.DateOrTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='camome.calendar.DateOrTime.date', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dateTime', full_name='camome.calendar.DateOrTime.dateTime', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='DateOrTime', full_name='camome.calendar.DateOrTime.DateOrTime',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=191,
  serialized_end=303,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='camome.calendar.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='camome.calendar.Event.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='camome.calendar.Event.end', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='summary', full_name='camome.calendar.Event.summary', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='camome.calendar.Event.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=437,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='camome.calendar.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='camome.calendar.Status.status_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=439,
  serialized_end=468,
)

_DATE.fields_by_name['date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATETIME.fields_by_name['dateTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATEORTIME.fields_by_name['date'].message_type = _DATE
_DATEORTIME.fields_by_name['dateTime'].message_type = _DATETIME
_DATEORTIME.oneofs_by_name['DateOrTime'].fields.append(
  _DATEORTIME.fields_by_name['date'])
_DATEORTIME.fields_by_name['date'].containing_oneof = _DATEORTIME.oneofs_by_name['DateOrTime']
_DATEORTIME.oneofs_by_name['DateOrTime'].fields.append(
  _DATEORTIME.fields_by_name['dateTime'])
_DATEORTIME.fields_by_name['dateTime'].containing_oneof = _DATEORTIME.oneofs_by_name['DateOrTime']
_EVENT.fields_by_name['start'].message_type = _DATEORTIME
_EVENT.fields_by_name['end'].message_type = _DATEORTIME
DESCRIPTOR.message_types_by_name['Date'] = _DATE
DESCRIPTOR.message_types_by_name['DateTime'] = _DATETIME
DESCRIPTOR.message_types_by_name['DateOrTime'] = _DATEORTIME
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), dict(
  DESCRIPTOR = _DATE,
  __module__ = 'event_pb2'
  # @@protoc_insertion_point(class_scope:camome.calendar.Date)
  ))
_sym_db.RegisterMessage(Date)

DateTime = _reflection.GeneratedProtocolMessageType('DateTime', (_message.Message,), dict(
  DESCRIPTOR = _DATETIME,
  __module__ = 'event_pb2'
  # @@protoc_insertion_point(class_scope:camome.calendar.DateTime)
  ))
_sym_db.RegisterMessage(DateTime)

DateOrTime = _reflection.GeneratedProtocolMessageType('DateOrTime', (_message.Message,), dict(
  DESCRIPTOR = _DATEORTIME,
  __module__ = 'event_pb2'
  # @@protoc_insertion_point(class_scope:camome.calendar.DateOrTime)
  ))
_sym_db.RegisterMessage(DateOrTime)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'event_pb2'
  # @@protoc_insertion_point(class_scope:camome.calendar.Event)
  ))
_sym_db.RegisterMessage(Event)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'event_pb2'
  # @@protoc_insertion_point(class_scope:camome.calendar.Status)
  ))
_sym_db.RegisterMessage(Status)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\021org.nomlab.camomeB\013EventProtos\252\002\025Camome.Calendar.Event'))

_SLACK = _descriptor.ServiceDescriptor(
  name='Slack',
  full_name='camome.calendar.Slack',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=470,
  serialized_end=541,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendEvent',
    full_name='camome.calendar.Slack.SendEvent',
    index=0,
    containing_service=None,
    input_type=_EVENT,
    output_type=_STATUS,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SLACK)

DESCRIPTOR.services_by_name['Slack'] = _SLACK

# @@protoc_insertion_point(module_scope)
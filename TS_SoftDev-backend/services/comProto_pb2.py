# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='comProto.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x63omProto.proto\"\x9a\x01\n\x0e\x63ommandMessage\x12\x0b\n\x03one\x18\x01 \x01(\t\x12\x0b\n\x03two\x18\x02 \x01(\t\x12\r\n\x05three\x18\x03 \x01(\t\x12\x0c\n\x04\x66our\x18\x04 \x01(\t\x12\x0c\n\x04\x66ive\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12\x10\n\x08passcode\x18\x07 \x01(\t\x12\x12\n\ngetCommand\x18\x08 \x01(\t\x12\x11\n\tuidLatest\x18\t \x01(\t\"n\n\rlatestCommand\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\x12\x10\n\x08response\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x10\n\x08passcode\x18\x05 \x01(\t\x12\x0f\n\x07resList\x18\x06 \x03(\t2B\n\x0e\x63ommandService\x12\x30\n\ntopCommand\x12\x0f.commandMessage\x1a\x0f.commandMessage\"\x00\x32I\n\x12getCommandsService\x12\x33\n\x0bgetCommands\x12\x0f.commandMessage\x1a\x0f.commandMessage\"\x00\x30\x01\x32\x46\n\x0csendResponse\x12\x36\n\x12setCommandResponse\x12\x0e.latestCommand\x1a\x0e.latestCommand\"\x00\x32G\n\x0bgetResponse\x12\x38\n\x12getCommandResponse\x12\x0e.latestCommand\x1a\x0e.latestCommand\"\x00\x30\x01\x62\x06proto3'
)




_COMMANDMESSAGE = _descriptor.Descriptor(
  name='commandMessage',
  full_name='commandMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='one', full_name='commandMessage.one', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='two', full_name='commandMessage.two', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='three', full_name='commandMessage.three', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='four', full_name='commandMessage.four', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='five', full_name='commandMessage.five', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='commandMessage.id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passcode', full_name='commandMessage.passcode', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getCommand', full_name='commandMessage.getCommand', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uidLatest', full_name='commandMessage.uidLatest', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=173,
)


_LATESTCOMMAND = _descriptor.Descriptor(
  name='latestCommand',
  full_name='latestCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='latestCommand.command', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='latestCommand.response', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uid', full_name='latestCommand.uid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='latestCommand.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passcode', full_name='latestCommand.passcode', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resList', full_name='latestCommand.resList', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=285,
)

DESCRIPTOR.message_types_by_name['commandMessage'] = _COMMANDMESSAGE
DESCRIPTOR.message_types_by_name['latestCommand'] = _LATESTCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

commandMessage = _reflection.GeneratedProtocolMessageType('commandMessage', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDMESSAGE,
  '__module__' : 'comProto_pb2'
  # @@protoc_insertion_point(class_scope:commandMessage)
  })
_sym_db.RegisterMessage(commandMessage)

latestCommand = _reflection.GeneratedProtocolMessageType('latestCommand', (_message.Message,), {
  'DESCRIPTOR' : _LATESTCOMMAND,
  '__module__' : 'comProto_pb2'
  # @@protoc_insertion_point(class_scope:latestCommand)
  })
_sym_db.RegisterMessage(latestCommand)



_COMMANDSERVICE = _descriptor.ServiceDescriptor(
  name='commandService',
  full_name='commandService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=287,
  serialized_end=353,
  methods=[
  _descriptor.MethodDescriptor(
    name='topCommand',
    full_name='commandService.topCommand',
    index=0,
    containing_service=None,
    input_type=_COMMANDMESSAGE,
    output_type=_COMMANDMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMANDSERVICE)

DESCRIPTOR.services_by_name['commandService'] = _COMMANDSERVICE


_GETCOMMANDSSERVICE = _descriptor.ServiceDescriptor(
  name='getCommandsService',
  full_name='getCommandsService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=355,
  serialized_end=428,
  methods=[
  _descriptor.MethodDescriptor(
    name='getCommands',
    full_name='getCommandsService.getCommands',
    index=0,
    containing_service=None,
    input_type=_COMMANDMESSAGE,
    output_type=_COMMANDMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GETCOMMANDSSERVICE)

DESCRIPTOR.services_by_name['getCommandsService'] = _GETCOMMANDSSERVICE


_SENDRESPONSE = _descriptor.ServiceDescriptor(
  name='sendResponse',
  full_name='sendResponse',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=430,
  serialized_end=500,
  methods=[
  _descriptor.MethodDescriptor(
    name='setCommandResponse',
    full_name='sendResponse.setCommandResponse',
    index=0,
    containing_service=None,
    input_type=_LATESTCOMMAND,
    output_type=_LATESTCOMMAND,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENDRESPONSE)

DESCRIPTOR.services_by_name['sendResponse'] = _SENDRESPONSE


_GETRESPONSE = _descriptor.ServiceDescriptor(
  name='getResponse',
  full_name='getResponse',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=502,
  serialized_end=573,
  methods=[
  _descriptor.MethodDescriptor(
    name='getCommandResponse',
    full_name='getResponse.getCommandResponse',
    index=0,
    containing_service=None,
    input_type=_LATESTCOMMAND,
    output_type=_LATESTCOMMAND,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GETRESPONSE)

DESCRIPTOR.services_by_name['getResponse'] = _GETRESPONSE

# @@protoc_insertion_point(module_scope)

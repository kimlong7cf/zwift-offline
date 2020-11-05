# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zfiles.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='zfiles.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0czfiles.proto\"H\n\x05ZFile\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0e\n\x06\x66older\x18\x02 \x02(\t\x12\x10\n\x08\x66ilename\x18\x03 \x02(\t\x12\x11\n\ttimestamp\x18\x04 \x02(\x04'
)




_ZFILE = _descriptor.Descriptor(
  name='ZFile',
  full_name='ZFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ZFile.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder', full_name='ZFile.folder', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='ZFile.filename', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ZFile.timestamp', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['ZFile'] = _ZFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ZFile = _reflection.GeneratedProtocolMessageType('ZFile', (_message.Message,), {
  'DESCRIPTOR' : _ZFILE,
  '__module__' : 'zfiles_pb2'
  # @@protoc_insertion_point(class_scope:ZFile)
  })
_sym_db.RegisterMessage(ZFile)


# @@protoc_insertion_point(module_scope)

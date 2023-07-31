# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/components/processors/proto/transformer_params.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGmediapipe/tasks/cc/components/processors/proto/transformer_params.proto\x12+mediapipe.tasks.components.processors.proto\"\xb3\x01\n\x15TransformerParameters\x12\x12\n\nbatch_size\x18\x01 \x01(\x05\x12\x16\n\x0emax_seq_length\x18\x02 \x01(\x05\x12\x15\n\rembedding_dim\x18\x03 \x01(\x05\x12\x18\n\x10hidden_dimension\x18\x04 \x01(\x05\x12\x16\n\x0ehead_dimension\x18\x05 \x01(\x05\x12\x11\n\tnum_heads\x18\x06 \x01(\x05\x12\x12\n\nnum_stacks\x18\x07 \x01(\x05\x42T\n6com.google.mediapipe.tasks.components.processors.protoB\x1aTransformerParametersProtob\x06proto3')



_TRANSFORMERPARAMETERS = DESCRIPTOR.message_types_by_name['TransformerParameters']
TransformerParameters = _reflection.GeneratedProtocolMessageType('TransformerParameters', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMERPARAMETERS,
  '__module__' : 'mediapipe.tasks.cc.components.processors.proto.transformer_params_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.components.processors.proto.TransformerParameters)
  })
_sym_db.RegisterMessage(TransformerParameters)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n6com.google.mediapipe.tasks.components.processors.protoB\032TransformerParametersProto'
  _TRANSFORMERPARAMETERS._serialized_start=121
  _TRANSFORMERPARAMETERS._serialized_end=300
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/text/text_classifier/proto/text_classifier_graph_options.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.tasks.cc.components.processors.proto import classifier_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_components_dot_processors_dot_proto_dot_classifier__options__pb2
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nQmediapipe/tasks/cc/text/text_classifier/proto/text_classifier_graph_options.proto\x12*mediapipe.tasks.text.text_classifier.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1aGmediapipe/tasks/cc/components/processors/proto/classifier_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xae\x02\n\x1aTextClassifierGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12Z\n\x12\x63lassifier_options\x18\x02 \x01(\x0b\x32>.mediapipe.tasks.components.processors.proto.ClassifierOptions2u\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xa5\x9f\xd1\xdc\x01 \x01(\x0b\x32\x46.mediapipe.tasks.text.text_classifier.proto.TextClassifierGraphOptionsBW\n4com.google.mediapipe.tasks.text.textclassifier.protoB\x1fTextClassifierGraphOptionsProto')



_TEXTCLASSIFIERGRAPHOPTIONS = DESCRIPTOR.message_types_by_name['TextClassifierGraphOptions']
TextClassifierGraphOptions = _reflection.GeneratedProtocolMessageType('TextClassifierGraphOptions', (_message.Message,), {
  'DESCRIPTOR' : _TEXTCLASSIFIERGRAPHOPTIONS,
  '__module__' : 'mediapipe.tasks.cc.text.text_classifier.proto.text_classifier_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.text.text_classifier.proto.TextClassifierGraphOptions)
  })
_sym_db.RegisterMessage(TextClassifierGraphOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TEXTCLASSIFIERGRAPHOPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n4com.google.mediapipe.tasks.text.textclassifier.protoB\037TextClassifierGraphOptionsProto'
  _TEXTCLASSIFIERGRAPHOPTIONS._serialized_start=337
  _TEXTCLASSIFIERGRAPHOPTIONS._serialized_end=639
# @@protoc_insertion_point(module_scope)

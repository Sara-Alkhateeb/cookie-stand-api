# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/audio/audio_classifier/proto/audio_classifier_graph_options.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nTmediapipe/tasks/cc/audio/audio_classifier/proto/audio_classifier_graph_options.proto\x12,mediapipe.tasks.audio.audio_classifier.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1aGmediapipe/tasks/cc/components/processors/proto/classifier_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xdb\x02\n\x1b\x41udioClassifierGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12Z\n\x12\x63lassifier_options\x18\x02 \x01(\x0b\x32>.mediapipe.tasks.components.processors.proto.ClassifierOptions\x12\'\n\x1f\x64\x65\x66\x61ult_input_audio_sample_rate\x18\x03 \x01(\x01\x32x\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x8c\xfe\xb4\xd7\x01 \x01(\x0b\x32I.mediapipe.tasks.audio.audio_classifier.proto.AudioClassifierGraphOptionsBZ\n6com.google.mediapipe.tasks.audio.audioclassifier.protoB AudioClassifierGraphOptionsProto')



_AUDIOCLASSIFIERGRAPHOPTIONS = DESCRIPTOR.message_types_by_name['AudioClassifierGraphOptions']
AudioClassifierGraphOptions = _reflection.GeneratedProtocolMessageType('AudioClassifierGraphOptions', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOCLASSIFIERGRAPHOPTIONS,
  '__module__' : 'mediapipe.tasks.cc.audio.audio_classifier.proto.audio_classifier_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.audio.audio_classifier.proto.AudioClassifierGraphOptions)
  })
_sym_db.RegisterMessage(AudioClassifierGraphOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_AUDIOCLASSIFIERGRAPHOPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n6com.google.mediapipe.tasks.audio.audioclassifier.protoB AudioClassifierGraphOptionsProto'
  _AUDIOCLASSIFIERGRAPHOPTIONS._serialized_start=342
  _AUDIOCLASSIFIERGRAPHOPTIONS._serialized_end=689
# @@protoc_insertion_point(module_scope)

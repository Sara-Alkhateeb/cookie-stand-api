# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/gesture_recognizer/proto/gesture_recognizer_graph_options.proto
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
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2
from mediapipe.tasks.cc.vision.gesture_recognizer.proto import hand_gesture_recognizer_graph_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_vision_dot_gesture__recognizer_dot_proto_dot_hand__gesture__recognizer__graph__options__pb2
from mediapipe.tasks.cc.vision.hand_landmarker.proto import hand_landmarker_graph_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_vision_dot_hand__landmarker_dot_proto_dot_hand__landmarker__graph__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nYmediapipe/tasks/cc/vision/gesture_recognizer/proto/gesture_recognizer_graph_options.proto\x12/mediapipe.tasks.vision.gesture_recognizer.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\x1a^mediapipe/tasks/cc/vision/gesture_recognizer/proto/hand_gesture_recognizer_graph_options.proto\x1aSmediapipe/tasks/cc/vision/hand_landmarker/proto/hand_landmarker_graph_options.proto\"\xd2\x03\n\x1dGestureRecognizerGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12o\n\x1dhand_landmarker_graph_options\x18\x02 \x01(\x0b\x32H.mediapipe.tasks.vision.hand_landmarker.proto.HandLandmarkerGraphOptions\x12\x81\x01\n%hand_gesture_recognizer_graph_options\x18\x03 \x01(\x0b\x32R.mediapipe.tasks.vision.gesture_recognizer.proto.HandGestureRecognizerGraphOptions2}\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xde\xe1\xb9\xe4\x01 \x01(\x0b\x32N.mediapipe.tasks.vision.gesture_recognizer.proto.GestureRecognizerGraphOptionsB_\n9com.google.mediapipe.tasks.vision.gesturerecognizer.protoB\"GestureRecognizerGraphOptionsProto')



_GESTURERECOGNIZERGRAPHOPTIONS = DESCRIPTOR.message_types_by_name['GestureRecognizerGraphOptions']
GestureRecognizerGraphOptions = _reflection.GeneratedProtocolMessageType('GestureRecognizerGraphOptions', (_message.Message,), {
  'DESCRIPTOR' : _GESTURERECOGNIZERGRAPHOPTIONS,
  '__module__' : 'mediapipe.tasks.cc.vision.gesture_recognizer.proto.gesture_recognizer_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.vision.gesture_recognizer.proto.GestureRecognizerGraphOptions)
  })
_sym_db.RegisterMessage(GestureRecognizerGraphOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_GESTURERECOGNIZERGRAPHOPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n9com.google.mediapipe.tasks.vision.gesturerecognizer.protoB\"GestureRecognizerGraphOptionsProto'
  _GESTURERECOGNIZERGRAPHOPTIONS._serialized_start=458
  _GESTURERECOGNIZERGRAPHOPTIONS._serialized_end=924
# @@protoc_insertion_point(module_scope)
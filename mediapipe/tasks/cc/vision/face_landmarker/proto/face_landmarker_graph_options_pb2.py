# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/face_landmarker/proto/face_landmarker_graph_options.proto
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
from mediapipe.tasks.cc.vision.face_detector.proto import face_detector_graph_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_vision_dot_face__detector_dot_proto_dot_face__detector__graph__options__pb2
from mediapipe.tasks.cc.vision.face_geometry.proto import face_geometry_graph_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_vision_dot_face__geometry_dot_proto_dot_face__geometry__graph__options__pb2
from mediapipe.tasks.cc.vision.face_landmarker.proto import face_landmarks_detector_graph_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_vision_dot_face__landmarker_dot_proto_dot_face__landmarks__detector__graph__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nSmediapipe/tasks/cc/vision/face_landmarker/proto/face_landmarker_graph_options.proto\x12,mediapipe.tasks.vision.face_landmarker.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\x1aOmediapipe/tasks/cc/vision/face_detector/proto/face_detector_graph_options.proto\x1aOmediapipe/tasks/cc/vision/face_geometry/proto/face_geometry_graph_options.proto\x1a[mediapipe/tasks/cc/vision/face_landmarker/proto/face_landmarks_detector_graph_options.proto\"\xd0\x04\n\x1a\x46\x61\x63\x65LandmarkerGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12i\n\x1b\x66\x61\x63\x65_detector_graph_options\x18\x02 \x01(\x0b\x32\x44.mediapipe.tasks.vision.face_detector.proto.FaceDetectorGraphOptions\x12~\n%face_landmarks_detector_graph_options\x18\x03 \x01(\x0b\x32O.mediapipe.tasks.vision.face_landmarker.proto.FaceLandmarksDetectorGraphOptions\x12$\n\x17min_tracking_confidence\x18\x04 \x01(\x02:\x03\x30.5\x12i\n\x1b\x66\x61\x63\x65_geometry_graph_options\x18\x05 \x01(\x0b\x32\x44.mediapipe.tasks.vision.face_geometry.proto.FaceGeometryGraphOptions2w\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xd6\xf9\xd8\xf2\x01 \x01(\x0b\x32H.mediapipe.tasks.vision.face_landmarker.proto.FaceLandmarkerGraphOptionsBY\n6com.google.mediapipe.tasks.vision.facelandmarker.protoB\x1f\x46\x61\x63\x65LandmarkerGraphOptionsProto')



_FACELANDMARKERGRAPHOPTIONS = DESCRIPTOR.message_types_by_name['FaceLandmarkerGraphOptions']
FaceLandmarkerGraphOptions = _reflection.GeneratedProtocolMessageType('FaceLandmarkerGraphOptions', (_message.Message,), {
  'DESCRIPTOR' : _FACELANDMARKERGRAPHOPTIONS,
  '__module__' : 'mediapipe.tasks.cc.vision.face_landmarker.proto.face_landmarker_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.vision.face_landmarker.proto.FaceLandmarkerGraphOptions)
  })
_sym_db.RegisterMessage(FaceLandmarkerGraphOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_FACELANDMARKERGRAPHOPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n6com.google.mediapipe.tasks.vision.facelandmarker.protoB\037FaceLandmarkerGraphOptionsProto'
  _FACELANDMARKERGRAPHOPTIONS._serialized_start=523
  _FACELANDMARKERGRAPHOPTIONS._serialized_end=1115
# @@protoc_insertion_point(module_scope)
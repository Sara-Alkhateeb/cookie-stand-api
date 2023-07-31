# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/video/video_pre_stream_calculator.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=mediapipe/calculators/video/video_pre_stream_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xcf\x02\n\x1fVideoPreStreamCalculatorOptions\x12;\n\x03\x66ps\x18\x01 \x01(\x0b\x32..mediapipe.VideoPreStreamCalculatorOptions.Fps\x1a\x94\x01\n\x03\x46ps\x12\r\n\x05value\x18\x01 \x01(\x01\x12H\n\x05ratio\x18\x02 \x01(\x0b\x32\x39.mediapipe.VideoPreStreamCalculatorOptions.Fps.Rational32\x1a\x34\n\nRational32\x12\x11\n\tnumerator\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65nominator\x18\x02 \x01(\x05\x32X\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x8b\xf0\x97H \x01(\x0b\x32*.mediapipe.VideoPreStreamCalculatorOptions')



_VIDEOPRESTREAMCALCULATOROPTIONS = DESCRIPTOR.message_types_by_name['VideoPreStreamCalculatorOptions']
_VIDEOPRESTREAMCALCULATOROPTIONS_FPS = _VIDEOPRESTREAMCALCULATOROPTIONS.nested_types_by_name['Fps']
_VIDEOPRESTREAMCALCULATOROPTIONS_FPS_RATIONAL32 = _VIDEOPRESTREAMCALCULATOROPTIONS_FPS.nested_types_by_name['Rational32']
VideoPreStreamCalculatorOptions = _reflection.GeneratedProtocolMessageType('VideoPreStreamCalculatorOptions', (_message.Message,), {

  'Fps' : _reflection.GeneratedProtocolMessageType('Fps', (_message.Message,), {

    'Rational32' : _reflection.GeneratedProtocolMessageType('Rational32', (_message.Message,), {
      'DESCRIPTOR' : _VIDEOPRESTREAMCALCULATOROPTIONS_FPS_RATIONAL32,
      '__module__' : 'mediapipe.calculators.video.video_pre_stream_calculator_pb2'
      # @@protoc_insertion_point(class_scope:mediapipe.VideoPreStreamCalculatorOptions.Fps.Rational32)
      })
    ,
    'DESCRIPTOR' : _VIDEOPRESTREAMCALCULATOROPTIONS_FPS,
    '__module__' : 'mediapipe.calculators.video.video_pre_stream_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.VideoPreStreamCalculatorOptions.Fps)
    })
  ,
  'DESCRIPTOR' : _VIDEOPRESTREAMCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.video.video_pre_stream_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.VideoPreStreamCalculatorOptions)
  })
_sym_db.RegisterMessage(VideoPreStreamCalculatorOptions)
_sym_db.RegisterMessage(VideoPreStreamCalculatorOptions.Fps)
_sym_db.RegisterMessage(VideoPreStreamCalculatorOptions.Fps.Rational32)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_VIDEOPRESTREAMCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _VIDEOPRESTREAMCALCULATOROPTIONS._serialized_start=115
  _VIDEOPRESTREAMCALCULATOROPTIONS._serialized_end=450
  _VIDEOPRESTREAMCALCULATOROPTIONS_FPS._serialized_start=212
  _VIDEOPRESTREAMCALCULATOROPTIONS_FPS._serialized_end=360
  _VIDEOPRESTREAMCALCULATOROPTIONS_FPS_RATIONAL32._serialized_start=308
  _VIDEOPRESTREAMCALCULATOROPTIONS_FPS_RATIONAL32._serialized_end=360
# @@protoc_insertion_point(module_scope)
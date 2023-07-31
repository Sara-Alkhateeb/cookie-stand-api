# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/image/image_cropping_calculator.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;mediapipe/calculators/image/image_cropping_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xe4\x03\n\x1eImageCroppingCalculatorOptions\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x13\n\x08rotation\x18\x03 \x01(\x02:\x01\x30\x12\x12\n\nnorm_width\x18\x04 \x01(\x02\x12\x13\n\x0bnorm_height\x18\x05 \x01(\x02\x12\x18\n\rnorm_center_x\x18\x06 \x01(\x02:\x01\x30\x12\x18\n\rnorm_center_y\x18\x07 \x01(\x02:\x01\x30\x12V\n\x0b\x62order_mode\x18\x08 \x01(\x0e\x32\x34.mediapipe.ImageCroppingCalculatorOptions.BorderMode:\x0b\x42ORDER_ZERO\x12\x18\n\x10output_max_width\x18\t \x01(\x05\x12\x19\n\x11output_max_height\x18\n \x01(\x05\"K\n\nBorderMode\x12\x16\n\x12\x42ORDER_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x42ORDER_ZERO\x10\x01\x12\x14\n\x10\x42ORDER_REPLICATE\x10\x02\x32W\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xdf\xd6\x93} \x01(\x0b\x32).mediapipe.ImageCroppingCalculatorOptions')



_IMAGECROPPINGCALCULATOROPTIONS = DESCRIPTOR.message_types_by_name['ImageCroppingCalculatorOptions']
_IMAGECROPPINGCALCULATOROPTIONS_BORDERMODE = _IMAGECROPPINGCALCULATOROPTIONS.enum_types_by_name['BorderMode']
ImageCroppingCalculatorOptions = _reflection.GeneratedProtocolMessageType('ImageCroppingCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _IMAGECROPPINGCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.image.image_cropping_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ImageCroppingCalculatorOptions)
  })
_sym_db.RegisterMessage(ImageCroppingCalculatorOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_IMAGECROPPINGCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _IMAGECROPPINGCALCULATOROPTIONS._serialized_start=113
  _IMAGECROPPINGCALCULATOROPTIONS._serialized_end=597
  _IMAGECROPPINGCALCULATOROPTIONS_BORDERMODE._serialized_start=433
  _IMAGECROPPINGCALCULATOROPTIONS_BORDERMODE._serialized_end=508
# @@protoc_insertion_point(module_scope)

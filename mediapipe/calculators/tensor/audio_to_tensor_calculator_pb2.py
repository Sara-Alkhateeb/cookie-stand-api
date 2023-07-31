# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/audio_to_tensor_calculator.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=mediapipe/calculators/tensor/audio_to_tensor_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xa9\x06\n\x1e\x41udioToTensorCalculatorOptions\x12\x14\n\x0cnum_channels\x18\x01 \x01(\x03\x12\x13\n\x0bnum_samples\x18\x02 \x01(\x03\x12\"\n\x17num_overlapping_samples\x18\x03 \x01(\x03:\x01\x30\x12\x1a\n\x12target_sample_rate\x18\x04 \x01(\x01\x12\x19\n\x0bstream_mode\x18\x05 \x01(\x08:\x04true\x12+\n\x1d\x63heck_inconsistent_timestamps\x18\x06 \x01(\x08:\x04true\x12\x10\n\x08\x66\x66t_size\x18\x07 \x01(\x03\x12\x1e\n\x16padding_samples_before\x18\x08 \x01(\x03\x12\x1d\n\x15padding_samples_after\x18\t \x01(\x03\x12\x65\n\nflush_mode\x18\n \x01(\x0e\x32\x33.mediapipe.AudioToTensorCalculatorOptions.FlushMode:\x1c\x45NTIRE_TAIL_AT_TIMESTAMP_MAX\x12\x62\n\x11\x64\x66t_tensor_format\x18\x0b \x01(\x0e\x32\x39.mediapipe.AudioToTensorCalculatorOptions.DftTensorFormat:\x0cWITH_NYQUIST\x12\x16\n\x0evolume_gain_db\x18\x0c \x01(\x01\"M\n\tFlushMode\x12\x08\n\x04NONE\x10\x00\x12 \n\x1c\x45NTIRE_TAIL_AT_TIMESTAMP_MAX\x10\x01\x12\x14\n\x10PROCEED_AS_USUAL\x10\x02\"w\n\x0f\x44\x66tTensorFormat\x12\x1d\n\x19\x44\x46T_TENSOR_FORMAT_UNKNOWN\x10\x00\x12\x1a\n\x16WITHOUT_DC_AND_NYQUIST\x10\x01\x12\x10\n\x0cWITH_NYQUIST\x10\x02\x12\x17\n\x13WITH_DC_AND_NYQUIST\x10\x03\x32X\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xb8\xc1\xf6\xd5\x01 \x01(\x0b\x32).mediapipe.AudioToTensorCalculatorOptions')



_AUDIOTOTENSORCALCULATOROPTIONS = DESCRIPTOR.message_types_by_name['AudioToTensorCalculatorOptions']
_AUDIOTOTENSORCALCULATOROPTIONS_FLUSHMODE = _AUDIOTOTENSORCALCULATOROPTIONS.enum_types_by_name['FlushMode']
_AUDIOTOTENSORCALCULATOROPTIONS_DFTTENSORFORMAT = _AUDIOTOTENSORCALCULATOROPTIONS.enum_types_by_name['DftTensorFormat']
AudioToTensorCalculatorOptions = _reflection.GeneratedProtocolMessageType('AudioToTensorCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOTOTENSORCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.tensor.audio_to_tensor_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.AudioToTensorCalculatorOptions)
  })
_sym_db.RegisterMessage(AudioToTensorCalculatorOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_AUDIOTOTENSORCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _AUDIOTOTENSORCALCULATOROPTIONS._serialized_start=115
  _AUDIOTOTENSORCALCULATOROPTIONS._serialized_end=924
  _AUDIOTOTENSORCALCULATOROPTIONS_FLUSHMODE._serialized_start=636
  _AUDIOTOTENSORCALCULATOROPTIONS_FLUSHMODE._serialized_end=713
  _AUDIOTOTENSORCALCULATOROPTIONS_DFTTENSORFORMAT._serialized_start=715
  _AUDIOTOTENSORCALCULATOROPTIONS_DFTTENSORFORMAT._serialized_end=834
# @@protoc_insertion_point(module_scope)

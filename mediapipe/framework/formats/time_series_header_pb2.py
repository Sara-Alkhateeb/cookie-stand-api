# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/formats/time_series_header.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4mediapipe/framework/formats/time_series_header.proto\x12\tmediapipe\"\x8e\x01\n\x10TimeSeriesHeader\x12\x13\n\x0bsample_rate\x18\x01 \x01(\x01\x12\x14\n\x0cnum_channels\x18\x02 \x01(\x05\x12\x13\n\x0bnum_samples\x18\x03 \x01(\x05\x12\x13\n\x0bpacket_rate\x18\x04 \x01(\x01\x12\x19\n\x11\x61udio_sample_rate\x18\x05 \x01(\x01*\n\x08\xa0\x9c\x01\x10\x80\x80\x80\x80\x02\"k\n\x1bMultiStreamTimeSeriesHeader\x12\x37\n\x12time_series_header\x18\x01 \x01(\x0b\x32\x1b.mediapipe.TimeSeriesHeader\x12\x13\n\x0bnum_streams\x18\x02 \x01(\x05')



_TIMESERIESHEADER = DESCRIPTOR.message_types_by_name['TimeSeriesHeader']
_MULTISTREAMTIMESERIESHEADER = DESCRIPTOR.message_types_by_name['MultiStreamTimeSeriesHeader']
TimeSeriesHeader = _reflection.GeneratedProtocolMessageType('TimeSeriesHeader', (_message.Message,), {
  'DESCRIPTOR' : _TIMESERIESHEADER,
  '__module__' : 'mediapipe.framework.formats.time_series_header_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TimeSeriesHeader)
  })
_sym_db.RegisterMessage(TimeSeriesHeader)

MultiStreamTimeSeriesHeader = _reflection.GeneratedProtocolMessageType('MultiStreamTimeSeriesHeader', (_message.Message,), {
  'DESCRIPTOR' : _MULTISTREAMTIMESERIESHEADER,
  '__module__' : 'mediapipe.framework.formats.time_series_header_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.MultiStreamTimeSeriesHeader)
  })
_sym_db.RegisterMessage(MultiStreamTimeSeriesHeader)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TIMESERIESHEADER._serialized_start=68
  _TIMESERIESHEADER._serialized_end=210
  _MULTISTREAMTIMESERIESHEADER._serialized_start=212
  _MULTISTREAMTIMESERIESHEADER._serialized_end=319
# @@protoc_insertion_point(module_scope)
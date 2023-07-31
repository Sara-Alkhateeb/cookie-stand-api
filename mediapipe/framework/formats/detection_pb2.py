# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/formats/detection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework.formats import location_data_pb2 as mediapipe_dot_framework_dot_formats_dot_location__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+mediapipe/framework/formats/detection.proto\x12\tmediapipe\x1a/mediapipe/framework/formats/location_data.proto\"\xde\x02\n\tDetection\x12\r\n\x05label\x18\x01 \x03(\t\x12\x14\n\x08label_id\x18\x02 \x03(\x05\x42\x02\x10\x01\x12\x11\n\x05score\x18\x03 \x03(\x02\x42\x02\x10\x01\x12.\n\rlocation_data\x18\x04 \x01(\x0b\x32\x17.mediapipe.LocationData\x12\x13\n\x0b\x66\x65\x61ture_tag\x18\x05 \x01(\t\x12\x10\n\x08track_id\x18\x06 \x01(\t\x12\x14\n\x0c\x64\x65tection_id\x18\x07 \x01(\x03\x12G\n\x15\x61ssociated_detections\x18\x08 \x03(\x0b\x32(.mediapipe.Detection.AssociatedDetection\x12\x14\n\x0c\x64isplay_name\x18\t \x03(\t\x12\x16\n\x0etimestamp_usec\x18\n \x01(\x03\x1a\x35\n\x13\x41ssociatedDetection\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nconfidence\x18\x02 \x01(\x02\"8\n\rDetectionList\x12\'\n\tdetection\x18\x01 \x03(\x0b\x32\x14.mediapipe.DetectionB4\n\"com.google.mediapipe.formats.protoB\x0e\x44\x65tectionProto')



_DETECTION = DESCRIPTOR.message_types_by_name['Detection']
_DETECTION_ASSOCIATEDDETECTION = _DETECTION.nested_types_by_name['AssociatedDetection']
_DETECTIONLIST = DESCRIPTOR.message_types_by_name['DetectionList']
Detection = _reflection.GeneratedProtocolMessageType('Detection', (_message.Message,), {

  'AssociatedDetection' : _reflection.GeneratedProtocolMessageType('AssociatedDetection', (_message.Message,), {
    'DESCRIPTOR' : _DETECTION_ASSOCIATEDDETECTION,
    '__module__' : 'mediapipe.framework.formats.detection_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.Detection.AssociatedDetection)
    })
  ,
  'DESCRIPTOR' : _DETECTION,
  '__module__' : 'mediapipe.framework.formats.detection_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Detection)
  })
_sym_db.RegisterMessage(Detection)
_sym_db.RegisterMessage(Detection.AssociatedDetection)

DetectionList = _reflection.GeneratedProtocolMessageType('DetectionList', (_message.Message,), {
  'DESCRIPTOR' : _DETECTIONLIST,
  '__module__' : 'mediapipe.framework.formats.detection_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.DetectionList)
  })
_sym_db.RegisterMessage(DetectionList)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.mediapipe.formats.protoB\016DetectionProto'
  _DETECTION.fields_by_name['label_id']._options = None
  _DETECTION.fields_by_name['label_id']._serialized_options = b'\020\001'
  _DETECTION.fields_by_name['score']._options = None
  _DETECTION.fields_by_name['score']._serialized_options = b'\020\001'
  _DETECTION._serialized_start=108
  _DETECTION._serialized_end=458
  _DETECTION_ASSOCIATEDDETECTION._serialized_start=405
  _DETECTION_ASSOCIATEDDETECTION._serialized_end=458
  _DETECTIONLIST._serialized_start=460
  _DETECTIONLIST._serialized_end=516
# @@protoc_insertion_point(module_scope)

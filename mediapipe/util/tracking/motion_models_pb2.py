# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/tracking/motion_models.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+mediapipe/util/tracking/motion_models.proto\x12\tmediapipe\"0\n\x10TranslationModel\x12\r\n\x02\x64x\x18\x01 \x01(\x02:\x01\x30\x12\r\n\x02\x64y\x18\x02 \x01(\x02:\x01\x30\"V\n\x0fSimilarityModel\x12\r\n\x02\x64x\x18\x01 \x01(\x02:\x01\x30\x12\r\n\x02\x64y\x18\x02 \x01(\x02:\x01\x30\x12\x10\n\x05scale\x18\x03 \x01(\x02:\x01\x31\x12\x13\n\x08rotation\x18\x04 \x01(\x02:\x01\x30\"Q\n\x15LinearSimilarityModel\x12\r\n\x02\x64x\x18\x01 \x01(\x02:\x01\x30\x12\r\n\x02\x64y\x18\x02 \x01(\x02:\x01\x30\x12\x0c\n\x01\x61\x18\x03 \x01(\x02:\x01\x31\x12\x0c\n\x01\x62\x18\x04 \x01(\x02:\x01\x30\"c\n\x0b\x41\x66\x66ineModel\x12\r\n\x02\x64x\x18\x01 \x01(\x02:\x01\x30\x12\r\n\x02\x64y\x18\x02 \x01(\x02:\x01\x30\x12\x0c\n\x01\x61\x18\x03 \x01(\x02:\x01\x31\x12\x0c\n\x01\x62\x18\x04 \x01(\x02:\x01\x30\x12\x0c\n\x01\x63\x18\x05 \x01(\x02:\x01\x30\x12\x0c\n\x01\x64\x18\x06 \x01(\x02:\x01\x31\"\x94\x01\n\nHomography\x12\x0f\n\x04h_00\x18\x01 \x01(\x02:\x01\x31\x12\x0f\n\x04h_01\x18\x02 \x01(\x02:\x01\x30\x12\x0f\n\x04h_02\x18\x03 \x01(\x02:\x01\x30\x12\x0f\n\x04h_10\x18\x04 \x01(\x02:\x01\x30\x12\x0f\n\x04h_11\x18\x05 \x01(\x02:\x01\x31\x12\x0f\n\x04h_12\x18\x06 \x01(\x02:\x01\x30\x12\x0f\n\x04h_20\x18\x07 \x01(\x02:\x01\x30\x12\x0f\n\x04h_21\x18\x08 \x01(\x02:\x01\x30\"J\n\x17MixtureLinearSimilarity\x12/\n\x05model\x18\x01 \x03(\x0b\x32 .mediapipe.LinearSimilarityModel\"6\n\rMixtureAffine\x12%\n\x05model\x18\x01 \x03(\x0b\x32\x16.mediapipe.AffineModel\"\xd0\x01\n\x11MixtureHomography\x12$\n\x05model\x18\x01 \x03(\x0b\x32\x15.mediapipe.Homography\x12>\n\x03\x64of\x18\x02 \x01(\x0e\x32(.mediapipe.MixtureHomography.VariableDOF:\x07\x41LL_DOF\"U\n\x0bVariableDOF\x12\x0b\n\x07\x41LL_DOF\x10\x00\x12\x13\n\x0fTRANSLATION_DOF\x10\x01\x12\x15\n\x11SKEW_ROTATION_DOF\x10\x02\x12\r\n\tCONST_DOF\x10\x03')



_TRANSLATIONMODEL = DESCRIPTOR.message_types_by_name['TranslationModel']
_SIMILARITYMODEL = DESCRIPTOR.message_types_by_name['SimilarityModel']
_LINEARSIMILARITYMODEL = DESCRIPTOR.message_types_by_name['LinearSimilarityModel']
_AFFINEMODEL = DESCRIPTOR.message_types_by_name['AffineModel']
_HOMOGRAPHY = DESCRIPTOR.message_types_by_name['Homography']
_MIXTURELINEARSIMILARITY = DESCRIPTOR.message_types_by_name['MixtureLinearSimilarity']
_MIXTUREAFFINE = DESCRIPTOR.message_types_by_name['MixtureAffine']
_MIXTUREHOMOGRAPHY = DESCRIPTOR.message_types_by_name['MixtureHomography']
_MIXTUREHOMOGRAPHY_VARIABLEDOF = _MIXTUREHOMOGRAPHY.enum_types_by_name['VariableDOF']
TranslationModel = _reflection.GeneratedProtocolMessageType('TranslationModel', (_message.Message,), {
  'DESCRIPTOR' : _TRANSLATIONMODEL,
  '__module__' : 'mediapipe.util.tracking.motion_models_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TranslationModel)
  })
_sym_db.RegisterMessage(TranslationModel)

SimilarityModel = _reflection.GeneratedProtocolMessageType('SimilarityModel', (_message.Message,), {
  'DESCRIPTOR' : _SIMILARITYMODEL,
  '__module__' : 'mediapipe.util.tracking.motion_models_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.SimilarityModel)
  })
_sym_db.RegisterMessage(SimilarityModel)

LinearSimilarityModel = _reflection.GeneratedProtocolMessageType('LinearSimilarityModel', (_message.Message,), {
  'DESCRIPTOR' : _LINEARSIMILARITYMODEL,
  '__module__' : 'mediapipe.util.tracking.motion_models_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.LinearSimilarityModel)
  })
_sym_db.RegisterMessage(LinearSimilarityModel)

AffineModel = _reflection.GeneratedProtocolMessageType('AffineModel', (_message.Message,), {
  'DESCRIPTOR' : _AFFINEMODEL,
  '__module__' : 'mediapipe.util.tracking.motion_models_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.AffineModel)
  })
_sym_db.RegisterMessage(AffineModel)

Homography = _reflection.GeneratedProtocolMessageType('Homography', (_message.Message,), {
  'DESCRIPTOR' : _HOMOGRAPHY,
  '__module__' : 'mediapipe.util.tracking.motion_models_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Homography)
  })
_sym_db.RegisterMessage(Homography)

MixtureLinearSimilarity = _reflection.GeneratedProtocolMessageType('MixtureLinearSimilarity', (_message.Message,), {
  'DESCRIPTOR' : _MIXTURELINEARSIMILARITY,
  '__module__' : 'mediapipe.util.tracking.motion_models_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.MixtureLinearSimilarity)
  })
_sym_db.RegisterMessage(MixtureLinearSimilarity)

MixtureAffine = _reflection.GeneratedProtocolMessageType('MixtureAffine', (_message.Message,), {
  'DESCRIPTOR' : _MIXTUREAFFINE,
  '__module__' : 'mediapipe.util.tracking.motion_models_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.MixtureAffine)
  })
_sym_db.RegisterMessage(MixtureAffine)

MixtureHomography = _reflection.GeneratedProtocolMessageType('MixtureHomography', (_message.Message,), {
  'DESCRIPTOR' : _MIXTUREHOMOGRAPHY,
  '__module__' : 'mediapipe.util.tracking.motion_models_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.MixtureHomography)
  })
_sym_db.RegisterMessage(MixtureHomography)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRANSLATIONMODEL._serialized_start=58
  _TRANSLATIONMODEL._serialized_end=106
  _SIMILARITYMODEL._serialized_start=108
  _SIMILARITYMODEL._serialized_end=194
  _LINEARSIMILARITYMODEL._serialized_start=196
  _LINEARSIMILARITYMODEL._serialized_end=277
  _AFFINEMODEL._serialized_start=279
  _AFFINEMODEL._serialized_end=378
  _HOMOGRAPHY._serialized_start=381
  _HOMOGRAPHY._serialized_end=529
  _MIXTURELINEARSIMILARITY._serialized_start=531
  _MIXTURELINEARSIMILARITY._serialized_end=605
  _MIXTUREAFFINE._serialized_start=607
  _MIXTUREAFFINE._serialized_end=661
  _MIXTUREHOMOGRAPHY._serialized_start=664
  _MIXTUREHOMOGRAPHY._serialized_end=872
  _MIXTUREHOMOGRAPHY_VARIABLEDOF._serialized_start=787
  _MIXTUREHOMOGRAPHY_VARIABLEDOF._serialized_end=872
# @@protoc_insertion_point(module_scope)
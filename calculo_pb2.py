# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: calculo.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'calculo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcalculo.proto\x12\x07\x63\x61lculo\"\x1e\n\x0bNumeroLista\x12\x0f\n\x07numeros\x18\x01 \x03(\x05\"\x1e\n\x0cNumeroMaximo\x12\x0e\n\x06maximo\x18\x01 \x01(\x05\x32R\n\x0fServidorCalculo\x12?\n\x0e\x43\x61lcularMaximo\x12\x14.calculo.NumeroLista\x1a\x15.calculo.NumeroMaximo\"\x00\x32S\n\x11ServidorOperacion\x12>\n\rObtenerMaximo\x12\x14.calculo.NumeroLista\x1a\x15.calculo.NumeroMaximo\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_NUMEROLISTA']._serialized_start=26
  _globals['_NUMEROLISTA']._serialized_end=56
  _globals['_NUMEROMAXIMO']._serialized_start=58
  _globals['_NUMEROMAXIMO']._serialized_end=88
  _globals['_SERVIDORCALCULO']._serialized_start=90
  _globals['_SERVIDORCALCULO']._serialized_end=172
  _globals['_SERVIDOROPERACION']._serialized_start=174
  _globals['_SERVIDOROPERACION']._serialized_end=257
# @@protoc_insertion_point(module_scope)

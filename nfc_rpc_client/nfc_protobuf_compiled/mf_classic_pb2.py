"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10mf_classic.proto\x12\x0cPB_MfClassic"R\n\x0bAuthRequest\x12\r\n\x05block\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\'\n\x08key_type\x18\x03 \x01(\x0e2\x15.PB_MfClassic.KeyType"\xa7\x01\n\x0cAuthResponse\x12"\n\x05error\x18\x01 \x01(\x0e2\x13.PB_MfClassic.Error\x12\r\n\x05block\x18\x02 \x01(\r\x12\x0b\n\x03key\x18\x03 \x01(\x0c\x12\'\n\x08key_type\x18\x04 \x01(\x0e2\x15.PB_MfClassic.KeyType\x12\n\n\x02nt\x18\x05 \x01(\x0c\x12\n\n\x02nr\x18\x06 \x01(\x0c\x12\n\n\x02ar\x18\x07 \x01(\x0c\x12\n\n\x02at\x18\x08 \x01(\x0c"W\n\x10ReadBlockRequest\x12\r\n\x05block\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\'\n\x08key_type\x18\x03 \x01(\x0e2\x15.PB_MfClassic.KeyType"E\n\x11ReadBlockResponse\x12"\n\x05error\x18\x01 \x01(\x0e2\x13.PB_MfClassic.Error\x12\x0c\n\x04data\x18\x02 \x01(\x0c*F\n\x05Error\x12\x08\n\x04None\x10\x00\x12\x0e\n\nNotPresent\x10\x01\x12\x0c\n\x08Protocol\x10\x02\x12\x08\n\x04Auth\x10\x03\x12\x0b\n\x07Timeout\x10\x04*%\n\x07KeyType\x12\x0c\n\x08KeyTypeA\x10\x00\x12\x0c\n\x08KeyTypeB\x10\x01B!\n\x1fcom.flipperdevices.nfc.protobufb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mf_classic_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.flipperdevices.nfc.protobuf'
    _ERROR._serialized_start = 448
    _ERROR._serialized_end = 518
    _KEYTYPE._serialized_start = 520
    _KEYTYPE._serialized_end = 557
    _AUTHREQUEST._serialized_start = 34
    _AUTHREQUEST._serialized_end = 116
    _AUTHRESPONSE._serialized_start = 119
    _AUTHRESPONSE._serialized_end = 286
    _READBLOCKREQUEST._serialized_start = 288
    _READBLOCKREQUEST._serialized_end = 375
    _READBLOCKRESPONSE._serialized_start = 377
    _READBLOCKRESPONSE._serialized_end = 446
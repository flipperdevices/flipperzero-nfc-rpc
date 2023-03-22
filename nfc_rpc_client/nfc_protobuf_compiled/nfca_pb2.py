"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nnfca.proto\x12\x07PB_Nfca"\r\n\x0bReadRequest"f\n\x0cReadResponse\x12\x1d\n\x05error\x18\x01 \x01(\x0e2\x0e.PB_Nfca.Error\x12\x0f\n\x07uid_len\x18\x02 \x01(\r\x12\x0b\n\x03uid\x18\x03 \x01(\x0c\x12\x0b\n\x03sak\x18\x04 \x01(\x0c\x12\x0c\n\x04atqa\x18\x05 \x01(\x0c*\x83\x01\n\x05Error\x12\x08\n\x04None\x10\x00\x12\x0e\n\nNotPresent\x10\x01\x12\x10\n\x0cColResFailed\x10\x02\x12\x12\n\x0eBufferOverflow\x10\x03\x12\x11\n\rCommunication\x10\x04\x12\x0c\n\x08FieldOff\x10\x05\x12\x0c\n\x08WrongCrc\x10\x06\x12\x0b\n\x07Timeout\x10\x07B!\n\x1fcom.flipperdevices.nfc.protobufb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nfca_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.flipperdevices.nfc.protobuf'
    _ERROR._serialized_start = 143
    _ERROR._serialized_end = 274
    _READREQUEST._serialized_start = 23
    _READREQUEST._serialized_end = 36
    _READRESPONSE._serialized_start = 38
    _READRESPONSE._serialized_end = 140
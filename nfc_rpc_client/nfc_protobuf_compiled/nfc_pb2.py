"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tnfc.proto\x12\x02PB"\x1d\n\x0fNfcaReadRequest\x12\n\n\x02ok\x18\x01 \x01(\x08"W\n\x10NfcaReadResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\x0b\n\x03uid\x18\x02 \x01(\x0c\x12\x0b\n\x03sak\x18\x03 \x01(\x0c\x12\x0c\n\x04atqa\x18\x04 \x01(\x0c\x12\x0f\n\x07uid_len\x18\x05 \x01(\rB!\n\x1fcom.flipperdevices.nfc.protobufb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nfc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.flipperdevices.nfc.protobuf'
    _NFCAREADREQUEST._serialized_start = 17
    _NFCAREADREQUEST._serialized_end = 46
    _NFCAREADRESPONSE._serialized_start = 48
    _NFCAREADRESPONSE._serialized_end = 135
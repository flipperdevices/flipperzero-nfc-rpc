"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tnfc.proto\x12\x02PB">\n\x17NfcAnticollisionRequest\x12#\n\x04type\x18\x01 \x01(\x0e2\x15.PB.anticollisionType"`\n\x19NfcAAnticollisionResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\x0b\n\x03uid\x18\x02 \x01(\x0c\x12\x0b\n\x03sak\x18\x03 \x01(\x0c\x12\x0c\n\x04atqa\x18\x04 \x01(\x0c\x12\x0f\n\x07uid_len\x18\x05 \x01(\r*T\n\x11anticollisionType\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NFCA\x10\x01\x12\x08\n\x04NFCB\x10\x02\x12\r\n\tNFCBPrime\x10\x03\x12\x08\n\x04NFCF\x10\x04\x12\x08\n\x04NFCV\x10\x05B!\n\x1fcom.flipperdevices.nfc.protobufb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nfc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.flipperdevices.nfc.protobuf'
    _ANTICOLLISIONTYPE._serialized_start = 179
    _ANTICOLLISIONTYPE._serialized_end = 263
    _NFCANTICOLLISIONREQUEST._serialized_start = 17
    _NFCANTICOLLISIONREQUEST._serialized_end = 79
    _NFCAANTICOLLISIONRESPONSE._serialized_start = 81
    _NFCAANTICOLLISIONRESPONSE._serialized_end = 177
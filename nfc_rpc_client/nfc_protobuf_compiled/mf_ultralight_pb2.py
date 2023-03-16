"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13mf_ultralight.proto\x12\x0fPB_MfUltralight"\x1f\n\x0fReadPageRequest\x12\x0c\n\x04page\x18\x01 \x01(\r".\n\x10ReadPageResponse\x12\x0c\n\x04page\x18\x01 \x01(\r\x12\x0c\n\x04data\x18\x02 \x01(\x0c"\x14\n\x12ReadVersionRequest"\xbe\x01\n\x13ReadVersionResponse\x12\x0e\n\x06header\x18\x01 \x01(\r\x12\x11\n\tvendor_id\x18\x02 \x01(\r\x12\x11\n\tprod_type\x18\x03 \x01(\r\x12\x14\n\x0cprod_subtype\x18\x04 \x01(\r\x12\x16\n\x0eprod_ver_major\x18\x05 \x01(\r\x12\x16\n\x0eprod_ver_minor\x18\x06 \x01(\r\x12\x14\n\x0cstorage_size\x18\x07 \x01(\r\x12\x15\n\rprotocol_type\x18\x08 \x01(\r".\n\x10WritePageRequest\x12\x0c\n\x04page\x18\x01 \x01(\r\x12\x0c\n\x04data\x18\x02 \x01(\x0c"#\n\x11WritePageResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08B!\n\x1fcom.flipperdevices.nfc.protobufb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mf_ultralight_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.flipperdevices.nfc.protobuf'
    _READPAGEREQUEST._serialized_start = 40
    _READPAGEREQUEST._serialized_end = 71
    _READPAGERESPONSE._serialized_start = 73
    _READPAGERESPONSE._serialized_end = 119
    _READVERSIONREQUEST._serialized_start = 121
    _READVERSIONREQUEST._serialized_end = 141
    _READVERSIONRESPONSE._serialized_start = 144
    _READVERSIONRESPONSE._serialized_end = 334
    _WRITEPAGEREQUEST._serialized_start = 336
    _WRITEPAGEREQUEST._serialized_end = 382
    _WRITEPAGERESPONSE._serialized_start = 384
    _WRITEPAGERESPONSE._serialized_end = 419
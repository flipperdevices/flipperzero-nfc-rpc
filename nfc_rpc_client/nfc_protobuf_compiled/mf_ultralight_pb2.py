"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13mf_ultralight.proto\x12\x0fPB_MfUltralight"\x1f\n\x0fReadPageRequest\x12\x0c\n\x04page\x18\x01 \x01(\r"U\n\x10ReadPageResponse\x12%\n\x05error\x18\x01 \x01(\x0e2\x16.PB_MfUltralight.Error\x12\x0c\n\x04page\x18\x02 \x01(\r\x12\x0c\n\x04data\x18\x03 \x01(\x0c"\x14\n\x12ReadVersionRequest"\xe5\x01\n\x13ReadVersionResponse\x12%\n\x05error\x18\x01 \x01(\x0e2\x16.PB_MfUltralight.Error\x12\x0e\n\x06header\x18\x02 \x01(\r\x12\x11\n\tvendor_id\x18\x03 \x01(\r\x12\x11\n\tprod_type\x18\x04 \x01(\r\x12\x14\n\x0cprod_subtype\x18\x05 \x01(\r\x12\x16\n\x0eprod_ver_major\x18\x06 \x01(\r\x12\x16\n\x0eprod_ver_minor\x18\x07 \x01(\r\x12\x14\n\x0cstorage_size\x18\x08 \x01(\r\x12\x15\n\rprotocol_type\x18\t \x01(\r".\n\x10WritePageRequest\x12\x0c\n\x04page\x18\x01 \x01(\r\x12\x0c\n\x04data\x18\x02 \x01(\x0c"J\n\x11WritePageResponse\x12%\n\x05error\x18\x01 \x01(\x0e2\x16.PB_MfUltralight.Error\x12\x0e\n\x06result\x18\x02 \x01(\x08"\x16\n\x14ReadSignatureRequest"L\n\x15ReadSignatureResponse\x12%\n\x05error\x18\x01 \x01(\x0e2\x16.PB_MfUltralight.Error\x12\x0c\n\x04data\x18\x02 \x01(\x0c")\n\x12ReadCounterRequest\x12\x13\n\x0bcounter_num\x18\x01 \x01(\r"_\n\x13ReadCounterResponse\x12%\n\x05error\x18\x01 \x01(\x0e2\x16.PB_MfUltralight.Error\x12\x13\n\x0bcounter_num\x18\x02 \x01(\r\x12\x0c\n\x04data\x18\x03 \x01(\x0c"*\n\x16ReadTearingFlagRequest\x12\x10\n\x08flag_num\x18\x01 \x01(\r"`\n\x17ReadTearingFlagResponse\x12%\n\x05error\x18\x01 \x01(\x0e2\x16.PB_MfUltralight.Error\x12\x10\n\x08flag_num\x18\x02 \x01(\r\x12\x0c\n\x04data\x18\x03 \x01(\x0c*F\n\x05Error\x12\x08\n\x04None\x10\x00\x12\x0e\n\nNotPresent\x10\x01\x12\x0c\n\x08Protocol\x10\x02\x12\x08\n\x04Auth\x10\x03\x12\x0b\n\x07Timeout\x10\x04B!\n\x1fcom.flipperdevices.nfc.protobufb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mf_ultralight_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.flipperdevices.nfc.protobuf'
    _ERROR._serialized_start = 922
    _ERROR._serialized_end = 992
    _READPAGEREQUEST._serialized_start = 40
    _READPAGEREQUEST._serialized_end = 71
    _READPAGERESPONSE._serialized_start = 73
    _READPAGERESPONSE._serialized_end = 158
    _READVERSIONREQUEST._serialized_start = 160
    _READVERSIONREQUEST._serialized_end = 180
    _READVERSIONRESPONSE._serialized_start = 183
    _READVERSIONRESPONSE._serialized_end = 412
    _WRITEPAGEREQUEST._serialized_start = 414
    _WRITEPAGEREQUEST._serialized_end = 460
    _WRITEPAGERESPONSE._serialized_start = 462
    _WRITEPAGERESPONSE._serialized_end = 536
    _READSIGNATUREREQUEST._serialized_start = 538
    _READSIGNATUREREQUEST._serialized_end = 560
    _READSIGNATURERESPONSE._serialized_start = 562
    _READSIGNATURERESPONSE._serialized_end = 638
    _READCOUNTERREQUEST._serialized_start = 640
    _READCOUNTERREQUEST._serialized_end = 681
    _READCOUNTERRESPONSE._serialized_start = 683
    _READCOUNTERRESPONSE._serialized_end = 778
    _READTEARINGFLAGREQUEST._serialized_start = 780
    _READTEARINGFLAGREQUEST._serialized_end = 822
    _READTEARINGFLAGRESPONSE._serialized_start = 824
    _READTEARINGFLAGRESPONSE._serialized_end = 920
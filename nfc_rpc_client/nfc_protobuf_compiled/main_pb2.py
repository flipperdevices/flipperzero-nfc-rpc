"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import nfca_pb2 as nfca__pb2
from . import mf_ultralight_pb2 as mf__ultralight__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmain.proto\x12\x03Nfc\x1a\nnfca.proto\x1a\x13mf_ultralight.proto"\x07\n\x05Empty"\xce\x02\n\x04Main\x12*\n\x0ecommand_status\x18\x01 \x01(\x0e2\x12.Nfc.CommandStatus\x12\x1b\n\x05empty\x18\x02 \x01(\x0b2\n.Nfc.EmptyH\x00\x12-\n\rnfca_read_req\x18\x03 \x01(\x0b2\x14.PB_Nfca.ReadRequestH\x00\x12/\n\x0enfca_read_resp\x18\x04 \x01(\x0b2\x15.PB_Nfca.ReadResponseH\x00\x12G\n\x1bmf_ultralight_read_page_req\x18\x05 \x01(\x0b2 .PB_MfUltralight.ReadPageRequestH\x00\x12I\n\x1cmf_ultralight_read_page_resp\x18\x06 \x01(\x0b2!.PB_MfUltralight.ReadPageResponseH\x00B\t\n\x07content*\xd6\x05\n\rCommandStatus\x12\x06\n\x02OK\x10\x00\x12\t\n\x05ERROR\x10\x01\x12\x10\n\x0cERROR_DECODE\x10\x02\x12\x19\n\x15ERROR_NOT_IMPLEMENTED\x10\x03\x12\x0e\n\nERROR_BUSY\x10\x04\x12(\n$ERROR_CONTINUOUS_COMMAND_INTERRUPTED\x10\x0e\x12\x1c\n\x18ERROR_INVALID_PARAMETERS\x10\x0f\x12\x1b\n\x17ERROR_STORAGE_NOT_READY\x10\x05\x12\x17\n\x13ERROR_STORAGE_EXIST\x10\x06\x12\x1b\n\x17ERROR_STORAGE_NOT_EXIST\x10\x07\x12#\n\x1fERROR_STORAGE_INVALID_PARAMETER\x10\x08\x12\x18\n\x14ERROR_STORAGE_DENIED\x10\t\x12\x1e\n\x1aERROR_STORAGE_INVALID_NAME\x10\n\x12\x1a\n\x16ERROR_STORAGE_INTERNAL\x10\x0b\x12!\n\x1dERROR_STORAGE_NOT_IMPLEMENTED\x10\x0c\x12\x1e\n\x1aERROR_STORAGE_ALREADY_OPEN\x10\r\x12\x1f\n\x1bERROR_STORAGE_DIR_NOT_EMPTY\x10\x12\x12\x18\n\x14ERROR_APP_CANT_START\x10\x10\x12\x1b\n\x17ERROR_APP_SYSTEM_LOCKED\x10\x11\x12\x19\n\x15ERROR_APP_NOT_RUNNING\x10\x15\x12\x17\n\x13ERROR_APP_CMD_ERROR\x10\x16\x12)\n%ERROR_VIRTUAL_DISPLAY_ALREADY_STARTED\x10\x13\x12%\n!ERROR_VIRTUAL_DISPLAY_NOT_STARTED\x10\x14\x12\x1d\n\x19ERROR_GPIO_MODE_INCORRECT\x10:\x12\x1f\n\x1bERROR_GPIO_UNKNOWN_PIN_MODE\x10;B!\n\x1fcom.flipperdevices.nfc.protobufb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'main_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.flipperdevices.nfc.protobuf'
    _COMMANDSTATUS._serialized_start = 399
    _COMMANDSTATUS._serialized_end = 1125
    _EMPTY._serialized_start = 52
    _EMPTY._serialized_end = 59
    _MAIN._serialized_start = 62
    _MAIN._serialized_end = 396
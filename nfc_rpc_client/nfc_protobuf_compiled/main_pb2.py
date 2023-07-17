"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import nfca_pb2 as nfca__pb2
from . import mf_ultralight_pb2 as mf__ultralight__pb2
from . import mf_classic_pb2 as mf__classic__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmain.proto\x12\x03Nfc\x1a\nnfca.proto\x1a\x13mf_ultralight.proto\x1a\x10mf_classic.proto"\x07\n\x05Empty"\xf6\x12\n\x04Main\x12*\n\x0ecommand_status\x18\x01 \x01(\x0e2\x12.Nfc.CommandStatus\x12\x1b\n\x05empty\x18\x02 \x01(\x0b2\n.Nfc.EmptyH\x00\x12-\n\rnfca_read_req\x18\x03 \x01(\x0b2\x14.PB_Nfca.ReadRequestH\x00\x12/\n\x0enfca_read_resp\x18\x04 \x01(\x0b2\x15.PB_Nfca.ReadResponseH\x00\x12>\n\x16nfca_emulate_start_req\x18\x05 \x01(\x0b2\x1c.PB_Nfca.EmulateStartRequestH\x00\x12@\n\x17nfca_emulate_start_resp\x18\x06 \x01(\x0b2\x1d.PB_Nfca.EmulateStartResponseH\x00\x12<\n\x15nfca_emulate_stop_req\x18\x07 \x01(\x0b2\x1b.PB_Nfca.EmulateStopRequestH\x00\x12>\n\x16nfca_emulate_stop_resp\x18\x08 \x01(\x0b2\x1c.PB_Nfca.EmulateStopResponseH\x00\x12G\n\x1bmf_ultralight_read_page_req\x18\t \x01(\x0b2 .PB_MfUltralight.ReadPageRequestH\x00\x12I\n\x1cmf_ultralight_read_page_resp\x18\n \x01(\x0b2!.PB_MfUltralight.ReadPageResponseH\x00\x12M\n\x1emf_ultralight_read_version_req\x18\x0b \x01(\x0b2#.PB_MfUltralight.ReadVersionRequestH\x00\x12O\n\x1fmf_ultralight_read_version_resp\x18\x0c \x01(\x0b2$.PB_MfUltralight.ReadVersionResponseH\x00\x12I\n\x1cmf_ultralight_write_page_req\x18\r \x01(\x0b2!.PB_MfUltralight.WritePageRequestH\x00\x12K\n\x1dmf_ultralight_write_page_resp\x18\x0e \x01(\x0b2".PB_MfUltralight.WritePageResponseH\x00\x12Q\n mf_ultralight_read_signature_req\x18\x0f \x01(\x0b2%.PB_MfUltralight.ReadSignatureRequestH\x00\x12S\n!mf_ultralight_read_signature_resp\x18\x10 \x01(\x0b2&.PB_MfUltralight.ReadSignatureResponseH\x00\x12M\n\x1emf_ultralight_read_counter_req\x18\x11 \x01(\x0b2#.PB_MfUltralight.ReadCounterRequestH\x00\x12O\n\x1fmf_ultralight_read_counter_resp\x18\x12 \x01(\x0b2$.PB_MfUltralight.ReadCounterResponseH\x00\x12V\n#mf_ultralight_read_tearing_flag_req\x18\x13 \x01(\x0b2\'.PB_MfUltralight.ReadTearingFlagRequestH\x00\x12X\n$mf_ultralight_read_tearing_flag_resp\x18\x14 \x01(\x0b2(.PB_MfUltralight.ReadTearingFlagResponseH\x00\x12O\n\x1fmf_ultralight_emulate_start_req\x18\x15 \x01(\x0b2$.PB_MfUltralight.EmulateStartRequestH\x00\x12Q\n mf_ultralight_emulate_start_resp\x18\x16 \x01(\x0b2%.PB_MfUltralight.EmulateStartResponseH\x00\x12M\n\x1emf_ultralight_emulate_stop_req\x18\x17 \x01(\x0b2#.PB_MfUltralight.EmulateStopRequestH\x00\x12O\n\x1fmf_ultralight_emulate_stop_resp\x18\x18 \x01(\x0b2$.PB_MfUltralight.EmulateStopResponseH\x00\x128\n\x13mf_classic_auth_req\x18\x19 \x01(\x0b2\x19.PB_MfClassic.AuthRequestH\x00\x12:\n\x14mf_classic_auth_resp\x18\x1a \x01(\x0b2\x1a.PB_MfClassic.AuthResponseH\x00\x12C\n\x19mf_classic_read_block_req\x18\x1b \x01(\x0b2\x1e.PB_MfClassic.ReadBlockRequestH\x00\x12E\n\x1amf_classic_read_block_resp\x18\x1c \x01(\x0b2\x1f.PB_MfClassic.ReadBlockResponseH\x00\x12E\n\x1amf_classic_write_block_req\x18\x1d \x01(\x0b2\x1f.PB_MfClassic.WriteBlockRequestH\x00\x12G\n\x1bmf_classic_write_block_resp\x18\x1e \x01(\x0b2 .PB_MfClassic.WriteBlockResponseH\x00\x12C\n\x19mf_classic_read_value_req\x18\x1f \x01(\x0b2\x1e.PB_MfClassic.ReadValueRequestH\x00\x12E\n\x1amf_classic_read_value_resp\x18  \x01(\x0b2\x1f.PB_MfClassic.ReadValueResponseH\x00\x12G\n\x1bmf_classic_change_value_req\x18! \x01(\x0b2 .PB_MfClassic.ChangeValueRequestH\x00\x12I\n\x1cmf_classic_change_value_resp\x18" \x01(\x0b2!.PB_MfClassic.ChangeValueResponseH\x00B\t\n\x07content*M\n\rCommandStatus\x12\x06\n\x02OK\x10\x00\x12\t\n\x05ERROR\x10\x01\x12\x19\n\x15ERROR_NOT_IMPLEMENTED\x10\x03\x12\x0e\n\nERROR_BUSY\x10\x04B!\n\x1fcom.flipperdevices.nfc.protobufb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'main_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.flipperdevices.nfc.protobuf'
    _COMMANDSTATUS._serialized_start = 2504
    _COMMANDSTATUS._serialized_end = 2581
    _EMPTY._serialized_start = 70
    _EMPTY._serialized_end = 77
    _MAIN._serialized_start = 80
    _MAIN._serialized_end = 2502
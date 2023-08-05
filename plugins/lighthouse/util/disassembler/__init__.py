#--------------------------------------------------------------------------
# Disassembler API Selector
#--------------------------------------------------------------------------
#
#    this file will select and load the shimmed disassembler API for the
#    appropriate (current) disassembler platform.
#
#    see api.py for more details regarding this API shim layer
#

disassembler = None

#--------------------------------------------------------------------------
# IDA API Shim
#--------------------------------------------------------------------------

if disassembler is None:
    try:
        from .ida_api import IDACoreAPI, IDAContextAPI
        disassembler = IDACoreAPI()
        DisassemblerContextAPI = IDAContextAPI
    except ImportError:
        pass

#--------------------------------------------------------------------------
# Binary Ninja API Shim
#--------------------------------------------------------------------------

if disassembler is None:
    try:
        from .binja_api import BinjaCoreAPI, BinjaContextAPI
        disassembler = BinjaCoreAPI()
        DisassemblerContextAPI = BinjaContextAPI
    except ImportError:
        pass

#--------------------------------------------------------------------------
# Unknown Disassembler
#--------------------------------------------------------------------------

if disassembler is None:
    raise NotImplementedError("Unknown or unsupported disassembler!")


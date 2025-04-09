from pyasn1.codec.der import decoder
from pyasn1.type import univ
from pyasn1_modules import rfc3739
import binascii

# Your hex DER-encoded qcStatement (as string)
hex_data = "300A3008060604008E460104"
der_data = binascii.unhexlify(hex_data)

# Decode the outer sequence
qc_statements, _ = decoder.decode(der_data, asn1Spec=univ.Sequence())

# Decode inner structure
inner_seq = qc_statements[0]

# Extract OID
qc_oid = inner_seq[0]

print("QCStatement OID:", qc_oid)

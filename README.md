# Swisscom CA replicated

Original certificates folder: SwisscomCAoriginal [Swisscom website](https://www.swisscom.ch/en/business/enterprise/offer/security/digital_certificate_service.html)\
New generated certificates folder: SwisscomCAreplica
#### Replicated:
### CA
Original [Swisscom Root CA 2 (sdcs-root2)](https://aia.swissdigicert.ch/sdcs-root2.txt)\
Replicated [Swisscom Root CA 2 replica](https://github.com/glebef/SwisscomCAreplica/blob/main/SwisscomCAreplica/sdcs-root2.pem)

Original [Swisscom Root CA 4 (sdcs-root4)](https://aia.swissdigicert.ch/sdcs-root4.txt)\
Replicated [Swisscom Root CA 4 replicated](https://github.com/glebef/SwisscomCAreplica/blob/main/SwisscomCAreplica/sdcs-root4.pem)

### Intermediate Certificate Authority (CA)
Original [Swisscom Diamant CA 4 (sdcs-diamant4)](https://aia.swissdigicert.ch/sdcs-diamant4.txt)\
Replicated [Swisscom Diamant CA 4 replicated](https://github.com/glebef/SwisscomCAreplica/blob/main/SwisscomCAreplica/sdcs-diamant4.pem)

Original [Swisscom Saphir CA 4 (sdcs-saphir4)](https://aia.swissdigicert.ch/sdcs-saphir4.txt)\
Replicated [Swisscom Saphir CA 4 replicated](https://github.com/glebef/SwisscomCAreplica/blob/main/SwisscomCAreplica/sdcs-saphir4.pem)

Original [Swisscom Rubin CA 4 (sdcs-rubin4)](https://aia.swissdigicert.ch/sdcs-rubin4.txt)\
Replicated [Swisscom Rubin CA 4 replicated](https://github.com/glebef/SwisscomCAreplica/blob/main/SwisscomCAreplica/sdcs-rubin4.pem)

#### Replicated data for each certificate
Issuer\
Validity\
Subject\
Serial Number\
Signature Algorithm\
Hash Algorithm\
Mask Algorithm\
Public Key Algorithm\
Public Key Size

#### Replicated X509v3 extensions
X509v3 Basic Constraints\
X509v3 Subject Key Identifier\
X509v3 Certificate Policies\
X509v3 Extended Key Usage\
X509v3 Key Usage

#### QCStatement not implemented for sdcs-diamant4

openssl asn1parse -in sdcs-diamant4.pem

1245:d=5  hl=2 l=   8 prim: OBJECT            :qcStatements\
1255:d=5  hl=2 l=  12 prim: OCTET STRING      [HEX DUMP]:300A3008060604008E460104

decode-qc.py [HEX DUMP]:300A3008060604008E460104

QCStatement:\
  OID: 0.4.0.1862.1.4  (id-etsi-qcs-QcSSCD)
  
Qualified Certificate Statement (QCS) claiming that the private key related to the certified public key resides in a qualified electronic Signature/Seal Creation Device (SSCD)\
ETSI EN 319 412-5

OpenSSL didn’t accept this config on the first attempt, so I don’t have more time to spend on it.

### Tools
OpenSSL 3.4.1 11 Feb 2025 (Library: OpenSSL 3.4.1 11 Feb 2025)

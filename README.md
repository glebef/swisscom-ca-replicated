# Swisscom CA replicated

Original certificates folder: SwisscomCAoriginal [Swisscom website](https://www.swisscom.ch/en/business/enterprise/offer/security/digital_certificate_service.html)\
New generated certificates folder: SwisscomCAreplica
#### Replicated:
### CA
sdcs-root2\
sdcs-root4
### Intermediate Certificate Authority (CA)
sdcs-diamant4\
sdcs-saphir4\
sdcs-rubin4
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

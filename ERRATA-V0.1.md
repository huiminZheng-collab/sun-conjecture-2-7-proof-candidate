# Packaging correction after v0.1

The scientific manuscript, proof claims, and verification program in v0.1
were correct as frozen locally. A fresh Windows clone could nevertheless fail
`VERIFY.ps1` because Git's automatic line-ending conversion changed LF bytes
to CRLF after checkout.

Version 0.2 is an additive packaging correction. It adds `.gitattributes`
with `* -text`, records this erratum, and regenerates the release manifest.
No theorem, proof, citation, PDF, or verification algorithm is changed.

# Exact verification program

c27_formal_group_verify.py is a diagnostic check, not part of the logical
proof.  It uses exact rational arithmetic and only the Python standard
library.

Run:

    python c27_formal_group_verify.py

The program verifies through q^99 that the modular parameter is integral
and odd and that the logarithmic derivative equals eta(4z)^6; it also
checks the CM prime-coefficient formula for every odd prime below 100.

# Proof candidate for Z.-H. Sun's Conjecture 2.7

This content-anonymous packet contains a formal-group proof candidate for
Conjecture 2.7 in Zhi-Hong Sun, *New congruences involving Apéry-like
numbers*, arXiv:2004.07172v2.

For the Apéry-like sequence `G_n` (OEIS A143583), the result proves the
all-depth three-term congruence for `G_(mp^r-1)/2` at primes
`p = x^2 + 4y^2`.  The central identity identifies its formal logarithm,
after an integral modular-lambda coordinate change, with the Eichler integral
of the CM newform `eta(4z)^6`.

## Status

This is a proof candidate, not a claim of journal acceptance or human peer
review.  Its formal-group normalization, signs, indices, and quantifiers have
undergone an independent internal audit, and the accompanying exact series
check passes.  A targeted literature search through 18 September 2026 did
not locate an earlier proof of the exact conjecture; that is not an exhaustive
guarantee of novelty.

Version 0.2 adds a checkout-safe line-ending policy and a regenerated
manifest. It corrects the v0.1 packaging defect described in
`ERRATA-V0.1.md` without changing the scientific files.

## Contents

- `paper/main.pdf`: content-anonymous manuscript.
- `paper/main.tex`: manuscript source.
- `support/c27_formal_group_verify.py`: exact power-series and CM coefficient
  checks.
- `RELEASE-MANIFEST.sha256`: SHA-256 hashes of the frozen payload.
- `VERIFY.ps1`: fail-closed manifest verifier.

## AI-use disclosure

OpenAI Codex served as the principal mathematical research tool.  All new
proof strategies and mathematical arguments in the manuscript were generated
by Codex.  It was also used for exact checks, literature triage, and drafting.
The future named author must independently verify the submission and accepts
full responsibility for it.  The AI system is not an author.

## Non-claims

Public availability does not imply journal submission, acceptance, peer
review, or correctness.  The payload omits the author's identity, but the
hosting account and Git history may be identity-linked; this is therefore a
content-anonymous release, not an author-unlinkable one.

tokenizer
=========

Orthographic profile tokenization tools, includes:

- tokenizer.py - Module for graphemeic and orthographic tokenization with orthography profiles.
- create_profiles.py - Script for generating information to create an initial orthography profile.
- get_environments.py - Get character environments given a list of words and a target character.

The profiles/ directory contains some example orthography profiles, e.g.

- IPA.prf
- IPA.csv - Data file that encodes Unicode IPA and some extra symbols (used in PHOIBLE)
- phoibleIPA.prf
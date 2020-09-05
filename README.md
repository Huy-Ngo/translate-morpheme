# Morpheme translator

A simple script that translates from morphology glossing to word.

This work best for analytic/isolated language. The more fusional
the language is and the more exceptions (irregularities) the rules have,
the more complicated the rule file would be.

# How to write rules

Rules are written as follow:

- words are separated by a space
- morphemes are separated by a dot (.)
- a morpheme representing multiple units can have underscore

Convention: morphemes that denote the meaning of the words are written in lowercase, morphemes that denote declension or conjugation are written in uppercase.

For examples, see the rules and morphemes written in `test/`

# Disclaimer

The outputed results can be slightly different from expected. The final full stop may be missing.

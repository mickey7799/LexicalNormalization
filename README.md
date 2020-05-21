# Lexical Normalization

Implement spelling correction methods for the tasks of lexical normalization, the process of transforming words to their standard form

## Data
- misspelled words(misspell): 10,322 tokens
- dictionary file: 370,100 reference  collection
- evaluation file: 10,322 corresponding canonical form to the tokens in misspell

## Method

### GED
For tokensin misspell, the GED between each dictionary entry was calculated, and the token with the smallest GEDwas returned as the most possible canonical form. 

The Needleman-Wunsch Algorithm was used to calculate the edit distance efficiently with the Levenshtein parameter of (m, i, d, r ) = (0, 1, 1, 1)

### Soundex
Soundex was used to convert all tokens in misspell into its Soundex representation, which then be compared to tokens in dictionary one by one.

The token with the exact match to  dictionary was returned as the most possible canonical form.

### Double Metaphone
Double Metaphone generates two alternate hashes for each token, which presents search results with two levels of precision. 

For every token in misspelled, if its two hashes are both the same as the two hashes of dictionary word, it is considered the best match for the canonical form. 

### Mixture of GED and Soundex & Mixture of GED and Metaphone
Firstly, GED technique was applied to find matches from dictionary within 2 (inclusive) edit distance of the token. 

Secondly, phonetic methods were applied to the set of matches based on edit distance, which refines the results to be phonetically similarto the token.

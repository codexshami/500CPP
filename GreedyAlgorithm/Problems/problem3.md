# Problem 3: Huffman Coding

## Problem Statement
Given a string of characters and their frequencies, build a Huffman Tree and return the Huffman codes for each character.

## Input Format
- A dictionary `freq` mapping characters to their frequencies.

## Output Format
- A dictionary mapping each character to its Huffman code (binary string).

## Constraints
- 1 <= number of unique characters <= 26
- 1 <= frequency <= 10^6

## Example
**Input:** freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}  
**Output:** {'f': '0', 'c': '100', 'd': '101', 'a': '1100', 'b': '1101', 'e': '111'}

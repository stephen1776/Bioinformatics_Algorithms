### 01 - Where in the Genome Does DNA Replication Occur?

#### Algorithmic Warmup
___
###### 01 Implement PatternCount
Given: {DNA strings}} Text and Pattern.

Return: Count(Text, Pattern).

###### 02 Frequent Words Problem

Find the most frequent k-mers in a string.

Given: A DNA string Text and an integer k.

Return: All most frequent k-mers in Text.

###### 03 Reverse Complement Problem

Find the reverse complement of a DNA string.

Given: A DNA string Pattern.

Return: Pattern*, the reverse complement of Pattern.

###### 04 Pattern Matching Problem

Find all occurrences of a pattern in a string.

Given: Strings Pattern and Genome.

Return: All starting positions in Genome where Pattern appears as a substring.

###### 05 Clump Finding Problem

Find patterns forming clumps in a string.

Given: A string Genome, and integers k, L, and t.

Return: All distinct k-mers forming (L, t)-clumps in Genome.
Sample Dataset

###### 06 Minimum Skew Problem

Find a position in a genome minimizing the skew.

Given: A DNA string Genome.

Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).

###### 07 Hamming Distance Problem

Compute the Hamming distance between two DNA strings.

Given: Two DNA strings.

Return: An integer value representing the Hamming distance.

###### 08 Approximate Pattern Matching Problem

Find all approximate occurrences of a pattern in a string.

Given: Strings Pattern and Text along with an integer d.

Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

###### 09 Frequent Words with Mismatches Problem

Find the most frequent k-mers with mismatches in a string.

Given: A string Text as well as integers k and d.

Return: All most frequent k-mers with up to d mismatches in Text.

###### 10 Frequent Words with Mismatches and Reverse Complements Problem

Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.

Given: A DNA string Text as well as integers k and d.

Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern*U) over all possible k-mers.

###### 11 Computing a Frequency Array

Generate the frequency array of a DNA string.

Given: A DNA string Text and an integer k.

Return: The frequency array of k-mers in Text.

###### 12 Implement PatternToNumber

Convert a DNA string to a number.

Given: A DNA string Pattern.

Return: PatternToNumber(Pattern).

###### 13 Implement NumberToPattern

Convert an integer to its corresponding DNA string.

Given: Integers index and k.

Return: NumberToPattern(index, k).

###### 14 Generate the d-Neighborhood of a String

Find all the neighbors of a pattern.

Given: A DNA string Pattern and an integer d.

Return: The collection of strings Neighbors(Pattern, d).
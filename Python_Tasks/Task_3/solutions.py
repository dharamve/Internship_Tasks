"""
Task 3: Python Coding & Problem-Solving
Reusable solutions for all 15 questions.
Each function returns its result.
"""

# Q1. Find the frequency of each word in a sentence
def word_frequency(sentence):
    """Return a dictionary containing the frequency of each word."""
    counts = {}
    for word in sentence.split():
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1
    return counts


# Q2. Find the frequency of each character in a word
def character_frequency(word):
    """Return a dictionary containing the frequency of each character."""
    counts = {}
    for character in word:
        counts[character] = counts.get(character, 0) + 1
    return counts


# Q3. Find the first non-repeating character in a word
def first_non_repeating_character(word):
    """Return the first character occurring once, or None if there is none."""
    counts = character_frequency(word)
    for character in word:
        if counts[character] == 1:
            return character
    return None


# Q4. Check whether two strings are anagrams
def are_anagrams(s1, s2):
    """Return True when both strings contain the same characters and counts."""
    return character_frequency(s1.replace(" ", "").lower()) == character_frequency(
        s2.replace(" ", "").lower()
    )


# Q5. Find the first repeating character in a string
def first_repeating_character(text):
    """Return the character whose second occurrence is met first, or None."""
    seen = set()
    for character in text:
        if character in seen:
            return character
        seen.add(character)
    return None


# Q6. Move all zeros to the end of a list
def move_zeros_to_end(nums):
    """Return a new list with non-zero values in order followed by all zeros."""
    non_zeros = [number for number in nums if number != 0]
    zeros = [number for number in nums if number == 0]
    return non_zeros + zeros


# Q7. Find the second highest distinct number in a list
def second_highest_distinct(nums):
    """Return the second-largest distinct number, or None if it does not exist."""
    distinct = sorted(set(nums), reverse=True)
    return distinct[1] if len(distinct) >= 2 else None


# Q8. Remove duplicates without changing the original order
def remove_duplicates_preserve_order(nums):
    """Return a list containing each value at its first occurrence."""
    result = []
    seen = set()
    for number in nums:
        if number not in seen:
            result.append(number)
            seen.add(number)
    return result


# Q9. Find the missing number from 1 to N
def find_missing_number(nums, n):
    """Return the missing value from the range 1 through n."""
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# Q10. Find the first pair whose sum equals a target
def two_sum_first_pair(nums, target):
    """Return the qualifying pair whose second item is encountered earliest."""
    seen = set()
    for number in nums:
        needed = target - number
        if needed in seen:
            return [needed, number]
        seen.add(number)
    return []


# Q11. Find the number closest to zero (positive wins a tie)
def closest_to_zero(nums):
    """Return the value closest to zero; choose the positive value on a tie."""
    return min(nums, key=lambda number: (abs(number), -number))


# Q12. Find common elements between two lists, preserving list1 order
def common_elements(list1, list2):
    """Return unique common values in their first-list order."""
    second_values = set(list2)
    result = []
    seen = set()
    for value in list1:
        if value in second_values and value not in seen:
            result.append(value)
            seen.add(value)
    return result


# Q13. Rotate a list to the right by K positions
def rotate_right(nums, k):
    """Return a list rotated right by k positions."""
    if not nums:
        return []
    k %= len(nums)
    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]


# Q14. Find the maximum sum of two consecutive elements
def max_consecutive_pair_sum(nums):
    """Return the largest sum made by any adjacent pair."""
    return max(nums[index] + nums[index + 1] for index in range(len(nums) - 1))


# Q15. Find all unique pairs whose sum equals a target
def all_unique_pairs(nums, target):
    """Return unique target-sum pairs, each sorted and results sorted by first value."""
    values = set(nums)
    pairs = set()
    for number in values:
        partner = target - number
        if partner in values and number <= partner:
            # Equal values require two distinct positions in the original list.
            if number != partner or nums.count(number) >= 2:
                pairs.add((number, partner))
    return [list(pair) for pair in sorted(pairs)]

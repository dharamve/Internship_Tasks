"""
Task 3: Run all 15 solutions from the VS Code terminal.
Run with: python main.py
"""
from solutions import (
    word_frequency,
    character_frequency,
    first_non_repeating_character,
    are_anagrams,
    first_repeating_character,
    move_zeros_to_end,
    second_highest_distinct,
    remove_duplicates_preserve_order,
    find_missing_number,
    two_sum_first_pair,
    closest_to_zero,
    common_elements,
    rotate_right,
    max_consecutive_pair_sum,
    all_unique_pairs,
)


def show(question, function, cases):
    print(f"\n{question}")
    for label, args in cases:
        print(f"  {label}: {function(*args)}")


if __name__ == "__main__":
    show("Q1. Word frequency", word_frequency, [
        ("Given input", ("python is easy and python is powerful",)),
        ("Additional test", ("data helps data teams",)),
    ])
    show("Q2. Character frequency", character_frequency, [
        ("Given input", ("banana",)),
        ("Additional test", ("hello",)),
    ])
    show("Q3. First non-repeating character", first_non_repeating_character, [
        ("Given input", ("swiss",)),
        ("Additional test", ("aabb",)),
    ])
    show("Q4. Anagrams", are_anagrams, [
        ("Given input", ("listen", "silent")),
        ("Additional test", ("hello", "world")),
    ])
    show("Q5. First repeating character", first_repeating_character, [
        ("Given input", ("programming",)),
        ("Additional test", ("abcdef",)),
    ])
    show("Q6. Move zeros to end", move_zeros_to_end, [
        ("Given input", ([0, 3, 0, 1, 2, 0, 4],)),
        ("Additional test", ([0, 0, 5],)),
    ])
    show("Q7. Second highest distinct number", second_highest_distinct, [
        ("Given input", ([10, 20, 40, 30, 40, 20],)),
        ("Additional test", ([7, 7, 7],)),
    ])
    show("Q8. Remove duplicates, preserve order", remove_duplicates_preserve_order, [
        ("Given input", ([4, 2, 4, 5, 2, 7, 5],)),
        ("Additional test", ([1, 1, 2, 3, 2],)),
    ])
    show("Q9. Missing number", find_missing_number, [
        ("Given input", ([1, 2, 4, 5, 6], 6)),
        ("Additional test", ([1, 3, 4], 4)),
    ])
    show("Q10. First target-sum pair", two_sum_first_pair, [
        ("Given input", ([2, 7, 11, 15], 9)),
        ("Additional test", ([1, 4, 2, 3], 5)),
    ])
    show("Q11. Closest to zero", closest_to_zero, [
        ("Given input", ([-8, -3, 2, 5, -2],)),
        ("Additional test", ([-4, 4, 7],)),
    ])
    show("Q12. Common elements", common_elements, [
        ("Given input", ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])),
        ("Additional test", ([2, 2, 1, 3], [3, 2, 2])),
    ])
    show("Q13. Rotate right", rotate_right, [
        ("Given input", ([1, 2, 3, 4, 5], 2)),
        ("Additional test", ([1, 2, 3], 4)),
    ])
    show("Q14. Maximum consecutive-pair sum", max_consecutive_pair_sum, [
        ("Given input", ([4, 7, 2, 9, 5],)),
        ("Additional test", ([-5, -2, -8],)),
    ])
    show("Q15. All unique target-sum pairs", all_unique_pairs, [
        ("Given input", ([2, 4, 3, 5, 7, 8, 1], 9)),
        ("Additional test", ([1, 1, 2, 3, 4], 4)),
    ])

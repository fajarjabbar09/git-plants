# Python Practice Test 2 — Evaluation Report

**Intern:** Fajar Jabbar  
**File Reviewed:** `test2.py`  
**Topics:** Booleans · Operators · Lists · Tuples · Sets · Dictionaries  
**Reviewer:** Bilal  
**Status:** Evaluated and executed successfully

---

## Overall Result

- Script runs from start to finish with **no runtime crash**.
- Strong work on operators, lists, and most dictionary basics.
- Several answers are incomplete (missing `print`), use the wrong variable, or do not match the requested output format.
- **Estimated score:** **58/72** (bonus section scored separately below).

---

## Score by Section

| Section | Topic | Score (approx.) |
|---------|--------|-----------------|
| 1 | Booleans | 3.5 / 5 |
| 2 | Operators | 7 / 7 |
| 3 | Lists | 18 / 19 |
| 4 | Tuples | 8 / 11 |
| 5 | Sets | 8 / 13 |
| 6 | Dictionaries | 13 / 17 |
| Bonus | Student Report | Partial |

---

## Strengths

- Operators section (arithmetic, comparison, logical, assignment, identity, membership, bitwise) is fully correct.
- List operations (`append`, `insert`, `remove`, `sort`, `reverse`, `extend`, `clear`, etc.) are well implemented.
- Tuple creation, indexing, unpacking, and single-item tuple syntax are correct.
- Dictionary creation, `.get()`, `.update()`, `del`, and nested access structure are mostly solid.
- Bonus logic for `passed` subjects and average calculation is on the right track.

---

## Items to Correct (Required)

### Section 1 — Booleans

1. **Q2 (e):** Last comparison should be `"hello" == "Hello"` (case-sensitive), not `"hello" == "hello"` again.
2. **Q3:** Do not reuse variable `f` for `bool(None)` — it overwrites `bool([1, 2, 3])`. Use separate variables and print all seven results (`a` through `g`).
3. **Q5:** Missing entirely. Add:
   - `isinstance(3.14, float)` → print result
   - `isinstance("hello", int)` → print result

### Section 3 — Lists

4. **Q16:** Slice should include index 3. Use `cities[1:4]` (not `[1:3]`) if the task means indices 1, 2, and 3.
5. **Q22:** `pop()` returns the removed item — print that value, e.g. `print(cities.pop())`, not only the list afterward.

### Section 4 — Tuples

6. **Q34:** Comment the expected error as **`TypeError`** (tuple items cannot be reassigned), and keep the short explanation.
7. **Q37:** Count `"blue"` in **`counts_tuple`**, not `colors`:
   - `print(counts_tuple.count("blue"))`  → expected: `3`
8. **Q40:** After converting back to a tuple, **print the final tuple**.

### Section 5 — Sets

9. **Q46:** Add a comment explaining that sets do not allow duplicate values.
10. **Q48:** `discard()` returns `None`. Call `team_a.discard("Zara")`, then `print(team_a)` separately.
11. **Q51–Q53:** Results are computed but never printed. Add `print()` for intersection, difference, and symmetric difference.
12. **Q54:** Check subset — e.g. `print({"Diana"}.issubset(team_a))` or `print({"Diana"} <= team_a)`.

### Section 6 — Dictionaries

13. **Q63:** Print values — `print(student.values())`.
14. **Q64:** Print items — `print(student.items())`.
15. **Q68:** Format output as `key  :  value` (not raw tuples), e.g.:
    ```python
    for key, value in student.items():
        print(f"{key}  :  {value}")
    ```
16. **Q69:** Print the **return value** of `pop("is_intern")`, not the whole dictionary.
17. **Q70:** Nested key should be **`"employees"`** (as in the spec), not `"employee"`.
18. **Q71:** Print only `age` from both dictionaries to show the copy is independent, e.g.:
    ```python
    print(student["age"])
    print(student_backup["age"])
    ```

### Bonus — Student Report

19. Add top/bottom separator lines (`================================`).
20. Print **marks** (e.g. `80, 45, 72`) — currently the Marks line is empty.
21. Use spaces after commas in subjects: `Math, Science, English`.
22. Prefer variable name `report` (lowercase) to match the spec; avoid shadowing built-in `list`.

---

## Minor Improvement Notes

- **Q7:** Comparison results are correct; printing order differs slightly from the question list (not wrong, just reorder if you want to match the sheet exactly).
- **Q42:** After fixing Q40, avoid printing `"purple"` twice in the loop.
- **Q71:** Printing full dicts still shows independence, but the question asks specifically for age from both.

---

## Recommendation

Please fix the required items above and resubmit `test2.py`.  
Section 2 and most of Section 3 are in good shape — focusing on missing prints, correct variables, and output formatting will bring this submission close to full marks.

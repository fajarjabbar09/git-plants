# Python Practice Test 3 — Evaluation Report

**Intern:** Fajar Jabbar  
**File Reviewed:** `test3.py`  
**Topics:** If...Else · Match · While Loops · For Loops (break, continue, pass, range, nested loops, else on loops)  
**Reviewer:** Bilal  
**Status:** Evaluated and executed successfully

---

## Overall Result

- Script runs from start to finish with **no runtime crash**.
- Strong, confident work on conditionals, match, range, nested loops, and comprehensions.
- A few answers have logic/formatting bugs, one question is missing entirely, and the **Bonus** section is incomplete (FizzBuzz prints a literal string, and the statistics part does not compute anything).
- **Estimated score:** **22 / 25** main questions, plus **Bonus: Partial** (scored separately below).

---

## Score by Section

| Section | Topic | Score (approx.) |
|---------|--------|-----------------|
| 1 | If...Else | 4.5 / 6 |
| 2 | Match | 2 / 2 |
| 3 | While Loops | 4 / 5 |
| 4 | For Loops | 11 / 12 |
| Bonus | FizzBuzz + Score Stats | Partial |

---

## Strengths

- Match statements (Q7, Q8), including the `|` (OR) pattern, are fully correct.
- `range()` usage (Q16, Q17), `break`/`continue` (Q18, Q19), and `pass` (Q20) are all correct and well commented.
- Nested loops — the number pattern (Q22) and 2D grid (Q23) — work as intended.
- Dictionary iteration (Q24) and both list comprehensions (Q25) produce the expected output exactly.
- `for...else` (Q21) and `while...else` (Q13) are used correctly.

---

## Items to Correct (Required)

### Section 1 — If...Else

1. **Q2:** The final `else` prints `"E"`, but the spec says **below 60 → `"F"`**. Change `print("E")` to `print("F")`. (The `72` case happens to print `"C"` correctly, but the grade table itself is wrong.)
2. **Q3:** The "Zero" branch is missing `print`. Line `("Zero")` is just an expression and prints nothing. Fix:
   ```python
   else:
       print("Zero")
   ```

### Section 3 — While Loops

3. **Q11:** Off-by-one — the loop prints **1 through 11** (it should stop at 10). Because `i` starts at `0` and is incremented at the top, the condition `i <= 10` runs one extra time. Fix either by starting at `i = 1` with the increment at the bottom, or change the condition:
   ```python
   i = 0
   while i < 10:
       i += 1
       if i == 5:
           continue
       print(i)
   ```
4. **Q12 (minor):** Output is `Attempt1: wrong` — add a space and match the requested format: `f"Attempt {attempts}: wrong"`. Also `"Too many attempts."` is missing its period.

### Section 4 — For Loops

5. **Q15:** Missing entirely. Add the `enumerate()` loop:
   ```python
   for index, animal in enumerate(animals):
       print(index, ":", animal)
   ```
6. **Q21 (minor):** Logic is correct, but the wording should match the spec: print `"Odd found: 17"` (the question asks for `"Odd found: X"`).

### Bonus — Part A (FizzBuzz)

7. The `else` branch prints the literal string `"the number"` 30+ times. It should print the actual number:
   ```python
   else:
       print(i)
   ```

### Bonus — Part B (Exam Statistics)

8. This part does not meet the requirements. The task asks you to **compute** five values using loops (no `sum`/`min`/`max` built-ins): average, highest, lowest, count passed (`>= 50`), count failed (`< 50`). The current code only prints labels per score and calculates nothing. Suggested approach:
   ```python
   scores = [88, 45, 72, 91, 55, 63, 78, 49, 95, 60]
   total = 0
   highest = scores[0]
   lowest = scores[0]
   passed = 0
   failed = 0
   for s in scores:
       total += s
       if s > highest:
           highest = s
       if s < lowest:
           lowest = s
       if s >= 50:
           passed += 1
       else:
           failed += 1
   print("Average:", total / len(scores))
   print("Highest:", highest)
   print("Lowest:", lowest)
   print("Passed:", passed)
   print("Failed:", failed)
   ```

---

## Minor Improvement Notes

- **Q10 / Q12 / loops:** Avoid using `sum` as a variable name (Q10) — it shadows the built-in `sum()`. Prefer `total`.
- **Q4:** `has_id == True` works, but `if age >= 18 and has_id:` is cleaner.
- **Q23:** Printing each number on its own line is fine; use `print(r, end=" ")` plus a `print()` per row if you want a grid layout.
- **Q6:** Indentation is inconsistent (mix of 3 and 4 spaces). It runs, but keep indentation at a consistent 4 spaces.

---

## Recommendation

Please fix the required items above and resubmit `test3.py`.  
Sections 2 and 4 are in excellent shape. The main focus areas are the two missing `print` issues (Q3), the Q11 off-by-one, the missing Q15, and completing the Bonus section — addressing these will bring this submission close to full marks.

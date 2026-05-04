# Python Practice Test Evaluation Report

**Intern:** Fajar Jabbar  
**File Reviewed:** `test.py`  
**Reviewer:** Bilal  
**Status:** Evaluated and executed

---

## Overall Result

- Script execution is successful when required input is provided.
- Most answers are correct and demonstrate good understanding of fundamentals.
- **Estimated score:** **46/60** (bonus formatting quality not fully included).

---

## Strengths

- Strong attempt across syntax, variables, data types, and casting.
- No major syntax errors that prevent the file from running.
- Bonus section correctly captures user input and displays output types.

---

## Items to Correct (Required)

1. **Q5**: Replace `sep="???"` with `sep=" | "`.
2. **Q11**: `is_intern` should be boolean `True`, not string `"True"`.
3. **Q16**: Error comment should be `# NameError`.
4. **Q26**: Print both the complex value and its type.
5. **Q29**: Add both:
   - `math.sqrt(144)`
   - `round(math.pi, 4)` (or equivalent formatting to 4 decimals)
6. **Q41**: Reverse slicing should be `sentence[::-1]`.
7. **Q45**: Use `sentence.split()` and print the resulting list.
8. **Q54**: Print `"Ha"` five times using the `*` operator.
9. **Q59**: Use `"PASS".center(60, "-")`.
10. **Q60**: Add and print a 3-line multiline string (triple quotes).
11. **Bonus section**:
    - Ask for **birth year** (not age directly),
    - calculate age using `2026 - birth_year`,
    - print output in the requested formatted summary layout.

---

## Minor Improvement Notes

- **Q1**: Expected output includes an exclamation mark (`!`).
- **Q51**: Use `.format()` with placeholders explicitly for the intended method.
- **Q58**: Apply `.swapcase()` directly to `"hELLO wORLD"` as requested.

---

## Recommendation

Please revise the listed items and resubmit.  
After these corrections, the submission should be close to full marks.
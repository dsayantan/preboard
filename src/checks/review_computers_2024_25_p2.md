# Independent review — computers_2024_25_p2 (CS pre-board 2024-25, Paper 2, Practical)

The source is `SET-1/COMPUTER PRACTICAL.pdf`, 4 pages, all rendered at 110 dpi and read.

## Findings and fixes

None. No changes were needed.

## Checked and found correct

- **Transcription.**
  - Instructions page: marks 3/7/2/3, Project 15, and "4 printed pages".
  - Q1: the definitions, the four examples and INVALID INPUT for 700/450.
  - Q2: the size limits (greater than 2, less than 10), tasks (a)–(c), both example matrices and their shifted
    forms, both "Second Smallest" lines, and Example 3's message.
  - Q3: the keypad grid and all three examples line by line.
  - All match the page images.
- **Syllabus.** All three are standard ISC practical problems and inside the syllabus:
  - Q1 is a number problem using methods.
  - Q2 uses 2D arrays.
  - Q3 uses strings.
- **Q1 (Prime-Adam).**
  - I recomputed it independently: 5..100 → 11 13 31; 100..200 → 101 103 113; 50..70 → NIL; 1..1000 →
    2 3 11 13 31 101 103 113 211 311.
  - I re-ran PrimeAdam.java on all five inputs, and the outputs match the paper's format exactly.
  - The squares are held in long, so large ranges do not overflow.
- **Q2 ("second smallest").**
  - Example 1: the shifted matrix's minimum is 15, and the next larger value is 32, at (1,3).
  - Example 2: the minimum is 12, and the next is 30, at (3,0).
  - Both match the paper with 0-based indices. The examples have no repeated values, so they cannot settle
    whether "second smallest" means distinct values or second in sorted order. The writer chose distinct values
    and says so; a repeated minimum would otherwise make the answer equal the minimum. I find this reasonable.
  - The rotation is the last column wrapping round to the first, which is what both examples show.
  - I re-ran ShiftMatrix.java on all four inputs, including the random one (shifted 1 9 5 / 3 7 1 / 3 6 8 →
    3 at (1,0)), and traced it by hand.
- **Q3 (keypad).**
  - I re-derived the press counts: DEAR → 3:3, 2:1, 7:3; ALL → 2:1, 5:6; THANK → 8:1, 4:2, 2:1, 6:2, 5:2;
    YOU → 9:3, 6:3, 8:2.
  - The first-use key order reproduces the paper's line order.
  - GOOD-LUCK is invalid.
  - I re-ran Keypad.java on all four inputs, and the outputs match the paper line for line.
- **Algorithms and recall panels.** They are correct and match the programs.
- **Page.** `python3 src/build.py computers_2024_25_p2` runs with no ERROR. I read all 14 preview slices: nothing
  overflows and the tables render. The paper has no figures to draw.

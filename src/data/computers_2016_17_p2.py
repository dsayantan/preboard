"""Computer Science pre-board 2016-17, Paper 2 (Practical).  Transcribed from the page images (scanned).
Checks (every program compiled and run): src/checks/computers_2016_17_p2_check.py."""
from kit import Q, SEC
import computers_2016_17_figs as F
from cs_b_kit import jcode, jout

M = "computers_2016_17_p2"

PRAC_NOTE = r"""<p class="note">Answer as the practical expects it: the algorithm, then the documented Java program,
then the output for the paper's example and for further inputs — every output below is from an actual run of this
program (JDK 11).</p>"""

SAMPLE_CAL = r"""<pre class="code">No of days between start date and end date: 98 days
----------------------------------
            August 2016
----------------------------------
SUN MON TUE WED THU FRI SAT
----------------------------------
     1   2   3   4   5   6
----------------------------------
 7   8   9  10  11  12  13
----------------------------------
14  15  16  17  18  19  20
----------------------------------
21  22  23  24  25  26  27
----------------------------------
28  29  30  31

----------------------------------

----------------------------------
           November 2016
----------------------------------
SUN MON TUE WED THU FRI SAT
----------------------------------
         1   2   3   4   5
----------------------------------
 6   7   8   9  10  11  12
----------------------------------
13  14  15  16  17  18  19
----------------------------------
20  21  22  23  24  25  26
----------------------------------
27  28  29  30
----------------------------------</pre>"""

ITEMS = [
    SEC("Problems", "Select any one of the following problems."),

    Q("1", 20, r"""<p><b>QUESTION 1</b><br>Write a program to accept two dates and the weekday name of the 1st day of the months to
find out the number of days between them (Include start date and Exclude end date in calculation). Also generate the
calendar of the given months. Valid dates should be checked for.</p>
<p><b>Example :</b><br><b>INPUT:</b><br>Start Date: 10/8/2016<br>End Date :16/11/2016<br>1<sup>st</sup> day of August : Monday<br>
1<sup>st</sup> day of November: Tuesday</p><p><b>OUTPUT :</b></p>""" + SAMPLE_CAL,
      a=PRAC_NOTE + r"""<p><b>Idea.</b> Turn each date into a serial day number (days from 1/1/0001 up to and including it,
counting leap years); the difference end − start counts the start date and excludes the end date:
10/8 → 16/11/2016 is 22 (Aug 10–31) + 30 + 31 + 15 (Nov 1–15) = 98. A date is valid if 1 ≤ month ≤ 12 and
1 ≤ day ≤ days in that month (29 in February of a leap year). The calendars are printed from the weekday given
for the 1st of each month. If both dates fall in the same month its calendar is printed once.</p>
<p><b>Algorithm</b></p>
<ol><li>Start. Input start date and end date as dd/mm/yyyy; split each at '/'.</li>
<li>If either is not a valid date (non-numeric, month outside 1–12, day outside 1–days(month, year)) print
"INVALID DATE" and stop.</li>
<li>serial(d, m, y) ← Σ days of years 1 … y−1 + Σ days of months 1 … m−1 of year y + d.</li>
<li>diff ← serial(end) − serial(start). If diff ≤ 0 print "INVALID INPUT" and stop.</li>
<li>Input the weekday name of the 1st of the start month (and of the end month if it is a different month);
convert to 0 (Sunday) … 6 (Saturday); if not a weekday name print "INVALID WEEKDAY" and stop.</li>
<li>Print "No of days between start date and end date: diff days".</li>
<li>For each month: print the month and year and the heading SUN … SAT; print f blank cells (f = weekday of the
1st); print 1 … days(month) in cells, starting a new line (and a dashed rule) after every 7th cell.</li>
<li>Stop.</li></ol>
<p><b>Program</b></p>""" + jcode(M, "DateCalendar.java") +
      r"<p><b>Output — the paper's example</b></p>" + jout(M, "date1") +
      r"<p><b>Output — further inputs</b> (dates in different years across a leap February; an invalid date)</p>" +
      jout(M, "date2") + jout(M, "date3"),
      topic="Arrays, Strings (date / calendar programs)",
      recall=r"<ul><li>Leap year: divisible by 400, or by 4 but not by 100.</li><li>Days between = serial(end) − serial(start) (start counted, end not).</li><li>Validate before computing.</li></ul>"),

    Q("2", 20, r"""<p><b>QUESTION 2</b><br>Write a Program in Java to input a number and check whether it is a Bouncy Number or not.</p>
<p><b>Increasing Number:</b> Working from left-to-right if no digit is exceeded by the digit to its left it is called an
increasing number; for example, 556778.</p>
<p><b>Decreasing Number:</b> Similarly if no digit is exceeded by the digit to its right it is called a decreasing number;
for example, 663320.</p>
<p><b>Bouncy Number:</b> A positive integer that is neither increasing nor decreasing is a "bouncy" number; for example,
29748. There cannot be any bouncy number below 100.</p>""",
      a=PRAC_NOTE + r"""<p><b>Algorithm</b></p>
<ol><li>Start. Input n; if n ≤ 0 print "INVALID INPUT" and stop. s ← n as a string.</li>
<li>inc ← true; for i = 1 to len(s) − 1: if s[i] &lt; s[i−1], inc ← false.</li>
<li>dec ← true; for i = 0 to len(s) − 2: if s[i] &lt; s[i+1], dec ← false.</li>
<li>If not inc and not dec, print "n is a Bouncy Number"; otherwise print "n is NOT a Bouncy Number" (with the
reason: increasing, decreasing, or all digits equal). Stop.</li></ol>
<p><b>Program</b></p>""" + jcode(M, "Bouncy.java") +
      r"<p><b>Output — the paper's three examples</b></p>" + jout(M, "bouncy1") + jout(M, "bouncy2") + jout(M, "bouncy3") +
      r"<p><b>Output — further inputs</b> (101, the smallest bouncy number; 7777, both increasing and decreasing)</p>" +
      jout(M, "bouncy4") + jout(M, "bouncy5"),
      topic="Methods (number programs)",
      recall=r"<ul><li>Compare each digit with its neighbour; a single violation decides.</li><li>A one- or two-digit number is always increasing or decreasing, so never bouncy.</li></ul>"),

    Q("3", 20, r"""<p><b>QUESTION 3</b><br>Given an array of integers, find the indices of the pair of integers that have the smallest
difference between them based on the following conditions:</p>
<ol><li>The actual difference between two elements (not their indices)</li>
<li>The pair with the lower first index (if the difference is the same between two pairs).</li>
<li>The pair with the lower second index (if the first indices are the same between two pairs and if the difference
between the elements is same).</li></ol>
<p><b>Sample Input 1</b><br>Consider an array {5, 3, 21, 10, 12, 7}<br>The distance between various pair of elements is
shown in the following figure.</p>{{fig:0}}
<p>The pairs [5,3], [10,12] have the difference 2. But the minimum valued pair is [5,3]. Therefore the index of
element 5 is 0 and 3 is 1.</p><p><b>Sample Output 1</b><br>The indices are 0, 1.</p>
<p><b>Sample Input 2</b><br>Consider an array {19, 0, -5, 4, 7, 10}<br>The distance between the pair of elements is
shown in the following figure.</p>{{fig:1}}
<p>The pairs [4,7], [7,10] have the difference 3. But the minimum valued pair is [4,7]. Therefore the index of
element 4 is 3 and 7 is 4.</p><p><b>Sample Output 2</b><br>The indices are 3, 4.</p>""",
      qfig=[F.fig_p2q3_pairs1, F.fig_p2q3_pairs2],
      a=PRAC_NOTE + r"""<p><b>Reading the problem.</b> The tables show only neighbouring pairs, but condition 3 ("the lower
second index if the first indices are the same") only makes sense if <i>any</i> two elements may form a pair, so all
pairs (i, j) with i &lt; j are compared, using the absolute difference. Sample 1 itself needs rule 3: over all
pairs, 5 and 7 (indices 0, 5) also differ by 2, and rule 3 picks 0, 1 over 0, 5. Both samples give the printed answer.
Scanning i upwards and, for each i, j upwards, and replacing the best pair only on a <i>strictly</i> smaller
difference, automatically applies the tie-break rules 2 and 3.</p>
<p><b>Algorithm</b></p>
<ol><li>Start. Input n; if n &lt; 2 print "INVALID INPUT" and stop. Input a[0..n−1].</li>
<li>best ← |a[0] − a[1]|, bi ← 0, bj ← 1.</li>
<li>For i = 0 to n−2, for j = i+1 to n−1: d ← |a[i] − a[j]|; if d &lt; best then best ← d, bi ← i, bj ← j.</li>
<li>Print "The indices are bi, bj." Stop.</li></ol>
<p><b>Program</b></p>""" + jcode(M, "MinDiff.java") +
      r"<p><b>Output — the paper's samples</b></p>" + jout(M, "pair1") + jout(M, "pair2") +
      r"""<p><b>Output — a further input</b> {40, 12, 31, 15, 29}: 31 and 29 (indices 2, 4) differ by 2, the smallest
of all pairs (12 and 15 differ by 3). Note that comparing only neighbours would wrongly give 3, 4.</p>""" +
      jout(M, "pair3"),
      topic="Arrays (single-dimensional)",
      recall=r"<ul><li>All pairs: nested loops i &lt; j, O(n²).</li><li>Use <code>Math.abs</code> for the actual difference.</li><li>A strict &lt; keeps the earliest pair on ties.</li></ul>"),
]

PAPER = dict(
    subject="computers",
    year="2016-17",
    slug="2016-17-paper-2",
    paper="Paper 2 (Practical)",
    source="PreBoard-PYQ/2016-17/COMPUTER SCIENCE PAPER II.pdf",
    marks=30, time="3 hours",
    practical=True,
    intro=r"""<p>(Candidates are allowed additional 15 minutes for only reading the paper. They must NOT start writing during
this time.)</p>
<p><b>The total time to be spent on the Planning session and Examination session is Three hours</b><br>
<i>Planning Session: 90 minutes</i><br><i>Examination Session: 90 minutes</i><br>
<b>Note : Candidates are to be permitted to proceed to the Examination Session <u>only after</u> the 90 minutes of the
planning session are over.</b></p>
<p><i>This paper consists of <b>three</b> problems from which candidates are required to attempt <b>any one</b> problem.</i></p>
<p><b>Candidates are expected to do the following:</b></p>
<ol><li>Write an algorithm for the selected problem. (Algorithm should be expressed clearly using any standard scheme
such as pseudo code or in steps which are simple enough to be obviously computable.) [3]</li>
<li>Write a program in <b>JAVA</b> language. The program should follow the algorithm and should be logically and
syntactically correct. [5]</li>
<li>Document the program using mnemonic names/ comments, identifying and clearly describing the choice of data types
and meaning of variables. [2]</li>
<li>Code/Type the program on the computer and get a printout (Hard Copy). Typically, this should be a program that
compiles and runs correctly. [2]</li>
<li>Test run the program on the computer using the given sample data and get a printout of the output in the format
specified in the problem. [5]</li>
<li>Viva-Voce on the <b><u>Selected Problem.</u></b> [3]</li></ol>
<p><b>Project File – [10]</b></p><p>This question paper consists of four printed pages.</p>
<p class="note">Each problem is worth the 20 marks of items 1–6; the remaining 10 are for the project file.</p>""",
    items=ITEMS,
)

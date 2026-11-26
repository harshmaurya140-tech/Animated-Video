# Six-Scene Storyboard
## Gaussian Elimination: Solving Three Unknowns Using Matrix Row Operations

**Learning objective:** By the end of the video, the viewer will be able to convert a 3 × 3 linear system into an augmented matrix, apply elementary row operations to obtain upper triangular form, and solve the system using back substitution.

| Scene | Target time | Visual plan | Mathematics / narration goal |
|---|---:|---|---|
| 1. Hook / Context | 25 sec | Title, then three equations appear one by one. | Ask how three unknowns can be found systematically. Introduce the system. |
| 2. Concept Introduction | 40 sec | Equations move into an augmented matrix; coefficient and constant columns are visually separated. | Define Gaussian elimination as a sequence of elementary row operations that creates zeros below pivots while preserving the solution set. |
| 3. Visual Intuition | 45 sec | Highlight the first pivot and show the entries below it as targets for elimination. | Explain pivots and why zeros are created below them. |
| 4. Worked Example | 150 sec | Matrix changes after each operation. Display one operation label at a time. | Show each arithmetic step clearly: scale row 2, replace row 2, replace row 3, then eliminate the second-column entry. |
| 5. Interpretation | 35 sec | Reveal the bottom equation first, then move upward through the system. | Explain upper triangular form and back substitution. |
| 6. Summary & Credits | 25 sec | Show the boxed solution and three key takeaways. End with credits and AI disclosure. | Recap augmented matrix, elimination, and back substitution. |

**Target total:** approximately 5 minutes 20 seconds. Adjust pauses and narration during editing, and keep the final video below the strict 7-minute maximum.

## Worked example

Solve:

\[
2x+y-z=8,\quad -3x-y+2z=-11,\quad -2x+y+2z=-3
\]

Initial augmented matrix:

\[
\left[\begin{array}{rrr|r}
2&1&-1&8\\
-3&-1&2&-11\\
-2&1&2&-3
\end{array}\right]
\]

Apply:
- \(R_2\rightarrow 2R_2\)
- \(R_2\rightarrow R_2+3R_1\)
- \(R_3\rightarrow R_3+R_1\)
- \(R_3\rightarrow R_3-2R_2\)

Upper triangular matrix:

\[
\left[\begin{array}{rrr|r}
2&1&-1&8\\
0&1&1&2\\
0&0&-1&1
\end{array}\right]
\]

Back substitution:
- \(-z=1\Rightarrow z=-1\)
- \(y+z=2\Rightarrow y=3\)
- \(2x+y-z=8\Rightarrow x=2\)

**Final answer:** \(x=2,\ y=3,\ z=-1\).

## Production notes

- Use a consistent palette: navy for mathematics, blue for operation labels, teal for pivots/highlights, green for the final answer.
- Keep equations large enough to read at 1080p.
- Animate one operation at a time. Do not skip intermediate matrices.
- Include an opening frame with project title, student name, and student ID.
- Include a closing frame with summary, references, music credits (if applicable), and AI disclosure.

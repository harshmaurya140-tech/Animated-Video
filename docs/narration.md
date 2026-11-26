# Voice-over Narration
## Gaussian Elimination: Solving Three Unknowns Using Matrix Row Operations

**Target duration:** approximately 5 minutes 20 seconds at a measured pace.  
**Note:** The timings are guides. Pause while the corresponding matrix operations appear.

### Scene 1 — Hook / Context (about 25 seconds)

Imagine you are given three equations containing three unknowns: x, y, and z. Solving them by substitution can become lengthy, especially when the numbers get complicated. Is there a systematic method that can organize the calculations and lead us to the answer? One such method is called Gaussian elimination. In this video, we will use it to solve a three-variable system, one row operation at a time.

### Scene 2 — Concept Introduction (about 40 seconds)

Gaussian elimination is a method for solving systems of linear equations. The main idea is to rewrite the system as an augmented matrix and then use elementary row operations to create zeros below the leading entries, which are called pivots.

An augmented matrix contains the coefficients of the variables and a final column containing the constants. The vertical line separates these two parts.

The important point is that the allowed elementary row operations preserve the solution set. These operations are swapping two rows, multiplying a row by a non-zero constant, and adding a multiple of one row to another row.

### Scene 3 — Visual Intuition (about 45 seconds)

We begin with the first column. Its leading entry, two, is our first pivot. We want the entries below this pivot to become zero.

Why? Because zeros make the system easier to solve. After eliminating the entries below the first pivot, we move to the second column and repeat the process.

This creates an upper triangular matrix. In this form, the bottom row contains only one variable, so we can solve it first and then work upward.

### Scene 4 — Worked Example (about 150 seconds)

Let's solve this system:

Two x plus y minus z equals eight.

Negative three x minus y plus two z equals negative eleven.

Negative two x plus y plus two z equals negative three.

First, write the coefficients and constants as an augmented matrix.

Our first pivot is two. To eliminate the negative three beneath it, we first multiply row two by two. This gives negative six, negative two, four, and negative twenty-two.

Now add three times row one to row two. The first entry becomes zero, the second becomes one, the third becomes one, and the constant becomes two.

Next, eliminate the negative two in the first column of row three. Add row one to row three. The new third row is zero, two, one, and five.

We have now cleared the entries below the first pivot.

Next, look at the second pivot, which is one in row two. We need to eliminate the two directly beneath it.

Subtract two times row two from row three. The third row becomes zero, zero, negative one, and one.

Our matrix is now in upper triangular form. Notice the zeros below the main diagonal. This is the key structure produced by Gaussian elimination.

### Scene 5 — Interpretation / Back Substitution (about 35 seconds)

Now we use back substitution.

The bottom row tells us that negative z equals one. Therefore, z equals negative one.

The second row gives y plus z equals two. Substituting negative one gives y equals three.

Finally, the first row gives two x plus y minus z equals eight. Substituting y equals three and z equals negative one gives two x plus four equals eight. Therefore, x equals two.

### Scene 6 — Summary & Credits (about 25 seconds)

We have found the solution: x equals two, y equals three, and z equals negative one.

Remember the three main steps: convert the equations into an augmented matrix, use elementary row operations to create zeros below the pivots, and apply back substitution.

That is Gaussian elimination: a systematic way to solve a system of linear equations.

**Closing credit:** M3 Educational Animation Project. Created using Python Manim. Add your name, student ID, references, and an accurate AI-tools disclosure here.

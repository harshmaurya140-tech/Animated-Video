
from manim import *


class GaussianElimination(Scene):

    def construct(self):

        # ==========================================
        # SCENE 1: INTRODUCTION
        # ==========================================

        title = Text(
            "GAUSSIAN ELIMINATION",
            font_size=42,
            color=BLUE_B,
            weight=BOLD
        )

        subtitle = Text(
            "Solving a system of linear equations",
            font_size=25,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.4)

        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(3)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            run_time=1.5
        )

        # ==========================================
        # SCENE 2: THE PROBLEM
        # ==========================================

        heading = Text(
            "The Problem",
            font_size=38,
            color=BLUE_B
        ).to_edge(UP)

        equations = VGroup(
            MathTex(r"x+y+z=6", font_size=42),
            MathTex(r"2x+3y+z=11", font_size=42),
            MathTex(r"x+2y+3z=14", font_size=42)
        ).arrange(DOWN, buff=0.45)

        self.play(Write(heading))
        self.play(
            LaggedStart(
                *[Write(eq) for eq in equations],
                lag_ratio=0.5
            ),
            run_time=3
        )

        explanation = Text(
            "Our goal is to find the values of x, y and z.",
            font_size=25,
            color=GRAY_B
        ).to_edge(DOWN, buff=0.8)

        self.play(FadeIn(explanation))
        self.wait(4)

        self.play(
            FadeOut(heading),
            FadeOut(equations),
            FadeOut(explanation)
        )

        # ==========================================
        # SCENE 3: AUGMENTED MATRIX
        # ==========================================

        heading = Text(
            "Step 1: Form the Augmented Matrix",
            font_size=34,
            color=BLUE_B
        ).to_edge(UP)

        matrix1 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"1&1&1&6\\"
            r"2&3&1&11\\"
            r"1&2&3&14"
            r"\end{array}\right]",
            font_size=54
        )

        explanation = Text(
            "Each row represents one equation.",
            font_size=26,
            color=GRAY_B
        ).next_to(matrix1, DOWN, buff=0.7)

        self.play(Write(heading))
        self.play(Write(matrix1), run_time=2.5)
        self.play(FadeIn(explanation))
        self.wait(4)

        self.play(
            FadeOut(heading),
            FadeOut(matrix1),
            FadeOut(explanation)
        )

        # ==========================================
        # SCENE 4: FIRST ROW OPERATION
        # ==========================================

        heading = Text(
            "Step 2: Eliminate the First Column",
            font_size=34,
            color=BLUE_B
        ).to_edge(UP)

        operation = MathTex(
            r"R_2 \rightarrow R_2-2R_1",
            font_size=38,
            color=YELLOW
        ).next_to(heading, DOWN, buff=0.6)

        matrix2 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"1&1&1&6\\"
            r"0&1&-1&-1\\"
            r"1&2&3&14"
            r"\end{array}\right]",
            font_size=52
        ).move_to(ORIGIN)

        explanation = Text(
            "Subtract twice the first row from the second row.",
            font_size=24,
            color=GRAY_B
        ).to_edge(DOWN, buff=0.8)

        self.play(Write(heading))
        self.play(Write(operation))
        self.play(Write(matrix2), run_time=2.5)
        self.play(FadeIn(explanation))
        self.wait(4)

        self.play(
            FadeOut(heading),
            FadeOut(operation),
            FadeOut(matrix2),
            FadeOut(explanation)
        )

        # ==========================================
        # SCENE 5: SECOND ROW OPERATION
        # ==========================================

        heading = Text(
            "Eliminate the First Entry of Row 3",
            font_size=34,
            color=BLUE_B
        ).to_edge(UP)

        operation = MathTex(
            r"R_3 \rightarrow R_3-R_1",
            font_size=38,
            color=YELLOW
        ).next_to(heading, DOWN, buff=0.6)

        matrix3 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"1&1&1&6\\"
            r"0&1&-1&-1\\"
            r"0&1&2&8"
            r"\end{array}\right]",
            font_size=52
        )

        explanation = Text(
            "Subtract the first row from the third row.",
            font_size=25,
            color=GRAY_B
        ).to_edge(DOWN, buff=0.8)

        self.play(Write(heading))
        self.play(Write(operation))
        self.play(Write(matrix3), run_time=2.5)
        self.play(FadeIn(explanation))
        self.wait(4)

        self.play(
            FadeOut(heading),
            FadeOut(operation),
            FadeOut(matrix3),
            FadeOut(explanation)
        )

        # ==========================================
        # SCENE 6: THIRD ROW OPERATION
        # ==========================================

        heading = Text(
            "Eliminate the Second Entry of Row 3",
            font_size=32,
            color=BLUE_B
        ).to_edge(UP)

        operation = MathTex(
            r"R_3 \rightarrow R_3-R_2",
            font_size=38,
            color=YELLOW
        ).next_to(heading, DOWN, buff=0.6)

        matrix4 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"1&1&1&6\\"
            r"0&1&-1&-1\\"
            r"0&0&3&9"
            r"\end{array}\right]",
            font_size=52
        )

        explanation = Text(
            "The entries below the main diagonal are now zero.",
            font_size=24,
            color=GRAY_B
        ).to_edge(DOWN, buff=0.8)

        self.play(Write(heading))
        self.play(Write(operation))
        self.play(Write(matrix4), run_time=2.5)
        self.play(FadeIn(explanation))
        self.wait(4)

        self.play(
            FadeOut(heading),
            FadeOut(operation),
            FadeOut(matrix4),
            FadeOut(explanation)
        )

        # ==========================================
        # SCENE 7: ROW ECHELON FORM
        # ==========================================

        heading = Text(
            "Step 3: Row Echelon Form",
            font_size=36,
            color=BLUE_B
        ).to_edge(UP)

        echelon = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"1&1&1&6\\"
            r"0&1&-1&-1\\"
            r"0&0&3&9"
            r"\end{array}\right]",
            font_size=55
        )

        explanation = Text(
            "The matrix is now in row echelon form.",
            font_size=27,
            color=GREEN_B
        ).next_to(echelon, DOWN, buff=0.7)

        self.play(Write(heading))
        self.play(Write(echelon), run_time=2.5)
        self.play(FadeIn(explanation))
        self.wait(5)

        self.play(
            FadeOut(heading),
            FadeOut(echelon),
            FadeOut(explanation)
        )

        # ==========================================
        # SCENE 8: BACK SUBSTITUTION
        # ==========================================

        heading = Text(
            "Step 4: Back Substitution",
            font_size=36,
            color=BLUE_B
        ).to_edge(UP)

        eq1 = MathTex(
            r"3z=9 \quad \Rightarrow \quad z=3",
            font_size=38
        )

        eq2 = MathTex(
            r"y-z=-1 \quad \Rightarrow \quad y=2",
            font_size=38
        )

        eq3 = MathTex(
            r"x+y+z=6 \quad \Rightarrow \quad x=1",
            font_size=38
        )

        steps = VGroup(eq1, eq2, eq3).arrange(
            DOWN,
            buff=0.8
        )

        self.play(Write(heading))

        self.play(Write(eq1), run_time=2)
        self.wait(2)

        self.play(Write(eq2), run_time=2)
        self.wait(2)

        self.play(Write(eq3), run_time=2)
        self.wait(4)

        self.play(
            FadeOut(heading),
            FadeOut(steps)
        )

        # ==========================================
        # SCENE 9: FINAL ANSWER
        # ==========================================

        heading = Text(
            "The Final Solution",
            font_size=40,
            color=BLUE_B
        ).to_edge(UP)

        answer = MathTex(
            r"\boxed{x=1,\quad y=2,\quad z=3}",
            font_size=52,
            color=GREEN_B
        )

        self.play(Write(heading))
        self.play(
            FadeIn(answer, scale=1.2),
            run_time=2
        )
        self.wait(5)

        self.play(
            FadeOut(heading),
            FadeOut(answer)
        )

        # ==========================================
        # SCENE 10: VERIFICATION
        # ==========================================

        heading = Text(
            "Step 5: Verify the Solution",
            font_size=36,
            color=BLUE_B
        ).to_edge(UP)

        check1 = MathTex(
            r"1+2+3=6",
            font_size=38
        )

        check2 = MathTex(
            r"2(1)+3(2)+3=11",
            font_size=38
        )

        check3 = MathTex(
            r"1+2(2)+3(3)=14",
            font_size=38
        )

        checks = VGroup(
            check1,
            check2,
            check3
        ).arrange(DOWN, buff=0.65)

        success = Text(
            "All three equations are satisfied!",
            font_size=27,
            color=GREEN_B
        ).to_edge(DOWN, buff=0.8)

        self.play(Write(heading))
        self.play(Write(check1))
        self.wait(1.5)

        self.play(Write(check2))
        self.wait(1.5)

        self.play(Write(check3))
        self.wait(2)

        self.play(FadeIn(success))
        self.wait(4)

        self.play(
            FadeOut(heading),
            FadeOut(checks),
            FadeOut(success)
        )

        # ==========================================
        # SCENE 11: CONCLUSION
        # ==========================================

        heading = Text(
            "What We Learned",
            font_size=40,
            color=BLUE_B
        ).to_edge(UP)

        points = VGroup(
            Text("1. Convert equations into an augmented matrix.",
                 font_size=25),
            Text("2. Apply elementary row operations.",
                 font_size=25),
            Text("3. Obtain row echelon form.",
                 font_size=25),
            Text("4. Use back substitution to find the solution.",
                 font_size=25)
        ).arrange(DOWN, buff=0.55)

        self.play(Write(heading))

        for point in points:
            self.play(
                FadeIn(point, shift=UP * 0.2),
                run_time=1.2
            )
            self.wait(1.5)

        self.wait(3)

        self.play(
            FadeOut(heading),
            FadeOut(points),
            run_time=1.5
        )

        # ==========================================
        # SCENE 12: ENDING
        # ==========================================

        ending = Text(
            "THANK YOU",
            font_size=52,
            color=GREEN_B,
            weight=BOLD
        )

        ending_subtitle = Text(
            "Gaussian Elimination",
            font_size=27,
            color=GRAY_B
        ).next_to(ending, DOWN, buff=0.5)

        self.play(Write(ending), run_time=2)
        self.play(FadeIn(ending_subtitle))
        self.wait(5)


from manim import *

# M3 Educational Animation Project
# Topic: Gaussian Elimination
# Render: manim -pqh src/gaussian_elimination.py GaussianElimination
# For 1080p: manim -p -r 1920,1080 src/gaussian_elimination.py GaussianElimination

class GaussianElimination(Scene):
    def construct(self):
        # Clean academic palette
        BG = "#F7F9FC"
        NAVY = "#14213D"
        BLUE = "#2563EB"
        TEAL = "#0F9D9A"
        GREY = "#526078"
        GREEN = "#16803C"
        RED = "#C2413B"

        self.camera.background_color = BG

        def heading(title, subtitle=None):
            title_mob = Text(title, font_size=34, color=NAVY, weight=BOLD)
            title_mob.to_edge(UP, buff=0.42)
            self.play(FadeIn(title_mob, shift=DOWN * 0.15), run_time=0.7)
            if subtitle:
                sub = Text(subtitle, font_size=19, color=GREY)
                sub.next_to(title_mob, DOWN, buff=0.16)
                self.play(FadeIn(sub), run_time=0.45)
                return VGroup(title_mob, sub)
            return title_mob

        def matrix_tex(rows, font_size=35):
            # rows is a list of strings, each containing a LaTeX row.
            body = " ".join(rows)
            return MathTex(
                r"\left[\begin{array}{rrr|r}",
                body,
                r"\end{array}\right]",
                font_size=font_size,
                color=NAVY
            )

        def op_label(text, color=BLUE):
            mob = Text(text, font_size=23, color=color, weight=MEDIUM)
            mob.to_edge(DOWN, buff=0.65)
            return mob

        # ------------------------------------------------------------
        # Scene 1: Hook / context
        # ------------------------------------------------------------
        title = Text("GAUSSIAN ELIMINATION", font_size=42, color=NAVY, weight=BOLD)
        subtitle = Text("Solving three unknowns, one row at a time", font_size=25, color=BLUE)
        title.move_to(UP * 1.0)
        subtitle.next_to(title, DOWN, buff=0.3)

        equations = MathTex(
            r"2x+y-z=8",
            r"-3x-y+2z=-11",
            r"-2x+y+2z=-3",
            font_size=34,
            color=NAVY
        ).arrange(DOWN, buff=0.35)
        equations.move_to(DOWN * 0.85)

        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(subtitle, shift=UP * 0.15), run_time=0.8)
        self.play(LaggedStart(*[Write(eq) for eq in equations], lag_ratio=0.25), run_time=2.5)
        hook = Text("Can we find x, y and z systematically?", font_size=24, color=TEAL)
        hook.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(hook), run_time=0.6)
        self.wait(2)
        self.play(FadeOut(VGroup(title, subtitle, equations, hook)), run_time=0.8)

        # ------------------------------------------------------------
        # Scene 2: Concept introduction
        # ------------------------------------------------------------
        h = heading("1. The idea", "Convert the equations into an augmented matrix")
        eq_small = MathTex(
            r"\begin{aligned}"
            r"2x+y-z&=8\\"
            r"-3x-y+2z&=-11\\"
            r"-2x+y+2z&=-3"
            r"\end{aligned}",
            font_size=29, color=NAVY
        )
        eq_small.move_to(LEFT * 3.2 + DOWN * 0.15)

        arrow = MathTex(r"\longrightarrow", font_size=48, color=BLUE)
        arrow.move_to(ORIGIN + DOWN * 0.1)

        aug = matrix_tex([
            r"2&1&-1&8\\",
            r"-3&-1&2&-11\\",
            r"-2&1&2&-3"
        ], font_size=31)
        aug.move_to(RIGHT * 3.0 + DOWN * 0.1)

        note = Text("The vertical bar separates coefficients from constants.", font_size=19, color=GREY)
        note.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(eq_small), run_time=1)
        self.play(FadeIn(arrow), run_time=0.5)
        self.play(FadeIn(aug), run_time=1)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(2)
        self.play(FadeOut(VGroup(h, eq_small, arrow, aug, note)), run_time=0.8)

        # ------------------------------------------------------------
        # Scene 3: Visual intuition
        # ------------------------------------------------------------
        h = heading("2. What elimination does", "Use pivots to create zeros below the diagonal")
        pivot_text = Text("A pivot is the leading non-zero entry in a row.", font_size=22, color=GREY)
        pivot_text.next_to(h, DOWN, buff=0.55)
        m1 = matrix_tex([
            r"\mathbf{2}&1&-1&8\\",
            r"-3&-1&2&-11\\",
            r"-2&1&2&-3"
        ], font_size=34)
        m1.move_to(UP * 0.05)
        pivot_circle = Circle(radius=0.36, color=TEAL, stroke_width=5).move_to(m1.get_center() + LEFT * 1.37 + UP * 0.83)
        explanation = Text("Start with the first pivot, then remove entries beneath it.", font_size=21, color=BLUE)
        explanation.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(pivot_text), FadeIn(m1), run_time=1)
        self.play(Create(pivot_circle), run_time=0.7)
        self.play(FadeIn(explanation), run_time=0.7)
        self.wait(2)
        self.play(FadeOut(VGroup(h, pivot_text, m1, pivot_circle, explanation)), run_time=0.8)

        # ------------------------------------------------------------
        # Scene 4: Worked example
        # ------------------------------------------------------------
        h = heading("3. Worked example", "Apply elementary row operations step by step")
        current = matrix_tex([
            r"2&1&-1&8\\",
            r"-3&-1&2&-11\\",
            r"-2&1&2&-3"
        ], font_size=36)
        current.move_to(UP * 0.15)
        self.play(FadeIn(current), run_time=0.8)

        # R2 <- 2R2
        label = op_label(r"First:  R_2 \rightarrow 2R_2")
        # Use a MathTex label for proper mathematical notation.
        label_math = MathTex(r"R_2\rightarrow 2R_2", font_size=30, color=BLUE).to_edge(DOWN, buff=0.55)
        next1 = matrix_tex([
            r"2&1&-1&8\\",
            r"-6&-2&4&-22\\",
            r"-2&1&2&-3"
        ], font_size=36).move_to(current)
        self.play(FadeIn(label_math), run_time=0.4)
        self.play(Transform(current, next1), run_time=1.2)
        self.wait(0.7)
        self.play(FadeOut(label_math), run_time=0.3)

        # R2 <- R2 + 3R1
        label_math = MathTex(r"R_2\rightarrow R_2+3R_1", font_size=30, color=BLUE).to_edge(DOWN, buff=0.55)
        next2 = matrix_tex([
            r"2&1&-1&8\\",
            r"0&1&1&2\\",
            r"-2&1&2&-3"
        ], font_size=36).move_to(current)
        self.play(FadeIn(label_math), run_time=0.4)
        self.play(Transform(current, next2), run_time=1.2)
        self.wait(0.7)
        self.play(FadeOut(label_math), run_time=0.3)

        # R3 <- R3 + R1
        label_math = MathTex(r"R_3\rightarrow R_3+R_1", font_size=30, color=BLUE).to_edge(DOWN, buff=0.55)
        next3 = matrix_tex([
            r"2&1&-1&8\\",
            r"0&1&1&2\\",
            r"0&2&1&5"
        ], font_size=36).move_to(current)
        self.play(FadeIn(label_math), run_time=0.4)
        self.play(Transform(current, next3), run_time=1.2)
        self.wait(0.7)
        self.play(FadeOut(label_math), run_time=0.3)

        # R3 <- R3 - 2R2
        label_math = MathTex(r"R_3\rightarrow R_3-2R_2", font_size=30, color=BLUE).to_edge(DOWN, buff=0.55)
        next4 = matrix_tex([
            r"2&1&-1&8\\",
            r"0&1&1&2\\",
            r"0&0&-1&1"
        ], font_size=36).move_to(current)
        self.play(FadeIn(label_math), run_time=0.4)
        self.play(Transform(current, next4), run_time=1.2)
        self.wait(1.2)
        self.play(FadeOut(label_math), run_time=0.3)

        upper_label = Text("Upper triangular form", font_size=24, color=TEAL, weight=BOLD)
        upper_label.next_to(current, DOWN, buff=0.55)
        self.play(FadeIn(upper_label), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(VGroup(h, current, upper_label)), run_time=0.8)

        # ------------------------------------------------------------
        # Scene 5: Interpretation / back substitution
        # ------------------------------------------------------------
        h = heading("4. Back substitution", "Start at the bottom row and work upward")
        rows = VGroup(
            MathTex(r"-z=1\quad\Rightarrow\quad z=-1", font_size=35, color=NAVY),
            MathTex(r"y+z=2\quad\Rightarrow\quad y=3", font_size=35, color=NAVY),
            MathTex(r"2x+y-z=8\quad\Rightarrow\quad x=2", font_size=35, color=NAVY)
        ).arrange(DOWN, buff=0.55)
        rows.move_to(ORIGIN + DOWN * 0.1)
        self.play(Write(rows[0]), run_time=1.2)
        self.play(Write(rows[1]), run_time=1.2)
        self.play(Write(rows[2]), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(VGroup(h, rows)), run_time=0.8)

        # ------------------------------------------------------------
        # Scene 6: Summary and credits
        # ------------------------------------------------------------
        h = heading("5. Final result")
        answer = MathTex(r"\boxed{x=2,\quad y=3,\quad z=-1}", font_size=46, color=GREEN)
        answer.move_to(UP * 0.75)
        summary = VGroup(
            Text("1. Write the system as an augmented matrix.", font_size=22, color=NAVY),
            Text("2. Use row operations to create zeros below each pivot.", font_size=22, color=NAVY),
            Text("3. Use back substitution to find the variables.", font_size=22, color=NAVY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary.next_to(answer, DOWN, buff=0.65)
        credits = Text("M3 Educational Animation Project  |  Created with Python Manim", font_size=16, color=GREY)
        credits.to_edge(DOWN, buff=0.35)

        self.play(Write(answer), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(line, shift=UP * 0.1) for line in summary], lag_ratio=0.3), run_time=2)
        self.play(FadeIn(credits), run_time=0.6)
        self.wait(3)

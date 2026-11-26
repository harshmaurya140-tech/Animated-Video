from manim import *

class TestScene(Scene):
    def construct(self):
        title = Text("Gaussian Elimination", font_size=42)
        matrix = MathTex(
            r"\begin{bmatrix}"
            r"1 & 2 & 1 \\"
            r"2 & 3 & 4 \\"
            r"3 & 5 & 2"
            r"\end{bmatrix}"
        )
        self.play(Write(title))
        self.play(title.animate.shift(UP * 1.5))
        self.play(Write(matrix))
        self.wait(2)

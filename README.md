# Gaussian Elimination | M3 Animation Video Project

**Topic:** Gaussian Elimination  
**Subtitle:** Solving Three Unknowns Using Matrix Row Operations  
**Animation tool:** Python Manim Community Edition  
**Style:** Clean, minimal, academic  
**Target:** Approximately 5 minutes; do not exceed 7 minutes.

## Project structure

```text
Gaussian_Elimination_Manim_Project/
├── src/
│   └── gaussian_elimination.py
├── docs/
│   ├── storyboard.md
│   └── narration.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Install

Use Python 3.10 or newer in a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate       # macOS / Linux
# .venv\Scripts\activate      # Windows

python -m pip install --upgrade pip
pip install -r requirements.txt
```

Manim also requires system dependencies for rendering. Follow the official Manim Community installation guide for your operating system:
https://docs.manim.community/en/stable/installation.html

## Render

From the project root:

```bash
manim -pqh src/gaussian_elimination.py GaussianElimination
```

For a 1080p render:

```bash
manim -p -r 1920,1080 src/gaussian_elimination.py GaussianElimination
```

The rendered MP4 is normally placed under `media/videos/`.

## Mathematical example

The video solves:

```text
2x + y - z = 8
-3x - y + 2z = -11
-2x + y + 2z = -3
```

Augmented matrix:

```text
[  2   1  -1 |   8 ]
[ -3  -1   2 | -11 ]
[ -2   1   2 |  -3 ]
```

Operations:
1. `R2 <- 2R2`
2. `R2 <- R2 + 3R1`
3. `R3 <- R3 + R1`
4. `R3 <- R3 - 2R2`

Result:

```text
[ 2  1  -1 | 8 ]
[ 0  1   1 | 2 ]
[ 0  0  -1 | 1 ]
```

Back substitution gives `z = -1`, `y = 3`, and `x = 2`.

## Important before submission

- Render and watch the complete video. Check every equation, transition, and text placement.
- Record and add your own clear voice-over. This starter project does not generate narration audio.
- Keep the final video 16:9, preferably 1080p, and under 7 minutes.
- Add the final MP4 to the repository, for example `Gaussian_Elimination_Video.mp4`.
- Keep the complete source code and editable project files in the repository.
- Add your name and student ID to the opening frame before final rendering.
- Verify the public GitHub repository in a private/incognito browser window.
- Include the storyboard PDF and any required supporting documents.
- Disclose AI assistance in scripting, coding, visuals, or voice as required by the instructor.
- Be prepared to explain the row operations and the code independently in the Q&A.

## Suggested GitHub repository name

`M3_AnimationVideo_GaussianElimination`

## AI disclosure template

“AI tools were used for assistance with initial planning, script drafting, and code development. The mathematical calculations, final implementation, verification, editing, and narration were reviewed by the student.”

Edit this statement so it accurately describes the tools and work you actually used.

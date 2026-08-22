def create_harshit_vector_svg():
    # Clean, modern geometric uppercase bold paths for H A R S H I T
    # Total viewBox height: 30
    # Each letter height: 26 (y from 2 to 28), stroke width: 4.5
    # Letter 1: H -> (x: 0..16)
    # Letter 2: A -> (x: 23..39)
    # Letter 3: R -> (x: 46..62)
    # Letter 4: S -> (x: 69..85)
    # Letter 5: H -> (x: 92..108)
    # Letter 6: I -> (x: 115..121)
    # Letter 7: T -> (x: 128..144)
    # Total width: ~146
    
    svg = '''<svg width="148" height="30" viewBox="0 0 148 30" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- H -->
  <path d="M2 2V28M14 2V28M2 15H14" stroke="white" stroke-width="4" stroke-linecap="square"/>
  <!-- A -->
  <path d="M22 28L28.5 2L35 28M24 20H33" stroke="white" stroke-width="4" stroke-linecap="square" stroke-linejoin="miter"/>
  <!-- R -->
  <path d="M43 28V2H52C55.3 2 57 3.7 57 7C57 10.3 55.3 12 52 12H43M51 12L57 28" stroke="white" stroke-width="4" stroke-linecap="square" stroke-linejoin="miter"/>
  <!-- S -->
  <path d="M78 4C76 2.5 73.5 2 70.5 2C66.5 2 64 4.5 64 7.5C64 11 67 12.5 71 14C75 15.5 78 17 78 20.5C78 24 75 26.5 70.5 26.5C67 26.5 64.5 25 63 23.5M64 7L64 7.5M77 21L77 21.5" stroke="white" stroke-width="4" stroke-linecap="square"/>
  <!-- H -->
  <path d="M86 2V28M98 2V28M86 15H98" stroke="white" stroke-width="4" stroke-linecap="square"/>
  <!-- I -->
  <path d="M107 2V28" stroke="white" stroke-width="4" stroke-linecap="square"/>
  <!-- T -->
  <path d="M116 2H132M124 2V28" stroke="white" stroke-width="4" stroke-linecap="square"/>
</svg>'''
    with open("public/assets/brand/nav_logo_white.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Vector SVG created successfully for nav_logo_white.svg")

create_harshit_vector_svg()

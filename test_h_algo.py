def test_h_recognition(points):
    total_pts = len(points) // 2
    if total_pts < 10:
        return False, "too few points"

    min_x = min(points[0::2])
    max_x = max(points[0::2])
    min_y = min(points[1::2])
    max_y = max(points[1::2])

    w = max_x - min_x
    h = max_y - min_y

    # Dimensions check
    if w < 0.06 or h < 0.08:
        return False, f"too small: w={w:.3f}, h={h:.3f}"

    aspect = h / w
    if aspect < 0.45 or aspect > 3.2:
        return False, f"bad aspect ratio: {aspect:.2f}"

    mid_y = (min_y + max_y) * 0.5

    left_pts = []
    right_pts = []
    mid_bar_pts = []
    top_mid_pts = []
    bot_mid_pts = []

    left_bound = min_x + w * 0.38
    right_bound = max_x - w * 0.38
    mid_y_low = min_y + h * 0.22
    mid_y_high = max_y - h * 0.22

    for i in range(0, len(points), 2):
        x = points[i]
        y = points[i+1]
        if x <= left_bound:
            left_pts.append(y)
        if x >= right_bound:
            right_pts.append(y)
        if min_x + w * 0.20 <= x <= max_x - w * 0.20:
            if mid_y_low <= y <= mid_y_high:
                mid_bar_pts.append((x, y))
            elif y > max_y - h * 0.15:
                top_mid_pts.append((x, y))
            elif y < min_y + h * 0.15:
                bot_mid_pts.append((x, y))

    if len(left_pts) < 3 or len(right_pts) < 3:
        return False, f"missing stems: left={len(left_pts)}, right={len(right_pts)}"

    left_span = max(left_pts) - min(left_pts)
    right_span = max(right_pts) - min(right_pts)

    if left_span < h * 0.45:
        return False, f"left stem too short: {left_span:.3f} < {h*0.45:.3f}"
    if right_span < h * 0.45:
        return False, f"right stem too short: {right_span:.3f} < {h*0.45:.3f}"

    # Must have points in the horizontal crossbar region
    if len(mid_bar_pts) < 1:
        return False, "missing crossbar"

    # Cannot have top-middle and bottom-middle both filled (like a closed box or O)
    if len(top_mid_pts) >= 4 and len(bot_mid_pts) >= 4 and len(mid_bar_pts) < 2:
        return False, "looks like a circle or box, not H"

    return True, "VALID H"

# Test 1: Single vertical line
line = []
for y in range(0, 100, 5):
    line.extend([0.0, y / 100])
print("Test 1 (Vertical line):", test_h_recognition(line))

# Test 2: Horizontal line
hline = []
for x in range(0, 100, 5):
    hline.extend([x / 100, 0.5])
print("Test 2 (Horizontal line):", test_h_recognition(hline))

# Test 3: Circle (O)
import math
circle = []
for deg in range(0, 360, 10):
    rad = math.radians(deg)
    circle.extend([math.cos(rad)*0.2, math.sin(rad)*0.2])
print("Test 3 (Circle O):", test_h_recognition(circle))

# Test 4: Valid H (continuous single stroke)
h_stroke = []
# Down left
for y in range(30, -31, -5):
    h_stroke.extend([-0.2, y / 100])
# Up to middle and across
for y in range(-30, 1, 5):
    h_stroke.extend([-0.2, y / 100])
for x in range(-20, 21, 5):
    h_stroke.extend([x / 100, 0.0])
# Up right and down right
for y in range(0, 31, 5):
    h_stroke.extend([0.2, y / 100])
for y in range(30, -31, -5):
    h_stroke.extend([0.2, y / 100])
print("Test 4 (Continuous H):", test_h_recognition(h_stroke))

# Test 5: Valid H (multi-stroke: left stem, right stem, crossbar)
h_multi = []
# Left stem
for y in range(30, -31, -5):
    h_multi.extend([-0.2, y / 100])
# Right stem
for y in range(30, -31, -5):
    h_multi.extend([0.2, y / 100])
# Crossbar
for x in range(-20, 21, 5):
    h_multi.extend([x / 100, 0.0])
print("Test 5 (Multi-stroke H):", test_h_recognition(h_multi))

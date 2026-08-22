import math

def analyze_h_gesture(strokes_list, raw_points):
    # strokes_list is a list of strokes, where each stroke is [x0, y0, x1, y1, ...]
    # If single stroke, strokes_list has 1 element. If multi-stroke, has 2, 3, etc.
    
    # 1. Total points check
    total_pts = len(raw_points) // 2
    if total_pts < 12:
        return False, "too few points"

    # 2. Check if whole drawing is just a single straight/diagonal line
    xs = raw_points[0::2]
    ys = raw_points[1::2]
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    
    # Check linear correlation (diagonal line detector)
    sxx = sum((x - mean_x)**2 for x in xs)
    syy = sum((y - mean_y)**2 for y in ys)
    sxy = sum((x - mean_x)*(y - mean_y) for x, y in zip(xs, ys))
    
    if sxx > 1e-5 and syy > 1e-5:
        r_sq = (sxy * sxy) / (sxx * syy)
        # If r_squared is very high (> 0.82) and aspect is around 1, it's just a single diagonal line!
        if r_sq > 0.80:
            return False, f"single diagonal line detected (r^2 = {r_sq:.2f})"

    # 3. Stroke-based identification OR segment-based decomposition
    # Break all strokes into segments
    segments = []
    
    # Extract strokes from strokes_list or by splitting on speed/direction
    active_strokes = [s for s in strokes_list if len(s) >= 4]
    
    # If drawn as 1 continuous stroke, split into segments by sharp corners / vertical-horizontal changes
    if len(active_strokes) <= 1 and len(raw_points) >= 16:
        # Detect direction changes in raw_points
        current_seg = [raw_points[0], raw_points[1]]
        for i in range(2, len(raw_points), 2):
            x, y = raw_points[i], raw_points[i+1]
            current_seg.extend([x, y])
            # Check segment length
            if len(current_seg) >= 8:
                seg_xs = current_seg[0::2]
                seg_ys = current_seg[1::2]
                dx = max(seg_xs) - min(seg_xs)
                dy = max(seg_ys) - min(seg_ys)
                # If segment is clearly vertical or horizontal
                # Keep accumulating
        active_strokes = [raw_points]

    # Find vertical components and horizontal components
    # Divide space into Left (x < midX - gap), Right (x > midX + gap), and Middle
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    w = max_x - min_x
    h = max_y - min_y

    if w < 0.06 or h < 0.08:
        return False, f"too small: w={w:.3f}, h={h:.3f}"
    
    mid_x = (min_x + max_x) * 0.5
    mid_y = (min_y + max_y) * 0.5

    left_pts = [(x, y) for x, y in zip(xs, ys) if x <= min_x + w * 0.35]
    right_pts = [(x, y) for x, y in zip(xs, ys) if x >= max_x - w * 0.35]
    cross_pts = [(x, y) for x, y in zip(xs, ys) if min_x + w * 0.20 <= x <= max_x - w * 0.20 and min_y + h * 0.18 <= y <= max_y - h * 0.18]

    if len(left_pts) < 4:
        return False, f"left stem insufficient: {len(left_pts)}"
    if len(right_pts) < 4:
        return False, f"right stem insufficient: {len(right_pts)}"

    left_ys = [p[1] for p in left_pts]
    right_ys = [p[1] for p in right_pts]

    left_span_y = max(left_ys) - min(left_ys)
    right_span_y = max(right_ys) - min(right_ys)

    left_span_x = max(p[0] for p in left_pts) - min(p[0] for p in left_pts)
    right_span_x = max(p[0] for p in right_pts) - min(p[0] for p in right_pts)

    # Both stems must be predominantly vertical
    if left_span_y < h * 0.48 or right_span_y < h * 0.48:
        return False, f"stems not tall enough: left={left_span_y:.2f}, right={right_span_y:.2f}, h={h:.2f}"

    # Left and right stems must be clearly separated horizontally
    mean_left_x = sum(p[0] for p in left_pts) / len(left_pts)
    mean_right_x = sum(p[0] for p in right_pts) / len(right_pts)
    stem_sep = mean_right_x - mean_left_x
    if stem_sep < w * 0.35 or stem_sep < 0.04:
        return False, f"stems not separated enough: {stem_sep:.3f}"

    # Check crossbar: must have points in the middle band
    if len(cross_pts) < 1:
        return False, "missing horizontal crossbar"

    # Check vertical overlap of stems:
    overlap_min = max(min(left_ys), min(right_ys))
    overlap_max = min(max(left_ys), max(right_ys))
    overlap = max(0, overlap_max - overlap_min)
    if overlap < h * 0.35:
        return False, f"stems do not overlap vertically: {overlap:.2f}"

    return True, "VALID H"


# Tests
print("--- TEST 1: Diagonal line ---")
diag = []
for i in range(30):
    t = i / 29.0
    diag.extend([-0.3 + 0.6*t, 0.3 - 0.6*t])
print("Diagonal line:", analyze_h_gesture([diag], diag))

print("\n--- TEST 2: Single vertical line ---")
vert = []
for i in range(30):
    t = i / 29.0
    vert.extend([0.0, -0.3 + 0.6*t])
print("Vertical line:", analyze_h_gesture([vert], vert))

print("\n--- TEST 3: Multi-stroke H ---")
s1 = [] # left down
for i in range(15):
    t = i / 14.0
    s1.extend([-0.18, 0.25 - 0.5*t])
s2 = [] # right down
for i in range(15):
    t = i / 14.0
    s2.extend([0.18, 0.25 - 0.5*t])
s3 = [] # crossbar
for i in range(15):
    t = i / 14.0
    s3.extend([-0.18 + 0.36*t, 0.0])
all_pts = s1 + s2 + s3
print("Multi-stroke H:", analyze_h_gesture([s1, s2, s3], all_pts))

print("\n--- TEST 4: Continuous H ---")
cont = []
# left down
for i in range(12):
    cont.extend([-0.18, 0.25 - 0.5*(i/11.0)])
# up to mid and cross
for i in range(6):
    cont.extend([-0.18, -0.25 + 0.25*(i/5.0)])
for i in range(10):
    cont.extend([-0.18 + 0.36*(i/9.0), 0.0])
# up right and down right
for i in range(6):
    cont.extend([0.18, 0.25*(i/5.0)])
for i in range(12):
    cont.extend([0.18, 0.25 - 0.5*(i/11.0)])
print("Continuous H:", analyze_h_gesture([cont], cont))

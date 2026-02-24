import math

def solve():
    try:
        line1 = input().split()
        if not line1: return
        r = float(line1[0])
        
        line2 = input().split()
        ax, ay = map(float, line2)
        
        line3 = input().split()
        bx, by = map(float, line3)
    except EOFError:
        return

    # Euclidean distance between A and B
    dist_ab = math.sqrt((ax - bx)**2 + (ay - by)**2)
    
    # Distance from origin to A and B
    da = math.sqrt(ax**2 + ay**2)
    db = math.sqrt(bx**2 + by**2)
    
    # Check if the segment AB intersects the circle
    # We use the dot product to find the closest point on the segment AB to the origin
    # Segment: P(t) = A + t(B-A), 0 <= t <= 1
    dx, dy = bx - ax, by - ay
    t = - (ax * dx + ay * dy) / (dx**2 + dy**2) if (dx**2 + dy**2) != 0 else 0
    
    # Restrict t to the segment [0, 1]
    t = max(0, min(1, t))
    closest_x = ax + t * dx
    closest_y = ay + t * dy
    dist_to_origin = math.sqrt(closest_x**2 + closest_y**2)
    
    if dist_to_origin >= r - 1e-9:
        # Path is not blocked
        print(f"{dist_ab:.10f}")
    else:
        # Path is blocked: Tangent A + Arc + Tangent B
        # Length of tangents
        l1 = math.sqrt(abs(da**2 - r**2))
        l2 = math.sqrt(abs(db**2 - r**2))
        
        # Angles
        angle_a = math.atan2(ay, ax)
        angle_b = math.atan2(by, bx)
        
        # Total central angle
        total_angle = abs(angle_a - angle_b)
        if total_angle > math.pi:
            total_angle = 2 * math.pi - total_angle
            
        # Angles of the tangent parts
        alpha1 = math.acos(r / da)
        alpha2 = math.acos(r / db)
        
        # Arc angle
        arc_angle = total_angle - alpha1 - alpha2
        arc_length = max(0, arc_angle) * r
        
        print(f"{l1 + l2 + arc_length:.10f}")

solve()
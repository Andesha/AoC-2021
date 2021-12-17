# left_x = 20; right_x = 30 + 1
left_x = 211; right_x = 232
# left_y = -10; right_y = -5 + 1
left_y = -124; right_y = -69

def pew(px, py, vx, vy):
    px += vx
    py += vy
    vy -= 1
    if vx != 0:
        vx = (vx - 1) if vx > 0 else (vx + 1)
    return px, py, vx, vy

max_height = 0
valid = 0
for i in range(0, right_x + 1):
    for j in range(left_y, 1000):
        vx, vy = i, j
        px, py = 0, 0
        within_run = 0

        while px <= right_x and py >= left_y:
            px, py, vx, vy = pew(px, py, vx, vy)
            if py > within_run:
                within_run = py
            if px >= left_x and px <= right_x and py >= left_y and py <= right_y:
                valid += 1
                if within_run > max_height:
                    max_height = within_run
                break
            if vx == 0 and px < left_x:
                break

print(max_height)
print(valid)
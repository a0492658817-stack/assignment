def check_stamp(step):
    return step.split()[0] == "stamp"

def move(x, y, step):
    part = step.split()
    if part[0] == "mv":
        x += float(part[1])
        y += float(part[2])
    return x, y

def angle_update(angle, step):
    part = step.split()
    if part[0] == "rotate":
        angle += float(part[1])
        angle = angle % 360
    return angle

def pattern_update(pattern, step):
    part = step.split()
    if part[0] == "set_pattern":
        pattern = part[1]
    return pattern

def color_update(color, step):
    part = step.split()
    if part[0] == "set_color":
        color = part[1]
    return color

def main():
    x, y = 0.0, 0.0
    angle = 0.0
    pattern = "no_pattern"
    color = "black"
    stamped = False
    steps = []

    for i in range(6):  
        steps.append(input())

    for step in steps:
        part = step.split()
        if part[0] == "reset":
            x, y, angle, pattern, color = 0.0, 0.0, 0.0, "no_pattern", "black"
        else:
            x, y = move(x, y, step)
            angle = angle_update(angle, step)
            pattern = pattern_update(pattern, step)
            color = color_update(color, step)

            if check_stamp(step):
                print(f"Stamping... [position: ({x:.2f}, {y:.2f}), rotation: {angle:.2f} degrees, pattern: {pattern}, color: {color}]")
                stamped = True

    if not stamped:
        print("Stamping canceled")

main()


main()


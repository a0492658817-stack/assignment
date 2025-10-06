def check_stamp(step):
    part = step.split()
    return part[0] == "stamp"

def move(x, y, step):
    part = step.split()
    if part[0] == "mv":
        x += float(part[1])
        y += float(part[2])
    return x, y

def Angle(angle, step):
    part = step.split()
    if part[0] == "rotate":
        angle += float(part[1])
        angle %= 360
    return angle

def Pattern(pattern, step):
    part = step.split()
    if part[0] == "set_pattern":
        pattern = part[1]
    return pattern

def Color(color, step):
    part = step.split()
    if part[0] == "set_color":
        color = part[1]
    return color

def reset_state():
    return 0.0, 0.0, 0.0, "no_pattern", "black"

def main():
    x, y = 0.0, 0.0
    angle = 0.0
    pattern = "no_pattern"
    color = "black"
    steps = []

    while True:
        try:
            data = input().strip()
            if not data:
                break
            steps.append(data)
        except EOFError:
            break

    # 是否有 stamp
    has_stamp = False
    for step in steps:
        part = step.split()
        if part[0] == "stamp":
            has_stamp = True

    if not has_stamp:
        print("Stamping canceled")
    else:
        for step in steps:
            part = step.split()
            if part[0] == "reset":
                x, y, angle, pattern, color = reset_state()
            else:
                x, y = move(x, y, step)
                angle = Angle(angle, step)
                pattern = Pattern(pattern, step)
                color = Color(color, step)
            if check_stamp(step):
                print(f"Stamping... [position: ({x:.2f}, {y:.2f}), rotation: {angle:.2f} degrees, pattern: {pattern}, color: {color}]")

main()

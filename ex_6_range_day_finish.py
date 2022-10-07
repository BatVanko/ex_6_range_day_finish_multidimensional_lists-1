def moving(ro, co, dir, steps):
    if dir == 'right':
        return ro, co + steps
    elif dir == 'left':
        return ro, co - steps
    elif dir == 'up':
        return ro - steps, co
    elif dir == 'down':
        return ro + steps, co


def is_inside(r, c, s):
    return 0 <= r < s and 0 <= c < s


matrix = []
first_position_row = 0
first_position_col = 0
sum_targets = 0
targets_positions = []
count_targets = sum_targets
for i in range(5):
    row = input().split()
    for j in range(5):
        if row[j] == 'A':
            first_position_row = i
            first_position_col = j
        elif row[j] == 'x':
            sum_targets += 1
    matrix.append(row)

number_of_commands = int(input())
count_targets = sum_targets
for c in range(number_of_commands):

    commands = input().split()
    command = commands[0]
    if command == 'move':
        direction = commands[1]
        steps = int(commands[2])
        next_row, next_col = moving(first_position_row, first_position_col, direction, steps)
        matrix[first_position_row][first_position_col] = '.'
        if is_inside(next_row, next_col, 5) and matrix[next_row][next_col] == '.':
            first_position_row = next_row
            first_position_col = next_col

    elif command == 'shoot':
        direction = commands[1]
        start_row_shoot_position = first_position_row
        start_col_shoot_position = first_position_col
        while True :
            next_row, next_col = moving(start_row_shoot_position, start_col_shoot_position, direction,1)
            if 0 > next_row or next_row >= 5 or 0 > next_col  or next_col >= 5:
                break
            if matrix [next_row][next_col] == 'x':
                count_targets -= 1
                targets_positions.append([next_row,next_col])
                matrix[next_row][next_col] = '.'
                break
            if count_targets == 0:
                break
            start_row_shoot_position = next_row
            start_col_shoot_position = next_col

if count_targets == 0:
    print(f"Training completed! All {sum_targets} targets hit.")
if count_targets > 0:
    print(f"Training not completed! {count_targets} targets left.")
[print(target) for target in targets_positions ]






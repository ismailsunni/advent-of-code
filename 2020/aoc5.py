# read input
with open("./input5.txt") as f:
    lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]


def parse_seat(seat):
    row_str = seat[:7]
    row_bin = row_str.replace("B", "1").replace("F", "0")
    row = int(row_bin, 2)
    col_str = seat[7:]
    col_bin = col_str.replace("R", "1").replace("L", "0")
    col = int(col_bin, 2)
    return row * 8 + col


seat_ids = [parse_seat(line) for line in lines]
print("number of seat", len(seat_ids))
print("max", max(seat_ids))
for i in range(127 * 8 + 7):
    if (i + 1) in seat_ids and (i - 1) in seat_ids and i not in seat_ids:
        seat_id = i
        break
print("my seat ID", seat_id)

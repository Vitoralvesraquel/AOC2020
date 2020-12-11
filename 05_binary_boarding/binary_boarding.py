
row_total = 128
column_total = 8
id_list = []
with open('boarding_pass_batch.txt') as batch:
    highest_id = None
    for seat_code in batch:
        row = list(range(row_total))
        row_half = row_total // 2
        for row_letter in seat_code[:7]:
            if row_letter == 'F':
                del row[row_half:]
            elif row_letter == 'B':
                del row[:row_half]
            row_half //= 2

        column = list(range(column_total))
        column_half = column_total // 2
        for column_letter in seat_code[7:]:
            if column_letter == 'L':
                del column[column_half:]
            elif column_letter == 'R':
                del column[:column_half]
            column_half //= 2

        seat_id = 8 * row[0] + column[0]
        id_list.append(seat_id)
        if highest_id is None or seat_id > highest_id:
            highest_id = seat_id
print('Highest ID:', highest_id)

for first_id in id_list:
    if first_id != highest_id and first_id + 1 not in id_list:
        print('Your Id:', first_id + 1)

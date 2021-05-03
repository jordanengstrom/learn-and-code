# PV SPACIAL ANALYSIS
# properties: p
# values: v
#
#
#    card1:      v1        v2        v3                   card1:         v1        v2       v3
#             ___________________________                              ___________________________
#         p1 | "diamond"                                            p1    1
#         p2 | "green"                            ====>             p2    1
#         p3 |                   "solid"                            p3                        1
#         p4 |   1                                                  p4    1


SHAPE_MAP = {
    "diamond": 1,
    "squiggle": 2,
    "oval": 3
}

COLOR_MAP = {
    "green": 1,
    "purple": 2,
    "red": 3
}

SHADE_MAP = {
    "solid": 1,
    "striped": 2,
    "outlined": 3
}

NUMBER_MAP = {
    "one": 1,
    "two": 2,
    "three": 3
}


class Card:
    def __init__(self, shape: int, color: int, shade: int, number: int):
        self.shape = shape
        self.color = color
        self.shade = shade
        self.number = number


def construct_grids(cards: list):
    c1 = cards[0]
    c2 = cards[1]
    c3 = cards[2]

    # grid = []
    #
    # # row 1
    # row = []
    # for v in SHAPE_MAP.values():
    #     if v == c1.shape:
    #         row.append(1)
    #     else:
    #         row.append(0)
    # grid.append(row)
    #
    # # row 2
    # row = []
    # for v in COLOR_MAP.values():
    #     if v == c1.color:
    #         row.append(1)
    #     else:
    #         row.append(0)
    # grid.append(row)
    #
    # # row 3
    # row = []
    # for v in SHADE_MAP.values():
    #     if v == c1.shade:
    #         row.append(1)
    #     else:
    #         row.append(0)
    # grid.append(row)
    #
    # # row 4
    # row = []
    # for v in NUMBER_MAP.values():
    #     if v == c1.number:
    #         row.append(1)
    #     else:
    #         row.append(0)
    # grid.append(row)

    c1_grid = [
        [1 if v == c1.shape else 0 for v in list(SHAPE_MAP.values())],
        [1 if v == c1.color else 0 for v in list(COLOR_MAP.values())],
        [1 if v == c1.shade else 0 for v in list(SHADE_MAP.values())],
        [1 if v == c1.number else 0 for v in list(NUMBER_MAP.values())]
    ]

    c2_grid = [
        [1 if v == c2.shape else 0 for v in SHAPE_MAP.values()],
        [1 if v == c2.color else 0 for v in COLOR_MAP.values()],
        [1 if v == c2.shade else 0 for v in SHADE_MAP.values()],
        [1 if v == c2.number else 0 for v in NUMBER_MAP.values()]
    ]

    c3_grid = [
        [1 if v == c3.shape else 0 for v in SHAPE_MAP.values()],
        [1 if v == c3.color else 0 for v in COLOR_MAP.values()],
        [1 if v == c3.shade else 0 for v in SHADE_MAP.values()],
        [1 if v == c3.number else 0 for v in NUMBER_MAP.values()]
    ]

    return [c1_grid, c2_grid, c3_grid]


def grid_overlay(grids: list):
    c1_grid = grids[0]
    c2_grid = grids[1]
    c3_grid = grids[2]

    master_grid = []
    for j in range(0, 4):
        for i in range(0, 3):
            row = [c1_grid[j][i] + c2_grid[j][i] + c3_grid[j][i] for i in range(0, 3)]
        master_grid.append(row)

    return master_grid


def validate_set(cards: list):
    # Three main steps:

    # Step 1: Create boolean grid
    grids = construct_grids(cards=cards)

    # Step 2: Consolidate/overlay the grids
    master_grid = grid_overlay(grids)

    # Step 3: Check each row for doubles
    for row in master_grid:
        if 2 in row:
            return False
    return True


def main():
    # known set:
    card1 = Card(1, 1, 3, 1)  # diamond, green, solid, one
    card2 = Card(1, 3, 3, 2)  # diamond, red, solid, two
    # card3 = Card(1, 2, 3, 3)  # diamond, purple, solid, three

    # known non-set
    card3 = Card(2, 2, 2, 2)  # squiggle, purple, striped, two

    chosen_set = [card1, card2, card3]

    is_chosen_set_valid = validate_set(cards=chosen_set)
    print(is_chosen_set_valid)


if __name__ == '__main__':
    main()

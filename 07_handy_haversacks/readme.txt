--- Day 7: Handy Haversacks ---

Many rules (input.txt) are being enforced about bags and their contents; bags must
be color-coded and must contain specific quantities of other color-coded bags.

    Part 1: How many bag colors can eventually contain at least one shiny gold bag?

    Part 2: How many individual bags are required inside your single shiny gold bag?

example:
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.

    Bags that can contain my_bag: 4
        A bright white bag, which can hold your shiny gold bag directly.
        A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
        A dark orange bag, which can hold bright white and muted yellow bags, either of which
            could then hold your shiny gold bag.
        A light red bag, which can hold bright white and muted yellow bags, either of which
            could then hold your shiny gold bag.

    Bags required inside my_bag: 32
        A single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus
        2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!
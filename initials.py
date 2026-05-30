# File: initials.py

# Description: Print out my initials in stylized large letters.

# Assignment Number: 1

# 

# Name: Cobbina David

# STUDENT ID:  2425403622

# Email: 2425403622@live.gctu.edu.gh

# Grader: Emma

# 

# On my honor, Cobbina David, this programming assignment is my own work

# and I have not provided this code to any other student.

def main():
    # Print initials CDB in large block letters made of their respective letters,
    # each 12 wide by 10 high, followed by a large period of 4 asterisks (2x2 block),
    # with 3 periods as padding columns on each side.
    print()
    print("...CDB")
    print()

    # Layout: ...[12 letter][4 period_col]...[12 letter][4 period_col]...[12 letter][4 period_col]...
    # Total = 3+12+4+3+12+4+3+12+4+3 = 60
    # The large period is a 2x2 block of ** at the bottom-right of the 4-wide period column
    # Rows 0-7: period column is "...."
    # Rows 8-9: period column is "**" + ".." giving 2 cols of asterisks at bottom

    # Row 0
    print("..." + "CCCCCCCCCCCC" + "...." + "..." + "DDDDDDDDDD.." + "...." + "..." + "BBBBBBBBBB.." + "...." + "...")
    # Row 1
    print("..." + "CC.........." + "...." + "..." + "DD.......DDD" + "...." + "..." + "BB.......BBB" + "...." + "...")
    # Row 2
    print("..." + "CC.........." + "...." + "..." + "DD........DD" + "...." + "..." + "BB........BB" + "...." + "...")
    # Row 3
    print("..." + "CC.........." + "...." + "..." + "DD........DD" + "...." + "..." + "BB........BB" + "...." + "...")
    # Row 4
    print("..." + "CC.........." + "...." + "..." + "DD........DD" + "...." + "..." + "BBBBBBBBBB.." + "...." + "...")
    # Row 5
    print("..." + "CC.........." + "...." + "..." + "DD........DD" + "...." + "..." + "BBBBBBBBBB.." + "...." + "...")
    # Row 6
    print("..." + "CC.........." + "...." + "..." + "DD........DD" + "...." + "..." + "BB........BB" + "...." + "...")
    # Row 7
    print("..." + "CC.........." + "...." + "..." + "DD........DD" + "...." + "..." + "BB........BB" + "...." + "...")
    # Row 8  -- top row of 2x2 period block
    print("..." + "CC.........." + "**.." + "..." + "DD.......DDD" + "**.." + "..." + "BB.......BBB" + "**.." + "...")
    # Row 9  -- bottom row of 2x2 period block
    print("..." + "CCCCCCCCCCCC" + "**.." + "..." + "DDDDDDDDDD.." + "**.." + "..." + "BBBBBBBBBB.." + "**.." + "...")

    print()

main()

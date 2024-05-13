# #This is my day to day training codes
# #Hello World
# print("Hello World")
#
# #The Loop Multiplication Table
#
# for i in range(1, 21):
#     for j in range(1, 21):
#         k = i * j
#         # Pad the number with 4 spaces
#         k = str(k).rjust(4)
#         print(k, end=" ")
#     print()  # Newline after each row
#

#Print Stars by using a loop
# Determine the number of rows
num_rows = 5

# Iterate over each row
for i in range(num_rows):
    # Print spaces for the current row
    for j in range(num_rows - i - 1):
        print(" ", end=" ")

    # Print stars for the current row
    for j in range(2 * i + 1):
        print("*", end=" ")

    # Move to the next line
    print()
#by using while loop:
# Initialize variables
row = 1
num_rows = 5

# Continue the loop until the desired number of rows is reached
while row <= num_rows:
    # Print spaces for the current row
    for i in range(num_rows - row):
        print(" ", end=" ")

    # Print stars for the current row
    for i in range(2 * row - 1):
        print("*", end=" ")

    # Move to the next line
    print()

    # Increment the row counter
    row += 1


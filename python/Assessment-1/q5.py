# 5. Write a function for Mobile Number Processing

# input:

# mobile = "9876543210"

# Write a program to:

# Find the length.

# Check whether it starts with "98".

# Extract the first 5 digits.

# Extract the last 5 digits.

# Replace the first 5 digits with "XXXXX".


def process_mobile(mobile):
    print("Length:", len(mobile))

    if mobile.startswith("98"):
        print("Starts with 98: Yes")
    else:
        print("Starts with 98: No")

    first_five = mobile[:5]
    print("First 5 digits:", first_five)

    last_five = mobile[-5:]
    print("Last 5 digits:", last_five)

    masked = "XXXXX" + mobile[5:]
    print("Masked Mobile:", masked)


mobile = "9876543210"
process_mobile(mobile)

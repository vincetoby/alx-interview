#!/usr/bin/python3
""" Lockboxes """

def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """

    # Initialize the result to False
    canUnlockAll = False

    # A dictionary to keep track of unlocked boxes, starting with the first box (index 0)
    keys = {0: True}

    # Total number of boxes
    n_boxes = len(boxes)

    # Continue checking until no new keys are found
    while(True):
        # Number of keys currently available
        n_keys = len(keys)

        # Iterate through each box
        for i in range(len(boxes)):
            # If the box is not empty and is unlocked
            if boxes[i] and keys.get(i, False):
                # Process each key in the current box
                for j in boxes[i]:
                    # If the key points to a valid box, mark that box as unlocked
                    if j < n_boxes:
                        keys[j] = True
                # Mark the box as None to prevent processing it again
                boxes[i] = None

        # If no new keys were added in this iteration, break the loop
        if not(len(keys) > n_keys):
            break

    # If the number of unlocked boxes equals the total number of boxes, set the result to True
    if n_keys == len(boxes):
        canUnlockAll = True

    # Return whether all boxes can be unlocked
    return canUnlockAll

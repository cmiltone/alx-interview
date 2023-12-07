"""
module to declare function that determines if all lock boxes can be opened
"""


def canUnlockAll(boxes):
    """determines if lock boxes can be opened"""
    current_boxes = set([0])

    tmp_boxes = set(boxes[0]).difference(set([0]))

    while len(tmp_boxes) > 0:
        i = tmp_boxes.pop()
        if not i or i >= len(boxes) or i < 0:
            continue
        if i not in current_boxes:
            tmp_boxes = tmp_boxes.union(boxes[i])
            current_boxes.add(i)

    if len(boxes) == len(current_boxes):
        return True
    return False

def go_to_cafe(list_friends: dict, cafe,
               friends_no_mask=int,
               friends_without_mask=None,
               masks_to_buy=None) -> None:

    for friend in list_friends:
        if not (friend.vaccinated):
            return "All friends should be vaccinated"

    friends_without_masks = 0
    for friend in list_friends:
        if not friend.has_mask:
            friends_no_mask += 1

    if friends_without_mask > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


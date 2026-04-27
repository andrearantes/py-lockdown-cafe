from app import cafe


def go_to_cafe(list_friends: dict,
               friends_no_mask: dict,
               friends_without_mask: dict,
               masks_to_buy: dict) -> None:

    for friend in list_friends:
        if not (friend.vaccinated):
            return "All friends should be vaccinated"

    for friend in list_friends:
        if not friend.has_mask:
            friends_no_mask += 1

    if friends_without_mask > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"

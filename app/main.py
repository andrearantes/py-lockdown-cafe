from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    try:
        if not (friends.vaccinated):
            raise ValueError("All friends should be vaccinated")

        if not (friends.mask):
            raise ValueError("Friends should buy {masks_to_buy} masks")

    except ValueError as ve:
        raise ValueError("Friends can go to {cafe.name}")

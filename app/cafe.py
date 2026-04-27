from errors import (NotVaccinatedError, OutdatedVaccineError,
                    NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: str, cafe: Cafe) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("...")

        exp_date = visitor["vaccine"]["expiration_date"]
        if exp_date < datetime.date.today():
            raise OutdatedVaccineError("...")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("...")

        return f"Welcome to {self.name}"

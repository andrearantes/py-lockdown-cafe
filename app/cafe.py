from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)
import datetime


class Cafe:
    def visit_cafe(self, friends: list, cafe: Cafe) -> None:
        if "vaccine" not in friends:
            raise NotVaccinatedError("Visitor is not vaccinated")

        exp_date = friends["vaccine"]["expiration_date"]
        if exp_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")

        if not friends.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"

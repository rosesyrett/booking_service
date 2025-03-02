from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class ClinicTimeslotKeys(StrEnum):
    id = "clinicId"
    clinic_name = "clinicName"
    start_time = "startTime"
    end_time = "endTime"
    booked = "booked"
    patient_name = "patientName"


@dataclass
class ClinicTimeslot:
    id: int
    clinic_name: str
    start_time: datetime
    end_time: datetime
    booked: bool
    patient_name: str | None = None

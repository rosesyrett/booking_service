from collections.abc import Callable
from datetime import datetime
import json

from booking_service.typings import ClinicTimeslot, ClinicTimeslotKeys


class SerializationError(Exception): ...


def deserialize(data: dict[str, str | bool]):
    constructor_kwargs = {}

    conversion_key_map: dict[ClinicTimeslotKeys, Callable[[str], int | datetime]] = {
        ClinicTimeslotKeys.id: int,
        ClinicTimeslotKeys.start_time: datetime.fromisoformat,
        ClinicTimeslotKeys.end_time: datetime.fromisoformat,
    }

    for each_key in ClinicTimeslotKeys:
        value = data.get(each_key.value)
        if value is None and each_key.value != "patientName":
            raise SerializationError(f"Field {each_key.value} is missing")

        if each_key in conversion_key_map:
            value = conversion_key_map[each_key](value)

        constructor_kwargs[each_key.name] = value

    return ClinicTimeslot(**constructor_kwargs)


def read_input_file(file_path: str) -> list[ClinicTimeslot]:
    """Reads input JSON file and checks it has the right format."""
    with open(file_path) as file:
        data = json.load(file)

    # Make some assertions, and if any are wrong, throw a more specific exception
    try:
        assert isinstance(data, list)
        assert all([isinstance(i, dict) for i in data])
    except AssertionError:
        raise SerializationError("JSON object is in the wrong format")

    return [deserialize(each_timeslot_json) for each_timeslot_json in data]

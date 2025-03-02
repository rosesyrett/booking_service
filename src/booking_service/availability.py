from collections import defaultdict

from booking_service.typings import ClinicTimeslot


def group_timeslots_by_clinic(
    timeslots: list[ClinicTimeslot],
) -> dict[str, list[ClinicTimeslot]]:
    grouped_timeslots = defaultdict(list)

    for timeslot in timeslots:
        grouped_timeslots[timeslot.clinic_name].append(timeslot)

    return grouped_timeslots


def calculate_percentage_availability_for_timeslots(timeslots: list[ClinicTimeslot]):
    booked_timeslots = [i.booked for i in timeslots]
    availability = 1 - (sum(booked_timeslots) / len(timeslots))
    return availability * 100


def calculate_availability_per_clinic(
    all_timeslots: list[ClinicTimeslot],
) -> dict[str, float]:
    grouped_timeslots = group_timeslots_by_clinic(all_timeslots)

    return {
        name: calculate_percentage_availability_for_timeslots(timeslots)
        for name, timeslots in grouped_timeslots.items()
    }

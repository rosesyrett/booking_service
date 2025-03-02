import argparse

from booking_service.availability import calculate_availability_per_clinic
from booking_service.deserialisation import read_input_file

import logging
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


def main():
    parser = argparse.ArgumentParser(prog="bookings", usage="%(prog)s file [options]")
    parser.add_argument(
        "file",
        nargs="+",
        help="Path to file which should be used to calculate clinic availability",
    )

    args = parser.parse_args()

    logger.info("Reading file...")
    timeslots = read_input_file(args.file[0])
    availability = calculate_availability_per_clinic(timeslots)

    logger.info("Availability calculated:")
    for clinic_name, percentage_available in availability.items():
        logger.info(f"    {clinic_name}: {percentage_available:.2f}%")


if __name__ == "__main__":
    main()

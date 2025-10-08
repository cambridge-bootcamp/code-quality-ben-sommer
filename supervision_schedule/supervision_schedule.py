def find_schedule_overlap(schedules):
    """
    Finds the common available times among a list of schedules.

    This function identifies the hours on each day that are present in every
    single schedule provided.

    Args:
        schedules: A list of schedule dictionaries. Each dictionary maps a
                   day (str) to a list of available integer hours.

    Returns:
        A new schedule dictionary representing the hours when everyone is
        available. Returns an empty dictionary if there's no overlap or
        if the input list is empty.
    """
    if not schedules:
        return {}
    if len(schedules) == 1:
        return schedules[0].copy()

    all_days = set()
    for schedule in schedules:
        all_days.update(schedule.keys())

    final_overlap = {}
    for day in all_days:
        if day not in schedules[0]:
            continue

        common_hours = set(schedules[0][day])

        for schedule in schedules[1:]:
            if day not in schedule:
                common_hours.clear()
                break

            common_hours.intersection_update(schedule[day])

        if common_hours:
            final_overlap[day] = sorted(list(common_hours))

    return final_overlap


def _parse_and_validate_hours(input_str):
    """
    Parses a string of space-separated hours, validates them, and returns a sorted list.

    Private helper function to encapsulate the validation logic.

    Args:
        input_str: The raw string from user input.

    Returns:
        A sorted list of valid integer hours (0-23).
    """
    hour_parts = input_str.split()
    validated_hours = []

    for part in hour_parts:
        try:
            # Convert the string part to an integer
            hour = int(part)
            # Add validation for the hour range (e.g., 0-23)
            if 0 <= hour <= 23:
                if hour not in validated_hours:  # Avoid duplicate hours
                    validated_hours.append(hour)
            else:
                print(
                    f"  -> Warning: Hour '{hour}' is outside the valid 0-23 range. Ignoring."
                )
        except ValueError:
            # Handle cases where the part is not a valid number
            print(f"  -> Warning: '{part}' is not a valid number. Ignoring.")

    return sorted(validated_hours)


def build_schedule_from_input():
    """
    Interactively builds a schedule by prompting the user for input.

    The function iterates through the days of the week, asking the user to
    enter their available hours for each day as a space-separated list of
    numbers. It handles invalid (non-numeric) input gracefully by ignoring
    it and notifying the user.

    Returns:
        A schedule dictionary built from the user's input.
    """
    new_schedule = {}
    days_of_week = ["mon", "tue"]  # , "wed", "thu", "fri"]

    print("Enter a schedule")
    print("  For each day, enter available hours as numbers separated by spaces.")
    print("  Press Enter to skip a day if you have no availability.\n")

    for day in days_of_week:
        try:
            prompt = f"Enter hours for {day.capitalize()}: ".ljust(20)
            input_str = input(prompt)
        except (EOFError, KeyboardInterrupt):
            print("\n\nSchedule creation cancelled.")
            return None

        if not input_str.strip():
            continue

        hours_for_day = _parse_and_validate_hours(input_str)

        if hours_for_day:
            new_schedule[day] = hours_for_day

    return new_schedule


def collect_schedules_and_find_overlap():
    """
    Manages the process of collecting multiple schedules from user input
    and calculating the overlapping available times.
    """
    schedules = []

    while True:
        try:
            num_schedules_str = input("How many schedules would you like to compare? ")
            num_schedules = int(num_schedules_str)
            if num_schedules > 1:
                break
            else:
                print("Please enter at least 2 schedules to find an overlap.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except (EOFError, KeyboardInterrupt):
            print("\n\nOperation cancelled.")
            return

    for i in range(num_schedules):
        print(f"\n{'=' * 10} Enter Schedule #{i + 1} {'=' * 10}")
        schedule = build_schedule_from_input()
        if schedule:
            schedules.append(schedule)
        else:
            print(
                f"Cancelled creation for schedule #{i + 1}. Aborting overlap calculation."
            )
            return

    if len(schedules) == num_schedules:
        print("\n\n" + "=" * 40)
        print("Calculating overlap for all collected schedules...")
        overlap = find_schedule_overlap(schedules)

        if overlap:
            print("\nCommon Available Times")
            print(overlap)
        else:
            print("\nNo common time slots found!")
        print("=" * 40)


if __name__ == "__main__":
    collect_schedules_and_find_overlap()

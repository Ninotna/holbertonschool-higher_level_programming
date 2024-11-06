#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.INFO)


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template with placeholders.

    Parameters:
    template (str): The string template containing placeholders.
    attendees (list): A list of dictionaries with keys: 'name', 'event_title',
                      'event_date', and 'event_location'.

    Returns:
    None: Outputs files named output_X.txt where X is the index of the attendee.
    """

    # Check if the template is a string
    if not isinstance(template, str):
        logging.error("Template should be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        logging.error("Attendees should be a list of dictionaries.")
        return

    # Check if the template is empty
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    # Check if the attendees list is empty
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Create a copy of the template to replace placeholders
        invitation = template[:]

        # Replace placeholders with attendee's data or "N/A" if data is missing
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A") or "N/A"
            invitation = invitation.replace(f"{{{key}}}", value)

        # Write the invitation to an output file
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, "w") as output_file:
                output_file.write(invitation)
            logging.info(f"Generated {output_filename}")
        except IOError as e:
            logging.error(f"Error writing to file {output_filename}: {e}")


# Example Main File to Test the Program
if __name__ == "__main__":
    # Read the template from a file
    with open("template.txt", "r") as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {
            "name": "Alice",
            "event_title": "Python Conference",
            "event_date": "2023-07-15",
            "event_location": "New York",
        },
        {
            "name": "Bob",
            "event_title": "Data Science Workshop",
            "event_date": "2023-08-20",
            "event_location": "San Francisco",
        },
        {
            "name": "Charlie",
            "event_title": "AI Summit",
            "event_date": None,
            "event_location": "Boston",
        },
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)

# The Booking Service

This service simply injests JSON data, reads it, and calculates availability per clinic.

The input JSON is expected to contain a list of objects conforming to this schema:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "clinicId": {
      "type": "string"
    },
    "clinicName": {
      "type": "string"
    },
    "startTime": {
      "type": "string",
      "format": "date-time"
    },
    "endTime": {
      "type": "string",
      "format": "date-time"
    },
    "booked": {
      "type": "boolean"
    },
    "patientName": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": ["clinicId", "clinicName", "startTime", "endTime", "booked"],
  "if": {
    "properties": {
      "booked": {
        "const": true
      }
    }
  },
  "then": {
    "required": ["patientName"]
  },
  "else": {
    "not": {
      "required": ["patientName"]
    }
  }
}
```


If it does not, this service will fail loudly.

Availability is logged as a percentage of the timeslots per clinic which are not yet booked.

## Usage and installation

To use, simply install the project...

```bash
pip install .
```

... and run like so:

```bash
bookings path/to/file.json
```

If you'd like to install with dev dependencies, do

```bash
pip install . '.[dev]'
```

## Improvements in the Roadmap

If I had more time, I would implement proper serialization of the input json objects. The task specifically mentioned I should not use external libraries. For this aim, I could use jsonschema, or something more modern/hip like pydantic.
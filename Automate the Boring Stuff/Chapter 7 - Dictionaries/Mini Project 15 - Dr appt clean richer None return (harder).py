
appointments = [
    {"patient": "  john  ", "doctor": "DR. SMITH", "appointment_type": "CHECKUP", "duration_mins": "30", "fee": "$*85,00"},
    {"patient": "Sarah", "doctor": "", "appointment_type": "surgery", "duration_mins": None, "fee": "$200"},
    {"patient": "  ", "doctor": "Dr. Jones", "appointment_type": "CONSULTATION", "duration_mins": "forty five", "fee": "$*60,00"},
    {"patient": "MIKE", "doctor": "dr. patel", "appointment_type": "xray", "duration_mins": "20", "fee": "$*45"},
    {"patient": "Emma", "doctor": "DR. WONG", "appointment_type": "checkup", "duration_mins": "30", "fee": "free"},
    {"patient": "  lisa  ", "doctor": "Dr. Brown", "appointment_type": "CONSULTATION", "duration_mins": "60", "fee": "$*90,00"},
    {"patient": None, "doctor": "Dr. Adams", "appointment_type": "checkup", "duration_mins": "15", "fee": "$50"},
]

def clean_app(app):

    name = (app.get('patient') or "").strip()

    if not name:

        return {'ok': False,
                'record': app,
                'field': 'name',
                'reason': "missing patient or None value"
                }

    name = name.strip().capitalize()

    doctor = app.get('doctor').strip().replace(".", "").capitalize()

    if not doctor:

        return {'ok': False,
                'record': app,
                'field': 'doctor',
                'reason': "Missing docrtor or None value"
                }



    app_type = app.get('appointment_type').lower()



    if app_type not in ['checkup', 'consultation', 'surgery']:

        return {'ok': False,
                'record': app,
                'field': 'app_type',
                'reason': "invalid appointment type"
                }

    try:
        duration = int(app.get('duration_mins', 30))
    except (ValueError, TypeError):
        duration = 30

    try:
        fee = float(app.get('fee', 0).replace(",", ".").replace("*", "").replace("$", ""))
    except (ValueError, TypeError):
        fee = 0


    return {'ok': True,
            'data': {
                'patient': name,
                'doctor': doctor,
                'app_type': app_type,
                'duration': duration,
                'fee': fee
                }
            }


def print_apps(cleaned, errors):


    for app_data in cleaned:

        name = app_data['patient']
        doctor = app_data['doctor']
        app_type = app_data['app_type']
        duration = app_data['duration']
        fee = app_data['fee']

        print(f"{doctor}:")
        print(f"  {name}:")
        print(f"    Appt type: {app_type} | {duration} mins | Fee: ${fee}\n")

    print("Errors:\n")

    for i, error in enumerate(errors, start = 1):

        status = error['ok']
        record = error['record']
        reason = error['reason']
        field = error['field']


        print(f"Error {i}.")
        print(f"Status: {status}")
        print(f"Record: {record}")
        print(f"Reason: {reason}")
        print(f"Field: {field}\n")



def main():

    errors = []
    cleaned = []

    for app in appointments:

        result = clean_app(app)

        if not result['ok']:
            errors.append(result)
            continue

        cleaned.append(result['data'])

    print_apps(cleaned, errors)

main()

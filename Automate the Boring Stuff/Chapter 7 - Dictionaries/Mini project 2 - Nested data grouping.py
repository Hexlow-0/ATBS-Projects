
from collections import Counter
from collections import defaultdict
import statistics as stats


raw_data = [
    {"continent": "Asia", "country": "Japan", "city": "Tokyo", "hospital": "Tokyo General", "department": "Cardiology", "doctor": "Dr. Tanaka", "patients": [{"name": "Alice", "condition": "Hypertension", "cost": 1200}, {"name": "Bob", "condition": "Arrhythmia", "cost": 1800}]},
    {"continent": "Asia", "country": "Japan", "city": "Tokyo", "hospital": "Tokyo General", "department": "Neurology", "doctor": "Dr. Sato", "patients": [{"name": "Charlie", "condition": "Migraine", "cost": 900}]},
    {"continent": "Asia", "country": "Japan", "city": "Osaka", "hospital": "Osaka Medical", "department": "Cardiology", "doctor": "Dr. Yamamoto", "patients": [{"name": "Diana", "condition": "Heart Disease", "cost": 3200}, {"name": "Alice", "condition": "Hypertension", "cost": 1100}]},
    {"continent": "Asia", "country": "China", "city": "Beijing", "hospital": "Beijing Central", "department": "Cardiology", "doctor": "Dr. Wang", "patients": [{"name": "Eve", "condition": "Arrhythmia", "cost": 1500}, {"name": "Frank", "condition": "Heart Disease", "cost": 2800}]},
    {"continent": "Europe", "country": "Germany", "city": "Berlin", "hospital": "Berlin Hospital", "department": "Neurology", "doctor": "Dr. Mueller", "patients": [{"name": "Grace", "condition": "Epilepsy", "cost": 2100}, {"name": "Henry", "condition": "Migraine", "cost": 800}]},
    {"continent": "Europe", "country": "Germany", "city": "Munich", "hospital": "Munich Clinic", "department": "Cardiology", "doctor": "Dr. Schmidt", "patients": [{"name": "Alice", "condition": "Hypertension", "cost": 1300}, {"name": "Ivan", "condition": "Heart Disease", "cost": 2900}]},
    {"continent": "Europe", "country": "France", "city": "Paris", "hospital": "Paris Medical", "department": "Neurology", "doctor": "Dr. Dupont", "patients": [{"name": "Julia", "condition": "Epilepsy", "cost": 1900}, {"name": "Bob", "condition": "Migraine", "cost": 750}]}
]

# =======================================
# BUILD AND GROUP DATA
# =======================================

def build_grouped_data(raw_data):

    groups = {}

    for data in raw_data:

        continent = data['continent']
        country = data['country']
        city = data['city']
        hospital = data['hospital']
        department = data['department']
        doctor = data['doctor']

        if continent not in groups:
            groups[continent] = {}

        if country not in groups[continent]:
            groups[continent][country] = {}

        if city not in groups[continent][country]:
            groups[continent][country][city] = {}

        if hospital not in groups[continent][country][city]:
            groups[continent][country][city][hospital] = {}

        if department not in groups[continent][country][city][hospital]:
             groups[continent][country][city][hospital][department] = {}

        if doctor not in groups[continent][country][city][hospital][department]:
            groups[continent][country][city][hospital][department][doctor] = []

        for patient in data['patients']:

            groups[continent][country][city][hospital][department][doctor].append(patient)

    return groups


# =======================================
# CALCULATE REVENUE PER CONTINENT
# =======================================

def calculate_continent_revenue(grouped_data):

    continent_revenue_total = defaultdict(int)

    for continent, country_data in grouped_data.items():
        for country, city_data in country_data.items():
            for city, hospital_data in city_data.items():
                for hospital, department_data in hospital_data.items():
                    for department, doctor_data in department_data.items():
                        for doctor, patient_data in doctor_data.items():
                            for data in patient_data:

                                cost = data['cost']

                                continent_revenue_total[continent] += cost

    return continent_revenue_total


# =======================================
# CALCULATE MOST COMMON CONDITION
# =======================================

def calculate_most_common_condition(grouped_data):

    condition_count = defaultdict(int)

    for continent, country_data in grouped_data.items():
        for country, city_data in country_data.items():
            for city, hospital_data in city_data.items():
                for hospital, department_data in hospital_data.items():
                    for department, doctor_data in department_data.items():
                        for doctor, patient_data in doctor_data.items():
                            for data in patient_data:

                                condition = data['condition']

                                condition_count[condition] += 1

    count = Counter(condition_count)

    # Set to three bc the top three were all equal anyway
    most_common_conditions = count.most_common(3)

    return most_common_conditions


# =======================================
# CALCULATE TOTAL SPENT PER PATIENT
# =======================================

def calculate_total_patients_spent(grouped_data):

    total_patient_spent = defaultdict(int)

    for continent, country_data in grouped_data.items():
        for country, city_data in country_data.items():
            for city, hospital_data in city_data.items():
                for hospital, department_data in hospital_data.items():
                    for department, doctor_data in department_data.items():
                        for doctor, patient_data in doctor_data.items():
                            for data in patient_data:

                                cost = data['cost']
                                name = data['name']

                                total_patient_spent[name] += cost

    return total_patient_spent

# =======================================
# CALCULATE PATIENT WHO SPENT THE MOST
# =======================================

def cacluate_most_spent_patient(total_patient_spent):

    count = Counter(total_patient_spent)

    most_spent = count.most_common(1)

    return most_spent

# =======================================
# PRINT SUMMARY - EXACTLY THE EXPECTED OUTPUT
# =======================================

def summary(grouped_data, continent_revenue, most_common_conditions, total_patient_spent, most_spent_patient):


    print("=" * 40)
    print("EXPECTED TASK OUTPUT".center(40))
    print("=" * 40)
    print()

    for continent, country_data in grouped_data.items():
        print(f"{continent}:")
        for country, city_data in country_data.items():
            print(f"  {country}:")
            for city, hospital_data in city_data.items():
                print(f"    {city}:")
                for hospital, department_data in hospital_data.items():
                    print(f"      {hospital}:")
                    for department, doctor_data in department_data.items():
                        print(f"        {department}:")
                        for doctor, patient_data in doctor_data.items():
                            print(f"          {doctor}:")

                            dr_total_rev = 0

                            for data in patient_data:

                                name = data['name']
                                condition = data['condition']
                                cost = data['cost']

                                dr_total_rev += data['cost']

                                print(f"            {name} - {condition} - ${cost:,}")

                            print(f"            Doctor total: ${dr_total_rev:,}")


    print()

    for continent, total_rev in continent_revenue.items():
        print(f"{continent} total: ${total_rev:,}")

    print()

    print("Most common conditions include:\n")

    for condition_and_cases in most_common_conditions:
        for conditions in condition_and_cases:
            if type(conditions) == str:
                print(f"{conditions} with ", end='')
            elif type(conditions) == int:
                print(f"{conditions} cases")


    print()

    print(f"Highest spending patient: {most_spent_patient[0][0]} with ${most_spent_patient[0][1]:,} total")

    print()
    print("=" * 40)
    print("FINISHED".center(40))
    print("=" * 40)
    print()

# =======================================
# MAIN PROGRAM TO CALL FUNCTIONS
# =======================================

def main(raw_data):

    grouped_data = build_grouped_data(raw_data)

    continent_revenue = calculate_continent_revenue(grouped_data)

    most_common_conditions = calculate_most_common_condition(grouped_data)

    total_patient_spent = calculate_total_patients_spent(grouped_data)

    most_spent_patient = cacluate_most_spent_patient(total_patient_spent)

    summary(grouped_data, continent_revenue, most_common_conditions, total_patient_spent, most_spent_patient)

# =======================================
# START THE PROGRAM
# =======================================

main(raw_data)

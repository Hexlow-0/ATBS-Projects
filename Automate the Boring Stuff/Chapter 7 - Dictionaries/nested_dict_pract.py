
from collections import Counter
from collections import defaultdict
import statistics as stats


raw_data = [
    {"region": "North America", "country": "USA", "division": "Engineering", "team": "Backend", "employee": "Alice", "project": "API Redesign", "hours": 120},
    {"region": "North America", "country": "USA", "division": "Engineering", "team": "Frontend", "employee": "Bob", "project": "Dashboard UI", "hours": 95},
    {"region": "North America", "country": "Canada", "division": "Engineering", "team": "Backend", "employee": "Charlie", "project": "Database Migration", "hours": 110},
    {"region": "North America", "country": "USA", "division": "Marketing", "team": "Digital", "employee": "Diana", "project": "SEO Campaign", "hours": 80},
    {"region": "Europe", "country": "Germany", "division": "Engineering", "team": "Backend", "employee": "Eve", "project": "API Redesign", "hours": 130},
    {"region": "Europe", "country": "Germany", "division": "Engineering", "team": "Frontend", "employee": "Frank", "project": "Mobile App", "hours": 100},
    {"region": "Europe", "country": "France", "division": "Marketing", "team": "Digital", "employee": "Grace", "project": "Social Media", "hours": 75},
    {"region": "North America", "country": "USA", "division": "Engineering", "team": "Backend", "employee": "Alice", "project": "Security Audit", "hours": 85},
    {"region": "Europe", "country": "Germany", "division": "Marketing", "team": "Digital", "employee": "Henry", "project": "Email Campaign", "hours": 90},
    {"region": "North America", "country": "Canada", "division": "Marketing", "team": "Digital", "employee": "Charlie", "project": "Brand Refresh", "hours": 65},
    {"region": "Europe", "country": "France", "division": "Engineering", "team": "Backend", "employee": "Eve", "project": "Cloud Migration", "hours": 140},
    {"region": "North America", "country": "USA", "division": "Engineering", "team": "Frontend", "employee": "Bob", "project": "Component Library", "hours": 110}
]



# ========================================
# BUILD GROUPED DATA
# ========================================

def group_data(raw_data):

    groups = {}

    for data in raw_data:

        region = data['region']
        country = data['country']
        division = data['division']
        team = data['team']
        employee = data['employee']


        if region not in groups:
            groups[region] = {}

        if country not in groups[region]:
            groups[region][country] = {}

        if division not in groups[region][country]:
            groups[region][country][division] = {}

        if team not in groups[region][country][division]:
            groups[region][country][division][team] = {}

        if employee not in groups[region][country][division][team]:
            groups[region][country][division][team][employee] = []

        groups[region][country][division][team][employee].append({'project': data['project'], 'hours': data['hours']})

    return groups

# ========================================
# CALCULATE TOTAL HOURS PER EMPLOYEE
# ========================================

def calculate_employee_hour(groups):

    hours_per_team = {}

    for region, country_data in groups.items():
        for country, division_data in country_data.items():
            for division, team_data in division_data.items():
                for team, employee_data in team_data.items():
                    for employee, project_data in employee_data.items():
                        for project in project_data:

                            hours_per_team[employee] = hours_per_team.get(employee, 0) + project['hours']

    return hours_per_team

# ========================================
# CALCULATE TOTAL HOURS PER DIVISION
# ========================================

def calculate_division_hour(groups):

    hours_per_division = {}

    for region, country_data in groups.items():
        for country, division_data in country_data.items():
            for division, team_data in division_data.items():
                for team, employee_data in team_data.items():
                    for employee, project_data in employee_data.items():
                        for project in project_data:

                            hours_per_division[division] = hours_per_division.get(division, 0) + project['hours']

    return hours_per_division

# ========================================
# CALUCLATE TOTAL HOURS PER REGION
# ========================================

def calculate_region_hours(groups):

    hours_per_region = {}

    for region, country_data in groups.items():
        for country, division_data in country_data.items():
            for division, team_data in division_data.items():
                for team, employee_data in team_data.items():
                    for employee, project_data in employee_data.items():
                        for project in project_data:

                            hours_per_region[region] = hours_per_region.get(region, 0) + project['hours']

    return hours_per_region

# ========================================
# CALCULATE HARDEST WORKER (MOST HOURS)
# ========================================

def calculate_hardest_worker(employee_total_hours):

    hardest_worker = Counter(employee_total_hours).most_common(1)

    return hardest_worker

# ========================================
# PRINT SUMMARY
# ========================================

def summary(employee_total_hours, division_total_hours, region_total_hours, hardest_worker):

    print("=" * 40)
    print("SUMMARY".center(40))
    print("=" * 40)
    print()

    print("=" * 40)
    print("HOURS PER EMPLOYEE".center(40))
    print("=" * 40)
    print()

    for employee, employee_hours in employee_total_hours.items():

        print(f"{employee}\tTotal hours: {employee_hours}")

    print()
    print("=" * 40)
    print("HOURS PER DIVISION".center(40))
    print("=" * 40)
    print()

    for division, division_hours in division_total_hours.items():

        print(f"{division} - Total hours: {division_hours}")

    print()
    print("=" * 40)
    print("HOURS PER REGION".center(40))
    print("=" * 40)
    print()

    for region, region_hours in region_total_hours.items():

        print(f"{region} - Total hours: {region_hours}")

    print()
    print("=" * 40)
    print("HARDEST WORKER".center(40))
    print("=" * 40)
    print()

    print(f"{hardest_worker[0][0]} with {hardest_worker[0][1]} hours!")

    print()
    print("=" * 40)
    print("THANK YOU!".center(40))
    print("=" * 40)
    print()

# ========================================
# MAIN FUNCTION TO CALL EACH SECTION
# ========================================

def main():

    groups = group_data(raw_data)

    employee_total_hours = calculate_employee_hour(groups)

    division_total_hours = calculate_division_hour(groups)

    region_total_hours = calculate_region_hours(groups)

    hardest_worker = calculate_hardest_worker(employee_total_hours)

    summary(employee_total_hours, division_total_hours, region_total_hours, hardest_worker)

main()





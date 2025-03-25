"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 180 minutes
Actual:   34 minutes
"""

from prac_07.project import Project
from datetime import datetime

TITLE = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date" \
       "\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    filename = "projects.txt"
    projects = load_file(filename)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {filename}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_file(filename)
        elif choice == "S":
            save_project(filename, projects)
        elif choice == "D":
            display_project(projects)
        elif choice == "F":
            projects = filter_project(projects)
        elif choice == "A":
            add_project(projects)
        # elif choice == "U":
        #     projects = update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def add_project(projects):
    """Add new project"""
    print("Let's add a new project")
    try:
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yy): ")
        priority = int(input("Priority: "))
        cost = float(input("Cost estimate: $"))
        complete = int(input("Percent complete: "))
        projects.append(Project(name, start_date, priority, cost, complete))
    except ValueError:
        print("Invalid input")


def filter_project(projects):
    """Show project who start after date"""
    is_valid = False
    while not is_valid:
        try:
            filter_project_date = []
            date = input("Show projects that start after date (dd/mm/yy): ")
            filter_date = datetime.strptime(date, "%d/%m/%Y").date()
            for project in projects:
                data_project = datetime.strptime(project.start_date, "%d/%m/%Y").date()
                if filter_date <= data_project:
                    filter_project_date.append(project)
            filter_project_date.sort(key=lambda x: datetime.strptime(x.start_date, "%d/%m/%Y"))
            display_project_detail(filter_project_date)
            is_valid = True
        except ValueError:
            print("Incorrect data format (day/month/year)")
    return projects


def display_project(projects):
    """Display not or complete project"""
    incomplete_project = []
    complete_project = []
    for project in projects:
        if project.complete == 100:
            complete_project.append(project)
            complete_project.sort()
        else:
            incomplete_project.append(project)
            incomplete_project.sort()
    print("Incomplete projects:")
    display_project_detail(incomplete_project)
    print("Complete projects:")
    display_project_detail(complete_project)


def display_project_detail(projects):
    """String for output project"""
    for project in projects:
        print(f" {project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.cost}, "
              f"completion: {project.complete}%")


def load_file(filename):
    """Load data from file"""
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        part = line.strip().split('\t')
        projects.append(Project(part[0], part[1], int(part[2]), float(part[3]), int(part[4])))
    in_file.close()
    return projects


def save_project(filename, projects):
    """Save project into file"""
    with open(filename, 'w') as out_file:
        print(TITLE, file=out_file)
        for project in projects:
            print(project, file=out_file)


main()

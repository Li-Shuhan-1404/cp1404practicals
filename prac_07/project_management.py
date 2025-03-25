"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 120 minutes
Actual:   34 minutes
"""

from prac_07.project import Project

TITLE = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date" \
       "\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    filename = "projects.txt"
    projects = load_file(filename)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_file(filename)
        elif choice == "S":
            save_project(filename, projects)
        elif choice == "D":
            display_project(projects)
        # elif choice == "F":
        #     projects = filter_project(projects)
        # elif choice == "A":
        #     add_project(projects)
        # elif choice == "U":
        #     projects = update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def display_project(projects):
    """Display not or complete project"""
    incomplete_project = []
    complete_project = []
    projects.sort()
    for project in projects:
        if project.complete == 100:
            complete_project.append(project)
        else:
            incomplete_project.append(project)
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
        for line in projects:
            print(line, file=out_file)


main()

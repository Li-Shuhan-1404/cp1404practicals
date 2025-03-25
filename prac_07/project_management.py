"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 120 minutes
Actual:   34 minutes
"""

from prac_07.project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date" \
       "\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    file = "projects.txt"
    projects = load_file(file)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_file(file)
        elif choice == "S":
            save_project(file, projects)
        elif choice == "D":
            display_project(projects)
        elif choice == "F":
            projects = filter_project(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            projects = update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_file(file):
    """Load data from file"""
    projects = []
    in_file = open(file, 'r')
    in_file.readline()
    for line in in_file:
        part = line.strip().split('\t')
        projects.append(Project(part[0], part[1], int(part[2]), float(part[3]), int(part[4])))
    in_file.close()
    return projects


def save_project(file, projects):
    """Save project into file"""
    with open(file, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for line in projects:
            print(line, file=out_file)


main()

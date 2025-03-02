"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 30 minutes
Actual:   34 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read file and display result"""
    records = get_record(FILENAME)
    champion_to_count, countries = process_record(records)
    display_result(champion_to_count, countries)


def display_result(champion_to_count, countries):
    """Display the result"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def process_record(records):
    """Change champion to count"""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def get_record(filename):
    """Read file and get record"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            part = line.strip().split(",")
            records.append(part)
    return records


main()

import wikipedia


def search_wikipedia():
    print("Wikipedia Page Search")

    while True:
        search_term = input("\nEnter page title: ").strip()
        if not search_term:
            print("Thank you.")
            break
        try:
            page = wikipedia.page(search_term)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{search_term}" does not match any pages. Try another id!')


if __name__ == "__main__":
    search_wikipedia()

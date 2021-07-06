from app import services


def format_search(query, results: list):
    msg = f"Результаты по запросу: {query}\n\n"
    rows = []
    for res in results:
        rows.append(f"{res['title']}\n{res['text']}\n{res['link']}")
    msg = msg + '\n\n\n'.join(rows)
    return msg


def get_search(query) -> str:
    scrapper = services.GScrapper()
    results = scrapper.get_search_results(query)
    if not results:
        return f"Ничего не найдено по запросу:\n{query}"
    return format_search(query, results)

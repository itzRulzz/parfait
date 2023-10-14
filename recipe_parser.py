def link_parser(query):
    # Принимает запрос из представления.
    # Делает парсинг по запросу.
    # Отсылает полученные данные обратно представлению.
    results = [f'http://{query}' for x in range(10)]
    return results

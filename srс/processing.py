a= [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
def filter_by_state(opz = "EXECUTED"):
    """Фильтрует список по состоянию."""
    results = []
    for item in a:
        if item.get('state') == opz:
            results.append(item)
    return results


start = "CANCELED"
filtered_results = filter_by_state()
print(filtered_results)

def sort_by_date(sliv,descending = True):
    return sorted(sliv, key=lambda x: x['date'], reverse=descending)

print(sort_by_date(a,False))
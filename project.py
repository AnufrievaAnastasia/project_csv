import csv

def csv_maker(filename):
    def decorator(func):
        def wrapped(list_dict):
          result = func(list_dict)
          with open(filename, 'w', newline='') as file:
              writer = csv.DictWriter(file, delimiter=' ', fieldnames=list(list_dict[0].keys()))
              writer.writeheader()
              writer.writerows(list_dict)
              return result
        return wrapped
    return decorator



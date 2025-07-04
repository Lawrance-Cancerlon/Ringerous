import json
import csv
from shared.models.Ring import Ring

def import_rings(paths):
    """
    Returns path, rings.
        """
    rings = []
    pathss = []
    for path in paths:
        with open(path) as f:
            data = json.load(f)
        rings.append(Ring(elements=data['elements'], add_table=data['add_table'], mul_table=data['mul_table']))
        pathss.append(path)
    return pathss, rings

def export_single_result(results, path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        headers = ["Property", "Result", "Counterexample"]
        writer.writerow(headers)
        for prop, result in results.items():
            writer.writerow([
                prop,
                str(result['result']),
                result['counterexample'] if not result["result"] else ""
            ])
        
def export_batch_results(results, path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        headers = ["Filename", "Property", "Result", "Counterexample"]
        writer.writerow(headers)
        for filename, props in results.items():
            for prop, result in props.items():
                writer.writerow([
                    filename,
                    prop,
                    str(result['result']),
                    result['counterexample'] if not result["result"] else ""
                ])

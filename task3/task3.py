import sys
import json


def main():
    if len(sys.argv) != 4:
        print("Please, usage: python task_2.py path_to_values_file path_to_tests_file path_to_report_file")
        sys.exit(1)
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    with open(rf"{values_path}", "r") as values_file:
        values = json.load(values_file)

    with open(rf"{tests_path}", "r") as tests_file:
        tests = json.load(tests_file)

    file_example = tests["tests"]
    values_to_add = values["values"]

    filling_form(file_example, values_to_add)

    with open(rf"{report_path}", "w") as report_file:
        json.dump(tests, report_file, indent=3)


def filling_form(form, results):
    if isinstance(form, dict):
        if "value" in form:
            for res in results:
                if res["id"] == form["id"]:
                    form["value"] = res["value"]
        if "values" in form:
            filling_form(form["values"], results)
    elif isinstance(form, list):
        for investment in form:
            filling_form(investment, results)


if __name__ == "__main__":
    main()

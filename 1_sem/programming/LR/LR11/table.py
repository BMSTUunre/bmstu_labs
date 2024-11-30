from prettytable import PrettyTable, SINGLE_BORDER


def print_table(sorted_res: list[int | float],
                random_res: list[int | float],
                reverse_res: list[int | float]) -> None:

    table = PrettyTable()
    table.field_names = ["", "Время N1", "Перестановки N1", "Время N2", "Перестановки N2", "Время N3", "Перестановки N3"]
    table.add_row(sorted_res, divider=True)
    table.add_row(random_res, divider=True)
    table.add_row(reverse_res)

    table.set_style(SINGLE_BORDER)

    print(table)

""" generic functions used for reading from excel"""
import openpyxl


def read_locators(file_name, sheet_name):
	workbook = openpyxl.load_workbook(file_name)
	worksheet = workbook[sheet_name]
	rows = worksheet.iter_rows(values_only=True)
	header = next(rows)

	data = {row[0]: (row[1], row[2]) for row in rows}
	return data
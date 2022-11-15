# Copyright (c) 2022, Code Space Techlabs and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import cstr


def execute(filters=None):
	columns, data = [], []

	columns = get_columns()
	data = get_data(filters)
	chart_data = get_chart_data(data, columns)
	return columns, data, None, chart_data


def get_columns():
	return [
		{
			"label": _("Stage"),
			"fieldname": "stage",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"label": _("Percentage"),
			"fieldname": "percentage",
			"fieldtype": "Percent",
			"width": 150,
		},
	]


def get_data(filters):

	result = frappe.db.sql("""
		SELECT
			stage,
			COUNT(*) * 100 / (SELECT COUNT(*) from `tabLeed` ) as "percentage"
		FROM
			`tabLeed`
		GROUP BY
			stage """, as_dict=True)

	return result

def get_chart_data(data, columns):

	labels = [x['stage'] for x in data]
	datasets = [{
		'name': "Pie Chart", 
		'values': [x['percentage'] for x in data]} 
	]

	chart = {
		"data": {
			"labels": labels,
			"datasets": datasets,
		},
		"type": "pie",
	}

	return chart

# Copyright (c) 2024, HS Rai and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

# 111111111111111111111111111111111111


#import frappe
from frappe.utils import cint

def before_save(doc, method):
    # Generate a slugified route from the Book Name
    base_route = frappe.utils.data.slug(doc.title)

    # Check if a route with the same name already exists
    similar_routes = frappe.get_all(
        'ArticleName',  # Replace 'YourDocType' with your actual DocType name
        filters={'route': ['like', f'{base_route}%']},
        fields=['route']
    )

    # If similar routes exist, append a number to make it unique
    if similar_routes:
        similar_route_numbers = [
            cint(route.get('route').replace(base_route, '') or 0)
            for route in similar_routes
        ]
        max_route_number = max(similar_route_numbers, default=0)
        doc.route = f"{base_route}-{max_route_number + 1}"
    else:
        doc.route = base_route


# 999999999999999999999999999999999999

#class ArticleName(Document):
class ArticleName(WebsiteGenerator):
	pass



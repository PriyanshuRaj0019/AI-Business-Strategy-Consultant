import re


def validate_company_name(company_name: str) -> str:
    """
    Validate and sanitize company name input.
    """

    company_name = company_name.strip()

    if not company_name:
        raise ValueError("Company name cannot be empty.")

    if len(company_name) > 100:
        raise ValueError("Company name is too long.")

    if not re.match(r"^[A-Za-z0-9 .,&()-]+$", company_name):
        raise ValueError("Invalid company name.")

    return company_name

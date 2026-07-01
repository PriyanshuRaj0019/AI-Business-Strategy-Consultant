from app.mcp.tools import get_company_information
from app.utils.validators import validate_company_name


class CompanyMCPServer:

    def get_company(self, company_name: str):

        company_name = validate_company_name(company_name)

        return get_company_information(company_name)
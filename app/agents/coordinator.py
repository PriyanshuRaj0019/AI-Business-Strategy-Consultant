from app.models.company import Company
from app.utils.logger import get_logger


class CoordinatorAgent:

    def __init__(self):
        self.logger = get_logger("Coordinator")

    def analyze_company(self, company: Company):

        self.logger.info(
            f"Received analysis request for {company.name}"
        )

        print("\n========== COMPANY DETAILS ==========")
        print(f"Name      : {company.name}")
        print(f"Industry  : {company.industry}")
        print(f"Country   : {company.country}")
        print("=====================================\n")

        print("Coordinator Agent initialized.")
        print("Research Agent would be called here.")
        print("SWOT Agent would be called here.")
        print("Finance Agent would be called here.")
        print("Report Agent would be called here.")

        
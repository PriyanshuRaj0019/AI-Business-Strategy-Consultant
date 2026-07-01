from app.agents.coordinator import CoordinatorAgent
from app.models.company import Company


def main():
    company = Company(
        name="Tesla",
        industry="Electric Vehicles",
        country="United States"
    )

    coordinator = CoordinatorAgent()
    coordinator.analyze_company(company)


if __name__ == "__main__":
    main()
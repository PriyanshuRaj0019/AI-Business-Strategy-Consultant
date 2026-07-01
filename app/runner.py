from app.graph.workflow import business_graph


def analyze_company(
    company: str,
    report_type: str,
) -> str:

    state = {

        "company": company,

        "report_type": report_type,

        "research": "",

        "market_analysis": "",

        "competitor_analysis": "",

        "swot": "",

        "pestle": "",

        "porter": "",

        "financial": "",

        "strategy": "",

        "executive_summary": "",

        "final_report": "",

    }

    result = business_graph.invoke(state)

    return result["final_report"]


if __name__ == "__main__":

    report = analyze_company(

        company="Tesla",

        report_type="Complete Business Report",

    )

    print(report)
    
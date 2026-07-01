from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
)
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path


def generate_pdf(company_name: str, report: str) -> str:
    """
    Generate a PDF report and return its file path.
    """

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    filename = reports_dir / f"{company_name}_Business_Report.pdf"

    doc = SimpleDocTemplate(str(filename))

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        f"<b>{company_name} Business Strategy Report</b>",
        styles["Title"],
    )

    story.append(title)

    story.append(
        Paragraph("<br/><br/>", styles["BodyText"])
    )

    for line in report.split("\n"):

        if line.strip():

            story.append(
                Paragraph(line, styles["BodyText"])
            )

    doc.build(story)

    return str(filename)
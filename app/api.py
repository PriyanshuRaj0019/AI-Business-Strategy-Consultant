from pathlib import Path
import shutil

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.runner import analyze_company

# =====================================================
# FastAPI
# =====================================================

app = FastAPI(
    title="AI Business Strategy Consultant",
    version="1.0.0",
)

# =====================================================
# CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# Request Model
# =====================================================

class AnalyzeRequest(BaseModel):
    company: str
    report_type: str


# =====================================================
# Health
# =====================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "AI Business Strategy Consultant",
        "version": "1.0.0",
    }


# =====================================================
# Analyze Company
# =====================================================

@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    try:

        report = analyze_company(
            company=request.company,
            report_type=request.report_type,
        )

        return {

            "success": True,

            "company": request.company,

            "report_type": request.report_type,

            "report": report,

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

# =====================================================
# Download PDF
# =====================================================

@app.get("/download/pdf")
def download_pdf():

    file = Path("reports/report.pdf")

    if not file.exists():

        raise HTTPException(
            status_code=404,
            detail="PDF not found",
        )

    return FileResponse(
        path=file,
        filename=file.name,
        media_type="application/pdf",
    )


# =====================================================
# Download PPT
# =====================================================

@app.get("/download/ppt")
def download_ppt():

    file = Path("reports/report.pptx")

    if not file.exists():

        raise HTTPException(
            status_code=404,
            detail="PowerPoint not found",
        )

    return FileResponse(
        path=file,
        filename=file.name,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
    )


# =====================================================
# Download Markdown
# =====================================================

@app.get("/download/md")
def download_md():

    file = Path("reports/report.md")

    if not file.exists():

        raise HTTPException(
            status_code=404,
            detail="Markdown not found",
        )

    return FileResponse(
        path=file,
        filename=file.name,
        media_type="text/markdown",
    )


# =====================================================
# Save Generated Reports
# =====================================================

def save_reports(pdf_path=None, ppt_path=None, md_path=None):

    reports = Path("reports")
    reports.mkdir(exist_ok=True)

    if pdf_path:
        shutil.copy(pdf_path, reports / "report.pdf")

    if ppt_path:
        shutil.copy(ppt_path, reports / "report.pptx")

    if md_path:
        shutil.copy(md_path, reports / "report.md")


# =====================================================
# Mount Frontend (MUST BE LAST)
# =====================================================

FRONTEND = Path(__file__).resolve().parent.parent / "frontend"

if FRONTEND.exists():

    app.mount(
        "/",
        StaticFiles(
            directory=str(FRONTEND),
            html=True,
        ),
        name="frontend",
    )

else:

    print(f"Frontend folder not found: {FRONTEND}")
    
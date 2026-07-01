const API = "http://127.0.0.1:8000";

const analyzeBtn = document.getElementById("analyzeBtn");
const companyInput = document.getElementById("company");
const reportSelect = document.getElementById("report");
const loading = document.getElementById("loading");

analyzeBtn.addEventListener("click", analyzeCompany);

async function analyzeCompany() {

    const company = companyInput.value.trim();
    const reportType = reportSelect.value;

    if (!company) {

        alert("Please enter a company name.");

        return;

    }

    loading.style.display = "block";

    analyzeBtn.disabled = true;
    analyzeBtn.innerHTML = "Analyzing...";

    try {

        const response = await fetch(
            `${API}/analyze`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    company: company,
                    report_type: reportType
                })
            }
        );

        const data = await response.json();

        if (!response.ok) {

            throw new Error(data.detail);

        }

        localStorage.setItem(
            "company_name",
            data.company
        );

        localStorage.setItem(
            "report_type",
            data.report_type
        );

        localStorage.setItem(
            "business_report",
            data.report
        );

        window.location.href = "report.html";

    }

    catch (err) {

        console.error(err);

        alert(err.message);

    }

    finally {

        loading.style.display = "none";

        analyzeBtn.disabled = false;

        analyzeBtn.innerHTML = "Analyze Company";

    }

}

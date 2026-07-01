// ========================================
// Load Report
// ========================================

const report = localStorage.getItem("business_report");

const company = localStorage.getItem("company_name");

const reportType = localStorage.getItem("report_type");

// ========================================
// Header
// ========================================

document.getElementById("companyName").innerHTML =
    company || "Business Report";

document.getElementById("reportType").innerHTML =
    reportType || "AI Generated Report";

// ========================================
// Report
// ========================================

document.getElementById("reportContent").innerHTML =

`<pre style="
white-space:pre-wrap;
font-family:inherit;
font-size:16px;
line-height:1.8;
color:white;
">

${report || "No Report Available"}

</pre>`;

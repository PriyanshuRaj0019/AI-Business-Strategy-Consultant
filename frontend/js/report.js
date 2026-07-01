const API = "http://127.0.0.1:8000";

// ======================================================
// Local Storage
// ======================================================

const company =
    localStorage.getItem("company_name") || "Company";

const reportType =
    localStorage.getItem("report_type") || "Business Report";

const report =
    localStorage.getItem("business_report") || "# No Report Generated";

const dashboard =
    JSON.parse(
        localStorage.getItem("dashboard") || "{}"
    );

// ======================================================
// Header
// ======================================================

document.getElementById("company").innerText =
    company;

document.getElementById("reportType").innerText =
    reportType;

const today = new Date();

document.getElementById("generatedDate").innerText =
    "Generated on: " +
    today.toLocaleDateString();

// ======================================================
// Report
// ======================================================

document.getElementById("report").innerHTML =
    marked.parse(report);

// ======================================================
// KPI Cards
// ======================================================

document.getElementById("healthScore").innerText =
    "92%";

document.getElementById("riskScore").innerText =
    "Low";

document.getElementById("industryGrowth").innerText =
    "21.7%";

document.getElementById("marketPosition").innerText =
    "#1";

// ======================================================
// Dashboard Data
// ======================================================

const market = dashboard.market || {

    share:82,

    growth:91,

    innovation:96,

    brand:95

};

const swot = dashboard.swot || {

    strength:95,

    weakness:45,

    opportunity:88,

    threat:52

};

// ======================================================
// Business Health Gauge
// ======================================================

new Chart(

    document.getElementById("healthChart"),

    {

        type:"doughnut",

        data:{

            labels:[

                "Health",

                "Remaining"

            ],

            datasets:[

                {

                    data:[92,8],

                    borderWidth:0

                }

            ]

        },

        options:{

            responsive:true,

            cutout:"75%",

            plugins:{

                legend:{

                    display:false

                }

            }

        }

    }

);

// ======================================================
// Market Position
// ======================================================

new Chart(

    document.getElementById("marketChart"),

    {

        type:"bar",

        data:{

            labels:[

                "Market Share",

                "Growth",

                "Innovation",

                "Brand"

            ],

            datasets:[

                {

                    label:company,

                    data:[

                        market.share,

                        market.growth,

                        market.innovation,

                        market.brand

                    ],

                    borderWidth:2

                }

            ]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false,

            scales:{

                y:{

                    beginAtZero:true,

                    max:100

                }

            }

        }

    }

);
// ======================================================
// SWOT Radar
// ======================================================

new Chart(

    document.getElementById("swotChart"),

    {

        type:"radar",

        data:{

            labels:[

                "Strength",

                "Weakness",

                "Opportunity",

                "Threat"

            ],

            datasets:[

                {

                    label:"SWOT Score",

                    data:[

                        swot.strength,

                        swot.weakness,

                        swot.opportunity,

                        swot.threat

                    ],

                    borderWidth:2,

                    fill:true

                }

            ]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false,

            scales:{

                r:{

                    beginAtZero:true,

                    max:100

                }

            }

        }

    }

);

// ======================================================
// Revenue Trend
// ======================================================

new Chart(

    document.getElementById("revenueChart"),

    {

        type:"line",

        data:{

            labels:[

                "2022",

                "2023",

                "2024",

                "2025",

                "2026"

            ],

            datasets:[

                {

                    label:"Revenue Outlook",

                    data:[

                        58,

                        71,

                        84,

                        92,

                        104

                    ],

                    borderWidth:3,

                    tension:0.4,

                    fill:false

                }

            ]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false,

            scales:{

                y:{

                    beginAtZero:false

                }

            }

        }

    }

);

// ======================================================
// Download Buttons
// ======================================================

document
.getElementById("pdfBtn")
.addEventListener(

    "click",

    () => {

        window.open(

            `${API}/download/pdf`,

            "_blank"

        );

    }

);

document
.getElementById("pptBtn")
.addEventListener(

    "click",

    () => {

        window.open(

            `${API}/download/ppt`,

            "_blank"

        );

    }

);

document
.getElementById("mdBtn")
.addEventListener(

    "click",

    () => {

        window.open(

            `${API}/download/md`,

            "_blank"

        );

    }

);

// ======================================================
// Console
// ======================================================

console.log("====================================");
console.log("AI Business Strategy Consultant");
console.log("Company:", company);
console.log("Report:", reportType);
console.log("Dashboard Loaded Successfully");
console.log("====================================");
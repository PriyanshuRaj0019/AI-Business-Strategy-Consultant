// ========================================
// Chart Defaults
// ========================================

Chart.defaults.color = "#ffffff";

Chart.defaults.font.family = "Poppins";

// ========================================
// Market Share
// ========================================

new Chart(

document.getElementById("marketChart"),

{

type:"doughnut",

data:{

labels:[
"Company",
"Competitors"
],

datasets:[{

data:[42,58],

backgroundColor:[
"#2563eb",
"#334155"
]

}]

}

}

);

// ========================================
// SWOT
// ========================================

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

datasets:[{

label:"SWOT",

data:[90,40,85,35],

fill:true,

backgroundColor:"rgba(37,99,235,.2)",

borderColor:"#3b82f6"

}]

}

}

);

// ========================================
// Porter
// ========================================

new Chart(

document.getElementById("porterChart"),

{

type:"bar",

data:{

labels:[

"Entry",

"Supplier",

"Buyer",

"Substitute",

"Rivalry"

],

datasets:[{

label:"Risk",

data:[3,2,4,2,5],

backgroundColor:"#0ea5e9"

}]

}

}

);

// ========================================
// Business Risk
// ========================================

new Chart(

document.getElementById("riskChart"),

{

type:"line",

data:{

labels:[

"Q1",

"Q2",

"Q3",

"Q4"

],

datasets:[{

label:"Risk Score",

data:[65,55,45,35],

borderColor:"#22c55e",

fill:false,

tension:.4

}]

}

}

);

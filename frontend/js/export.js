// ========================================
// Download Markdown
// ========================================

document.getElementById("downloadMd")

.addEventListener(

"click",

function(){

const report =

localStorage.getItem("business_report");

const blob = new Blob(

[report],

{

type:"text/markdown"

}

);

const url =

window.URL.createObjectURL(blob);

const a =

document.createElement("a");

a.href = url;

a.download =

"Business_Report.md";

a.click();

window.URL.revokeObjectURL(url);

}

);

// ========================================
// Download PDF
// ========================================

document.getElementById("downloadPdf")

.addEventListener(

"click",

function(){

window.open(

"http://127.0.0.1:8000/download/pdf"

);

}

);

// ========================================
// Download PPT
// ========================================

document.getElementById("downloadPpt")

.addEventListener(

"click",

function(){

window.open(

"http://127.0.0.1:8000/download/ppt"

);

}

);

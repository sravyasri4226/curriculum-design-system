// Configuration
const API_BASE_URL = "http://localhost:8000";

// DOM Elements
const curriculumForm = document.getElementById("curriculumForm");
const resultsSection = document.getElementById("resultsSection");
const curriculumOutput = document.getElementById("curriculumOutput");
const loadingSpinner = document.getElementById("loadingSpinner");
const errorMessage = document.getElementById("errorMessage");
const formSection = document.querySelector(".form-section");

// Event Listeners
document.addEventListener("DOMContentLoaded", () => {
    curriculumForm.addEventListener("submit", handleFormSubmit);
});

/**
 * Handle form submission
 */
async function handleFormSubmit(e) {
    e.preventDefault();

    // Get form values
    const topic = document.getElementById("topic").value.trim();
    const level = document.getElementById("level").value;
    const duration_weeks = parseInt(document.getElementById("duration_weeks").value);
    const learning_style = document.getElementById("learning_style").value;

    // Validate form
    if (!topic || !level || !duration_weeks || !learning_style) {
        showError("Please fill in all fields");
        return;
    }

    // Show loading state
    showLoading();

    try {
        // Call API
        const response = await fetch(`${API_BASE_URL}/generate-curriculum`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                topic,
                level,
                duration_weeks,
                learning_style,
            }),
        });

        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }

        const data = await response.json();

        if (data.status === "success") {
            displayCurriculum(data.curriculum);
        } else {
            throw new Error(data.status || "Failed to generate curriculum");
        }
    } catch (error) {
        showError(`Error: ${error.message}`);
        console.error("Full error:", error);
    }
}

/**
 * Display curriculum in results section
 */
function displayCurriculum(curriculum) {
    // Hide form section
    formSection.style.display = "none";

    // Show results section
    resultsSection.style.display = "block";

    // Hide loading spinner
    loadingSpinner.style.display = "none";

    // Hide error message
    errorMessage.style.display = "none";
    errorMessage.textContent = "";

    // Format and display curriculum
    const formattedCurriculum = formatCurriculum(curriculum);
    curriculumOutput.innerHTML = formattedCurriculum;

    // Scroll to results
    resultsSection.scrollIntoView({ behavior: "smooth" });
}

/**
 * Format curriculum text to HTML
 */
function formatCurriculum(text) {
    let html = text;

    // Convert markdown-style headers to HTML
    html = html.replace(/^# (.*?)$/gm, "<h3>$1</h3>");
    html = html.replace(/^## (.*?)$/gm, "<h4>$1</h4>");
    html = html.replace(/^### (.*?)$/gm, "<h5>$1</h5>");

    // Convert bold text
    html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

    // Convert italic text
    html = html.replace(/\*(.*?)\*/g, "<em>$1</em>");

    // Convert line breaks to paragraphs
    html = html.split("\n\n").map((para) => {
        if (para.match(/^<h[3-5]/)) {
            return para;
        }
        return `<p>${para.replace(/\n/g, "<br>")}</p>`;
    });

    return html.join("");
}

/**
 * Show loading spinner
 */
function showLoading() {
    resultsSection.style.display = "block";
    loadingSpinner.style.display = "flex";
    curriculumOutput.innerHTML = "";
    errorMessage.style.display = "none";
    errorMessage.textContent = "";
    formSection.style.display = "none";
}

/**
 * Show error message
 */
function showError(message) {
    resultsSection.style.display = "block";
    loadingSpinner.style.display = "none";
    curriculumOutput.innerHTML = "";
    errorMessage.style.display = "block";
    errorMessage.textContent = message;
}

/**
 * Reset form and return to input
 */
function resetForm() {
    // Reset form fields
    curriculumForm.reset();

    // Show form section
    formSection.style.display = "block";

    // Hide results section
    resultsSection.style.display = "none";

    // Scroll to form
    formSection.scrollIntoView({ behavior: "smooth" });

    // Clear outputs
    curriculumOutput.innerHTML = "";
    errorMessage.textContent = "";
}

/**
 * Test API connection
 */
async function testApiConnection() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        const data = await response.json();
        console.log("API Status:", data);
        return data.status === "healthy";
    } catch (error) {
        console.error("API Connection Error:", error);
        console.warn(
            "Backend not running. Make sure the FastAPI server is started."
        );
        return false;
    }
}

// Test API on page load
window.addEventListener("load", () => {
    testApiConnection();
});

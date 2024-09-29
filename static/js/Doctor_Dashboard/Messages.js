// Dropdown functionality for profile icon
const profileIcon = document.getElementById("profile-icon");
const dropdown = document.getElementById("dropdown");

profileIcon.addEventListener("click", () => {
  dropdown.style.display =
    dropdown.style.display === "block" ? "none" : "block";
});

// Close dropdown if clicked outside
window.addEventListener("click", (event) => {
  if (!profileIcon.contains(event.target)) {
    dropdown.style.display = "none";
  }
});

// Function to handle section display
function showSection(sectionId) {
  const sections = document.querySelectorAll(".section");
  sections.forEach((section) => {
    section.classList.remove("active");
  });
  document.getElementById(sectionId).classList.add("active");
}

// Function for no doctors message
function noDoctors() {
  const message = document.getElementById("message");
  message.textContent = "No doctors available for this specialization.";
}

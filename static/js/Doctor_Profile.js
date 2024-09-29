const hamburger = document.querySelector(".hamburger");
const mobileMenu = document.querySelector(".mobile-menu");

hamburger.addEventListener("click", () => {
  mobileMenu.classList.toggle("show");
});

document.addEventListener("DOMContentLoaded", function () {
  document.querySelector(".btn.about").addEventListener("click", function () {
    alert("About section clicked!");
  });

  document.querySelector(".btn.contact").addEventListener("click", function () {
    alert("Contact section clicked!");
  });

  document.querySelector(".btn.review").addEventListener("click", function () {
    alert("Review section clicked!");
  });

  var ctx = document.getElementById("practiceAreasChart").getContext("2d");
  var practiceAreasChart = new Chart(ctx, {
    type: "pie",
    data: {
      labels: ["No. of Patients", "Hours of Counsulataion", "Reviews"],
      datasets: [
        {
          label: "Practice Areas",
          data: [35, 35, 30],
          backgroundColor: ["#f44336", "#03a9f4", "#4caf50"],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "bottom",
        },
      },
    },
  });
});

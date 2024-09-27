const sign_up_btn = document.querySelector("#sign-up-btn");
const sign_in_btn = document.querySelector("#sign-in-btn");
const container = document.querySelector(".container");
const loginContainer = document.querySelector(".login-container"); // Select the login container

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
  container.classList.remove("change");

  // Delay showing the login container by 1 second (1000 milliseconds)
  setTimeout(() => {
    loginContainer.classList.add("active");
  }, 1000);
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");

  // Delay hiding the login container by 1 second (1000 milliseconds)
  setTimeout(() => {
    loginContainer.classList.remove("active");
  }, 1000);
});


const togglePassword = (toggleId, passwordId) => {
  const toggleIcon = document.querySelector(toggleId);
  const passwordField = document.querySelector(passwordId);

  if (toggleIcon && passwordField) {
    toggleIcon.addEventListener("click", () => {
      const type = passwordField.getAttribute("type") === "password" ? "text" : "password";
      passwordField.setAttribute("type", type);

      toggleIcon.classList.toggle("fa-eye");
      toggleIcon.classList.toggle("fa-eye-slash");
    });
  }
};

togglePassword("#toggle-login-password", "#login-password");

togglePassword("#toggle-signup-password", "#signup-password");

// login/Sign up functionality

 // login/Sign up functionality
 let signup = document.querySelector(".login-signup");
 let login = document.querySelector(".login-login");
 let slider = document.querySelector(".login-slider");
 let formSection = document.querySelector(".login-form-section");

 signup.addEventListener("click", () => {
     slider.classList.add("login-moveslider");
     formSection.classList.add("login-form-section-move");
 });

 login.addEventListener("click", () => {
     slider.classList.remove("login-moveslider");
     formSection.classList.remove("login-form-section-move");
 });

 
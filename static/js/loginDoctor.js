
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
 let change = document.querySelector(".change-color")

 signup.addEventListener("click", () => {
     slider.classList.add("login-moveslider");
     formSection.classList.add("login-form-section-move");
     change.classList.add("change-color")

   

 });

 login.addEventListener("click", () => {
     slider.classList.remove("login-moveslider");
     formSection.classList.remove("login-form-section-move");

 });


 function togglePasswordVisibility(inputId) {
    const inputField = document.getElementById(inputId);
    inputField.type = inputField.type === 'password' ? 'text' : 'password';
}

function checkPasswords() {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
    const errorElement = document.getElementById('password-error');

    if (password !== confirmPassword) {
        errorElement.style.display = 'block';
    } else {
        errorElement.style.display = 'none';
        // Submit the form or perform further actions
        alert('Form submitted successfully!');
    }
}

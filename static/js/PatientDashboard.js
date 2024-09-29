const specializations = [
    { name: 'Cardiology', doctors: 12 },
    { name: 'Dermatology', doctors: 5 },
    { name: 'Pediatrics', doctors: 8 },
    { name: 'Neurology', doctors: 0 },
    { name: 'Orthopedics', doctors: 7 },
    { name: 'Oncology', doctors: 3 },
    { name: 'Psychiatry', doctors: 4 }
];

// Sample doctor data in JSON format
const doctorsData = [
    {
        name: 'John Smith',
        qualification: 'MBBS',
        specialization: 'Cardiology',
        rating: 4.5,
        image: 'https://api.dicebear.com/9.x/adventurer/svg?seed=Jack'
    },
    {
        name: 'John Smith',
        qualification: 'MBBS',
        specialization: 'Cardiology',
        rating: 4.5,
        image: 'https://api.dicebear.com/9.x/adventurer/svg?seed=Jack'
    },
    {
        name: 'John Smith',
        qualification: 'MBBS',
        specialization: 'Cardiology',
        rating: 4.5,
        image: 'https://api.dicebear.com/9.x/adventurer/svg?seed=Jack'
    },
    {
        name: 'Jane Doe',
        qualification: 'MD',
        specialization: 'Dermatology',
        rating: 4.8,
        image: 'https://api.dicebear.com/9.x/adventurer/svg?seed=Jack'
    },
    {
        name: 'Jane Doe',
        qualification: 'MD',
        specialization: 'Dermatology',
        rating: 4.8,
        image: 'https://api.dicebear.com/9.x/adventurer/svg?seed=Jack'
    },
    {
        name: 'Jane Doe',
        qualification: 'MD',
        specialization: 'Dermatology',
        rating: 4.8,
        image: 'https://api.dicebear.com/9.x/adventurer/svg?seed=Jack'
    },
    {
        name: 'Emily Johnson',
        qualification: 'DNB',
        specialization: 'Pediatrics',
        rating: 4.7,
        image: 'https://api.dicebear.com/9.x/adventurer/svg?seed=Jack'
    },
    {
        name: 'Ana Johnson',
        qualification: 'DNB',
        specialization: 'Pediatrics',
        rating: 4.7,
        image: 'https://api.dicebear.com/9.x/adventurer/svg?seed=Jack'
    },
    {
        name: 'Lily Johnson',
        qualification: 'DNB',
        specialization: 'Pediatrics',
        rating: 4.7,
        image: 'https://api.dicebear.com/9.x/adventurer/svg?seed=Jack'
    }
];

// function filterSpecializations() {
//     const input = document.getElementById('searchInput').value.toLowerCase();
//     const specializationDiv = document.getElementById('specializations');
//     const resultsDiv = document.getElementById('results');
//     const cardContainer = resultsDiv.querySelector('.card-container');
//     specializationDiv.innerHTML = '';
//     cardContainer.innerHTML = ''; // Clear previous cards
//     resultsDiv.style.display = 'none'; // Hide results initially

//     const filteredSpecializations = specializations.filter(s => s.name.toLowerCase().includes(input));

//     filteredSpecializations.forEach(specialization => {
//         const div = document.createElement('div');
//         div.classList.add('specialization-item');
//         div.textContent = specialization.name;
//         div.onclick = () => showResults(specialization);
//         specializationDiv.appendChild(div);
//     });

//     specializationDiv.style.display = filteredSpecializations.length > 0 ? 'block' : 'none';
// }

// function showResults(specialization) {
//     const resultsDiv = document.getElementById('results');
//     const inputField = document.getElementById('searchInput');
//     const cardContainer = resultsDiv.querySelector('.card-container');

//     // Set the input field value to the selected specialization
//     inputField.value = specialization.name;

//     // Clear previous cards
//     cardContainer.innerHTML = '';

//     // Filter doctors based on specialization
//     const filteredDoctors = doctorsData.filter(doctor => doctor.specialization === specialization.name);

//     // Populate cards with doctor data
//     if (filteredDoctors.length > 0) {
//         filteredDoctors.forEach(doctor => {
//             const card = document.createElement('div');
//             card.classList.add('card1');
//             card.innerHTML = `
//                 <div class="cardIcon">
//                     <img src="${doctor.image}" alt="${doctor.name}">
//                 </div>
//                 <div class="card-title">
//                     <h3>${doctor.name}</h3>
//                 </div>
//                 <div class="cardQualification">
//                     <p><span>Qualification: </span>${doctor.qualification}</p>
//                 </div>
//                 <div class="cardSpecalization">
//                     <p><span>Specialization: </span>${doctor.specialization}</p>
//                 </div>
//                 <div class="cardRating">
//                     <p><span>Rating: </span>${doctor.rating}</p>
//                 </div>
//                 <button class="cardBook">Book Now</button>
//             `;
//             cardContainer.appendChild(card);
//         });

//         resultsDiv.style.display = 'block'; // Show results section if there are doctors
//     } else {
//         resultsDiv.innerHTML = '<p class="default-message">No doctors available for this specialization.</p>';
//         resultsDiv.style.display = 'block'; // Show results section with no doctors message
//     }

//     // Hide specialization dropdown
//     document.getElementById('specializations').style.display = 'none';
// }

// Add event listener for input focus to hide dropdown

function createSpecializationButtons() {
    const specializationDiv = document.getElementById('specializations');
    specializationDiv.innerHTML = ''; // Clear existing buttons

    specializations.forEach(specialization => {
        const button = document.createElement('button');
        button.classList.add('specialization-button');
        button.textContent = specialization.name;
        button.onclick = () => showResults(specialization);
        specializationDiv.appendChild(button);
    });
}

function showResults(specialization) {
    const resultsDiv = document.getElementById('results');
    const cardContainer = resultsDiv.querySelector('.card-container');

    // Clear previous cards
    cardContainer.innerHTML = '';

    // Filter doctors based on specialization
    const filteredDoctors = doctorsData.filter(doctor => doctor.specialization === specialization.name);

    // Populate cards with doctor data
    if (filteredDoctors.length > 0) {
        filteredDoctors.forEach(doctor => {
            const card = document.createElement('div');
            card.classList.add('card1');
            card.innerHTML = `
                <div class="cardIcon">
                    <img src="${doctor.image}" alt="${doctor.name}">
                </div>
                <div class="card-title">
                    <h3>${doctor.name}</h3>
                </div>
                <div class="cardQualification">
                    <p><span>Qualification: </span>${doctor.qualification}</p>
                </div>
                <div class="cardSpecalization">
                    <p><span>Specialization: </span>${doctor.specialization}</p>
                </div>
                <div class="cardRating">
                    <p><span>Rating: </span>${doctor.rating}</p>
                </div>
                <button class="cardBook">Book Now</button>
            `;
            cardContainer.appendChild(card);
        });

        resultsDiv.style.display = 'block'; // Show results section if there are doctors
    } else {
        resultsDiv.innerHTML = '<p class="default-message">No doctors available for this specialization.</p>';
        resultsDiv.style.display = 'block'; // Show results section with no doctors message
    }
}

// Call to create specialization buttons on page load
createSpecializationButtons();


document.getElementById('searchInput').addEventListener('focus', () => {
    document.getElementById('specializations').style.display = 'none'; // Hide dropdown when input is focused
});

const doctorList = [
    { id: 1, name: 'Dr. Smith', specialty: 'Cardiology', rating: 4.5 },
    { id: 2, name: 'Dr. Johnson', specialty: 'Dermatology', rating: 4.7 },
    { id: 3, name: 'Dr. Lee', specialty: 'Pediatrics', rating: 4.8 },
];

const hamburger = document.querySelector(".hamburger");
const mobileMenu = document.querySelector(".mobile-menu");

hamburger.addEventListener("click", () => {
  mobileMenu.classList.toggle("show");
});




let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
    nav.classList.toggle("navclose");
})

function toggleDropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dp')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}


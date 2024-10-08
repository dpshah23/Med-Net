const hamburger = document.querySelector(".hamburger");
const mobileMenu = document.querySelector(".mobile-menu");

hamburger.addEventListener("click", () => {
  mobileMenu.classList.toggle("show");
});

function toggleChatbot() {
  const chatbotContainer = document.getElementById('chatbotContainer');
  chatbotContainer.style.display = chatbotContainer.style.display === 'none' ? 'block' : 'none';
}


function displayMessage(sender, message) {
  const messagesContainer = document.getElementById('chatbotMessages');
  const messageElement = document.createElement('div');
  messageElement.textContent = `${sender}: ${message}`;
  messagesContainer.appendChild(messageElement);
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

async function getChatbotResponse(message) {
  const response = await fetch('http://127.0.0.1:8000/api_reply/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ question: message })
  });
  console.log(response);
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return await response.json();

}

document.getElementById('chatbotInput').addEventListener('keypress', function (event) {
  if (event.key === 'Enter') {
    sendMessage();
  }
});

async function sendMessage() {
  const input = document.getElementById('chatbotInput');
  const message = input.value;
  if (message.trim() === '') return;

  // Display user message
  const userMessageElement = document.createElement("div");
  userMessageElement.className = "message user-message";
  userMessageElement.innerHTML = "<strong>You:</strong> " + message;
  document.getElementById("chatbotMessages").appendChild(userMessageElement);

  input.value = "";

  // Send message to the API and display the bot response
  try {
    const response = await getChatbotResponse(message);
    const chatbotMessageElement = document.createElement("div");
    chatbotMessageElement.className = "message chatbot-message";
    chatbotMessageElement.innerHTML = "<strong>Bot:</strong> " + response.answer;
    document.getElementById("chatbotMessages").appendChild(chatbotMessageElement);
  } catch (error) {
    console.error('Error:', error);
    const chatbotMessageElement = document.createElement("div");
    chatbotMessageElement.className = "message chatbot-message";
    chatbotMessageElement.innerHTML = "<strong>Bot:</strong> " + "Sorry, something went wrong.";
    document.getElementById("chatbotMessages").appendChild(chatbotMessageElement);
  }

  // Scroll to the latest message
  document.getElementById("chatbotMessages").scrollTop =
    document.getElementById("chatbotMessages").scrollHeight;
}

document.addEventListener('DOMContentLoaded', () => {
  const chatMessages = document.getElementById('chat-messages');
  const chatForm = document.getElementById('chat-form');
  const userInput = document.getElementById('user-input');
  const sendBtn = document.getElementById('send-btn');

  // Prevent script from breaking if elements aren't found
  if (!chatForm || !userInput || !chatMessages) {
    console.error("Required chat elements missing in DOM.");
    return;
  }

  // Generate or retrieve persistent user_id for session memory
  let userId = localStorage.getItem('chat_user_id');
  if (!userId) {
    userId = 'user_' + Math.random().toString(36).substring(2, 9);
    localStorage.setItem('chat_user_id', userId);
  }

  // Append a chat bubble to the UI
  function appendMessage(role, text) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', role);

    const contentDiv = document.createElement('div');
    contentDiv.classList.add('message-content');
    contentDiv.textContent = text;

    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Add animated typing indicator
  function showTypingIndicator() {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', 'assistant');
    messageDiv.id = 'typing-indicator';

    const contentDiv = document.createElement('div');
    contentDiv.classList.add('message-content', 'typing-dots');
    contentDiv.innerHTML = '<span>.</span><span>.</span><span>.</span>';

    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Remove typing indicator
  function removeTypingIndicator() {
    const indicator = document.getElementById('typing-indicator');
    if (indicator) indicator.remove();
  }

  // Handle message submission
  chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = userInput.value.trim();
    if (!message) return;

    // 1. Render User Message
    appendMessage('user', message);
    userInput.value = '';
    userInput.disabled = true;
    if (sendBtn) sendBtn.disabled = true;

    // 2. Show Typing Dots
    showTypingIndicator();

    try {
      // 3. Send request to FastAPI endpoint
      const response = await fetch('/chat', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json' 
        },
        body: JSON.stringify({
          user_id: userId,
          message: message
        })
      });

      if (!response.ok) {
        throw new Error(`Server status error: ${response.status}`);
      }

      const data = await response.json();
      removeTypingIndicator();

      // 4. Render Bot Response
      if (data && data.response) {
        appendMessage('assistant', data.response);
      } else {
        appendMessage('assistant', "Received empty response from server.");
      }

    } catch (err) {
      console.error("Chat Error:", err);
      removeTypingIndicator();
      appendMessage('assistant', "Sorry, I ran into an error connecting to the server. Please try again.");
    } finally {
      // Re-enable input focus
      userInput.disabled = false;
      if (sendBtn) sendBtn.disabled = false;
      userInput.focus();
    }
  });
});

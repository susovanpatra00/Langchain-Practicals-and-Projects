# Enhanced Q&A Chatbot

This Streamlit application is an "Enhanced Q&A Chatbot" that leverages various open-source language models through the OllamaLLM integration, allowing users to interact with AI models in a user-friendly interface.

### Key Features:
1. **Model Selection**: Users can choose from three available language models:
   - **gemma2:2b**: A medium-sized language model.
   - **mistral**: A model optimized for performance and accuracy.

2. **Adjustable Parameters**:
   - **Temperature**: A slider allows users to control the creativity of the responses, with values ranging from 0.0 (more deterministic) to 1.0 (more creative and varied).
   - **Max Tokens**: Another slider lets users set the maximum length of the response, ranging from 50 to 300 tokens.

3. **User Interaction**:
   - Users input their questions in a text field, and the app generates a response using the selected model and parameters.
   - The response is processed through a custom prompt template, which includes system instructions and user queries, ensuring consistent and helpful responses.

4. **Environment Configuration**:
   - The app loads environment variables from a `.env` file, including the LangChain API key and project settings, which are crucial for integrating with the LangChain platform and enabling tracing for debugging and monitoring.

This setup provides a flexible and interactive chatbot experience, where users can experiment with different models and settings to generate tailored responses.
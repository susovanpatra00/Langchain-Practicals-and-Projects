## Ollama

In this section I tried how to build a simple Generative AI application using LangChain and the Ollama Gemma2:2b model, integrated with the Streamlit framework for a user-friendly interface. The application leverages LangChain's capabilities for prompt management, language model interaction, and output parsing.

### Key Features:

1. **Environment Setup**:
   - Loaded environment variables for LangChain API and project setup using `dotenv`.
   - Enabled LangSmith tracing for monitoring and debugging during development.

2. **Prompt Template**:
   - Created a chat prompt template where the system behaves as a helpful assistant, responding to user questions.

3. **Ollama Gemma2:2b Model**:
   - Integrated the Ollama Gemma2:2b model via LangChain's Ollama LLM wrapper to generate responses.

4. **Streamlit Integration**:
   - Used Streamlit to build a simple web app that allows users to input their questions and receive responses from the model in real time.


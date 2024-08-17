# LangChain Expression Language (LCEL) and API Server

This section demonstrates the use of LangChain Expression Language (LCEL) for building a language translation application and serving it as an API using `FastAPI` and `LangServe`.

## Key Components

1. **LCEL (LangChain Expression Language)**: Used to express and chain together different components of the language model pipeline.

2. **Groq LPU**: Utilized the Groq Language Processing Unit for efficient AI inference.

3. **ChatGroq Model**: Implemented a language model using the Gemma2-9b-it model through the Groq API.

4. **Prompt Templates**: Created reusable prompt templates for translation tasks.

5. **FastAPI and LangServe**: Set up a web API to serve the language model chain.

## Implementations

1. Set up environment variables for API keys (OpenAI and Groq).
2. Initialized a ChatGroq model.
3. Created a basic translation chain using LCEL.
4. Developed a more flexible translation chain using prompt templates.
5. Built a FastAPI application to serve the translation chain as an API.

## Learnings

1. **LCEL Basics**: How to chain together different components (prompts, models, parsers) using the `|` operator.
2. **Prompt Engineering**: Creating and using prompt templates for more dynamic interactions.
3. **Model Integration**: Integrating the Groq API and using the Gemma2-9b-it model.
4. **API Development**: Setting up a FastAPI application and using LangServe to easily add routes for your LangChain runnable.

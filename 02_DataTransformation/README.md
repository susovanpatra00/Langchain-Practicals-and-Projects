## Data Transformation - Document Splitters

This section of the notebook covers techniques for transforming and processing ingested data, preparing it for embedding and further analysis. The key transformations learned include:

1. **RecursiveCharacterTextSplitter**:
   - Splits text data into smaller chunks based on characters, using a recursive approach to handle complex structures.

2. **CharacterTextSplitter**:
   - A simpler splitter that breaks down text into smaller character-based chunks, ideal for straightforward text splitting.

3. **HTMLTextSplitter**:
   - Specifically designed for splitting HTML content, preserving the structure and ensuring that HTML tags are properly managed.

4. **RecursiveJsonSplitter**:
   - Handles JSON data, recursively splitting it to manage nested structures and large JSON files efficiently.

### Additional Resources:
For more details on other available splitters and transformations, refer to the LangChain documentation:
[LangChain Document Transformers](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/)

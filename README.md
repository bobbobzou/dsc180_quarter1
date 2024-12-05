
# Guardrails Implementation in Generative AI Apps

This project demonstrates the implementation of Google’s Perspective API as a guardrail in a generative AI-powered translation application. The application utilizes OpenAI's GPT-3.5-turbo for language translation, with content moderation applied to ensure responsible outputs.

## Requirements
Before running this project, ensure you have the following:
1. **API Keys**: Obtain API keys for both OpenAI and Google’s Perspective API. Store them in a `.env` file in the root directory with the following structure:
   ```plaintext
   OPENAI_API_KEY=<your_openai_api_key>
   PERSPECTIVE_API_KEY=<your_perspective_api_key>
   ```
2. **Install Dependencies**: Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

## Files Overview
- **`replication.py`**: 
  - The main Python file containing the Streamlit application with the Perspective API guardrail installed.
  - Allows users to interact with the translation system and observe content moderation in action.
  - Users can adjust the moderation threshold within this file to experiment with different levels of sensitivity.
- **`test_data.ipynb`**: 
  - A Jupyter notebook containing a manually created dataset for testing.
  - Includes prompts and their associated labels to evaluate the performance of the guardrail system.
  - Prompts can be customized, allowing users to test alternative inputs for diverse scenarios.
- **`old_app.py`**: 
  - A deprecated version of the application, showing the original implementation without the updated guardrail system.
  - Useful for comparing performance or exploring legacy functionality.

## Running the Application
To launch the application, use the following command:
```bash
streamlit run replication.py
```
This will start a Streamlit server, allowing you to interact with the application in your web browser.

## Adjusting Thresholds
The moderation threshold for Google’s Perspective API can be adjusted in `replication.py`. Locate the `threshold` variable in the `check_profanity_perspective` function and modify its value to test different sensitivity levels:
```python
# Example threshold adjustment
threshold = 0.3  # Change to your preferred value
```

## Dataset
The dataset used for testing is included in `test_data.ipynb`. Key features of the dataset include:
- **Manually Created Prompts**: A balanced dataset with half the sentences containing inappropriate content (e.g., toxicity, profanity) and the other half consisting of neutral or appropriate sentences.
- **Labels**: Each sentence is labeled for:
  - `toxicity`
  - `insult`
  - `profanity`
  - `identity attack`
  - `okay to translate`
- **Customizable Prompts**: Users can modify the prompts to test different scenarios and evaluate the system’s performance under varied inputs.

## Notes
- **API Limits**: Be mindful of the API limits for both Google’s Perspective API and OpenAI services, which could impact performance for large-scale testing.
- **Guardrail Focus**: This application uses Perspective API as an **output guardrail**, moderating content after the LLM generates translations. Input guardrails are not implemented but could be added in future iterations.
- **Scalability**: While the current implementation is ideal for small-scale demonstrations, large-scale deployments may require optimization to handle API rate limits and latency issues.

This project provides a practical example of combining generative AI models with robust moderation systems to ensure safe and responsible AI-driven applications.

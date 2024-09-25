**UCR SP Search** is a project designed to automate the process of categorizing university courses based on their alignment with the United Nations' 17 Sustainable Development Goals (SDGs). The system analyzes course descriptions and predicts whether a course is “sustainable” and which SDG it aligns with. For example, if a course focuses on reducing economic disparity, it would be classified under SDG 1: No Poverty. This project helps universities identify and promote courses that contribute to sustainability, which can lead to increased funding from organizations like the UN.

### Technologies and Tools
- **Flask**: For the backend API and server-side logic.
- **Elasticsearch**: To index and search course data efficiently.
- **PostgreSQL**: For managing and storing course data.
- **SQLite**: Used for lightweight local database handling.
- **Next.js**: For building the user-facing frontend.

### Project Purpose
The project aims to streamline the process of classifying university courses into sustainable development categories, helping universities showcase their contribution to sustainability goals. The long-term goal is to enhance the accuracy of SDG alignment predictions using machine learning and natural language processing (NLP) techniques.

## Environment Variables
```env
ELASTIC_SEARCH_API_ENDPOINT=
ELASTIC_SEARCH_API_KEY=
```

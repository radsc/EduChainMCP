**Overview**

This repository demonstrates an MCP (Modular Content Provider) server built using the EduChain library to generate educational content such as MCQs and lesson plans.

**Setup**

Requirements

•	Python 3.8+

•	Install dependencies: pip install fastapi uvicorn educhain

**Set OPEN API KEY :** set OPENAI_API_KEY=replace with your key

**Running the Server** (Command w.r.t Anaconda prompt)

python -m uvicorn server:app --reload --port 8000

**API Endpoints**

POST /generate-questions
MCQ generation
curl -X POST "http://127.0.0.1:8000/generate-questions" -H "Content-Type: application/json" -d "{\"topic\": \"Python loops\", \"num_questions\": 5}"

POST /generate-lesson-plan
Lesson plan generation
curl -X POST "http://127.0.0.1:8000/generate-lesson-plan " -H "Content-Type: application/json" -d "{\"topic\": \" Algebra \"}"

**Testing using Swagger UI:**

Once the MCP server is up and running, open the URL "http://127.0.0.1:8000/docs" in the browser to open Swagger UI landing page. Expand each endpoint and execute by providing the json request.



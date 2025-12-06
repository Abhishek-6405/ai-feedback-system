project:
  title: "Task 2 – Two-Dashboard AI Feedback System (Web-Based)"
  description: >
    This project is a complete AI-powered user feedback collection and analysis system
    built using Streamlit and Google Gemini AI as part of the AI Intern Take-Home Assessment.
    It allows users to submit feedback and ratings, AI to generate a response, summary,
    and admin action, and the admin to view, analyze, and download all feedback.
    All features are deployed in a single cloud application with real-time synchronization.

deployment:
  live_app:
    description: "User & Admin Combined Deployment (Final Working App)"
    link: "PASTE YOUR STREAMLIT DEPLOYMENT LINK HERE"
    note: "Single deployment contains both User Feedback page and Admin Dashboard via sidebar navigation."

problem_statement: >
  Design and deploy an AI-powered feedback system where users can submit ratings and textual
  feedback, AI automatically generates a polite reply, internal summary, and recommended
  admin action, and the admin can view analytics and export feedback data.

deployment_issue_and_resolution:
  initial_approach:
    description: "Two Separate Streamlit Applications"
    apps:
      - app_user.py: "User feedback submission app"
      - app_admin.py: "Admin dashboard app"
    local_status: "Worked perfectly in local execution"

  issue_after_cloud_deployment:
    platform: "Streamlit Cloud"
    reasons:
      - "Each deployed app runs in a separate isolated container"
      - "Each container has its own independent file system"
    result:
      - "User app wrote to its own data.csv"
      - "Admin app attempted to read a different data.csv"
      - "Admin could not see user submissions"
    conclusion: "Worked locally but failed on cloud due to container isolation"

  final_solution:
    approach:
      - "Merged User & Admin into a single Streamlit application"
      - "Implemented sidebar navigation"
      - "Used one shared data.csv file"
    outcome:
      - "Real-time data synchronization"
      - "Fully cloud-compatible"
      - "Stable production deployment"
    learned: "Demonstrates real-world cloud debugging and deployment architecture handling"

features:
  user_feedback_page:
    - "1–5 star rating system"
    - "Text-based review submission"
    - "AI-generated polite user response"
    - "AI-generated internal summary"
    - "AI-generated admin recommended action"
    - "Automatic CSV storage"
    - "Input validation and AI fallback handling"

  admin_dashboard:
    - "Live feedback table"
    - "Rating distribution bar chart"
    - "Download complete feedback CSV"
    - "Auto-refresh after every submission"

  ai_intelligence:
    provider: "Google Gemini API"
    capabilities:
      - "Auto-detects supported AI model"
      - "Structured output parsing"
      - "Fail-safe fallback handling if AI fails"
    output_format:
      - "AI_RESPONSE"
      - "SUMMARY"
      - "ACTION"

technology_stack:
  - "Python"
  - "Streamlit"
  - "Google Gemini AI"
  - "Pandas"
  - "CSV File System"
  - "GitHub"
  - "Streamlit Cloud"

project_structure:
  root: "task2-ai-feedback-system/"
  files:
    - "app.py: Single combined User + Admin application"
    - "data.csv: Feedback storage"
    - "requirements.txt: Dependencies"
    - "README.md: Documentation"
    - ".gitignore"

environment_setup:
  steps:
    - step: "Clone Repository"
      command:
        - "git clone https://github.com/Abhishek-6405/task2-ai-feedback-system.git"
        - "cd task2-ai-feedback-system"

    - step: "Create Virtual Environment"
      command:
        - "python -m venv task2env"

    - step: "Activate Virtual Environment"
      command:
        - "task2env\\Scripts\\activate"

    - step: "Install Dependencies"
      command:
        - "pip install -r requirements.txt"

    - step: "Set Gemini API Key (Local)"
      command:
        - "setx GEMINI_API_KEY \"YOUR_API_KEY\""
      note: "Restart terminal after setting the key"

    - step: "Set API Key on Streamlit Cloud"
      instructions:
        - "Go to App Settings → Secrets"
        - "Add GEMINI_API_KEY = \"YOUR_API_KEY\""

run_locally:
  command: "streamlit run app.py"

ai_usage:
  purposes:
    - "User response generation"
    - "Review summarization"
    - "Recommended admin actions"
  notes:
    - "Only prompt engineering is used"
    - "No model fine-tuning required"

sample_stored_output:
  columns:
    - "Timestamp"
    - "Rating"
    - "Review"
    - "AI Response"
    - "Summary"
    - "Action"
  example:
    Timestamp: "2025-12-06"
    Rating: 4
    Review: "Service was good"
    AI_Response: "Thank you for your feedback"
    Summary: "Positive experience"
    Action: "No action required"

error_handling_and_reliability:
  - "Prevents empty review submission"
  - "Gemini API exception handling"
  - "Default fallback responses"
  - "Auto CSV creation"
  - "Cloud-safe single instance storage"
  - "Production-safe deployment behavior"

final_project_status:
  - "Fully Deployed on Streamlit Cloud"
  - "Gemini AI Integrated Successfully"
  - "User & Admin Data Synced in Real-Time"
  - "CSV Download Enabled"
  - "Cloud Isolation Bug Permanently Fixed"
  - "Internship Task 2 Successfully Completed"

submission_checklist:
  - "GitHub Repository"
  - "Streamlit Deployment Link"
  - "AI Model Integration"
  - "User Feedback System"
  - "Admin Dashboard"
  - "Cloud Debugging Explanation"
  - "CSV Export"

author:
  name: "Abhishek Maurya"
  role: "AI Intern – Take Home Assessment"
  github: "https://github.com/Abhishek-6405"

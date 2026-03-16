# 🔧 Term-AI-Debugger 
### A Multimodal Gemini 2.0 Flash Terminal Assistant

[![Gemini 2.0 Flash](https://img.shields.io/badge/Model-Gemini%202.0%20Flash-blue)](https://deepmind.google/technologies/gemini/)
[![Google Cloud Run](https://img.shields.io/badge/Deployment-Cloud%20Run-orange)](https://cloud.google.com/run)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Inspiration
As a first-year engineering student at **Symbiosis Institute of Technology (SIT), Pune**, I noticed a recurring theme: students losing hours of productivity to cryptic terminal errors and complex CLI syntax. I built **Term-AI-Debugger** to serve as a "Senior Engineer in a Box," providing real-time, intelligent guidance directly where developers work—the terminal.

## 🛠️ Key Features
- **Natural Language CLI:** Convert human intent (e.g., "ask how to find files over 100MB") into perfect shell commands using Gemini 2.0 Flash.
- **Intelligent Error Analysis:** Automatically intercepts shell failures to explain the root cause and provide a copy-pasteable fix.
- **Multimodal Screenshot Debugging:** Uses Gemini's vision capabilities to analyze terminal or IDE screenshots, identifying syntax errors or environment issues that text alone might miss.

## 🏗️ Technical Architecture
- **Language:** Python 3.10+
- **API Framework:** Flask (stateless microservice)
- **AI Engine:** Gemini 2.0 Flash via Google Vertex AI SDK
- **Infrastructure:** Dockerized container deployed on **Google Cloud Run**

## 🚀 Deployment & Setup
The backend is live and serving traffic at:  
`https://gemini-live-backend-816727277645.us-central1.run.app`

### Local Development
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/jayvee2010/term-ai-debugger.git](https://github.com/jayvee2010/term-ai-debugger.git)
   cd term-ai-debugger

<h1><b>AI Travel Itinerary Planner</b></h1>
<h3>An Intelligent, LLM-Powered Travel Planning System with Cost Estimation & Route Optimization</h3>

<p>
Planning a trip shouldn't be overwhelming — it should be <b>intelligent</b>, <b>personalized</b>, and <b>effortless</b>.<br>
AI Travel Itinerary Planner introduces an advanced travel planning pipeline that leverages <b>Meta LLaMA 4 Scout</b>, real-time <b>weather forecasting</b>, automated <b>cost estimation</b>, and <b>Google Maps integration</b> to generate optimized multi-day itineraries tailored to your interests.
</p>

<p>
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-3.10+-skyblue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-Interactive%20UI-red?style=for-the-badge&logo=streamlit"/>
  <img src="https://img.shields.io/badge/LLaMA-4%20Scout%2017B-purple?style=for-the-badge&logo=meta"/>
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge"/>
</p>

---

## Overview

AI Travel Itinerary Planner answers a fundamental travel planning question:

> **"How can AI transform trip planning from hours of research into a single, intelligent conversation?"**

Using the powerful **Meta LLaMA 4 Scout 17B 16E Instruct** model via Groq API, this application:

- Automatically detects your current location
- Generates personalized day-by-day itineraries based on your travel focus
- Estimates real-world costs for attractions and activities
- Fetches live weather forecasts for your destination
- Creates optimized Google Maps routes for seamless navigation
- Refines itineraries based on natural language feedback
- Integrates flight booking with pre-filled dates

This project is **fully functional**, **user-friendly**, and designed for **real-world travel planning**.

---

## Key Features

| Category                  | Description                                                           |
| ------------------------- | --------------------------------------------------------------------- |
| **AI-Powered Planning**   | LLaMA 4 Scout 17B for intelligent itinerary generation                |
| **Geolocation Detection** | Automatic user location detection via IP-API                          |
| **Weather Integration**   | Real-time weather forecasts for each day of your trip                 |
| **Cost Estimation**       | LLM-based cost analysis with daily and total trip expense calculation |
| **Route Optimization**    | Google Maps integration for multi-stop navigation                     |
| **Flight Integration**    | Direct links to Google Flights with pre-filled travel dates           |
| **Feedback Refinement**   | Natural language itinerary updates based on user preferences          |
| **Interactive UI**        | Streamlit-powered web interface for seamless user experience          |

---

## How It Works

<table>
<tr>
<td width="50%" valign="top">

### **1. Input Your Preferences**
- Destination city
- Trip duration (1-7 days)
- Travel focus:
  - 🎭 Culture (museums, galleries, history)
  - 🍜 Food (markets, restaurants, cuisine)
  - 🌲 Nature (parks, hiking, scenery)
  - 💕 Romantic (couples' activities)
  - 🎉 Party (nightlife, entertainment)
- Departure date (auto-calculates return date)

</td>
<td width="50%" valign="top">

### **2. AI-Powered Generation**
- LLaMA 4 Scout analyzes your preferences
- Generates detailed day-by-day itinerary
- Lists specific attractions with descriptions
- Estimates costs for each location
- Fetches weather forecasts
- Creates optimized routes

</td>
</tr>

<tr>
<td width="50%" valign="top">

### **3. Review & Plan**
- View complete itinerary breakdown
- Check daily weather conditions
- Review cost estimates per day
- Access Google Maps routes
- Search for flights with one click

</td>
<td width="50%" valign="top">

### **4. Refine with Feedback**
- Provide natural language feedback:
  - "Add more food experiences"
  - "Reduce walking distance"
  - "Skip day 3"
  - "Include more nightlife"
- AI regenerates itinerary based on your input
- Maintains location accuracy and format consistency

</td>
</tr>
</table>

---

## Sample Output

### 📍 **4-Day Tokyo Itinerary (Culture Focus)**

| Day | Highlights | Daily Cost | Weather |
|-----|------------|------------|---------|
| **Day 1** | Sensō-ji Temple, Tokyo National Museum, Ueno Park | $85 | ⛅ Partly Cloudy, 18°C |
| **Day 2** | Meiji Shrine, Yoyogi Park, Harajuku Shopping | $70 | ☀️ Sunny, 20°C |
| **Day 3** | Imperial Palace, Tsukiji Outer Market, Ginza | $95 | 🌧️ Light Rain, 16°C |
| **Day 4** | Asakusa Culture Center, Sumida River Cruise | $60 | ☀️ Clear, 19°C |

**Total Trip Cost:** ~$310 (attractions + activities)

> 📌 **Note:** Costs exclude flights, accommodation, and meals. See full PDF output example: [AI_Trip_Itinerary.pdf](AI_Trip_Itinerary.pdf)

---

## Tech Stack

<p>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" height="45" />
<img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" height="45" />
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Meta-Logo.png/120px-Meta-Logo.png" height="45" />
<img src="https://www.gstatic.com/images/branding/product/2x/maps_96dp.png" height="45" />
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" height="45" />
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" height="45" />
</p>

### **Core Technologies**

| Technology | Purpose |
|------------|---------|
| **Python 3.10+** | Core programming language |
| **Streamlit** | Interactive web UI framework |
| **Groq API** | LLM inference platform |
| **Meta LLaMA 4 Scout 17B** | AI model for itinerary generation |
| **IP-API** | Geolocation detection |
| **wttr.in** | Weather forecasting API |
| **Google Maps API** | Route optimization and directions |
| **Google Flights** | Flight search integration |

---

## Installation & Usage

### **Prerequisites**
```bash
Python 3.10 or higher
Groq API key (get one at https://console.groq.com)
```

### **Setup**

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/AI-Travel-Itenary-Planner.git
cd AI-Travel-Itenary-Planner
```

2. **Install dependencies**
```bash
pip install streamlit openai requests
```

3. **Configure API Key**

Create an `AI.env` file or update the API key in `GeoTravelAI_AllInOne.py`:
```python
GROQ_API_KEY = "your_groq_api_key_here"
```

4. **Run the application**
```bash
streamlit run GeoTravelAI_AllInOne.py
```

5. **Open your browser**
```
Navigate to: http://localhost:8501
```

---

## Project Structure

```
AIT/
│
├── GeoTravelAI_AllInOne.py    # Main application (233 lines)
│   ├── Location Detection      # IP-API geolocation
│   ├── Itinerary Generation    # LLM-powered planning
│   ├── Weather Integration     # wttr.in API
│   ├── Cost Estimation         # LLM-based cost analysis
│   ├── Route Optimization      # Google Maps integration
│   └── Feedback Refinement     # Natural language updates
│
├── AI.env                      # Environment variables (API keys)
├── AI_Trip_Itinerary.pdf       # Sample output (Tokyo 4-day trip)
└── README.md                   # This file
```

---

## Key Components

### **1. Location Detection**
```python
def get_user_location()
    → Detects user's city via IP-API
    → Fallback: "Unknown" if detection fails
```

### **2. Itinerary Generation**
```python
def generate_itinerary(destination, days, focus)
    → Input: City, duration (1-7 days), travel focus
    → Output: Structured day-by-day itinerary with locations
    → Model: Meta LLaMA 4 Scout 17B via Groq
```

### **3. Weather Forecasting**
```python
def get_weather_forecast(city)
    → API: wttr.in
    → Returns: Current weather conditions
    → Timeout: 5 seconds
```

### **4. Cost Estimation**
```python
def estimate_costs(itinerary)
    → Extracts locations from itinerary text
    → LLM estimates tourist costs in USD
    → Aggregates daily and total trip costs
    → Regex parsing: $XX per location
```

### **5. Route Planning**
```python
def build_directions_link(origin, locations)
    → Creates Google Maps multi-stop route
    → Returns: Direct link to optimized navigation
```

### **6. Feedback Refinement**
```python
def refine_itinerary(original, feedback)
    → Input: Current itinerary + user feedback
    → LLM regenerates itinerary based on preferences
    → Maintains format consistency and real locations
```

---

## Advanced Features

### **🎯 Travel Focus Categories**

| Focus | What You'll Get |
|-------|-----------------|
| **Culture** | Museums, galleries, historical sites, temples, cultural centers |
| **Food** | Local markets, restaurants, food tours, culinary experiences |
| **Nature** | Parks, hiking trails, scenic viewpoints, outdoor activities |
| **Romantic** | Couples' activities, sunset spots, intimate dining, scenic walks |
| **Party** | Nightlife, bars, clubs, entertainment districts, live music |

### **💰 Cost Breakdown**

- Per-location cost estimates (entrance fees, typical expenses)
- Daily cost summaries
- Total trip cost calculation
- Excludes: Flights, accommodation, meals (unless specified)

### **🗺️ Route Optimization**

- Multi-stop Google Maps integration
- Origin-to-destination routing
- Day-by-day navigation links
- Optimized for minimal travel time

### **🔄 Intelligent Refinement**

Natural language feedback examples:
- "Add more shopping experiences"
- "Make day 2 less busy"
- "Include kid-friendly activities"
- "Focus on budget-friendly options"
- "Skip the museum, add a park"

---

## Sample Screenshots

### **Input Interface**
![Input](https://img.shields.io/badge/Feature-Input%20Form-blue?style=for-the-badge)
- Auto-detected location display
- Destination city input
- Trip duration slider (1-7 days)
- Travel focus dropdown
- Date picker with auto-calculated return date

### **Itinerary Display**
![Itinerary](https://img.shields.io/badge/Feature-AI%20Generated%20Plan-green?style=for-the-badge)
- Day-by-day breakdown
- Location descriptions
- Weather forecasts per day
- Cost estimates per location
- Daily route maps
- Flight search links

### **Refinement Interface**
![Refinement](https://img.shields.io/badge/Feature-Natural%20Language%20Updates-orange?style=for-the-badge)
- Feedback text area
- "Update Plan" button
- Real-time itinerary regeneration

---

## Future Enhancements

### **🚀 Planned Features**

- [ ] **Multi-city itineraries** (Paris → Rome → Barcelona)
- [ ] **Accommodation recommendations** (hotels, Airbnb, hostels)
- [ ] **Restaurant reservations** (OpenTable integration)
- [ ] **Local transportation** (public transit, car rentals, ride-sharing)
- [ ] **User accounts** (save and share itineraries)
- [ ] **Collaborative planning** (multi-user trip editing)
- [ ] **Budget optimization** (maximize experiences within budget)
- [ ] **Photo integration** (preview destinations with images)
- [ ] **Review aggregation** (TripAdvisor, Google Reviews)
- [ ] **Offline mode** (downloadable itineraries)
- [ ] **Mobile app** (iOS/Android)
- [ ] **Voice input** (speak your preferences)

### **🔬 Research Directions**

- Fine-tuned travel domain LLMs
- Reinforcement learning for optimal route planning
- Personalization via user preference modeling
- Real-time price tracking and alerts
- Sentiment analysis for review-based filtering
- Multi-modal models (text + images + maps)

---

## Technical Details

### **LLM Configuration**

```python
Model: llama-4-scout-17b-16e-instruct
Endpoint: https://api.groq.com/openai/v1
Temperature: 0.7 (balanced creativity/accuracy)
Max Tokens: 2000 (detailed itineraries)
```

### **API Endpoints Used**

| Service | Endpoint | Rate Limit |
|---------|----------|------------|
| Groq API | https://api.groq.com/openai/v1 | Varies by plan |
| IP-API | http://ip-api.com/json/ | 45 req/min (free) |
| wttr.in | https://wttr.in/{city}?format=3 | No official limit |
| Google Maps | https://www.google.com/maps/dir/ | No API key required |
| Google Flights | https://www.google.com/travel/flights | No API key required |

### **Session State Management**

Uses Streamlit's `st.session_state` to persist:
- Generated itinerary text
- Selected destination
- Departure and return dates
- User feedback history

---

## Limitations & Disclaimers

⚠️ **Important Notes:**

1. **Cost Estimates:** AI-generated costs are approximate. Actual prices vary by season, availability, and exchange rates.
2. **Weather Forecasts:** Real-time weather may differ from forecasts. Always check closer to travel dates.
3. **Location Accuracy:** AI recommends real places but cannot guarantee current status (closures, renovations, etc.).
4. **API Dependencies:** Requires internet connection and active API keys.
5. **Security:** API keys should be stored in environment variables for production use.

---

## Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

**Powered By:**
- **Meta AI** — LLaMA 4 Scout 17B 16E Instruct model
- **Groq** — Ultra-fast LLM inference platform
- **Streamlit** — Interactive Python web framework
- **Google Maps** — Route optimization and navigation
- **IP-API** — Geolocation services
- **wttr.in** — Weather forecasting API

**Inspiration:**
Modern travel planning deserves modern tools. This project demonstrates how Large Language Models can transform complex, multi-step research tasks into conversational, intelligent experiences.

---



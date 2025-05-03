import streamlit as st
from openai import OpenAI
import requests
from urllib.parse import quote_plus
from datetime import datetime, timedelta
import re

# ---------------------------
# Groq API Client
# ---------------------------
client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

# ---------------------------
# Get User Location
# ---------------------------
def get_user_location():
    try:
        res = requests.get("http://ip-api.com/json/").json()
        return res.get("city", "Unknown")
    except:
        return "Unknown"

# ---------------------------
# Weather
# ---------------------------
def get_weather_forecast(city):
    try:
        response = requests.get(f"https://wttr.in/{quote_plus(city)}?format=3", timeout=5)
        return response.text if response.status_code == 200 else "Weather unavailable"
    except:
        return "Weather unavailable"

# ---------------------------
# Cost Estimator Agent
# ---------------------------
def estimate_costs(destination, day_plan):
    prompt = (
        f"For the following places in {destination}, estimate the average tourist cost in USD:\n"
        f"Return results in the format:\n- Place: $amount\n\nPlaces:\n" + "\n".join(f"- {p}" for p in day_plan)
    )
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "system", "content": "You estimate average real-world travel costs."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# ---------------------------
# Clean formatting
# ---------------------------
def sanitize_itinerary(text):
    text = re.sub(r"(?<!\n)(Day\s*\d+)", r"\n\1", text, flags=re.IGNORECASE)
    text = re.sub(r"\n\s*[•*]", "\n-", text)
    return text.strip()

# ---------------------------
# Parse itinerary
# ---------------------------
def parse_itinerary(text):
    route_dict = {}
    current_day = None
    for line in text.splitlines():
        line = line.strip()
        if re.match(r"(?i)^day\s*\d+", line):
            current_day = line
            route_dict[current_day] = []
        elif line.startswith("-") and current_day:
            route_dict[current_day].append(line[1:].strip())
    return route_dict

# ---------------------------
# Google Directions
# ---------------------------
def build_directions_link(places, destination):
    return "https://www.google.com/maps/dir/" + "/".join(
        [quote_plus(f"{p} {destination}") for p in places]
    )

# ---------------------------
# Generate Itinerary
# ---------------------------
def generate_itinerary(destination, days, interest):
    prompt = (
        f"Create a {days}-day itinerary in {destination} focusing on {interest}. "
        f"Use format:\nDay 1:\n- Place One (desc)\n- Place Two (desc)\n...\nOnly include real places."
    )
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "system", "content": "You are a travel planner."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# ---------------------------
# Refine Itinerary
# ---------------------------
def refine_itinerary(original, feedback):
    prompt = (
        f"Original itinerary:\n{original}\n\n"
        f"User feedback: {feedback}\nUpdate it accordingly. Keep bullet format and add real places."
    )
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "system", "content": "You refine travel plans."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="AI Travel Planner", layout="wide")
st.title("🧭 AI Travel Planner with Groq + Cost Estimator")

user_city = get_user_location()
st.markdown(f"📍 **Detected Location:** `{user_city}`")

destination = st.text_input("🌍 Destination City", "Tokyo")
days = st.slider("📅 Trip Duration", 1, 7, 3)
interest = st.selectbox("🎯 Focus", ["culture", "food", "nature", "romantic", "party"])
departure_date = st.date_input("🛫 Departure Date", datetime.today())
return_date = departure_date + timedelta(days=days)
st.markdown(f"🛬 **Return Date:** `{return_date.strftime('%Y-%m-%d')}`")

# ---------------------------
# Generate Itinerary
# ---------------------------
if st.button("Generate My Trip"):
    with st.spinner("Generating itinerary..."):
        itinerary = generate_itinerary(destination, days, interest)
        st.session_state.itinerary = itinerary
        st.session_state.destination = destination
        st.session_state.dates = (departure_date, return_date)

        st.subheader("📋 Itinerary")
        st.markdown(itinerary)

        # Flights
        dep = departure_date.strftime("%Y-%m-%d")
        ret = return_date.strftime("%Y-%m-%d")
        flight_url = f"https://www.google.com/travel/flights?q=Flights+from+{quote_plus(user_city)}+to+{quote_plus(destination)}+on+{dep}+returning+on+{ret}"
        st.subheader("✈️ Flights")
        st.markdown(f"[🔗 Flights from {user_city} to {destination}]({flight_url})", unsafe_allow_html=True)

        # Route to destination
        st.subheader("🚗 Route to Destination")
        st.markdown(f"[📍 View Map]({build_directions_link([user_city, destination], destination)})", unsafe_allow_html=True)

        # Daily route & costs
        st.subheader("🗺️ Daily Plans with Cost & Weather")
        cleaned = sanitize_itinerary(itinerary)
        routes = parse_itinerary(cleaned)

        total_cost = 0
        for day, places in routes.items():
            st.markdown(f"### {day}")
            st.markdown(f"🌤️ Weather: {get_weather_forecast(destination)}")
            for p in places:
                st.markdown(f"- {p}")
            cost_block = estimate_costs(destination, places)
            st.markdown("💰 **Estimated Costs:**")
            st.code(cost_block.strip())

            # ✅ Only count lines like "- Place: $amount"
            day_cost = 0
            for line in cost_block.splitlines():
                if re.match(r"-\s+.*?:\s+\$\d+", line):
                    match = re.search(r"\$(\d+(?:\.\d+)?)", line)
                    if match:
                        day_cost += float(match.group(1))

            total_cost += day_cost
            st.success(f"Day Cost: ${day_cost:.2f}")

            if len(places) >= 2:
                link = build_directions_link(places, destination)
                st.markdown(f"[🧭 Route Map for {day}]({link})", unsafe_allow_html=True)

        st.markdown(f"## 💵 **Total Estimated Trip Cost: ${total_cost:.2f}**")

# ---------------------------
# Refine Itinerary
# ---------------------------
if "itinerary" in st.session_state:
    st.subheader("📝 Refine Your Plan")
    feedback = st.text_area("Feedback (e.g., more food, less walking, skip Day 3):")
    if st.button("Update Plan"):
        with st.spinner("Refining itinerary..."):
            updated = refine_itinerary(st.session_state.itinerary, feedback)
            st.session_state.itinerary = updated

            st.subheader("✨ Updated Itinerary")
            st.markdown(updated)

            st.subheader("🗺️ Refined Daily Plans with Cost & Weather")
            cleaned = sanitize_itinerary(updated)
            routes = parse_itinerary(cleaned)
            total_cost = 0
            for day, places in routes.items():
                st.markdown(f"### {day}")
                st.markdown(f"🌤️ Weather: {get_weather_forecast(destination)}")
                for p in places:
                    st.markdown(f"- {p}")
                cost_block = estimate_costs(destination, places)
                st.markdown("💰 **Estimated Costs:**")
                st.code(cost_block.strip())

                # ✅ Filter and add real costs only
                day_cost = 0
                for line in cost_block.splitlines():
                    if re.match(r"-\s+.*?:\s+\$\d+", line):
                        match = re.search(r"\$(\d+(?:\.\d+)?)", line)
                        if match:
                            day_cost += float(match.group(1))

                total_cost += day_cost
                st.success(f"Day Cost: ${day_cost:.2f}")

                if len(places) >= 2:
                    link = build_directions_link(places, destination)
                    st.markdown(f"[🧭 Route Map for {day}]({link})", unsafe_allow_html=True)

            st.markdown(f"## 💵 **Updated Total Estimated Trip Cost: ${total_cost:.2f}**")

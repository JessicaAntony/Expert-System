import streamlit as st

# Define the knowledge base with educational pathways
knowledge_base = {
    "engineering": [
        "🛠 Mechanical Engineering",
        "⚡ Electrical Engineering",
        "🏗 Civil Engineering",
        "🚀 Consider specializing in emerging areas like robotics or renewable energy."
    ],
    "humanities": [
        "📜 History",
        "🧠 Philosophy",
        "📚 Literature",
        "💻 Consider enhancing your studies with courses in digital humanities or critical theory."
    ],
    "business": [
        "🏢 Business Administration",
        "💹 Economics",
        "💼 Finance",
        "📈 Enhance your profile by pursuing internships and certifications like CFA or CPA."
    ],
    "science": [
        "🧬 Biology",
        "🧪 Chemistry",
        "⚛ Physics",
        "🔬 Engage in research projects and consider a path towards advanced degrees for greater specialization."
    ],
    "art_and_design": [
        "🎨 Graphic Design",
        "👗 Fashion Design",
        "🏡 Interior Design",
        "💡 Build a strong portfolio and stay updated with the latest software and design trends."
    ]
}

# Set title with emoji
st.title("🎓 Educational Pathway Counseling System")

# Progress bar to indicate completion of form sections
progress = st.progress(0)

# Function to display colorful container for recommendations
def show_recommendations(category):
    st.markdown(f"<h3 style='color: #2E8B57;'>We recommend pursuing a degree in {category.capitalize()}:</h3>", unsafe_allow_html=True)
    for i in knowledge_base[category]:
        st.write(f"- {i}")

# Function to respond with educational recommendations
def respond(input_data):
    skills, interests, traits, education_goals = input_data

    with st.container():
        if ("technical" in skills and "innovation" in interests and "problem-solving" in traits and "engineering" in education_goals):
            show_recommendations("engineering")
        elif ("analytical" in skills and "critical thinking" in interests and "reflective" in traits and "humanities" in education_goals):
            show_recommendations("humanities")
        elif ("business" in skills and "entrepreneurial" in interests and "leadership" in traits and "business" in education_goals):
            show_recommendations("business")
        elif ("scientific" in skills and "curiosity" in interests and "detail-oriented" in traits and "science" in education_goals):
            show_recommendations("science")
        elif ("creative" in skills and "artistic" in interests and "innovative" in traits and "art and design" in education_goals):
            show_recommendations("art_and_design")
        else:
            st.warning("We couldn't find a suitable educational pathway based on your inputs. Please consider consulting an academic advisor.")
    
    progress.progress(100)

# Main execution of the Streamlit app
if __name__ == "__main__":
    st.markdown("### Select your skills, interests, traits, and education goals below:")

    # Step 1: Select Skills
    st.markdown("#### Step 1: Choose your skills 🛠️")
    skills = st.multiselect("Select your skills:", ["technical", "analytical", "business", "scientific", "creative"])
    progress.progress(20)

    # Step 2: Select Interests
    st.markdown("#### Step 2: Choose your interests 🌱")
    interests = st.multiselect("Select your interests:", ["innovation", "critical thinking", "entrepreneurial", "curiosity", "artistic"])
    progress.progress(40)

    # Step 3: Select Personality Traits
    st.markdown("#### Step 3: Choose your personality traits 🧠")
    traits = st.multiselect("Select your personality traits:", ["problem-solving", "reflective", "leadership", "detail-oriented", "innovative"])
    progress.progress(60)

    # Step 4: Select Education Goals
    st.markdown("#### Step 4: Choose your education goals 🎯")
    education_goals = st.multiselect("Select your education goals:", ["engineering", "humanities", "business", "science", "art and design"])
    progress.progress(80)

    # Button for recommendations
    if st.button("🔍 Get Educational Pathway Recommendations"):
        respond([skills, interests, traits, education_goals])

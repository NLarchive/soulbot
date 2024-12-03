# personality_data.py

MBTI_EXPLANATIONS = {
    "INTJ": "The Architect: Innovative and strategic thinkers, driven by logic and a desire for efficiency.",
    "INTP": "The Logician: Creative and curious individuals, who enjoy analyzing ideas and solving complex problems.",
    "ENTJ": "The Commander: Bold and decisive leaders, focused on achieving their goals and inspiring others.",
    # ... (Add more MBTI types)
}

DISC_EXPLANATIONS = {
    "D": "Dominance: Direct, decisive, and results-oriented.",
    "I": "Influence: Enthusiastic, persuasive, and outgoing.",
    "S": "Steadiness: Patient, reliable, and cooperative.",
    # ... (Add more DISC types)
}

ENNEAGRAM_EXPLANATIONS = {
    "1": "Reformer: Principled, purposeful, and self-critical.",
    "2": "Helper: Generous, demonstrative, and people-pleasing.",
    "3": "Achiever: Adaptable, driven, and image-conscious.",
    # ... (Add more Enneagram types)
}


BIG_FIVE_EXPLANATIONS = {
    "Openness": "Openness to experience: Imaginative, curious, and open-minded.",
    "Conscientiousness": "Conscientiousness: Organized, responsible, and disciplined.",
    "Extraversion": "Extraversion: Outgoing, sociable, and assertive.",
    "Agreeableness": "Agreeableness: Cooperative, compassionate, and trusting.",
    "Neuroticism": "Neuroticism: Prone to negative emotions like anxiety and moodiness.",
}

SEI_EXPLANATIONS = {  # Social & Emotional Intelligence
    "Self-Awareness": "Understanding your own emotions and their impact on others.",
    "Self-Regulation": "Managing your emotions and impulses effectively.",
    # ... (Add more SEI aspects)
}

PERSONALITY_SYSTEMS = {
    "MBTI": {
        "full_name": "Myers-Briggs Type Indicator",
        "dimensions": 4,  # Extraversion/Introversion, Sensing/Intuition, Thinking/Feeling, Judging/Perceiving
        "description": "A psychological assessment that identifies personality types based on four dichotomies."
    },
    "DISC": {
        "full_name": "DISC Assessment",
        "dimensions": 4,  # Dominance, Influence, Steadiness, Conscientiousness
        "description": "A behavioral assessment that identifies individual preferences in terms of dominance, influence, steadiness, and conscientiousness.",
    },
    "Enneagram": {
        "full_name": "Enneagram of Personality",
        "dimensions": 9,
        "description": "A system of personality typing that describes patterns in behavior, motivations, and fears.",
    },
    "Big Five": {
        "full_name": "Big Five Personality Traits",
        "dimensions": 5,  # Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism
        "description": "A model of personality based on five broad dimensions of personality traits.",
    },
    "SEI": {
        "full_name": "Social & Emotional Intelligence",
        "dimensions": "Various",  # Can vary based on specific model
        "description": "The ability to understand and manage your own emotions and the emotions of others.",
    },
}
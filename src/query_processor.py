"""
Project TrustEngine - Coupang Search Loop Re-architecture
File: src/query_processor.py
Description: Simulates NLP query intent parsing and budget extraction.
"""

def mock_nlp_query_processor(user_query: str) -> dict:
    """
    Simulates using an NLP pipeline (like spaCy) for Named Entity Recognition (NER)
    and intent parsing to extract core search elements.
    """
    print(f"Parsing raw user query: '{user_query}'")
    
    # Lowercase for uniform processing
    query_lower = user_query.lower()
    
    # Default values
    extracted_intent = {
        "core_category": "general",
        "attributes": [],
        "budget_intent": "neutral", # budget can be: discount, premium, neutral
        "inferred_tags": []
    }
    
    # Simulate keyword token matching (representing spaCy NER entities)
    if "shoe" in query_lower or "sneaker" in query_lower:
        extracted_intent["core_category"] = "apparel_footwear"
    elif "phone" in query_lower or "electronics" in query_lower:
        extracted_intent["core_category"] = "electronics"
        
    if "running" in query_lower:
        extracted_intent["attributes"].append("athletic")
    if "waterproof" in query_lower:
        extracted_intent["attributes"].append("weather_resistant")
        
    # Extracting price/budget sensitivity modifiers
    if any(word in query_lower for word in ["cheap", "budget", "affordable", "sale", "low price"]):
        extracted_intent["budget_intent"] = "discount"
        extracted_intent["inferred_tags"].append("value_seeking")
    elif any(word in query_lower for word in ["premium", "luxury", "high end", "expensive"]):
        extracted_intent["budget_intent"] = "premium"
        extracted_intent["inferred_tags"].append("luxury_seeking")
        
    return extracted_intent

# Example Execution
if __name__ == "__main__":
    sample_query = "cheap waterproof running shoes"
    parsed_result = mock_nlp_query_processor(sample_query)
    
    print("\n--- Extracted Search Metadata ---")
    for key, value in parsed_result.items():
        print(f"{key}: {value}")

"""
Project TrustEngine - Coupang Search Loop Re-architecture
File: src/hybrid_retrieval.py
Description: Simulates an unbiased ranking layer influenced by user budget tier personalization.
"""

# Mock Product Database (Item_ID, Name, Category, Price, Brand_Type, Base_Relevance_Score)
MOCK_CATALOG = [
    {"id": 101, "name": "Coupang Comet Running Shoes", "price": 15000, "brand_type": "PB", "base_score": 8.5},
    {"id": 102, "name": "Premium Nike Air Max", "price": 89000, "brand_type": "Third-Party", "base_score": 9.2},
    {"id": 103, "name": "Standard Everyday Sneakers", "price": 25000, "brand_type": "Third-Party", "base_score": 7.9},
    {"id": 104, "name": "Coupang Base Athletics", "price": 12000, "brand_type": "PB", "base_score": 8.1}
]

def generate_personalized_ranking(user_profile: dict, parsed_query: dict) -> list:
    """
    Ranks products objectively by combining base semantic relevance with 
    individual user profile affinity instead of global corporate overrides.
    """
    ranked_results = []
    user_tier = user_profile.get("historical_budget_preference", "neutral")
    
    print(f"Personalizing results for User Tier: '{user_tier.upper()}'")
    
    for item in MOCK_CATALOG:
        final_score = item["base_score"]
        
        # Scenario A: User profile or query intent matches value/Private Brand pricing
        if user_tier == "discount" or parsed_query["budget_intent"] == "discount":
            if item["brand_type"] == "PB":
                # Elevate naturally due to personalization match
                final_score += 1.5 
                
        # Scenario B: User profile shows preference for premium brands
        elif user_tier == "premium" or parsed_query["budget_intent"] == "premium":
            if item["brand_type"] == "Third-Party" and item["price"] > 50000:
                final_score += 1.5
                
        ranked_results.append({
            "id": item["id"],
            "name": item["name"],
            "price": f"₩{item['price']}",
            "brand": item["brand_type"],
            "final_ranking_score": round(final_score, 2)
        })
        
    # Sort candidates by final personalized ranking score descending
    ranked_results.sort(key=lambda x: x["final_ranking_score"], reverse=True)
    return ranked_results

if __name__ == "__main__":
    # Simulate a value-seeking user profile fetched from cache
    mock_user_profile = {"user_id": "usr_9921", "historical_budget_preference": "discount"}
    mock_query_intent = {"budget_intent": "discount"}
    
    final_feed = generate_personalized_ranking(mock_user_profile, mock_query_intent)
    
    print("\n--- Rendered Search Results ---")
    for index, product in enumerate(final_feed, 1):
        print(f"Rank {index}: {product['name']} [{product['brand']}] - Score: {product['final_ranking_score']} ({product['price']})")

"""
Project TrustEngine - Coupang Search Loop Re-architecture
File: src/integrity_engine.py
Description: Simulates review text analysis and velocity anomaly detection.
"""

def evaluate_review_integrity(product_id: int, recent_reviews: list) -> bool:
    """
    Analyzes review batches to check for spam signatures or highly repetitive text blocks.
    Returns False if an anomaly is detected (untrustworthy product status).
    """
    print(f"Running integrity audit on Product ID: {product_id}...")
    
    seen_texts = set()
    duplicate_count = 0
    
    for review in recent_reviews:
        text = review["text"].strip().lower()
        # Look for identical or highly repetitive review patterns (common in review manipulation groups)
        if text in seen_texts:
            duplicate_count += 1
        seen_texts.add(text)
        
    # If more than 30% of reviews in a short time frame are identical text strings
    anomaly_threshold = len(recent_reviews) * 0.3
    if duplicate_count > anomaly_threshold:
        print(f"⚠️ ANOMALY DETECTED: Product {product_id} has suspicious review duplication patterns.")
        return False
        
    print(f"✅ Product {product_id} passed review text integrity validation.")
    return True

if __name__ == "__main__":
    # Test cases
    clean_reviews = [
        {"user": "userA", "text": "Great shoes, fits nicely."},
        {"user": "userB", "text": "Very comfortable for daily runs."},
        {"user": "userC", "text": "Decent quality for the low price point."}
    ]
    
    suspicious_reviews = [
        {"user": "bot1", "text": "Amazing quality product! Recommended to buy!"},
        {"user": "bot2", "text": "Amazing quality product! Recommended to buy!"},
        {"user": "bot3", "text": "Very cheap and nice."},
        {"user": "bot4", "text": "Amazing quality product! Recommended to buy!"}
    ]
    
    print("--- Audit 1 ---")
    evaluate_review_integrity(101, clean_reviews)
    
    print("\n--- Audit 2 ---")
    evaluate_review_integrity(104, suspicious_reviews)

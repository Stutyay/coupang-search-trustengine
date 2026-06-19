# Project TrustEngine: Compliant & Personalized Search Architecture for Coupang

**Prepared by:** Stuti Gupta | B.Sc. Computer Science (Expected 2027)  
**Target Role:** Search Product Manager Intern

---

## 📌 Executive Summary & Market Context

In light of recent regulatory scrutiny from the Korea Fair Trade Commission (FTC) regarding private-label product ranking bias and review manipulation, Coupang faces a critical product challenge. The objective is to design a search and recommendation engine that maximizes search-to-cart conversion rates and protects gross margin without relying on hardcoded algorithmic biases. 

**Project TrustEngine** proposes a shift from a business-prioritized ranking model to an objective, hyper-personalized vector search ecosystem. By leveraging Natural Language Processing (NLP) and Retrieval-Augmented Generation (RAG), Coupang can naturally elevate high-value items based on individual user data while autonomously sanitizing the review ecosystem to restore consumer trust.

---

## 🚀 Core Product Features

| Feature Name | Product Value & User Empathy | Technical Mechanism | Key Metric Impact |
| :--- | :--- | :--- | :--- |
| **Budget-Driven Vector Search** | Connects users with affordable items naturally, without forced global rankings. | Embeds individual historical budget thresholds directly into the dense-retrieval vector space. | Search-to-Cart Conversion Rate |
| **Review Integrity Engine** | Ensures users feel safe relying on platform social proof. | A RAG pipeline flagging anomalous review velocities or semantic similarity clusters. | Net Promoter Score (NPS) |
| **Dynamic Transparency Badges** | Restores buyer confidence and platform compliance. | UI indicators explaining recommendation logic (e.g., "Top Value based on your price history"). | Search Click-Through Rate (CTR) |

---

## ⚙️ Technical Architecture & System Design Flow

To achieve a compliant, high-converting search loop, the architecture must move away from fixed corporate priority weights and rely on intelligent, dynamic retrieval.

```mermaid
graph TD
    A[User Search Query] --> B[NLP Query Processing: spaCy]
    B --> C[Embedding Generation: Gemini API]
    C --> D[Hybrid Retrieval Layer: FAISS / Qdrant + BM25]
    D --> E[Review Integrity Filter: RAG Pipeline]
    E --> F[Hyper-Personalization Re-ranking: User Budget Mapping]
    F --> G[Final Compliant Search Results Rendered]


---

## 📊 A/B Testing & Success Metrics

To validate the TrustEngine architecture safely, we will deploy a phased experimentation framework over 4 weeks.

### Experiment Setup
* **Target Audience:** 5% of active mobile app users (randomly bucketed).
* **Control Group (A):** The current, legacy Coupang search ranking system.
* **Variant Group (B):** The new TrustEngine personalized, unbiased hybrid search loop.

### Core Metrics Tracked
* **Primary Success Metric:** **Search-to-Cart Conversion Rate.** We hypothesize that hyper-personalized search will increase the likelihood of a user adding an item to their cart from the search results page by at least 2%.
* **Secondary Metric:** **Click-Through Rate (CTR)** on organically ranked, non-sponsored items, demonstrating improved relevance.
* **Guardrail Metric:** **Gross Merchandise Value (GMV)**. Overall revenue per session must not drop by more than **0.5%** during the experiment. This ensures that while we adjust for compliance, the core business bottom line is protected.

---

## 💻 Technical Implementation & Proof of Work

To demonstrate the feasibility of this architecture, this repository will contain proof-of-concept scripts detailing the core logic:

* 📂 `src/`
    * 📄 `query_processor.py` *(Demonstrates the spaCy NLP pipeline parsing user intent)*
    * 📄 `hybrid_retrieval.py` *(Sample logic merging dense vector similarity scores with BM25 exact matching)*
    * 📄 `integrity_engine.py` *(A mock RAG function flagging identical review text patterns)*

*Note: For proprietary reasons, no actual Coupang user data or exact proprietary ranking algorithms are utilized in these demonstration scripts. All tests are conceptually designed using standard e-commerce best practices.*

# AI

## **Day 1: LLM Foundations**

- Topics:  
    **
  - **ML vs DL vs LLMs (high-level difference).  
        **
  - **Transformers: self-attention, why they scale well.  
        **
  - **Tokens & context window (important when talking about code).  
        **
- **Material:  
    **
  - **Video**
  - [**But what is a neural network? | Deep learning chapter 1**](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=2) **→**[](https://www.youtube.com/watch?v=U0s0f995w14&utm_source=chatgpt.com)
  - [**Large Language Models explained briefly**](https://www.youtube.com/watch?v=LPZh9BOjkQs&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=5)
  - [**Transformers, the tech behind LLMs | Deep Learning Chapter 5**](https://www.youtube.com/watch?v=wjZofJX0v4M&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=6)

## **Day 2: Embeddings & Vector Search**

- **Topics:  
    **
  - **What embeddings are, how text/code → vector.  
        **
  - **Semantic search vs keyword search.  
        **
  - **Why embeddings + vector DB are key for code analysis.  
        **
- **Material:  
    **
  - **Blog →** [**OpenAI Embeddings Guide**](https://platform.openai.com/docs/guides/embeddings?utm_source=chatgpt.com)**.  
        **
  - **Blog → Pinecone: What are Vector Embeddings?.  
        **

## **Day 3: Retrieval-Augmented Generation (RAG)**

- **Topics:  
    **
  - **Why you don’t fine-tune for every repo → instead use RAG.  
        **
  - **Chunking code (functions/classes).  
        **
  - **Latency & retrieval accuracy challenges.  
        **
- **Material:  
    **
  - **Blog → RAG Explained Simply.  
        **
  - **Example → OpenAI Cookbook:** [**"Question answering with embeddings"**](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb?utm_source=chatgpt.com)**.  
        **

## **Day 4: Model Context Protocol (MCP)**

- **Topics:  
    **
  - **What MCP is (standard to connect IDE ↔ AI models).  
        **
  - **MCP servers expose tools (e.g., repo fetch, search).  
        **
  - **How IDE (like VSCode) can use MCP to visualize & extend context.  
        **
- **Material:  
    **
  - **Docs → Model Context Protocol official site.  
        **
  - **Explore → Anthropic’s MCP GitHub repos (reference implementations).  
        **

## **Day 5: AI in Developer Tools**

- **Topics:  
    **
  - **How AI is used in IDEs today (GitHub Copilot, Cody, Cursor).  
        **
  - **Limitations of current tools (context length, repo size).  
        **
  - **Where your project fits in (repo-aware MCP server).  
        **
- **Material:  
    **
  - **Blog → How GitHub Copilot Works.  
        **
  - **Video → “AI for Code” talk at Stanford (searchable on YouTube).  
        **

## **Day 6: Challenges & Trade-offs**

- **Topics:  
    **
  - **Token limits → need chunking + retrieval.  
        **
  - **Latency → caching embeddings.  
        **
  - **Cost → avoid sending full repos to LLM.  
        **
  - **Security → handling private repos, OAuth.  
        **
- **Material:  
    **
  - **Blog →** [**LLM Limitations (OpenAI)**](https://platform.openai.com/docs/guides/limitations?utm_source=chatgpt.com)**.  
        **
  - **Short read → Best practices for RAG.  
        **




## **📌 Cheat Sheet: ML vs DL vs LLMs**

**Machine Learning (ML)**

- **Algorithms that learn from data to make predictions (e.g., decision trees, regression, SVM).**
- **Doesn’t require deep neural networks.**
- **Example: Predicting house prices from features.  
    **

**Deep Learning (DL)**

- **Subset of ML using neural networks with many layers.**
- **Learns features automatically (no manual feature engineering).**
- **Example: Image recognition using CNNs, speech recognition using RNNs.**

**Large Language Models (LLMs)**

- **A special type of DL model (transformers) trained on massive text/code datasets.**
- **Learns statistical patterns in language.**
- **Can generate, summarize, translate, and reason about text/code.**
- **Examples: GPT, Claude, LLaMA.  
    **

**_“Machine Learning is about algorithms that learn patterns from data, like regression or decision trees. Deep Learning is a subset that uses large neural networks to automatically extract features, making it powerful for images, speech, and text. Large Language Models are a specific kind of deep learning model, based on transformers, trained on massive amounts of text and code. They’re designed to work with natural language — generating, summarizing, or reasoning about it.”_**

**_Token and context window_**

**_TOKENS - “LLMs process text as tokens, not characters. A token is a chunk of text like a word or part of a word. The context window is the max number of tokens the model can handle in one go. For example, GPT-4 can handle up to 128k tokens, which is about 300 pages. This limit is why you can’t just feed an entire codebase at once — instead you split it into chunks and use embeddings + retrieval. Code gets tokenized too (operators, keywords, identifiers often become separate tokens).”_**

**_CONTEXT WINDOW- “In GPT-3, the context window is ~4k tokens. At every step, the model predicts the next token based on everything in the current context. For conversations, the entire history is passed back in at each turn, so it doesn’t have true memory — it just reprocesses the dialogue every time. Once you hit the 4k limit, older parts of the conversation are truncated, which is why long chats eventually lose earlier details. So it has working memory(short term) of 4k characters only allowing it maintain coherence”  
<br/>\- Multi-turn conversation - GPT doesn’t have memory between turns like a human brain. Instead, the conversation history is packed into the input every time:  
Turn 1: User: Hello Assistant: Hi, how can I help?  
Turn 2: Input to GPT is now the entire conversation so far: User: Hello Assistant: Hi, how can I help? User: Can you explain transformers? →  
The model sees both the old and new text (as tokens) and predicts the next assistant reply._**

**LLM, Tech behind LLM, attention**

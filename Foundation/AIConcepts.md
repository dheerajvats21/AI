# AI

## **Day 1: LLM Foundations**

- **Topics:  
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

## **Day 7: Wrap-up & Mock Q&A**

- **Topics:  
    **
  - **Summarize what you learned.  
        **
  - **Prepare short crisp answers (2–3 sentences per concept).  
        **
  - **Mock questions:  
        **
    - **_How do LLMs understand code?  
            _**
    - **_Why embeddings?  
            _**
    - **_How would you scale an AI code assistant?  
            _**
    - **_Why not fine-tune on repos?  
            _**
- **Material:  
    **
  - **OpenAI Cookbook examples → skim Q&A demos.  
        **
  - **Practice explaining concepts out loud (interviewer style).  
        **

# **🎯 Optional Project Story (only if asked)**

**If interviewer asks “Do you have hands-on AI experience?”:**

- **Your story (short pitch):  
    _“I’m working on a personal project: a custom MCP server that connects Git repos with LLMs for real-time code exploration. It fetches code, generates embeddings, stores them in a vector DB, and lets developers query in natural language from inside the IDE. This avoids fine-tuning by using a retrieval-based approach. I’ve studied the architecture, and I’m in the process of implementing it.”  
    _**
- **If they push for details → talk about:  
    **
  - **Architecture (MCP server ↔ Git ↔ Vector DB ↔ LLM).  
        **
  - **Challenges (token limits, latency, cost).  
        **
  - **Why MCP (standardized, IDE integration).  
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

## **_🧠 LLMs & Transformers — Short Notes_**

### **_1\. LLM (Large Language Model)_**

- **_A type of deep learning model specialized for text._**
- **_Built using transformer architecture (introduced by Google in 2017)._**
- **_Learns from massive text datasets to predict next tokens.  
    _**

### **_2\. Core Tech Behind LLMs_**

#### **_🔹 Embeddings_**

- **_Input text → tokens → vectors in high-dimensional space._**
- **_Each token gets an embedding vector (E1 ... En).  
    _**

#### **_🔹 Attention Mechanism (Self-Attention)_**

- **_Goal: capture relationships between tokens (short & long range)._**
- **_Uses Query (Q), Key (K), Value (V) matrices:_**
  - **_Each embedding Ei transformed into Q, K, V._**
  - **_Compute attention scores = dot product (Q·K)._**
  - **_Apply softmax → weights showing “how much token i attends to token j”._**
  - **_Weighted sum: Σ (attention\[i,j\] \* Vj).  
        _**
- **_Output = new contextual embedding for each token._**
- **_Visualise like every other token/word providing info about its correlation with a word, Ek\*value multiplying itself to attention value and making a deltaEi to be added to Ei._**

#### **_🔹 Multi-Head Attention For different language_**

- **_Multiple Q/K/V projections capture different relationships (syntax, meaning, order, etc.)._**
- **_Outputs are concatenated._**

#### **_🔹 Feedforward / MLP Block_**

- **_After attention → embeddings pass through MLP layers:_**
  - **_Up-projection + bias → activation → down-projection + bias._**
- **_Adds non-linear transformations for richer representation. RELU. 0 if negative, y= x if >= 0_**
- **_MLP stores facts in the LLM._**
- **_The upprojection is like asking questions (is previous word adjective, is it talking about micheal jordan , sports etc). EAch row is like a question. So dimension are increased according to up porjection matrix._**
- **_Bias is added and negatives are made 0. This is like taking dot product. if dot product is more, its like answering yes to the question. I.e saying yes the given embedding is aligning better with question “Is it talking about micheal jordan, sports etc”._**
- **_Then We need to put this info about context into final embeddings, i.e when we have downprojection matrix, to put this oontextual info back to embedding in its dimensions. So higher dimension vector multiplied by down projection and it's like multiplying the weighted sum of columns in this matrix to upward projected vector. Each column is same dimension as embeddings, So can be thought of as direction in embedding space lets say direction related to basket ball, Born 1962 etc. We multiply each column by corresponding answer in previous step. To incorporate final context , facts in final embeddings._**

### **_3\. Stacking Layers_**

- **_GPT-3 has 96 transformer layers (repeating Attention + MLP)._**
- **_Each layer refines token representations with more context._**

### **_4\. Output Prediction_**

- **_Final embeddings → unembedding matrix → logits (scores for vocab tokens)._**
- **_Softmax → probability distribution._**
- **_Pick next token (argmax or sampling)._**

### **_📝 Mind Map Keywords_**

**_LLM → Transformer → Tokens → Embeddings → Q/K/V → Attention → Multi-Head → MLP → Residual → LayerNorm → Stacked Layers → Unembedding → Softmax → Next Token_**

### Token and context window

**_TOKENS - “LLMs process text as tokens, not characters. A token is a chunk of text like a word or part of a word. The context window is the max number of tokens the model can handle in one go. For example, GPT-4 can handle up to 128k tokens, which is about 300 pages. This limit is why you can’t just feed an entire codebase at once — instead you split it into chunks and use embeddings + retrieval. Code gets tokenized too (operators, keywords, identifiers often become separate tokens).”_**

**_CONTEXT WINDOW- “In GPT-3, the context window is ~4k tokens. At every step, the model predicts the next token based on everything in the current context. For conversations, the entire history is passed back in at each turn, so it doesn’t have true memory — it just reprocesses the dialogue every time. Once you hit the 4k limit, older parts of the conversation are truncated, which is why long chats eventually lose earlier details. So it has working memory(short term) of 4k characters only allowing it maintain coherence”  
<br/>\- Multi-turn conversation - GPT doesn’t have memory between turns like a human brain. Instead, the conversation history is packed into the input every time:  
Turn 1: User: Hello Assistant: Hi, how can I help?  
Turn 2: Input to GPT is now the entire conversation so far: User: Hello Assistant: Hi, how can I help? User: Can you explain transformers? →  
The model sees both the old and new text (as tokens) and predicts the next assistant reply._**

### Why do LLMs scale pretty well, i.e why by increasing dimension to letssay n we just dont get n dimensions we get more than that

**_Actually when we increase dimensions the features that we catch i.e dimentions we actually get grows exponentially. Coz actually dimensions does not need to be absolutely perpendicular but in range of 89 to 91 degrees. . And as we increase the dimension in embeddings i,e the actual dimensions that the Trasformers get are exponentially more in practise, i.e the features that it captures are far far more than dimensions. That is why it scales pretty well, just by increasing dimensions, we get far more contextual info from text._**

**_So in MLP layer we thought that single row / question would tell about a feature in the text, i.e a single value in upward projected vector is a feature. And column in second matrix also dictates the amount by which that feature goes into final embeddings. But one single value is not a single feature in practise, It is combination of multiple values (neurons). I.e feature is combination of multiple perpendicular dimensions i.e directions for features doesnot have to be prependicular.  
THIS IDEA IS CALLED SUPERPOSITION. Nearly perpendicular direction increase exponentially with perpendicular dimensions i.e why exponentially more features that can be caught. So a feature is not one question or one neuron but combination of more than one._**

**_PART 2_**

## Embeddings and semantic Search

[Video1](https://www.youtube.com/watch?v=OATCgQtNX2o) - How we do semantic search, similarity, mean pooling

[Video2](https://www.youtube.com/watch?v=JdFaPXdOEzM) - DB semantic search

[Video3](https://www.youtube.com/watch?v=orLGv2LgWDE) - RAG and why Vector DB matters to get good answers from LLM

- _Each_ **_word/token_** _is converted into a numerical vector (embedding)._
- _To represent a_ **_sentence/document_**_, you combine the embeddings of its tokens (commonly by_ **_mean pooling_** _→ take the average of all token vectors)._
- _This gives you a single fixed-length vector for the whole sentence._
- _To compare two sentences (or query vs document), you compute_ **_cosine similarity_** _between their vectors._
  - _High cosine similarity → semantically close in meaning._
  - _Low similarity → different meanings._

_👉 In short:_ **_Tokens → embeddings → mean pooling → sentence embedding → cosine similarity for search/retrieval._**

**_Semantic Search Demo in DB Snowflake of sentences_**

- **_First, all sentences/documents are converted to embeddings and stored in a vector database._**
- **_When a query comes in, it is also converted into an embedding._**
- **_The system finds the most similar embeddings (via cosine similarity or another distance metric)._**
- **_Instead of returning raw results, the retrieved text is passed into an LLM, which can then summarize, rephrase, or extract answers → this is the semantic search + LLM layer._**

**_👉 In short: Embedding DB for retrieval + LLM for summarization = smarter semantic search._**

### **Why Embeddings + Vector DBs Matter for Code Analysis**

- **LLMs are trained broadly** → they don’t know _your_ private codebase or data.
- To answer repo-specific questions, we need to **supply relevant context**.

**How it works:**

1. **Preprocess code/docs** → split into chunks (functions, classes).
2. **Generate embeddings** for each chunk (vector representation of meaning).
3. Store embeddings in a **Vector Database**.
4. At query time:
    - Convert query → embedding.
    - Do **semantic search** in Vector DB → fetch nearest code chunks.
    - Send query + retrieved chunks → **LLM**.
    - LLM uses both to generate the answer.

**Why important for code analysis:**

- LLM alone may hallucinate → embeddings + Vector DB ensure **grounding in actual repo code**.
- Efficient retrieval → scales to large repos without retraining the LLM.

👉 In short: _Vector DB + embeddings = memory for your codebase. LLM = reasoning engine._

**Asking LLM directly** → it guesses from general training (risk of hallucination).**With embeddings + Vector DB (RAG)** → it grounds answers in your actual data/code (accurate + context-aware).

Query → Embed Query → Vector DB (find neighbors) → Retrieved Context + Query → LLM → Answer

##

##

## RAG

### **1️⃣ What is Retrieval-Augmented Generation (RAG)?**

[Video1](https://www.youtube.com/watch?v=T-D1OfcDW1M)

[Video2](https://www.youtube.com/watch?v=gweRh5Xtkq0)

- LLMs don’t “know everything” and can’t access private/up-to-date info.
- RAG solves this by:
  - **Step 1:** Store external data (docs, code, emails, etc.) in a **vector DB**.
  - **Step 2:** When a query comes, embed it → find semantically similar chunks.
  - **Step 3:** Send both **query + retrieved chunks** to the LLM.
- This grounds the model’s answer in relevant knowledge → less hallucination, more accuracy.

👉 **Key point:** RAG = LLM + Retrieval layer → dynamic, flexible knowledge injection.

Query → Orchestrator → Retrieval (Vector DB) → Augmentation (add context) → Generation (LLM Answer)

### **Fine-tuning**

**✅ Pros:**

- Model learns domain-specific patterns deeply.
- Can perform well without external retrieval.

**⚠️ Cons:**

- Expensive & time-consuming (training cost).
- Needs lots of domain data.
- Hard to update (must retrain for new data).
- Risk of overfitting to a narrow dataset.

### **RAG (Retrieval-Augmented Generation)**

**✅ Pros:**

- No retraining needed → just update vector DB.
- Flexible → works across many domains.
- Reduces hallucinations by grounding answers.
- Faster to adapt to new knowledge.

**⚠️ Cons:**

- Retrieval adds **latency**.
- Chunking & embedding quality matter.
- Context window size limits how much you can pass.
- Bad retrieval = bad answer.

## Why chunking matters

- **_LLMs can’t handle entire documents/repos because of context window limits._**
- **_So we must split (chunk) the data into smaller pieces._**
- **_Good chunking = better retrieval → better answers._**
- **_Bad chunking = irrelevant or broken context → hallucinations._**

### **_Common Chunking Techniques_**

1. **_Fixed-size chunks_**
    - **_Split by characters or tokens (e.g., 500 tokens each)._**
    - **_✅ Simple, fast._**
    - **_❌ May cut off sentences/functions → loses context._**
2. **_Sliding window_**
    - **_Overlapping chunks (e.g., 500 tokens with 100 overlap)._**
    - **_✅ Preserves continuity across chunk boundaries._**
    - **_❌ Increases storage & retrieval cost._**
3. **_Semantic / Natural boundaries_**
    - **_Split on paragraphs, headings, functions, classes._**
    - **_✅ Keeps meaning intact._**
    - **_❌ Harder to implement, chunk sizes vary._**
    - **_In semantic , we can embed sentences into embeddings and join sentences with similar meaning into a single chunk. So i.e by semantic chunking._**
4. **_Hybrid (structured)_**
    - **_Combination of fixed size + natural boundaries._**
    - **_✅ Balances retrieval accuracy & efficiency._**
    - **_Often best for code (split by class/function, but cap size)._**

### **_Key Takeaway_**

- **_Goal: Chunks must be big enough to carry useful context, but small enough to fit many in the retrieval window._**
- **_In code: chunk by functions or classes, not arbitrary lines._**
- **_In docs: chunk by paragraphs/sections, not random token counts._**

**_👉 Short version:  
“Chunking ensures the data stored in a vector DB is meaningful and retrievable. Fixed-size is simple but can break meaning, semantic chunking preserves context, and hybrids balance both. For code, function/class-based chunking works best.”_**

**_“Document → Chunking → Embeddings → Vector DB_**

## **_Best RAG Chunking Methods_**

### **_🔹 Problem with naive chunking_**

- **_Fixed-size chunks (e.g., 500 tokens) often cut off meaning mid-sentence/section._**
- **_Retrieval then returns fragments → LLM gets poor/irrelevant context → hallucinations._**

### **_🔹 Smarter Chunking Tactics from the Video_**

1. **_Contextual Headers and Chunks -> segments_**
    - **_Keep headings/section titles with the chunk._**
    - **_Ensures chunk carries semantic context even if short. So libraries divide the text into segments then with each chunk add the segment as header, sometimes a summary too._**
    - **_With this we get better relevancy of the chunk with the user query._**
    - **_By adding segment we give zoom out view of chunk to LLM. So better context._**

### **_🔹 Why this improves RAG_**

- **_Retrieval accuracy: Relevant chunks are more likely to be found._**
- **_Coherence: LLM sees complete thoughts, not fragments._**
- **_Less hallucination: Model is grounded in cleaner, structured context._**

### **_💡 one-liner_**

**_“Instead of slicing text blindly, the best RAG chunking methods use contextual headers, semantic boundaries, and small overlaps so chunks remain coherent and retrieval is accurate.”_**

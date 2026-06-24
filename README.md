# PS3
PS3: A Multimodal Transformer Integrating Pathology Reports with Histology Images and Biological Pathways for Cancer Survival Prediction

**Abstract**: Current multimodal fusion approaches in computational oncology primarily focus on integrating multi-gigapixel histology whole slide images (WSIs) with genomic or transcriptomic data, demonstrating improved survival prediction. We hypothesize that incorporating pathology reports can further enhance prognostic performance. Pathology reports, as essential components of clinical workflows, offer readily available complementary information by summarizing histopathological findings and integrating expert interpretations and clinical context. However, fusing these modalities poses challenges due to their heterogeneous nature. WSIs are high-dimensional, each containing several billion pixels, whereas pathology reports consist of concise text summaries of varying lengths, leading to potential modality imbalance. 

To address this, we propose a prototype-based approach to generate balanced representations, which are then integrated using a Transformer-based fusion model for survival prediction that we term PS3 (Predicting Survival from Three Modalities). Specifically, we present: 
(1) Diagnostic prototypes from pathology reports, leveraging self-attention to extract diagnostically relevant sections and standardize text representation; 
(2) Histological prototypes to compactly represent key morphological patterns in WSIs; and 
(3) Biological pathway prototypes to encode transcriptomic expressions, accurately capturing cellular functions. 

PS3, the three-modal transformer model, processes the resulting prototype-based multimodal tokens and models intra-modal and cross-modal interactions across pathology reports, WSIs and transcriptomic data. The proposed model outperforms state-of-the-art methods when evaluated against clinical, unimodal and multimodal baselines on six datasets from The Cancer Genome Atlas (TCGA). 

![PS3 model workflow](src/Main_figure.pdf)

Accepted at **ICCV 2025**.

[Paper on arXiv](https://arxiv.org/abs/2509.20022) | [PDF](https://arxiv.org/pdf/2509.20022)

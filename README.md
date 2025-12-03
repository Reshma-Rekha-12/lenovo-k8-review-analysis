Amazon Review Analysis - Lenovo K8 Mobile

Natural Language Processing analysis of customer reviews to extract insights about product sentiment and key features discussed by customers.

🎯 Overview

This project analyzes 14,675 Amazon customer reviews for the Lenovo K8 mobile phone to understand customer sentiment and identify key product features that matter most to users. The analysis helps Lenovo comprehend the voice of the customer and assess product strengths and weaknesses.

📊 Dataset

Source: Amazon reviews for Lenovo K8 mobile (scraped data)

Structure:

Sentiment: value: 1 = positive, 0 = negative
Reviews: Main text of customer reviews
Size: 14,675 reviews
Dataset Source: Kaggle - Manish Gupta

🚀 Installation
bash
# Clone the repository
git clone https://github.com/yourusername/lenovo-k8-review-analysis.git
cd lenovo-k8-review-analysis

# Install required packages
pip install -r requirements.txt

Required Libraries

pandas
nltk
numpy
matplotlib
wordcloud
jupyter
NLTK Downloads


The script will automatically download required NLTK data:

punkt
averaged_perceptron_tagger
wordnet
stopwords
words
omw-1.4
💻 Usage

Option 1: Run Python Script

bash
python src/review_analysis.py

Option 2: Open Jupyter Notebook

bash
jupyter notebook notebooks/review_analysis.ipynb
🔧 Methodology

1. Data Preprocessing Pipeline

Text Normalization:

Converted all text to lowercase
Removed punctuation using str.maketrans()
Removed English stopwords using NLTK


Advanced Text Processing:

Part-of-Speech (POS) tagging using NLTK
Lemmatization with WordNet based on POS tags
Custom POS mapping function to enhance accuracy


2. Analysis Techniques

Frequency Distribution:

Generated frequency distribution of words using NLTK's FreqDist
Visualized top 15 most frequent terms
Word Cloud Visualization:

Created word cloud to identify prominent themes
Customizable colormap support


🔍 Key Findings

Most Frequently Mentioned Terms:

phone, good, battery, camera - Most discussed topics
Positive Indicators:
Words like performance, feature, best, great, awesome suggest positive customer sentiment about specific features.

Concerns Identified:
Terms like heat, bad, problem, issue indicate potential product issues that need attention.

Competitive Analysis:
Presence of Redmi and compare suggests customers are benchmarking against competitor devices, particularly Redmi products.

Business Insights:
Battery and camera are critical decision factors for customers
Product performance receives mixed feedback
Customers actively compare Lenovo K8 with competitor devices
Some heating and quality issues reported


🛠️ Technologies Used

Python 3.x
Libraries:
pandas - Data manipulation
nltk - Natural Language Processing
numpy - Numerical operations
matplotlib - Data visualization
wordcloud - Word cloud generation


📁 Project Structure


lenovo-k8-review-analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── K8 Reviews.csv
│
├── notebooks/
│   └── review_analysis.ipynb
│
├── src/
│   └── review_analysis.py
│
└── outputs/
    ├── frequency_plot.png
    └── wordcloud.png


📈 Results


The analysis provides actionable insights for product development:

Focus on battery and camera improvements
Address heating issues
Benchmark features against Redmi competitors
Maintain strong performance attributes


🙏 Acknowledgments
Dataset provided by Manish Gupta on Kaggle
NLTK library for NLP capabilities



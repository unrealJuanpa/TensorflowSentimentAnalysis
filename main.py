from sentiment_analysis_spanish import sentiment_analysis

sentiment = sentiment_analysis.SentimentAnalysisSpanish()

while True:
    s = input('>>> ')
    print(sentiment.sentiment(s))
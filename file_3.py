'''
Problem Statement:
Perform sentiment analysis on a collection of travel blog entries stored in travel_blogs.txt. Identify and count the 
occurrences of positive words (e.g., "amazing", "enjoy", "beautiful") and negative words (e.g., "bad", "disappointing", "poor").
'''
#with open('travel_blogs.txt', 'w') as file:#
    #file.write('open')#

def analyze_blog_sentiments(blog_file):
    try:
        
        positive_words = ["amazing", "enjoy", "beautiful", "wonderful", "memorable", "excellent", "fantastic"]
        negative_words = ["bad", "disappointing", "poor", "lackluster", "scarce"]

        positive_count = 0
        negative_count = 0

        with open(blog_file, 'r') as file:
           
            blog_entries = file.readlines()

            for entry in blog_entries:
                words = entry.lower().split()
                for word in words:
                   
                    if word in positive_words:
                        positive_count += 1
                    elif word in negative_words:
                        negative_count += 1

        return positive_count, negative_count

    except FileNotFoundError:
        print(f"File '{blog_file}' not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


blog_file = "travel_blogs.txt"

positive_count, negative_count = analyze_blog_sentiments(blog_file)
if positive_count is not None and negative_count is not None:
    print("Sentiment Analysis Results:")
    print("Positive words count:", positive_count)
    print("Negative words count:", negative_count)

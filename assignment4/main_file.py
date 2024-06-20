def ReadFiles(FileData):
    FeedbackData = []
    
    for FileName in FileData:
        
        try:
            with open(FileName, 'r') as file:
                FeedbackData.extend(file.readlines())
        
        except FileNotFoundError:
            print(f"Error: {FileName} not found.")
    
    return FeedbackData


def FeedbackParsing(FeedbackData):
    FeedbackParse = []
    TotalRating = 0
    
    for Feedback in FeedbackData:
        
        try:
            name, rest = Feedback.split(': ', 1)
            rating, comment = rest.split(' - ', 1)
            rating = float(rating)
            FeedbackParse.append((name, rating, comment.strip()))
            TotalRating += rating
        
        except ValueError:
            print(f"Error: Unable to parse feedback: {Feedback}")
    
    return FeedbackParse, TotalRating


def CalculateAverage(TotalRating, count):
    
    if count == 0:
        return 0
    
    return TotalRating / count

def WritingSummary(SummaryFile, FeedbackParse, AverageRating):
    
    with open(SummaryFile, 'w') as file:
        file.write(f"Total Feedback Entries: {len(FeedbackParse)}\n")
        file.write(f"Average Rating: {AverageRating:.2f}\n\n")
        file.write("Feedbacks:\n")
        
        for name, rating, comment in FeedbackParse:
            file.write(f"{name}: {rating} - {comment}\n")

def main():
  FeedbackList = ['feedback1.txt', 'feedback2.txt', 'feedback3.txt']
  FeedbackData = ReadFiles(FeedbackList)
  
  if not FeedbackData:
    print("No feedback data found.")
    return

  FeedbackParse, TotalRating = FeedbackParsing(FeedbackData)
  AverageRating = CalculateAverage(TotalRating, len(FeedbackParse))
  
  WritingSummary('feedback_summary.txt', FeedbackParse, AverageRating)
  print("Summary file 'feedback_summary.txt' created successfully.")

main()
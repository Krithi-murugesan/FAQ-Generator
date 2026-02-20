from src.crew import FaqGeneratorCrew

def run():
    inputs = {
        'source_text': """
        Our refund policy allows customers to return products within 30 days. 
        Items must be in original packaging. Shipping costs are non-refundable. 
        Digital products are exempt from refunds once downloaded.
        """
    }
    result = FaqGeneratorCrew().crew().kickoff(inputs=inputs)
    
    # Save output to a file
    with open("faq_output.json", "w") as f:
        f.write(result.raw)
    
    print("FAQ Generation Complete! Check faq_output.json")

if __name__ == "__main__":
    run()

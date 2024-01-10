from secret import OPENAI_API_KEY 
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts.example_selector.base import BaseExampleSelector
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.schema.output_parser import StrOutputParser
import os
from nltk.tokenize import sent_tokenize

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def FullLLMChain(claim):

    chat = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"])

        # Detailed prompt
    prompt = """
    As an AI developed by OpenAI, you have been trained on a diverse range of internet text. However, you do not know everything and do not have access to real-time or proprietary databases. You should not be seen as a perfectly accurate or primary source of information. 

    Given this, please fact-check the following claim:

    "{}"

    Your response should start with one of the following statements:
    - "This claim has been identified as true."
    - "This claim has been identified as false."
    - "This claim has been identified as partially false."
    - "We are unable to reach a definitive conclusion regarding this claim's accuracy."
    """.format(claim)

    # Create chain and run it on the input
    runnable = chat | StrOutputParser()
    output = runnable.invoke(prompt)

    return output

def EssayLLMChain(essay):
    chat = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"])

    # Split the essay into sentences
    sentences = sent_tokenize(essay)

    results = []
    true_count = 0
    total_count = 0

    # Loop through each sentence
    for sentence in sentences:
        # Detailed prompt
        prompt = """
        As an AI developed by OpenAI, you have been trained on a diverse range of internet text. However, you do not know everything and do not have access to real-time or proprietary databases. You should not be seen as a perfectly accurate or primary source of information. 

        Given this, please fact-check the following claim:

        "{}"

        Your response should start with one of the following statements:
        - "This claim has been identified as true."
        - "This claim has been identified as false."
        - "This claim has been identified as partially false."
        - "We are unable to reach a definitive conclusion regarding this claim's accuracy."
        """.format(sentence)

        # Create chain and run it on the input
        runnable = chat | StrOutputParser()
        output = runnable.invoke(prompt)

        # Count the results
        if "This claim has been identified as true." in output:
            true_count += 1
        elif "This claim has been identified as false." in output or "This claim has been identified as partially false." in output or "We are unable to reach a definitive conclusion regarding this claim's accuracy." in output:
            results.append(sentence)
        total_count += 1

    # Calculate the accuracy percentage
    accuracy_percentage = (true_count / total_count) * 100

    return results, accuracy_percentage
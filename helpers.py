from secret import OPENAI_API_KEY 
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts.example_selector.base import BaseExampleSelector
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.schema.output_parser import StrOutputParser
import os
from nltk.tokenize import sent_tokenize
import torch

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

    You should then provide brief explanation (2-3 sentences) of your reasons for making this determination regarding the claim's accuracy. 

    Additionally, after doing that, provide four sources with hyperlinks and brief information that support your conclusion. Format the sources as follows:

    "Sources:
    []
    []
    []
    []"
    """.format(claim)

    # Create chain and run it on the input
    runnable = chat | StrOutputParser()
    output = runnable.invoke(prompt)

    return output

# from transformers import AutoTokenizer, DPRQuestionEncoderTokenizer, RagRetriever, RagSequenceForGeneration
# import os
# from langchain.chat_models import ChatOpenAI
# from langchain.schema.output_parser import StrOutputParser

# def FullLLMChain(claim):
#     # Initialize RAG Components
#     # Load the DPRQuestionEncoderTokenizer with the appropriate checkpoint for DPR
#     # tokenizer = DPRQuestionEncoderTokenizer.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
#     tokenizer = AutoTokenizer.from_pretrained("facebook/rag-sequence-nq")

#     # Initialize the RagRetriever and RagSequenceForGeneration
#     # Note: You should replace 'use_dummy_dataset=True' with the actual dataset if you're not just testing
#     retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="exact", use_dummy_dataset=True)
#     model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)

#     inputs = tokenizer("How many people live in Paris?", return_tensors="pt")
#     targets = tokenizer(text_target="In Paris, there are 10 million people.", return_tensors="pt")
#     input_ids = inputs["input_ids"]
#     labels = targets["input_ids"]
#     outputs = model(input_ids=input_ids, labels=labels)

#     # Retrieve documents with RAG
#     # input_ids = tokenizer(claim, return_tensors="pt").input_ids
#     # rag_outputs = rag_model.generate(input_ids)
#     # retrieved_docs = tokenizer.batch_decode(rag_outputs, skip_special_tokens=True)

#     # print(outputs)

#     # Prepare the prompt for Chat model
#     # prompt = """
#     # As an AI developed by OpenAI, you have been trained on a diverse range of internet text. However, you do not know everything and do not have access to real-time or proprietary databases. You should not be seen as a perfectly accurate or primary source of information. 

#     # Given this, please fact-check the following claim:

#     # "{}"

#     # Use information from these following relevant documents as needed to do so:

#     # "{}"

#     # Your response should start with one of the following statements:
#     # - "This claim has been identified as true."
#     # - "This claim has been identified as false."
#     # - "This claim has been identified as partially false."
#     # - "We are unable to reach a definitive conclusion regarding this claim's accuracy."
#     # """.format(claim)

#     # # Initialize Chat model and run the prompt
#     # chat = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"])
#     # runnable = chat | StrOutputParser()
#     # output = runnable.invoke(prompt)

#     return output

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
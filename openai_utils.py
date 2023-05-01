import openai
import json

def read_api_key(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def initialize_openai(api_key):
    api_key = read_api_key("openai_api_key.txt")
    openai.api_key = api_key

def generate_response(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        temperature=0.1,
        max_tokens=1000,
        top_p=0.1,
        frequency_penalty=0.2,
        presence_penalty=0.2,        
    )
    return completion.choices[0].message.content

def gpt_3_call(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        temperature=0,
        top_p=0.1,
        frequency_penalty=0,
        presence_penalty=0,  
    )
    return completion.choices[0].message.content



def generate_user_response(messages, message_summarys):
    if len(messages) > 5:
        message_summarys5_10 = message_summarys[-5:-15]
        messages = messages[-5:]
    else:
        message_summarys5_10 = []


def summarize_chat_message(messages, role):

    if len(messages) > 1 and len(messages) <= 2:
        last_message = messages[-1]
        messages = messages[-2]
        system_prompt = [{"role": "system", "content": "Your Goal is to summarizre the content of the specified message in the conversation, while keeping as much information as possible."}]
        message_indicator = [{"role": "user", "content": "this is the message you can use as context:"}]
        examples_prompt = [{"role": "user", "content": 
                "Examples:"
                "" + role + ":You mentioned clustering and two other ways to categorize or manage your data. Are there any others?"
                "s:" + role + ":asks if there are any other ways to categorize or manage data besides clustering, classification, and summarization.\n"
                "" + role + ":Sure, I'd be happy to help you with that."

                "Firstly, we can perform searches on the data in my memory based on keywords, phrases, or topics that are relevant to the information stored in my memory. We can also use natural language processing techniques to extract entities and relationships between them to perform more complex searches."

                "Elasticsearch is a search engine based on the Lucene library. It is designed for distributed environments and can handle large amounts of data. A vector database is a type of database that stores vectors (arrays of numbers) and allows for efficient similarity searches. We can use Elasticsearch in combination with a vector database to perform similarity searches on the data in my memory."

                "To process my memory, we can use techniques such as clustering, classification, and summarization. Clustering can group similar pieces of information together, classification can categorize information into different classes or categories, and summarization can extract the most important information from a piece of text."

                "To create a hierarchical access system for my memory, we can use techniques such as topic modeling and entity extraction to identify key topics and entities in the data. We can then organize the data into a hierarchical structure based on these topics and entities, allowing for easier navigation and access to specific pieces of information."
                "s:" + role + ":"
                "- Assistant explains different techniques to perform searches on the data in memory, including natural language processing, Elasticsearch, and vector databases."
                "- Assistant suggests using clustering, classification, and summarization to process the memory."
                "- Assistant proposes using topic modeling and entity extraction to create a hierarchical access system based on key topics and entities."
            }]
        summarize_prompt = [{"role": "user", "content": "Write a concise summary of the next message by the" + role + " without losing any relevant information. use the stated message as context to Specify named entities if needed. Also specify if the User or assistant asks something, asks for something, explains something, etc. Output your summary after s: and only output the summary. See the examples above. The message is not directed at you. you you should solely focus on summarizing the content of the message."}]
        prompt = system_prompt + examples_prompt + message_indicator + [messages] + summarize_prompt + [last_message]
        message_summary = gpt_3_call(prompt)

    elif len(messages) > 2:
        last_message = messages[-1]
        messages = messages[-2]
        system_prompt = [{"role": "system", "content": "Your Goal is to summarizre the content of the specified message in the conversation, while keeping as much information as possible."}]
        message_indicator = [{"role": "user", "content": "this is the message you can use as context:"}]
        examples_prompt = [{"role": "user", "content": 
                "Examples:"
                "" + role + ":You mentioned clustering and two other ways to categorize or manage your data. Are there any others?"
                "s:" + role + ":asks if there are any other ways to categorize or manage data besides clustering, classification, and summarization.\n"
                "" + role + ":Sure, I'd be happy to help you with that."

                "Firstly, we can perform searches on the data in my memory based on keywords, phrases, or topics that are relevant to the information stored in my memory. We can also use natural language processing techniques to extract entities and relationships between them to perform more complex searches."

                "Elasticsearch is a search engine based on the Lucene library. It is designed for distributed environments and can handle large amounts of data. A vector database is a type of database that stores vectors (arrays of numbers) and allows for efficient similarity searches. We can use Elasticsearch in combination with a vector database to perform similarity searches on the data in my memory."

                "To process my memory, we can use techniques such as clustering, classification, and summarization. Clustering can group similar pieces of information together, classification can categorize information into different classes or categories, and summarization can extract the most important information from a piece of text."

                "To create a hierarchical access system for my memory, we can use techniques such as topic modeling and entity extraction to identify key topics and entities in the data. We can then organize the data into a hierarchical structure based on these topics and entities, allowing for easier navigation and access to specific pieces of information."
                "s:" + role + ":"
                "- Assistant explains different techniques to perform searches on the data in memory, including natural language processing, Elasticsearch, and vector databases."
                "- Assistant suggests using clustering, classification, and summarization to process the memory."
                "- Assistant proposes using topic modeling and entity extraction to create a hierarchical access system based on key topics and entities."
            }]
        summarize_prompt = [{"role": "user", "content": "Write a concise summary of the next message by the" + role + " without losing any relevant information. use the stated message as context to Specify named entities if needed. Also specify if the User or assistant asks something, asks for something, explains something, etc. Output your summary after s: and only output the summary. See the examples above. The message is not directed at you. you you should solely focus on summarizing the content of the message."}]
        prompt = system_prompt + examples_prompt + message_indicator + [messages] + summarize_prompt + [last_message]
        message_summary = gpt_3_call(prompt)

    else:
        last_message = messages[-1]
        system_prompt = [{"role": "system", "content": "Your Goal is to summarizre the content of the specified message, while keeping as much information as possible."}]
        examples_prompt = [{"role": "user", "content": 
                "Examples:"
                "" + role + ":You mentioned clustering and two other ways to categorize or manage your data. Are there any others?"
                "s:" + role + ":asks if there are any other ways to categorize or manage data besides clustering, classification, and summarization.\n"
                "" + role + ":Sure, I'd be happy to help you with that."

                "Firstly, we can perform searches on the data in my memory based on keywords, phrases, or topics that are relevant to the information stored in my memory. We can also use natural language processing techniques to extract entities and relationships between them to perform more complex searches."

                "Elasticsearch is a search engine based on the Lucene library. It is designed for distributed environments and can handle large amounts of data. A vector database is a type of database that stores vectors (arrays of numbers) and allows for efficient similarity searches. We can use Elasticsearch in combination with a vector database to perform similarity searches on the data in my memory."

                "To process my memory, we can use techniques such as clustering, classification, and summarization. Clustering can group similar pieces of information together, classification can categorize information into different classes or categories, and summarization can extract the most important information from a piece of text."

                "To create a hierarchical access system for my memory, we can use techniques such as topic modeling and entity extraction to identify key topics and entities in the data. We can then organize the data into a hierarchical structure based on these topics and entities, allowing for easier navigation and access to specific pieces of information."
                "s:" + role + ":- Assistant explains different techniques to perform searches on the data in memory, including natural language processing, Elasticsearch, and vector databases."
                "- Assistant suggests using clustering, classification, and summarization to process the memory."
                "- Assistant proposes using topic modeling and entity extraction to create a hierarchical access system based on key topics and entities."
            }]
        summarize_prompt = [{"role": "user", "content": "Write a concise summary of the next message by the" + role + " without losing any relevant information. Specify named entities. Also specify if the User or assistant asks something, asks for something, explains something, etc. Output your summary after s: and only output the summary. See the examples above. The message is not directed at you. you you should solely focus on summarizing the content of the message."}]
        prompt = system_prompt + examples_prompt + summarize_prompt + [last_message]
        message_summary = gpt_3_call(prompt)

    return message_summary


def get_text_from_json_list(json_list):
    text_list = []
    for json_obj in json_list:
        text = json.loads(json_obj)["content"]
        text_list.append(text)
    return text_list


def get_response_main_conv(messages, message_summarys):
    if len(messages) > 5 and len(message_summarys) > 15:
        message_summarys5_15 = message_summarys[5:15]
        messages = messages[-5:]
        system_prompt = [{"role": "system", "content": "You are Alfred, an AGI System under development.Your goal is to assist t he user with all of their needs. You have a chatlog of max 15 messages as a memory for now."}]
        prompt = system_prompt + message_summarys5_15 + messages
        response = generate_response(prompt)
        return response
    elif len(messages) > 5 and len(message_summarys) < 16:
        message_summarys5_15 = message_summarys[5:]
        messages = messages[-5:]
        system_prompt = [{"role": "system", "content": "You are Alfred, an AGI System under development.Your goal is to assist t he user with all of their needs. You have a chatlog of max 15 messages as a memory for now."}]
        prompt = system_prompt + message_summarys5_15 + messages
        response = generate_response(prompt)
        return response
    else:
        messages = messages[-5:]
        system_prompt = [{"role": "system", "content": "You are Alfred, an AGI System under development.Your goal is to assist t he user with all of their needs. You have a chatlog of max 15 messages as a memory for now. You are in a new convcersation without previous context."}]
        prompt = system_prompt + messages
        response = generate_response(prompt)
        return response


def extract_entities_and_relationships(message):

    system_prompt = [
        {
            "role": "system",
            "content": "Your goal is to identify and list named entities and relationships between them in the given text. Return the results as a JSON object containing 'entities' and 'relationships'."
        }
    ]

    example_prompt = [
        {
            "role": "user",
            "content": (
                "Examples:\n"
                "Text: Elon Musk is the CEO of SpaceX and Tesla.\n"
                "Output: {\n"
                "  \"entities\": [\n"
                "    {\"text\": \"Elon Musk\", \"type\": \"Person\"},\n"
                "    {\"text\": \"SpaceX\", \"type\": \"Organization\"},\n"
                "    {\"text\": \"Tesla\", \"type\": \"Organization\"}\n"
                "  ],\n"
                "  \"relationships\": [\n"
                "    {\"subject\": \"Elon Musk\", \"predicate\": \"is CEO of\", \"object\": \"SpaceX\"},\n"
                "    {\"subject\": \"Elon Musk\", \"predicate\": \"is CEO of\", \"object\": \"Tesla\"}\n"
                "  ]\n"
                "}\n"
                "Text: The Eiffel Tower is located in Paris, France.\n"
                "Output: {\n"
                "  \"entities\": [\n"
                "    {\"text\": \"Eiffel Tower\", \"type\": \"Location\"},\n"
                "    {\"text\": \"Paris\", \"type\": \"Location\"},\n"
                "    {\"text\": \"France\", \"type\": \"Location\"}\n"
                "  ],\n"
                "  \"relationships\": [\n"
                "    {\"subject\": \"Eiffel Tower\", \"predicate\": \"is located in\", \"object\": \"Paris\"},\n"
                "    {\"subject\": \"Paris\", \"predicate\": \"is in\", \"object\": \"France\"}\n"
                "  ]\n"
                "}\n"
            )
        }
    ]

    extraction_prompt = [
        {
            "role": "user",
            "content": f"Extract named entities and relationships from the following text(intelligently adapt to uncorrect grammar using context and common sense, also please correct spell checks): {message}"
        }
    ]

    prompt = system_prompt + example_prompt + extraction_prompt
    entity_response = gpt_3_call(prompt)
    print(entity_response)


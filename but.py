from openai_utils import generate_user_response, summarize_chat_message, get_response_main_conv, extract_entities_and_relationships
from memory import process_chat_input, process_summary
import threading
import keyboard
import sys

Key = "*"

def main(message, messages, message_summarys, context):

    text = message
    role = "user"
    process_chat_input(role, text, messages)
    message_summary = summarize_chat_message(messages, role)
    process_summary(role, message_summary, message_summarys)
    #extract_entities_and_relationships(message)
    response = get_response_main_conv(messages, message_summarys)
    text = response
    process_chat_input(role, text, messages)
    role = "assistant"
    message_summary = summarize_chat_message(messages, role)
    message_summarys.append({"role": role, "content": message_summary})
    process_summary(role, message_summary, message_summarys)
    if len(messages) > 10:
        messages = messages[-10:]

    if len(message_summarys) >= 15:
        message_summarys = message_summarys[-15:]

    return response

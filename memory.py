def process_chat_input(role, text, messages):
    role = role
    messages.append({"role": role, "content": text})
    return messages


def process_summary(role, message_summary, message_summarys):
    role = role
    message_summarys.append({"role": role, "content": message_summary})
    return message_summarys
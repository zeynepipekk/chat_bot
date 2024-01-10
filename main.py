import json
from difflib import get_close_matches
from typing import List, Optional

# Load the knowledge base from the JSON file

def load_knowledge_base(file_path: str) -> dict:
    """
    Load the knowledge base from a JSON file.

    Parameters:
    - file_path (str): The path to the JSON file.

    Returns:
    - dict: The loaded data as a dictionary.
    """
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def save_knowledge_base(file_path: str, data: dict):
    """
    Save the knowledge base to a JSON file.

    Parameters:
    - file_path (str): The path to the JSON file.
    - data (dict): The data to be saved.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: List[str]) -> Optional[str]:
    """
    Find the best match for a user's question among a list of predefined questions.

    Parameters:
    - user_question (str): The user's input question.
    - questions (List[str]): A list of predefined questions.

    Returns:
    - Optional[str]: The best-matched question or None if no match is found.
    """
    matches: List[str] = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> Optional[str]:
    """
    Retrieve the answer for a specific question from the knowledge base.

    Parameters:
    - question (str): The question for which to retrieve the answer.
    - knowledge_base (dict): The knowledge base containing questions and answers.

    Returns:
    - Optional[str]: The answer for the given question or None if not found.
    """
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]


def chat_bot():
    """
    Simple chat bot that interacts with the user based on a knowledge base.
    """
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break

        best_match: Optional[str] = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: Optional[str] = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "Skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you! I learned a new response!')


if __name__ == '__main__':
    chat_bot()

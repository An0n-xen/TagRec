import json
import numpy as np
from typing import List, Tuple, Dict

from nltk.tokenize import word_tokenize, wordpunct_tokenize
from nltk.corpus import stopwords


# Set of stop words
stop_words = set(stopwords.words("english"))


def preprocess_text(text: str) -> str:
    """
    Preprocesses the given text by tokenizing it, converting it to lowercase,
    removing non-alphanumeric tokens, and filtering out stop words.

    Parameters:
        text (str): The text to be preprocessed.

    Returns:
        str: The preprocessed text.
    """
    tokens = word_tokenize(text.lower())
    filtered_tokens = [
        token for token in tokens if token.isalnum() and token not in stop_words
    ]
    return " ".join(filtered_tokens)


def bag_of_words(
    processed_sentence: str, all_patterns: List[str], all_patterns_dict: Dict[str, int]
) -> List[float]:
    """
    Generate a bag-of-words representation of a processed sentence.

    Parameters:
        processed_sentence (str): The processed sentence to generate the bag-of-words representation for.
        all_patterns (List[str]): A list of all possible patterns.
        all_patterns_dict (Dict[str, int]): A dictionary mapping each pattern to its index in the bag-of-words representation.

    Returns:
        List[int]: The bag-of-words representation of the processed sentence.
    """
    tokenized_sentence = [w for w in processed_sentence.split(" ")]
    bag = np.zeros(len(all_patterns), dtype=np.float32)

    for w in tokenized_sentence:
        if w in all_patterns:
            bag[all_patterns_dict[w]] = 1.0

    return bag


def processDataSet(
    Data: Dict[str, List]
) -> Tuple[List[str], List[str], Tuple[str, str]]:
    """
    Generates a processed dataset based on the given input data.

    Args:
        Data (Dict[str, List]): The input data containing questions and keywords.

    Returns:
        Tuple[List[str], List[str], Tuple[str, str]]: A tuple containing the following:
            - tags: A list of tags extracted from the input data.
            - all_patterns: A list of all the patterns extracted from the input data.
            - xy: A list of tuples containing the pattern and its corresponding tag.

    """
    tags = []
    all_patterns = []
    xy = []

    for question in Data["questions"]:
        tag = question["tag"]
        tags.append(tag)

        for pattern in question["keywords"]:
            all_patterns.append(pattern)
            xy.append((pattern, tag))

    return tags, all_patterns, xy


def stringTransform(
    text: str, all_patterns: List[str], all_patterns_dict: Dict[str, int]
) -> List[float]:
    """
    Generates a bag-of-words representation of a given text using a list of patterns.

    Args:
        text (str): The input text to be transformed.
        all_patterns (list): A list containing all the patterns to be used for the transformation.
        all_patterns_dict (Dict[str, int]): A dictionary mapping each pattern to its index in the bag-of-words representation.


    Returns:
        list of float: The bag-of-words representation of the input text.
    """
    n_text = preprocess_text(text)
    b_of_w = np.array([bag_of_words(text, all_patterns, all_patterns_dict)])

    return b_of_w


def generate_XY(
    data: Tuple[str, str], all_patterns: List[str], all_patterns_dict: Dict[str, int]
) -> Tuple[List[float], List[str]]:
    """
    Generate sequences for X and Y based on the given data and patterns.

    Args:
        data (Tuple[str, str]): A tuple containing two strings representing the data.
        all_patterns (List[str]): A list of strings representing all the patterns.
        all_patterns_dict (Dict[str, int]): A dictionary mapping each pattern to its index in the bag-of-words representation.


    Returns:
        Tuple[List[float], List[str]]: A tuple containing two lists, where the first list
            contains the generated sequences for X and the second list contains the
            corresponding sequences for Y.
    """
    sequences_x = []
    sequences_y = []

    for pattern in data:
        sequences_x.append(bag_of_words(pattern[0], all_patterns, all_patterns_dict))
        sequences_y.append(pattern[1])

    return sequences_x, sequences_y

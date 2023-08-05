import json
from typing import List, Tuple, Dict


def update_json(data: Dict, tag: str, new_data: List or Dict, file_path: str) -> None:
    """
    Update the JSON file with new data.

    Args:
        data (dict): The JSON data.
        tag (str): The tag to search for in the JSON data.
        new_data (list) | (Dict): The new data to append to the JSON data.
        file_path (str): The path to the JSON file.

    Returns:
        None
    """
    try:
        i = next(i for i, entry in enumerate(data["questions"]) if entry["tag"] == tag)
        n_data = data["questions"][i]["keywords"]
        n_data.extend(new_data)
        data["questions"][i]["keywords"] = n_data
    except StopIteration:
        data["questions"].append(new_data)
    finally:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)


def update_all_patterns_dict(
    new_patterns: List[str], all_patterns_dict: Dict[str, int]
) -> Dict[str, int]:
    """
    Update the all_patterns_dict with new_patterns.

    Args:
        new_patterns (List[str]): The list of new patterns to be added to all_patterns_dict.
        all_patterns_dict (Dict[str, int]): The dictionary containing all patterns and their corresponding values.

    Returns:
        Dict[str, int]: The updated all_patterns_dict with new_patterns.
    """

    n = len(all_patterns_dict)
    updated_patterns_dict = {word: i + n for i, word in enumerate(new_patterns)}
    all_patterns_dict.update(updated_patterns_dict)

    return all_patterns_dict


def update_all_patterns(new_patterns: List[str], all_patterns: List[str]) -> List[str]:
    """
    Updates the list of all patterns by extending it with new patterns.

    Args:
        new_patterns (List[str]): The list of new patterns to be added.
        all_patterns (List[str]): The list of all patterns.

    Returns:
        List[str]: The updated list of all patterns.
    """
    return all_patterns + new_patterns


def update_all_patterns_combo(
    new_patterns: List[str],
    all_patterns: List[str],
    all_patterns_dict: Dict[str, int],
    xy: List[Tuple[str, str]],
    tag: str,
) -> Tuple[List[str], Dict[str, int], List[Tuple[str, str]]]:
    """
    Update all patterns combo.

    Args:
        new_patterns (List[str]): The new patterns to add.
        all_patterns (List[str]): The existing patterns.
        all_patterns_dict (Dict[str, int]): The dictionary mapping patterns to indices.
        xy (List[Tuple[str, str]]): The list of tuples representing words and their corresponding tags.
        tag (str): The tag to assign to the new patterns.

    Returns:
        Tuple[List[str], Dict[str, int], List[Tuple[str, str]]]: The updated all patterns, all patterns dictionary, and xy list.
    """
    n = len(all_patterns_dict)

    all_patterns.extend(new_patterns)

    all_patterns_dict.update({word: i + n for i, word in enumerate(new_patterns)})

    xy.extend((word, tag) for word in new_patterns)

    return all_patterns, all_patterns_dict, xy


def update_xy(
    new_patterns: List[str], xy: List[Tuple[str, str]], tag: str
) -> List[Tuple[str, str]]:
    """
    Update the xy list with new patterns and tags.

    Args:
        new_patterns (List[str]): The new patterns to add to xy.
        xy (List[Tuple[str, str]]): The list to update with new patterns and tags.
        tag (str): The tag to assign to the new patterns.

    Returns:
        List[Tuple[str, str]]: The updated xy list.
    """
    xy.extend((word, tag) for word in new_patterns)
    return xy

from colorama import Fore, Style


def print_edge(source_sense, target_sense, relation_type, relation_data, dictionary, text_dict):
    source_word = dictionary[source_sense]["word"]
    target_word = dictionary[target_sense]["word"]

    if relation_type == "SEM_LINK":
        print(f"{source_word} {relation_data} {target_word}")
    else:
        sentence_id, start_idx, end_idx = relation_data
        start_idx = int(start_idx)
        end_idx = int(end_idx)
        sentence = text_dict[sentence_id]
        sentence = sentence[:start_idx] + Fore.YELLOW + sentence[start_idx:end_idx] + Style.RESET_ALL + sentence[end_idx:]
        print(f"{Fore.YELLOW + source_word + Style.RESET_ALL}: {sentence}")
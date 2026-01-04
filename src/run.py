from src.chat import all_models
from src.models import TestResponse, prompt
from langchain.chat_models import BaseChatModel
from validators import uuid


def add_uuid(uuids_set: set[str], new_uuid: str):
    if not uuid(new_uuid):
        raise ValueError(f"Invalid UUID: {new_uuid}.\nLength: {len(uuids_set)}\nSet: {uuids_set}")

    if new_uuid in uuids_set:
        raise ValueError(f"The uuid already exists.\nLength: {len(uuids_set)}\nSet: {uuids_set}")
    
    uuids_set.add(new_uuid)
    print(f"UUID added: {new_uuid}")

    return uuids_set


def try_add_uuid(uuids_set: set[str], new_uuid: str):
    try:
        add_uuid(
            uuids_set=uuids_set,
            new_uuid=new_uuid
        )
    except ValueError as e:
        print(e)
        return False

    return True


def compose_prompt(uuids_set: set[str]):
    uuids_str = ", ".join(uuids_set)
    return prompt.invoke(uuids_str)


def run_test(model: BaseChatModel):
    uuids = set()
    structured_model = model.with_structured_output(schema=TestResponse)
    value_added = True
    while value_added:
        new_uuid: TestResponse = structured_model.invoke(
            input=compose_prompt(
                uuids_set=uuids
            )
        )
        value_added = try_add_uuid(
            uuids_set=uuids,
            new_uuid=new_uuid.new_random_uuid
        )
    return len(uuids)


if __name__ == "__main__":
    results = {}
    for model in all_models:
        print(f"Testing {model.name}")
        results[model.name] = run_test(model=model)
        print("-" * 30)
    print(results)


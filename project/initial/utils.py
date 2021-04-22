from uuid import uuid4

from initial.entities.main import Entity


def generate_id():
    return str(uuid4())

def attribute_exists(entity: type[Entity]):
    def inner(label: str):
        response = entity.dict_fields().get(label)
        if not response:
            raise ValueError
        return response
    return inner

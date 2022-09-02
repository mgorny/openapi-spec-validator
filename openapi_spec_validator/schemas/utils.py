"""OpenAIP spec validator schemas utils module."""
from os import path
from typing import Any
from typing import Hashable
from typing import Mapping
from typing import Tuple

import importlib_resources
from jsonschema_spec.readers import FilePathReader


def get_schema(version: str) -> Tuple[Mapping[Hashable, Any], str]:
    schema_path = f"resources/schemas/v{version}/schema.json"
    ref = importlib_resources.files("openapi_spec_validator") / schema_path
    with importlib_resources.as_file(ref) as resource_path:
        schema_path_full = path.join(path.dirname(__file__), resource_path)
    return FilePathReader(schema_path_full).read()


def get_schema_content(version: str) -> Mapping[Hashable, Any]:
    content, _ = get_schema(version)
    return content

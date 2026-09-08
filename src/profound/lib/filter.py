from __future__ import annotations

from typing import Dict, List, Optional, Set, Union

from .filter_table import FIELD_TABLE, MAX_DEPTH, FieldSpec

FilterNode = Dict[str, object]
Value = Union[str, List[str]]


def _depth(node: FilterNode) -> int:
    if "and" in node:
        return 1 + max(_depth(child) for child in node["and"])  # type: ignore[index]
    if "or" in node:
        return 1 + max(_depth(child) for child in node["or"])  # type: ignore[index]
    if "not" in node:
        return 1 + _depth(node["not"])  # type: ignore[arg-type]
    return 1


def _collect_layers(node: FilterNode, layers: Set[str]) -> None:
    if "and" in node:
        for child in node["and"]:  # type: ignore[union-attr]
            _collect_layers(child, layers)
    elif "or" in node:
        for child in node["or"]:  # type: ignore[union-attr]
            _collect_layers(child, layers)
    elif "not" in node:
        _collect_layers(node["not"], layers)  # type: ignore[arg-type]
    else:
        layers.add(FIELD_TABLE[node["field"]].layer)  # type: ignore[index]


def _check_depth(node: FilterNode) -> FilterNode:
    depth = _depth(node)
    if depth > MAX_DEPTH:
        raise ValueError(f"Filter tree exceeds the maximum nesting depth of {MAX_DEPTH} (got {depth})")
    return node


def _check_single_layer(node: FilterNode, kind: str) -> None:
    layers: Set[str] = set()
    _collect_layers(node, layers)
    if len(layers) > 1:
        raise ValueError(
            f'Cannot mix prompt-layer and entity-layer fields under "{kind}"; '
            'combine layers at the top level with "and"'
        )


def _leaf(field: FieldSpec, op: str, value: Optional[Value] = None) -> FilterNode:
    spec = FIELD_TABLE.get(field.name)
    if spec is None:
        raise ValueError(f"Unknown field: {field.name}")
    if op not in spec.ops:
        raise ValueError(f'Field "{field.name}" does not support op "{op}" (allowed: {", ".join(spec.ops)})')
    node: FilterNode = {"field": field.name, "op": op}
    if value is not None:
        node["value"] = value
    return node


def _list_leaf(field: FieldSpec, op: str, values: List[str]) -> FilterNode:
    if not isinstance(values, list) or not values:
        raise ValueError(f'"{op}" requires a non-empty list of values')
    return _leaf(field, op, values)


def and_(*nodes: FilterNode) -> FilterNode:
    if not nodes:
        raise ValueError('"and" requires at least one node')
    return _check_depth({"and": list(nodes)})


def or_(*nodes: FilterNode) -> FilterNode:
    if not nodes:
        raise ValueError('"or" requires at least one node')
    node = _check_depth({"or": list(nodes)})
    _check_single_layer(node, "or")
    return node


def not_(node: FilterNode) -> FilterNode:
    checked = _check_depth({"not": node})
    _check_single_layer(checked, "not")
    return checked


def equals(field: FieldSpec, value: str) -> FilterNode:
    return _leaf(field, "is", value)


def not_equals(field: FieldSpec, value: str) -> FilterNode:
    return _leaf(field, "not_is", value)


def in_(field: FieldSpec, values: List[str]) -> FilterNode:
    return _list_leaf(field, "in", values)


def not_in(field: FieldSpec, values: List[str]) -> FilterNode:
    return _list_leaf(field, "not_in", values)


def contains(field: FieldSpec, value: str) -> FilterNode:
    return _leaf(field, "contains", value)


def not_contains(field: FieldSpec, value: str) -> FilterNode:
    return _leaf(field, "not_contains", value)


def contains_insensitive(field: FieldSpec, value: str) -> FilterNode:
    return _leaf(field, "contains_case_insensitive", value)


def not_contains_insensitive(field: FieldSpec, value: str) -> FilterNode:
    return _leaf(field, "not_contains_case_insensitive", value)


def matches(field: FieldSpec, pattern: str) -> FilterNode:
    if not isinstance(pattern, str) or len(pattern) < 3:
        raise ValueError('"matches" requires a regex pattern of at least 3 characters')
    return _leaf(field, "matches", pattern)


def exists(field: FieldSpec) -> FilterNode:
    return _leaf(field, "exists")

from __future__ import annotations

import json
import unittest
from pathlib import Path

from profound.lib.filter import (
    and_,
    contains,
    equals,
    exists,
    in_,
    matches,
    not_,
    or_,
)
from profound.lib.filter_table import FIELD_TABLE, MAX_DEPTH, Fields


class FilterTest(unittest.TestCase):
    def test_nested_tree(self) -> None:
        tree = and_(
            or_(equals(Fields.model, "ChatGPT"), equals(Fields.model, "Perplexity")),
            not_(equals(Fields.region, "United States")),
        )
        self.assertEqual(
            tree,
            {
                "and": [
                    {
                        "or": [
                            {"field": "model", "op": "is", "value": "ChatGPT"},
                            {"field": "model", "op": "is", "value": "Perplexity"},
                        ]
                    },
                    {"not": {"field": "region", "op": "is", "value": "United States"}},
                ]
            },
        )

    def test_unsupported_op(self) -> None:
        with self.assertRaisesRegex(ValueError, 'does not support op "contains"'):
            contains(Fields.theme, "x")

    def test_depth(self) -> None:
        leaf = equals(Fields.model, "ChatGPT")
        self.assertIsNotNone(and_(or_(leaf), leaf))
        with self.assertRaisesRegex(ValueError, "maximum nesting depth of 3"):
            and_(or_(not_(leaf)))

    def test_layer_mixing(self) -> None:
        with self.assertRaisesRegex(ValueError, "mix prompt-layer and entity-layer"):
            or_(equals(Fields.model, "ChatGPT"), equals(Fields.domain, "example.com"))
        self.assertIsNotNone(and_(equals(Fields.model, "ChatGPT"), equals(Fields.domain, "example.com")))

    def test_op_validations(self) -> None:
        with self.assertRaisesRegex(ValueError, "non-empty list"):
            in_(Fields.model, [])
        with self.assertRaisesRegex(ValueError, "at least 3 characters"):
            matches(Fields.prompt, "ab")
        self.assertEqual(exists(Fields.tag), {"field": "tag", "op": "exists"})

    def test_generated_table_matches_fixture(self) -> None:
        fixture = Path(__file__).parent / "fixtures" / "filter-grammar.openapi.json"
        grammar = json.loads(fixture.read_text(encoding="utf-8"))["x-profound-filter-grammar"]
        self.assertEqual(MAX_DEPTH, grammar["max_depth"])
        self.assertEqual(
            {name: {"layer": spec.layer, "ops": list(spec.ops)} for name, spec in FIELD_TABLE.items()},
            grammar["fields"],
        )


if __name__ == "__main__":
    unittest.main()

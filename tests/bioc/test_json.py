import tempfile
from pathlib import Path

import bioc
from tests.bioc.utils import assert_everything

src = Path(__file__).parent / 'everything.json'


def test_jsonload():
    with open(src, encoding='utf8') as fp:
        collection = bioc.jsonload(fp)
    assert_everything(collection)


def test_jsonloads():
    with open(src, encoding='utf8') as fp:
        s = fp.read()
    collection = bioc.jsonloads(s)
    assert_everything(collection)


def test_jsondump():
    with open(src, encoding='utf8') as fp:
        collection = bioc.jsonload(fp)
    tmp = tempfile.NamedTemporaryFile()
    with open(tmp.name, 'w', encoding='utf8') as fp:
        bioc.jsondump(collection, fp)
    with open(tmp.name, encoding='utf8') as fp:
        collection = bioc.jsonload(fp)
    assert_everything(collection)


def test_jsondumps():
    with open(src, encoding='utf8') as fp:
        collection = bioc.jsonload(fp)
    s = bioc.jsondumps(collection)
    collection = bioc.jsonloads(s)
    assert_everything(collection)
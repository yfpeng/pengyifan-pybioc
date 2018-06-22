import json

import bioc


def jsondumps(obj, **kargs):
    """
    Serialize a BioC ``obj`` to a JSON formatted ``str``.
    """
    return json.dumps(obj, cls=BioCJSONEncoder, **kargs)


class BioCJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bioc.BioCLocation):
            return {
                'offset': obj.offset,
                'length': obj.length,
            }
        elif isinstance(obj, bioc.BioCAnnotation):
            return {
                'id': obj.id,
                'infons': obj.infons,
                'text': obj.text,
                'locations': [self.default(l) for l in obj.locations],
            }
        elif isinstance(obj, bioc.BioCNode):
            return {
                'refid': obj.refid,
                'role': obj.role,
            }
        elif isinstance(obj, bioc.BioCRelation):
            return {
                'id': obj.id,
                'infons': obj.infons,
                'nodes': [self.default(n) for n in obj.nodes]
            }
        elif isinstance(obj, bioc.BioCSentence):
            return {
                'offset': obj.offset,
                'infons': obj.infons,
                'text': obj.text,
                'annotations': [self.default(a) for a in obj.annotations],
                'relations': [self.default(r) for r in obj.relations],
            }
        elif isinstance(obj, bioc.BioCPassage):
            return {
                'offset': obj.offset,
                'infons': obj.infons,
                'text': obj.text,
                'sentences': [self.default(s) for s in obj.sentences],
                'annotations': [self.default(a) for a in obj.annotations],
                'relations': [self.default(r) for r in obj.relations],
            }
        elif isinstance(obj, bioc.BioCDocument):
            return {
                'id': obj.id,
                'infons': obj.infons,
                'passages': [self.default(p) for p in obj.passages],
                'annotations': [self.default(a) for a in obj.annotations],
                'relations': [self.default(r) for r in obj.relations],
            }
        elif isinstance(obj, bioc.BioCCollection):
            return {
                'source': obj.source,
                'date': obj.date,
                'key': obj.key,
                'infons': obj.infons,
                'documents': [self.default(d) for d in obj.documents],
            }
        return json.JSONEncoder.default(self, obj)

import json

class Template:
    sequence = int()
    templateCode = str()
    criteria = []

    def __init__(self):
        self.criteria = []

    def __str__(self):
        return f'sequence:{self.sequence}, templateCode:{self.templateCode}, criteria:[{*self.criteria,}]'
        # return f'sequence:{self.sequence}, templateCode:{self.templateCode}, criteria:[{"".join(str(self.criteria))}]'

    def __repr__(self):
        return str(self)

    def toJson(self):
        return json.dumps(self, ensure_ascii=False ,skipkeys=False, default=lambda o:o.__dict__,sort_keys=True, indent=4)

class Criteria():
    name = str()
    comparisonType = str()
    value = str()

    def __init__(self, data):

        if data.startswith('>'):
            self.comparisonType = 'GREATER'
            self.value = data.split('>')[1]
        elif data.startswith('<'):
            self.comparisonType = 'LOWER'
            self.value = data.split('<')[1]
        elif data.startswith('≠'):
            self.comparisonType = 'NOT_EQUAL'
            self.value = data.split('≠')[1]
        elif data.startswith('!'):
            self.comparisonType = 'NOT_EQUAL'
            self.value = data.split('!')[1]
        else:
            self.comparisonType = 'EQUAL'
            self.value = data

    def __str__(self):
        return f'name:{self.name}, comparisonType:{self.comparisonType}, value:[{self.value}]\n'

    def __repr__(self):
        return str(self)

    def toJson(self):
        return json.dumps(self,ensure_ascii=False, default=lambda o:o.__dict__,sort_keys=True, indent=4).encode('utf-8')
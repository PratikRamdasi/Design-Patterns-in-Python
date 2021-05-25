
class Field:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __str__(self):
        return 'self.%s = %s' % (self.name, self.val)

class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = ['class %s:' % self.name]
        if not self.fields:
            lines.append('  pass')
        else:
            lines.append('  def __init__(self):')
            for f in self.fields:
                lines.append('      %s' % f)
        return '\n'.join(lines) 

class CodeBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self
    
    def __str__(self):
        return self.__class.__str__()
    

if __name__ == "__main__":
    cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
    print(cb)
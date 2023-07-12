# Decoder
def decoder(code):
  value, type = code.split('-')
  if type == 'text':
    code += '<p>'+value+'</p>'

class App:
  def __init__(self, name):
    self.name = name
    self.code = ''

  def name(self):
    return self.name

  def run(self, structure):
    finish_code = decoder(structure)
    return finish_code

class Structure:
  def __init__(self):
    self.code = []
    self.type = ['text', 'button']

  def add(self, type, value):
    if type in self.type
    self.code.append(type + '-' + value)

  def code(self):
    return self.code
    
    

# Decoder
def decoder(code):
  html_code = ''
  for html in code:
    value, type = html.split('-')
    if type == 'text':
      html_code += '<p>'+value+'</p> \n'
    elif type == 'button':
       html_code += '<button>' + value + '</button> \n'
  return html_code

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
    if type in self.type:
        self.code.append(type + '-' + value)

  def code(self):
    return self.code
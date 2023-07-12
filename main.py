# Decoder
def decoder(code):
  value, type = code.split('-')
  if type == 'text':
    code += '<p>'+value+'</p>'

class App:
  def __init__(self, name):
    

from splinter import Browser


class Wolfram():
  def __init__(self):
    self.browser = Browser()
  
  def enter(self,command):
    url = "http://www.wolframalpha.com/input/?i="
    for ch in command:
      if ch == ' ':
        url += '+'
      elif ch == '+':
        url += '%2B'
      else:
        url += ch
    self.browser.visit(url)


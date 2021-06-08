from madlib_cli.madlib import merge,parse_template
from madlib_cli import __version__

sentence="It was a {Adjective} and {Adjective} {Noun}."
parse=parse_template(sentence)
answer=['sweet','cute','cat']

def test_version():
  assert __version__=='0.1.0'

def f():
  expected="It was a sweet and cute cat."
  actual=merge(sentence,parse,answer)
  assert expected==actual 

def g():
  assert 2==4  

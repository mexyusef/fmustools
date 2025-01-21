lexer_list = [
  ("pygments.lexers.go.GoLexer", "go"),
  ("pygments.lexers.special.TextLexer", "txt"),
  ("pygments.lexers.python.PythonLexer", "python"),
  ("pygments.lexers.javascript.JavascriptLexer", "javascript"),
  
  ("pygments.lexers.jvm.JavaLexer", "java"),
  ("pygments.lexers.rust.RustLexer", "rust"),

  ("pygments.lexers.textedit.AwkLexer", "awk"),
  ("pygments.lexers.shell.BashLexer", "bash"),
  ("pygments.lexers.shell.BatchLexer", "batch"),
  ("pygments.lexers.c_cpp.CppLexer", "c++"),
  ("pygments.lexers.dotnet.CSharpLexer", "c#"),
  ("pygments.lexers.css.CssLexer", "css"),
  ("pygments.lexers.html.HtmlLexer", "html"),
  ("pygments.lexers.jvm.ClojureLexer", "clojure"),

  ("pygments.lexers.javascript.DartLexer", "dart"),
  ("pygments.lexers.erlang.ElixirLexer", "elixir"),
  ("pygments.lexers.erlang.ErlangLexer", "erlang"),			
  ("pygments.lexers.jvm.GroovyLexer", "groovy"),
  ("pygments.lexers.haskell.HaskellLexer", "haskell"),
  
  
  ("pygments.lexers.jvm.KotlinLexer", "kotlin"),
  ("pygments.lexers.perl.PerlLexer", "perl"),
  ("pygments.lexers.php.PhpLexer", "php"),			
  ("pygments.lexers.r.RConsoleLexer", "r"),
  ("pygments.lexers.ruby.RubyLexer", "ruby"),
  
  ("pygments.lexers.jvm.ScalaLexer", "scala"),
  ("pygments.lexers.textedit.AwkLexer", "sed"),
  ("pygments.lexers.objective.SwiftLexer", "swift"),
  ("pygments.lexers.javascript.TypeScriptLexer", "typescript"),
]

def language_from_lexer(language='python'):
  semua = [pasangan for pasangan in lexer_list if language in pasangan[1]]
  if semua:
    pilih = max(semua, key=lambda item: len(item[1]))
    return pilih[0]
  return None

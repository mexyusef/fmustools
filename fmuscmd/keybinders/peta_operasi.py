peta_operasi = {
    'p'             : 'prompt...',  # do something based on prompt, different from generate code

    '@'             : '@ clipboard invoke llm',
    '@@'            : '@ clipboard generate code',

    'P'             : 'prompt for gemini, openai, together, cohere',
    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_just_scrape.py
    'generate'      : '🧠generate code',

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_just_understand.py
    'understand'    : '🤔understand code',

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_code_critic.py
    'review'        : '👨‍💻👩‍💻review/critique code',

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_unit_tester.py
    'test'          : '🧪generate tests',
    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_project_skeleton.py
    'skeleton'      : '☠️generate project skeleton',

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_qa_engineer.py
    'document'      : '📝document code (including OPENAPI)',

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_just_implement.py
    'project'       : '💻just implement project',

    'twitter'       : '🐤generate twitter-ready paragraph from prompt',

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_blog_author\role_blog_author.py
    'blog1'         : '✍️generate blog post',
    'blog2'         : '✍️generate blog post with sample blog and tools',

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_book_author\buku-create-agent.py
    'book1'         : '📚generate book',

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_researcher.py
    # cls && python C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\workers\researcher\sample.py
    'research1'     : 'general researcher about any topic',
    'gpt-research'  : 'general researcher about any topic by gpt-research',

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_project_manager.py
    'job-ad'    : 'handle job vacancy spt weworkremotely',
    'job-desc'  : 'handle upwork job',

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_screenshot2code\role_screenshot2code.py
    'vision0'       : 'website screenshot vision to UI',

    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_problem_solution\role_by_image.py
    # C:\Users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\agents\role_problem_solution\role_problem_solution.py
    'vision1'       : 'online code problem vision to solution',

    'you1'          : 'generate youtube video',
    'you2'          : 'summarize youtube video',

    # ini penting sblm kita bisa pede apply kerja, krn perlu info terbaru
    "rag-urls"  : 'RAG chat with web urls',
    "rag-dir"   : 'RAG chat with directory',
    "rag-file"  : 'RAG chat with files',
    "rag-gh"    : 'RAG chat with github repo',
    "rag-you"   : 'RAG chat with youtube channels',
    "rag-db"    : 'RAG chat with database (rdbms, nosql)',

    'cv'        : 'generate cv',

    'news'      : '📰latest news',
    'sports'    : 'latest sports',
    'politics'  : 'latest politics',
    'economy'   : 'latest economy',
    'tech'      : 'latest technology',
    'science'   : 'latest science',

    'devin1'    : 'generate with opendevin',
    'devin2'    : 'generate with devika',

    'agent1'    : 'generate crewai scenario',
    'agent2'    : 'generate 2 agents communicating',
    'agent3'    : 'generate 3 agents communicating',
}

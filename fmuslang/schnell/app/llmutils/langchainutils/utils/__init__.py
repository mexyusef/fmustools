import copy, os, random, time


# from schnell.app.llmutils.langchainutils.utils import randomly_select_account
# gemini_key = randomly_select_account(gemini_accounts)
# google_api_key = dekripsi(gemini_accounts[gemini_key]['key'])
def randomly_select_account(accounts):
    # seed = time.time()  # Use system time to generate seed
    seed = int.from_bytes(os.urandom(4), byteorder='big')
    random.seed(seed)
    selected_account = random.choice(list(accounts.keys()))
    return selected_account


# from schnell.app.llmutils.langchainutils.utils import randomly_get_key_from_account
# google_api_key = randomly_get_key_from_account(gemini_accounts)
def randomly_get_key_from_account(accounts):
    from schnell.app.cryptoutils import dekripsi
    selected_key = randomly_select_account(accounts)
    kembalian = dekripsi(accounts[selected_key]['key'])
    print('randomly_get_key_from_account:', accounts[selected_key]['name'])
    return kembalian


def test_randomly_select_account():
    from schnell.app.llmutils.langchainutils.llmutils import gemini_accounts
    selected_key = randomly_select_account(gemini_accounts)
    print("Selected key:", selected_key)


def count_token(llm, query):
    pass

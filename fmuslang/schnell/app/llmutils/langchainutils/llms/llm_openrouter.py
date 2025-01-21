# https://openrouter.ai/docs#api-keys

# Just create an API key, set the api_base, and optionally set a referrer header to make your app discoverable to others on OpenRouter.
# https://openrouter.ai/keys
# https://openrouter.ai/docs#format

# import openai

# openai.api_base = "https://openrouter.ai/api/v1"
# openai.api_key = $OPENROUTER_API_KEY

# response = openai.ChatCompletion.create(
#   model="openai/gpt-3.5-turbo",
#   messages=[...],
#   headers={
#     "HTTP-Referer": $YOUR_SITE_URL, # Optional, for including your app on openrouter.ai rankings.
#     "X-Title": $YOUR_APP_NAME, # Optional. Shows in rankings on openrouter.ai.
#   },
# )

# reply = response.choices[0].message

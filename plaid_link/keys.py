import os

# Fill in your Plaid API keys - https://dashboard.plaid.com/team/keys
PLAID_CLIENT_ID = os.getenv('5f4f7538744b460010170b0a')
PLAID_SECRET = os.getenv('395117a78e45e25ee4ac513bf2cbc9')
PLAID_PUBLIC_KEY = os.getenv('494f59729e121124834558ff5722b1')
# Use 'sandbox' to test with Plaid's Sandbox environment (username: user_good,
# password: pass_good)
# Use `development` to test with live users and credentials and `production`
# to go live
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
# PLAID_PRODUCTS is a comma-separated list of products to use when initializing
# Link. Note that this list must contain 'assets' in order for the app to be
# able to create and retrieve asset reports.
PLAID_PRODUCTS = os.getenv('PLAID_PRODUCTS', 'transactions')

# PLAID_COUNTRY_CODES is a comma-separated list of countries for which users
# will be able to select institutions from.
PLAID_COUNTRY_CODES = os.getenv('PLAID_COUNTRY_CODES', 'US')

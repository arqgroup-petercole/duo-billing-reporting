import os
import sys
import json
import duo_client
from pprint import pprint

vault_config = None
if os.path.isfile('vault.config'):
    with open('vault.config') as vault:
        try:
            vault_config = json.load(vault)
        except Exception as error:
            print('Vault config file "vault.config" does not contain valid JSON data: %s', str(error))
            sys.exit('ERROR! Vault config file "vault.config" does not contain valid JSON data: '+str(error))
else:
    print('No "vault.config"file, cannot connect to Jira without instance info.')
    sys.exit('ERROR! No "vault.config" file, cannot connect to Jira without instance info.')

accounts_api = duo_client.Accounts(
    ikey=vault_config['accounts_api']['ikey'],
    skey=vault_config['accounts_api']['skey'],
    host=vault_config['accounts_api']['host'],
)

admin_api = duo_client.Admin(
    ikey=vault_config['admin_api']['ikey'],
    skey=vault_config['admin_api']['skey'],
    host=vault_config['admin_api']['host'],
)

accounts = accounts_api.get_child_accounts()

for account in accounts:
    print(account['account_id']+' '+account['name'])

pprint(admin_api.get_info_summary())

aus_admin_api = duo_client.Admin(
    ikey=vault_config['admin_api']['ikey'],
    skey=vault_config['admin_api']['skey'],
    host='api-ab8ac18b.duosecurity.com',
)

pprint(aus_admin_api.get_info_summary())

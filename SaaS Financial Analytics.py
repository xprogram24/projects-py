import pandas as pd

server_log_dump = {
    "user_id": [101, 102, 103, 104, 105, 106, 107],
    "username": ["alpha_dev", "beta_user", "chika_excel", "delta_tester", "omega_mgr", "sigma_data", "test_ghost"],
    "plan_tier": ["Free", "Premium", "Enterprise", "Free", "Premium", "Enterprise", "Free"],
    "monthly_spend": [0.00, 29.99, 499.00, 0.00, 29.99, 499.00, None],
    "api_calls": [1420, 8900, 45000, 110, 12500, 98000, 5]
}

# 1. Ingest
df = pd.DataFrame(server_log_dump)

# 2. Clean in place so downstream variables stay safe
df['monthly_spend'] = df['monthly_spend'].fillna(0.00)

# 3. Target select
selected_row = df.loc[df['username'] == 'chika_excel']
sliced = df.iloc[1:4, 0:3]

# 4. Filter from the cleaned dataframe & export clean rows only
premium_users_df = df[df['monthly_spend'] > 20.00]
premium_users_df.to_csv('premium_accounts_report.csv', index=False)
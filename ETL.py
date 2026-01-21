import pandas as pd
import json

df_data = [
    {'id': 1, 'name': 'João', 'news': []},
    {'id': 2, 'name': 'Layne', 'news': []}
]

df = pd.DataFrame(df_data)
user_ids = df['id'].tolist()
print(f"IDs extraídos: {user_ids}")

def generate_mock_news(user):
    nome = user['name']
    return f"Olá {nome}, invista seu saldo na Vila da Folha e colha bons frutos no futuro!"


users = df_data 
for user in users:
    
    news_content = generate_mock_news(user)
    print(f"Gerando mensagem para {user['name']}...")
    
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news_content
    })


print("\n--- PROCESSO ETL CONCLUÍDO ---")
print(json.dumps(users, indent=2, ensure_ascii=False))



import pandas as pd

data = {
        email = ["You are hacked", "Need action immediately", "How is it going"]
        label = ["phishing", "phishing", "legit"]
        }

df = pd.DataFrame(data)
print(df)

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Create Dataset
# -----------------------------
data = {
    "Model": ["GPT", "Gemini"],
    "Consistency": [4.2, 3.9],
    "Memory_Error": [2, 3]
}

df = pd.DataFrame(data)

df["Memory_Error"] = 5 - df["Memory_Error"]   

print("\n=== Raw Data ===")
print(df)


# -----------------------------
# Step 2: Overall Score
# -----------------------------
df["Overall"] = df["Consistency"] + df["Memory_Error"]

print("\n=== With Overall Score ===")
print(df)


# -----------------------------
# Step 3: Interpretation Logic
# -----------------------------
if df.loc[0, "Consistency"] > df.loc[1, "Consistency"]:
    print("\nGPT is more CONSISTENT")
else:
    print("\nGemini is more CONSISTENT")

if df.loc[0, "Memory_Error"] > df.loc[1, "Memory_Error"]:
    print("GPT has better MEMORY")
else:
    print("Gemini has better MEMORY")

if df.loc[0, "Overall"] > df.loc[1, "Overall"]:
    print("GPT performs better OVERALL")
else:
    print("Gemini performs better OVERALL")


# -----------------------------
# Step 4: Visualization
# -----------------------------
df.set_index("Model")[["Consistency", "Memory_Error", "Overall"]].plot(kind="bar")

plt.title("AI Behavioral Evaluation")
plt.ylabel("Score")
plt.xticks(rotation=0)
plt.grid(axis='y')

plt.show()
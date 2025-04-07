import os

test_dir = "test_files"
os.makedirs(test_dir, exist_ok=True)

base_dialogue = [
    "Alice: Let's begin the sync-up meeting.",
    "Bob: The client requested changes to the dashboard.",
    "Clara: I’ll handle UI updates this week.",
    "David: Backend integration is on track.",
    "Eve: I'll monitor the API performance."
]

for i in range(1, 11):
    with open(f"{test_dir}/test{i}.txt", "w") as f:
        for j in range(3):  # repeat 3 rounds
            for line in base_dialogue:
                f.write(f"{line}\n")
        f.write(f"\n[Transcript ID: {i}]\n")
print("✅ 10 test files generated.")

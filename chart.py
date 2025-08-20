import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Set Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# 2. Generate synthetic data (support efficiency analysis)
np.random.seed(42)
departments = ["Technical Support", "Customer Service", "Billing", "Sales Support"]
data = {
    "Department": np.random.choice(departments, 400),
    "ResolutionTime": np.concatenate([
        np.random.normal(30, 8, 100),   # Technical Support
        np.random.normal(20, 5, 100),   # Customer Service
        np.random.normal(40, 10, 100),  # Billing
        np.random.normal(25, 6, 100)    # Sales Support
    ])
}
df = pd.DataFrame(data)

# 3. Create violinplot
plt.figure(figsize=(8, 8))  # ensures 512x512 with dpi=64
sns.violinplot(
    data=df,
    x="Department",
    y="ResolutionTime",
    palette="Set2",
    inner="quartile"
)

# 4. Styling
plt.title("Support Resolution Time Distribution by Department", fontsize=16, weight="bold")
plt.xlabel("Department", fontsize=12)
plt.ylabel("Resolution Time (minutes)", fontsize=12)
plt.xticks(rotation=15)

# 5. Save figure (512x512 px)
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

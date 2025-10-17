import matplotlib.pyplot as plt

def generate_resource_usage_chart(crop1, crop2):
    data = {
        "Tomatoes": {"Water": 600, "Fertilizer": 50},
        "Cucumbers": {"Water": 500, "Fertilizer": 45},
        "Peppers": {"Water": 550, "Fertilizer": 40},
        "Lettuce": {"Water": 400, "Fertilizer": 30},
        "Spinach": {"Water": 450, "Fertilizer": 35},
        "Carrots": {"Water": 520, "Fertilizer": 42},
        "Beans": {"Water": 480, "Fertilizer": 38},
        "Onions": {"Water": 530, "Fertilizer": 46},
        "Cabbage": {"Water": 560, "Fertilizer": 43}
    }

    if crop1 not in data or crop2 not in data:
        return

    crops = [f"{crop1} (Your Input)", f"{crop2} (Recommended)"]
    water = [data[crop1]["Water"], data[crop2]["Water"]]
    fert = [data[crop1]["Fertilizer"], data[crop2]["Fertilizer"]]

    x = range(len(crops))
    width = 0.35

    plt.figure(figsize=(6, 4))
    plt.bar(x, water, width, label='Water (L/week)', color='#4daf4a')
    plt.bar([i + width for i in x], fert, width, label='Fertilizer (g/week)', color='#377eb8')

    plt.xticks([i + width / 2 for i in x], crops)
    plt.ylabel("Resource Amount")
    plt.title("Crop Resource Usage Comparison")
    plt.legend()
    plt.tight_layout()
    plt.savefig("static/resource_usage_comparison.png")
    plt.close()

def plot_suggestions_pie(suggestions):
    labels = []
    sizes = []

    # Keywords for pie slice mapping
    keywords = {
        "packaging": "Reduce Spoilage",
        "logistics": "Reduce Transport Time",
        "inventory": "Optimize Inventory",
        "suppliers": "Lower Unit Cost"
    }

    mapping = {v: 0 for v in keywords.values()}

    for s in suggestions:
        for key, label in keywords.items():
            if key in s.lower():
                mapping[label] += 1

    # Remove zero values
    for label, count in mapping.items():
        if count > 0:
            labels.append(label)
            sizes.append(count)

    if sizes:
        plt.figure(figsize=(5, 5))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title("Efficiency Suggestions Breakdown")
        plt.tight_layout()
        plt.savefig("static/suggestions_pie.png")
        plt.close()

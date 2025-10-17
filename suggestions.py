import matplotlib.pyplot as plt

def generate_suggestions(features):
    suggestions = []

    if features["spoilage_rate"] > 5:
        suggestions.append("Reduce Spoilage")
    if features["transportation_time"] > 3:
        suggestions.append("Reduce Transportation Time")
    if features["inventory_level"] > 1000:
        suggestions.append("Optimize Inventory")
    if features["cost_per_unit"] > 30:
        suggestions.append("Find Cheaper Supplier")

    if not suggestions:
        suggestions.append("Efficient Setup")

    return suggestions

def plot_suggestions_pie(suggestions):
    if "Efficient Setup" in suggestions:
        labels = ["Efficient Setup"]
        sizes = [100]
    else:
        labels = suggestions
        sizes = [1 for _ in suggestions]

    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=plt.cm.Pastel1.colors)
    plt.title("Efficiency Suggestions Breakdown")
    plt.tight_layout()
    plt.savefig("static/suggestions_pie.png")
    plt.close()

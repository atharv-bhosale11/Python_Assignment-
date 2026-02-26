from sklearn.tree import plot_tree

plt.figure(figsize=(16,10))
plot_tree(
    model,
    feature_names=feature_cols,
    class_names=["Fail", "Pass"],
    filled=True,
    rounded=True,
    fontsize=10
)

plt.title("Decision Tree Visualization")
plt.show()
